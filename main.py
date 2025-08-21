import time
import random
from Class.Strategies.AutoMatchFinder import AutoMatchFinder
from Class.Strategies.AutoClickerInRectRegion import AutoClickerInRectRegion
from Class.Button import Button
from Class.Strategies.AutoFarmLoop import AutoFarmLoop

    # 1. 配置目标查找类
target_judge_func = lambda gold, elixir: (
        gold + elixir >= 500_000 and gold < 2_500_000 and elixir < 2_500_000
    )
auto_match_finder = AutoMatchFinder(
        attack_btn_path = r"D:\python-project\Coc_VisionBot\templates\Home_Village\Attack_Icon\attack_1.png",
        find_match_btn_path = r"D:\python-project\Coc_VisionBot\templates\Find_a_Match.png",
        next_btn_img_path = r"D:\python-project\Coc_VisionBot\templates\next.png",
        target_judge_func = target_judge_func
    )

    # 2. 配置撒兵类
clicker = AutoClickerInRectRegion(
        btn_img_path=r"D:\python-project\Coc_VisionBot\templates\dragon.png",
        region_yaml_path='D:\\python-project\\Coc_VisionBot\\config\\regions.yaml',
        region_name='rectangle_region',
        n_clicks=20,
        btn_y_offset=100
    )

    # 3. 配置 Return Home 按钮模板路径
return_home_btn_path = r"D:\python-project\Coc_VisionBot\templates\return_village\return_home_village.png"

    # 4. 运行主循环
farm = AutoFarmLoop(auto_match_finder, clicker, return_home_btn_path)
farm.run()