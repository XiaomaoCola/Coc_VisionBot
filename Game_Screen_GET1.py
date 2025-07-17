import pygetwindow as gw
import pyautogui
import datetime
import os
import time

def screenshot_bluestacks(save_dir=r"D:\python-project\Coc_VisionBot\screenshots"):
    os.makedirs(save_dir, exist_ok=True)
    windows = [w for w in gw.getWindowsWithTitle("BlueStacks") if w.visible]
    if not windows:
        print("没有找到 BlueStacks 窗口")
        return
    window = windows[0]
    window.activate()   # 把 BlueStacks 窗口前置
    time.sleep(0.3)     # 给一点时间让窗口刷新到前面
    left, top, width, height = window.left, window.top, window.width, window.height
    img = pyautogui.screenshot(region=(left, top, width, height))
    now = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    save_path = os.path.join(save_dir, f"screenshot_{now}.png")
    img.save(save_path)
    print(f"已保存窗口截图：{save_path}")

if __name__ == "__main__":
    screenshot_bluestacks()
