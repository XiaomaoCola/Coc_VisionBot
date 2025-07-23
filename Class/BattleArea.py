import yaml
import pygetwindow as gw

class BattleArea:
    """
    从config/regions.yaml 中拿到设置，
    """

    def __init__(self, yaml_path):
        with open(yaml_path, 'r', encoding='utf-8') as f:
            self.areas_yaml = yaml.safe_load(f)

    def _get_bluestacks_topleft(self):
        window = [w for w in gw.getWindowsWithTitle('BlueStacks') if w.visible][0]
        return window.left, window.top

    def get_coords(self, area_name):
        """返回指定区域的实际像素坐标(tuple: 左上x, 左上y, 右下x, 右下y)"""
        if area_name not in self.areas_yaml:
            raise ValueError(f"区域名 {area_name} 不存在！")
            # raise 是专门用来主动“抛出”一个异常（exception），让程序中断或者提醒出现了严重问题。
            # ValueError表示“传入的值不对、不符合预期”。
        d = self.areas_yaml[area_name]
        if d['type'] != 'rectangle':
            raise NotImplementedError("当前只支持矩形区域！")
            # NotImplementedError 表示“这个功能还没实现，或者不支持这种用法”。

        x0, y0 = self._get_bluestacks_topleft()
        return (x0 + d['x1'], y0 + d['y1'], x0 + d['x2'], y0 + d['y2'])
