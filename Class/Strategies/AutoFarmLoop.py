import time
import random
from Class.Strategies.AutoMatchFinder import AutoMatchFinder
from Class.Strategies.AutoClickerInRectRegion import AutoClickerInRectRegion
from Class.Button import Button

class AutoFarmLoop:
    """
    自动刷资源 + 自动撒兵 + 自动回家 的完整循环流程。
    """

    def __init__(self,auto_match_finder : AutoMatchFinder, clicker: AutoClickerInRectRegion, return_home_btn_path):
        self.auto_match_finder = auto_match_finder
        self.clicker = clicker
        self.return_home_btn_path = return_home_btn_path

    def run(self, max_loops=10000):
        for i in range(1, max_loops+1):
            print(f"\n==== 第 {i} 轮开始 ====")
            # 1. 自动查找目标
            gold, elixir = self.auto_match_finder.run()
            print(f"本轮目标：金币={gold}, 圣水={elixir}")

            # 2. 自动撒兵
            self.clicker.run()

            # 3. 等待2分30秒~3分钟
            sleep_sec = random.uniform(180, 200)
            print(f"等待 {sleep_sec/60:.2f} 分钟（模拟打完一局）")
            time.sleep(sleep_sec)

            # 4. 自动点击Return Home按钮
            print("准备返回主页面...")
            return_btn = Button(self.return_home_btn_path)
            return_btn.find_and_click_button_random(y_offset=150)
            print("已点击 Return Home 按钮")

            # 5. 额外短暂等待，防止太快
            time.sleep(random.uniform(2, 5))
            print(f"==== 第 {i} 轮结束 ====\n")

if __name__ == "__main__":
    # 1. 配置目标查找类
    target_judge_func = lambda gold, elixir: (
        gold + elixir >= 500_000 and gold < 2_500_000 and elixir < 2_500_000
    )
    auto_match_finder = AutoMatchFinder(
        attack_btn_path = r"D:\python-project\Coc_VisionBot\templates\attack_4.png",
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
