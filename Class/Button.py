import pygetwindow as gw
import pyautogui
from PIL import Image
import cv2
import numpy as np
import random
import time

class Button:
    def __init__(self, template_path, threshold=0.8):
        self.template = cv2.imread(template_path, 0)
        self.w, self.h = self.template.shape[::-1]
        self.threshold = threshold

    def find_button(self, screenshot=None):
        if screenshot is None:
            # 查找标题包含 'BlueStacks' 的窗口
            windows = [w for w in gw.getWindowsWithTitle('BlueStacks') if w.visible]
            if not windows:
                raise Exception("No BlueStacks window found.")
            window = windows[0]

            window.activate()
            time.sleep(0.6)

            # 获取窗口位置和大小
            left, top, width, height = window.left, window.top, window.width, window.height
            # 截图窗口区域
            img = pyautogui.screenshot(region=(left, top, width, height))
        else:
            img = Image.open(screenshot)

        img_np = np.array(img)
        img_gray = cv2.cvtColor(img_np, cv2.COLOR_BGR2GRAY)
        # 将截屏转化成灰度图。

        res = cv2.matchTemplate(img_gray, self.template, cv2.TM_CCOEFF_NORMED)
        loc = np.where(res >= self.threshold)
        if len(loc[0]) > 0:
            # 返回第一个匹配点中心
            pt = (loc[1][0] + self.w // 2, loc[0][0] + self.h // 2)
            return pt
        else:
            return None



    def click_button(self, pos):
        if pos is not None:
            pyautogui.moveTo(pos[0], pos[1], duration=0.2)
            pyautogui.click()
            print(f"Clicked at {pos}")
        else:
            print("Button not found.")


    def click_button_random(self, pos, offset_range_x=5, offset_range_y=5, y_offset=0):
        if pos is not None:
            # 在按钮中心附近随机±8像素
            # offset_x = random.randint(-8, +8)
            # offset_y = random.randint(-8, +8)
            # random.randint是取-8到8之间的整数。

            offset_x = random.uniform(-offset_range_x, offset_range_x)
            offset_y = random.uniform(-offset_range_y, offset_range_y)
            # random.uniform是取两数之间的小数。
            # 设置这两个参数offset_range_x, offset_range_y的原因是：不同大小的按钮不同随机点击范围。

            x = pos[0] + offset_x
            y = pos[1] + offset_y + y_offset
            move_time = random.uniform(0.1, 0.35)  # 这里可以根据需要微调范围
            pyautogui.moveTo(x, y, duration=move_time)
            pyautogui.click()

            print(f"Clicked at ({x:.2f}, {y:.2f}) with move_time={move_time:.2f}s")
            # .2f 是 Python 意思是“保留两位小数的浮点数”。
        else:
            print("Button not found.")

    def find_and_click_button_random(self, screenshot=None, offset_range_x=5, offset_range_y=5, y_offset=0):
        """
        组合 find_button 和 click_button_random。
        自动查找按钮并随机偏移点击。
        """
        pos = self.find_button(screenshot)
        self.click_button_random(pos, offset_range_x, offset_range_y, y_offset)