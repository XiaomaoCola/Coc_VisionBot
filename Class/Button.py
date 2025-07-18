import pygetwindow as gw
import pyautogui
from PIL import Image
import cv2
import numpy as np
import random

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
            # 获取窗口位置和大小
            left, top, width, height = window.left, window.top, window.width, window.height
            # 截图窗口区域
            img = pyautogui.screenshot(region=(left, top, width, height))
        else:
            img = Image.open(screenshot)
        img_np = np.array(img)
        img_gray = cv2.cvtColor(img_np, cv2.COLOR_BGR2GRAY)
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


    def click_button_random(self, pos):
        if pos is not None:
            # 在按钮中心附近随机±5像素
            offset_x = random.randint(-5, 5)
            offset_y = random.randint(-5, 5)
            x = pos[0] + offset_x
            y = pos[1] + offset_y
            pyautogui.moveTo(x, y, duration=0.2)
            pyautogui.click()
            print(f"Clicked at ({x}, {y})")
        else:
            print("Button not found.")