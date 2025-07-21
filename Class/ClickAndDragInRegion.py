import pyautogui
import random
import time

class ClickAndDragInRegion:
    def __init__(self, region):
        """
        region: (x1, y1, x2, y2) 区域左上和右下像素坐标。
        如果是这样定义的话，这个class目前只支持长方形区域。
        
        """
        self.x1, self.y1, self.x2, self.y2 = region

    def _random_point(self):
        # 单下划线开头（_xxx），在python里面代表这个方法是“内部用的”，建议只在类的内部用，不建议在类外部直接用。
        x = random.randint(self.x1, self.x2)
        y = random.randint(self.y1, self.y2)
        return x, y

    def random_click(self, n=1):
        for _ in range(n):
        # 可以写成for i in range(5):，但是i在这边是用不到的。
        # 所以换成下划线的这行代码的意思是：循环 n 次，但每次循环都不需要用到循环变量。
            x, y = self._random_point()
            move_time = random.uniform(0.1, 0.3)
            pyautogui.moveTo(x, y, duration=move_time)
            pyautogui.click()
            print(f"Click at ({x},{y})  用时 {move_time:.2f}s")
            time.sleep(random.uniform(0.15, 0.35))

    def random_drag(self, n=1):
        for _ in range(n):
            x1, y1 = self._random_point()
            x2, y2 = self._random_point()
            move_time1 = random.uniform(0.1, 0.25)
            move_time2 = random.uniform(0.15, 0.4)
            pyautogui.moveTo(x1, y1, duration=move_time1)
            pyautogui.mouseDown()
            print(f"MouseDown at ({x1},{y1})")
            time.sleep(random.uniform(0.08, 0.15))
            pyautogui.moveTo(x2, y2, duration=move_time2)
            pyautogui.mouseUp()
            print(f"Drag to ({x2},{y2})  用时 {move_time2:.2f}s")
            time.sleep(random.uniform(0.18, 0.4))

# =======================
# 用法示例
if __name__ == "__main__":
    region = (120, 480, 320, 900)  # 改成你实际区域
    click_and_drag_region = ClickAndDragInRegion(region)
    click_and_drag_region.random_click(n=6)    # 区域内随机点6次
    # click_and_drag_region.random_drag(n=2)   # 区域内随机拖动2次
