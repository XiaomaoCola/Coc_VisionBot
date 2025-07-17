import pygetwindow as gw
import pyautogui
import datetime
import os

def screenshot_bluestacks(save_dir=r"D:\python-project\Coc_VisionBot\screenshots"):
    # 确保保存目录存在
    os.makedirs(save_dir, exist_ok=True)

    # 查找BlueStacks窗口
    windows = [w for w in gw.getWindowsWithTitle("BlueStacks") if w.visible]
    if not windows:
        print("没有找到 BlueStacks 窗口")
        return

    window = windows[0]
    left, top, width, height = window.left, window.top, window.width, window.height
    img = pyautogui.screenshot(region=(left, top, width, height))

    # 保存图片，文件名带时间戳
    now = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    save_path = os.path.join(save_dir, f"screenshot_{now}.png")
    img.save(save_path)
    print(f"已保存窗口截图：{save_path}")

if __name__ == "__main__":
    screenshot_bluestacks()
