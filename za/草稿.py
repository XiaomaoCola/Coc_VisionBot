import yaml
import pygetwindow as gw

class Region:
    def __init__(self, name, type_, data):
        self.name = name
        self.type = type_
        self.data = data  # 矩形：dict，三角形：list等

    def get_absolute(self, x0, y0):
        """返回区域在屏幕上的绝对坐标（加上窗口左上角偏移）"""
        if self.type == 'rectangle':
            # 叠加bluestacks左上角
            return (
                x0 + self.data['x1'],
                y0 + self.data['y1'],
                x0 + self.data['x2'],
                y0 + self.data['y2']
            )
        elif self.type == 'triangle':
            # 三角形点也加偏移
            return [
                [x0 + p[0], y0 + p[1]] for p in self.data['points']
            ]
        else:
            raise NotImplementedError(f"不支持的区域类型: {self.type}")

# 读取yaml并实例化Region
def load_regions(yaml_path):
    with open(yaml_path, 'r', encoding='utf-8') as f:
        regions_yaml = yaml.safe_load(f)
    regions = {}
    for name, d in regions_yaml.items():
        type_ = d['type']
        data = {}
        if type_ == 'rectangle':
            data = {k: d[k] for k in ('x1', 'y1', 'x2', 'y2')}
        elif type_ == 'triangle':
            data = {'points': d['points']}
        regions[name] = Region(name, type_, data)
    return regions

def get_bluestacks_topleft():
    window = [w for w in gw.getWindowsWithTitle('BlueStacks') if w.visible][0]
    return window.left, window.top

# 用法演示
if __name__ == "__main__":
    regions = load_regions('regions.yaml')
    x0, y0 = get_bluestacks_topleft()
    # 获取 main_deploy 区域的绝对坐标
    main_deploy_abs = regions['main_deploy'].get_absolute(x0, y0)
    print("主下兵区绝对坐标:", main_deploy_abs)
    # 获取 triangle_test 区域的绝对坐标
    triangle_abs = regions['triangle_test'].get_absolute(x0, y0)
    print("三角形区域绝对坐标:", triangle_abs)
