import time
from Class.Button import Button
from Class.ResourceReader import ResourceReader
from Class.TargetFinder import TargetFinder

if __name__ == "__main__":
    # 1. 点击 attack 按钮
    attack_btn_path = r"/templates/attack_2.png"
    attack_btn = Button(attack_btn_path)
    attack_pos = attack_btn.find_button()
    if attack_pos:
        adjusted_attack_pos = (attack_pos[0], attack_pos[1] + 100)
        attack_btn.click_button(adjusted_attack_pos)
        print("已点击attack按钮")
    else:
        print("没有找到attack按钮，脚本退出")
        exit(1)

    # 2. 等待“Find a Match”按钮出现
    time.sleep(2)  # 视网络延迟自行调整

    # 3. 查找并点击 Find a Match 按钮
    find_match_btn_path = r"/templates/Find_a_Match.png"
    match_finder = Button(find_match_btn_path)
    match_pos = match_finder.find_button()
    if match_pos:
        # pos[0] 是x坐标，pos[1]是y坐标
        adjusted_match_pos = (match_pos[0], match_pos[1] + 100)
        match_finder.click_button(adjusted_match_pos)
        print("已点击Find a Match按钮（向下偏移100像素）")
    else:
        print("没有找到Find a Match按钮，脚本退出")
        exit(1)

    # 4. 等待对战页面加载
    time.sleep(10)

    # 实例化资源识别器（不循环的时候用下面三行代码）
    # reader = ResourceReader()
    # gold, elixir = reader.get_resource_values()
    # print(f"金币: {gold}, 圣水: {elixir}")


    # 5. 使用 TargetFinder 自动查找满足条件的目标
    target_judge_func = lambda gold, elixir: gold + elixir >= 2_000_000
    next_btn_img_path = r"/templates/next.png"

    finder = TargetFinder(target_judge_func, next_btn_img_path)
    gold, elixir = finder.find_target()
    print(f"最终金币: {gold}, 圣水: {elixir}")
