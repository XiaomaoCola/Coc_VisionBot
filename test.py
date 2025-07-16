from Class.ButtonFinder import ButtonFinder
from PIL import Image

if __name__ == '__main__':
    # 1. 指定模板图片路径
    template_path = 'C:\\Users\\LuluL\\Desktop\\SharedFiles\\attack.png'  # 记得放在 Coc_VisionBot 主目录或写绝对路径
    finder = ButtonFinder(template_path)

    # 2. 找按钮并返回位置
    pos = finder.find_button()
    print(f"按钮位置: {pos}")





    # 3. 截图并保存一份，方便人工验证
    # 使用 find_button 内部的 pyautogui.screenshot(region=...) 逻辑自己再调用一次
    import pygetwindow as gw
    import pyautogui

    windows = [w for w in gw.getWindowsWithTitle('BlueStacks') if w.visible]
    if not windows:
        raise Exception("No BlueStacks window found.")
    window = windows[0]
    left, top, width, height = window.left, window.top, window.width, window.height
    img = pyautogui.screenshot(region=(left, top, width, height))
    img.save('bluestacks_window.png')
    print("已保存 BlueStacks 窗口截图为 bluestacks_window.png")
