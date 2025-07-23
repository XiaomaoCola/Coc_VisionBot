import time
import random
from Class.Button import Button
from Class.BattleArea import BattleArea
from Class.ClickAndDragInRegion import ClickAndDragInRegion

class AutoClickerInRectRegion:
    """
    自动点击指定兵种按钮，并在指定矩形区域内随机点击n次的自动撒兵类。
    """

    def __init__(
        self,
        btn_img_path,
        region_yaml_path,
        region_name,
        n_clicks=20,
        btn_y_offset=100,
    ):
        self.btn_img_path = btn_img_path
        self.region_yaml_path = region_yaml_path
        self.region_name = region_name
        self.n_clicks = n_clicks
        self.btn_y_offset = btn_y_offset

    def run(self):
        # 1. 点击兵种按钮
        button = Button(self.btn_img_path)
        button.find_and_click_button_random(y_offset=self.btn_y_offset)
        time.sleep(random.uniform(0.15, 0.35))  # 默认随机等待

        # 2. 获取下兵区域坐标
        ba = BattleArea(self.region_yaml_path)
        region_tuple = ba.get_coords(self.region_name)

        # 3. 区域内点击
        clicker = ClickAndDragInRegion(region_tuple)
        clicker.random_click(n=self.n_clicks)
        print(f"已在区域 {self.region_name} 内随机点击 {self.n_clicks} 次。")



if __name__ == "__main__":
    auto_clicker = AutoClickerInRectRegion(
        btn_img_path="D:\\python-project\\Coc_VisionBot\\templates\\dragon.png",
        region_yaml_path='D:\\python-project\\Coc_VisionBot\\config\\regions.yaml',
        region_name='rectangle_region',
        n_clicks=20,
        btn_y_offset=100
    )
    auto_clicker.run()

