from Class.ButtonFinder import ButtonFinder
from PIL import Image

if __name__ == '__main__':
    # 1. 指定模板图片路径
    template_path = 'C:\\Users\\LuluL\\Desktop\\SharedFiles\\attack.png'  # 记得放在 Coc_VisionBot 主目录或写绝对路径
    finder = ButtonFinder(template_path)

    # 2. 找按钮并返回位置
    pos = finder.find_button()
    print(f"按钮位置: {pos}")


    finder.click_button(pos)