import time
import random
from Class.Button import Button
from Class.TargetFinder import TargetFinder

class AutoMatchFinder:
    """
    可以自动查找目标，当资源数满足一定要求的时候，会停止程序。

    用法示例:
        target_judge_func = lambda gold, elixir: gold + elixir >= 2000000 and gold < 2500000 and elixir < 2500000
        auto = AutoMatchFinder(
            attack_btn_path = r"...",
            find_match_btn_path = r"...",
            next_btn_img_path = r"...",
            target_judge_func = target_judge_func
        )
        gold, elixir = auto.run()
        print(f"最终金币: {gold}, 圣水: {elixir}")
    """

    def __init__(self, attack_btn_path, find_match_btn_path, next_btn_img_path, target_judge_func):
        self.attack_btn_path = attack_btn_path
        self.find_match_btn_path = find_match_btn_path
        self.next_btn_img_path = next_btn_img_path
        self.target_judge_func = target_judge_func

    def run(self):
        # 1. 随机点击 attack 按钮
        attack_btn = Button(self.attack_btn_path)
        attack_btn.find_and_click_button_random(offset_range_x=8, offset_range_y=8, y_offset=100)
        print("已点击 attack 按钮")

        # 2. 等待“Find a Match”按钮出现
        sleep_time_before_Find_a_Match = random.uniform(1.8, 3.2)
        time.sleep(sleep_time_before_Find_a_Match)
        print(f"等待了 {sleep_time_before_Find_a_Match:.2f} 秒等待‘Find a Match’按钮出现")

        # 3. 随机点击 Find a Match 按钮
        match_finder = Button(self.find_match_btn_path)
        match_finder.find_and_click_button_random(offset_range_x=8, offset_range_y=8, y_offset=150)
        print("已点击 Find a Match 按钮")

        # 4. 等待对战页面加载
        sleep_time_after_Find_a_Match = random.uniform(7, 9)
        time.sleep(sleep_time_after_Find_a_Match)
        print(f"等待了 {sleep_time_after_Find_a_Match:.2f} 秒等待对战页面加载")

        # 5. 自动查找满足条件的目标
        finder = TargetFinder(self.target_judge_func, self.next_btn_img_path)
        gold, elixir = finder.find_target()
        print(f"最终金币: {gold}, 圣水: {elixir}")
        return gold, elixir

if __name__ == "__main__":
    target_judge_func = lambda gold, elixir: (
        gold + elixir >= 1_000_000 and gold < 2_500_000 and elixir < 2_500_000
    )
    auto = AutoMatchFinder(
        attack_btn_path = r"D:\python-project\Coc_VisionBot\templates\attack.png",
        find_match_btn_path = r"D:\python-project\Coc_VisionBot\templates\Find_a_Match.png",
        next_btn_img_path = r"D:\python-project\Coc_VisionBot\templates\next.png",
        target_judge_func = target_judge_func
    )
    gold, elixir = auto.run()
    print(f"最终金币: {gold}, 圣水: {elixir}")