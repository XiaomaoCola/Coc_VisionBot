import time
from Class.ButtonFinder import ButtonFinder
from Class.ResourceReader import ResourceReader

if __name__ == "__main__":
    # 1. 点击 attack 按钮
    attack_btn_path = r"D:\python-project\Coc_VisionBot\templates\attack_1.png"
    finder = ButtonFinder(attack_btn_path)
    attack_pos = finder.find_button()
    if attack_pos:
        finder.click_button(attack_pos)
        print("已点击attack按钮")
    else:
        print("没有找到attack按钮，脚本退出")
        exit(1)

    # 2. 等待“Find a Match”按钮出现
    time.sleep(2)  # 视网络延迟自行调整

    # 3. 查找并点击 Find a Match 按钮
    find_match_btn_path = r"D:\python-project\Coc_VisionBot\templates\Find_a_Match.png"
    match_finder = ButtonFinder(find_match_btn_path)
    match_pos = match_finder.find_button()
    if match_pos:
        match_finder.click_button(match_pos)
        print("已点击Find a Match按钮")
    else:
        print("没有找到Find a Match按钮，脚本退出")
        exit(1)

    # 4. 等待对战页面加载
    time.sleep(10)

    # 5. 读取金币和圣水数量
    reader = ResourceReader()
    gold, elixir = reader.get_resource_values()
    print(f"金币: {gold}, 圣水: {elixir}")
