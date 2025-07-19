import time
from Class.ResourceReader import ResourceReader
from Class.Button import Button
import random

class TargetFinder:
    def __init__(self, target_judge_func, next_btn_img_path):
        """
        :param target_judge_func: 目标判定函数，参数为 (gold, elixir, ...) 返回 True 表示达标
        :param next_btn_img_path: next 按钮模板路径
        """
        self.target_judge_func = target_judge_func
        self.next_btn_img_path = next_btn_img_path
        self.reader = ResourceReader()
        self.next_finder = Button(self.next_btn_img_path)

    def find_target(self):
        while True:
            gold, elixir = self.reader.get_resource_values()
            print(f"金币: {gold}, 圣水: {elixir}")

            if self.target_judge_func(gold, elixir):
                print("目标已满足，脚本结束！")
                return gold, elixir

            # print("目标未满足，点击 next...")
            # next_pos = self.next_finder.find_button()
            # adjusted_next_pos =  (next_pos[0], next_pos[1] + 100)
            # if next_pos:
            #     self.next_finder.click_button(adjusted_next_pos)
            # else:
            #     print("找不到 next 按钮，脚本退出")
            #     return gold, elixir

            clicked_pos = self.next_finder.find_and_click_button_random(offset_range_x=8, offset_range_y=8, y_offset=100)
            if clicked_pos is None:
                print("找不到 next 按钮，脚本退出")
                return gold, elixir



            time.sleep(random.uniform(6, 8))


# def my_target_judge(gold, elixir):
#     return gold + elixir >= 2_000_000
#
# finder = TargetFinder(my_target_judge, r"D:\python-project\Coc_VisionBot\templates\next.png")
# gold, elixir = finder.find_target()
# print(f"达标：金币={gold}, 圣水={elixir}")
