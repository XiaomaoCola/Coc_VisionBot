from Class.Button import Button
from Class.BattleArea import BattleArea
from Class.ClickAndDragInRegion import ClickAndDragInRegion
import time
import random

if __name__ == "__main__":
    # 1. 找到火龙按钮并点击（假设你已经有火龙按钮的模板图片路径）
    dragon_btn_path = "D:\\python-project\\Coc_VisionBot\\templates\\dragon.png"
    # 你需要替换成自己的模板图片路径
    dragon_button = Button(dragon_btn_path)
    dragon_button.find_and_click_button_random(y_offset= 100)
    time.sleep(random.uniform(0.15, 0.35))  # 稍微等一下，防止点太快

    # 2. 计算下兵区域的屏幕坐标
    ba = BattleArea('config/regions.yaml')
    region_tuple = ba.get_coords('rectangle_region')  # 区域名和yaml里保持一致

    # 3. 区域内撒兵
    click_and_drag_region = ClickAndDragInRegion(region_tuple)
    click_and_drag_region.random_click(n=20)  # 在区域里随机点击20次
