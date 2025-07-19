import time
from Class.Button import Button
from Class.ResourceReader import ResourceReader
from Class.TargetFinder import TargetFinder
import random

if __name__ == "__main__":
    # 1. 随机点击 attack 按钮
    attack_btn_path = r"D:\python-project\Coc_VisionBot\templates\attack_3.png"
    attack_btn = Button(attack_btn_path)
    attack_btn.find_and_click_button_random(offset_range_x=8, offset_range_y=8, y_offset=100)
    print("已点击 attack 按钮")

    # 2. 等待“Find a Match”按钮出现
    sleep_time_wait_Find_a_Match = random.uniform(1.8, 3.2)
    time.sleep(sleep_time_wait_Find_a_Match)
    print(f"等待了 {sleep_time_wait_Find_a_Match:.2f} 秒等待‘Find a Match’按钮出现")

    # 3. 随机点击 Find a Match 按钮
    find_match_btn_path = r"D:\python-project\Coc_VisionBot\templates\Find_a_Match.png"
    match_finder = Button(find_match_btn_path)
    match_finder.find_and_click_button_random(offset_range_x=8, offset_range_y=8, y_offset=100)
    print("已点击 Find a Match 按钮")

    # 4. 等待对战页面加载
    sleep_time_after_Find_a_Match = random.uniform(7, 9)
    time.sleep(sleep_time_after_Find_a_Match)
    print(f"等待了 {sleep_time_after_Find_a_Match:.2f} 秒等待对战页面加载")

    # 5. 自动查找满足条件的目标
    target_judge_func = lambda gold, elixir: gold + elixir >= 2_000_000
    next_btn_img_path = r"D:\python-project\Coc_VisionBot\templates\next.png"
    finder = TargetFinder(target_judge_func, next_btn_img_path)
    gold, elixir = finder.find_target()
    print(f"最终金币: {gold}, 圣水: {elixir}")
