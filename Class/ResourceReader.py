import pytesseract
from PIL import Image
import pyautogui
import pygetwindow as gw
import cv2
import numpy as np
import os
from paddleocr import PaddleOCR

class ResourceReader:
    def __init__(self, window_title="BlueStacks", template_dir="A:\\Projects\\Coc_VisionBot\\templates"):
        # 查找窗口
        windows = [w for w in gw.getWindowsWithTitle(window_title) if w.visible]
        if not windows:
            raise Exception("No window found with title:", window_title)
        self.window = windows[0]

        # 加载金币和圣水图标模板
        self.gold_icon_path = os.path.join(template_dir, "gold_icon.png")
        self.elixir_icon_path = os.path.join(template_dir, "elixir_icon.png")
        self.gold_template = cv2.imread(self.gold_icon_path, 0)
        self.elixir_template = cv2.imread(self.elixir_icon_path, 0)

        # self.ocr = PaddleOCR(use_angle_cls=False, lang='en')  # 注意self.ocr

    def screenshot_whole_window(self):
        # 截全窗口
        left = self.window.left
        top = self.window.top
        width = self.window.width
        height = self.window.height
        img = pyautogui.screenshot(region=(left, top, width, height))
        return img

    def match_icon(self, window_img, template_img):
        # 模板匹配，返回图标左上角坐标 (x, y)
        img_gray = cv2.cvtColor(np.array(window_img), cv2.COLOR_BGR2GRAY)
        result = cv2.matchTemplate(img_gray, template_img, cv2.TM_CCOEFF_NORMED)
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
        return max_loc  # (x, y)

    # ====== 调试用！！这边是用tesseract来识别数字的，tesseract在游戏中发挥不好。 ======
    def read_number(self, img):
        # OCR识别数字

        img = img.convert('L')
        # 这个是转灰色图片，如果想用原来的彩色图片，直接注释掉就行。

        text = pytesseract.image_to_string(img, config='--psm 7 digits')
        # --psm 7 是告诉 tesseract“图片里只有一行文字”（适合识别单行数字），digits表示只识别数字。
        text = text.replace(',', '').replace(' ', '').strip()
        text = ''.join(c for c in text if c.isdigit())
        # 只保留字符串里的数字，去掉其他任何奇怪字符。
        # 把字符串 text 里的每一个字符 c 拿出来，判断 c.isdigit() 是否为真（即是否是“数字”0-9），是的话就保留，不是就扔掉。
        return int(text) if text.isdigit() else 0
        # 如果字符串全是数字（isdigit()），就转成整数返回。否则就返回0，表示识别失败。
    # ====== end ======

    # 和上面的read_number不一样的是，这个是建立在paddleocr上的，
    # 在__init__里面需要初始化：self.ocr = PaddleOCR(use_angle_cls=False, lang='en')
    # def read_number(self, img):
    #     img_np = np.array(img)
    #     result = self.ocr.predict(img_np)
    #     print(result[0]['rec_texts'])
    #     text = ''.join([c for c in result[0]['rec_texts'][0] if c.isdigit()])
    #     return int(text) if text.isdigit() else 0



    def get_resource_values(self):
        window_img = self.screenshot_whole_window()

        # 找金币和圣水图标位置
        gold_pos = self.match_icon(window_img, self.gold_template)  # (x, y)
        elixir_pos = self.match_icon(window_img, self.elixir_template)

        # 假设数字区在图标右侧6像素，宽200，高与图标高度一致
        w_gold, h_gold = self.gold_template.shape[::-1]
        w_elixir, h_elixir = self.elixir_template.shape[::-1]

        gold_num_area = (gold_pos[0] + w_gold + 4, gold_pos[1], 200, h_gold)
        elixir_num_area = (elixir_pos[0] + w_elixir + 4, elixir_pos[1], 200, h_elixir)

        gold_img = window_img.crop((gold_num_area[0], gold_num_area[1],
                                    gold_num_area[0] + gold_num_area[2],
                                    gold_num_area[1] + gold_num_area[3]))
        elixir_img = window_img.crop((elixir_num_area[0], elixir_num_area[1],
                                      elixir_num_area[0] + elixir_num_area[2],
                                      elixir_num_area[1] + elixir_num_area[3]))
        # .crop是截图，需要左上角和右下角坐标，(x1, y1, x2, y2)。
        # 这个就是要把刚刚写的区域给截图截下来。

        # ====== 保存刚刚的图，这边是用来调试用的！！回头要删掉或者注释掉 ======
        debug_dir = r"A:\Projects\Coc_VisionBot\debug"
        os.makedirs(debug_dir, exist_ok=True)
        gold_img_path = os.path.join(debug_dir, "debug_gold.png")
        elixir_img_path = os.path.join(debug_dir, "debug_elixir.png")
        if not os.path.exists(gold_img_path):
            gold_img.save(gold_img_path)
        if not os.path.exists(elixir_img_path):
            elixir_img.save(elixir_img_path)
        # ====== end ======

        gold = self.read_number(gold_img)
        elixir = self.read_number(elixir_img)
        return gold, elixir

# 用法示例（写在主脚本里，不要放类文件里）
# reader = ResourceReader()
# gold, elixir = reader.get_resource_values()
# print("金币:", gold, "圣水:", elixir)
