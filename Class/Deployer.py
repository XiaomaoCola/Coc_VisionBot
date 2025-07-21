import time
import random

class Deployer:
    def __init__(self, button, click_and_drag_in_region):
        self.button = button
        self.click_and_drag_in_region = click_and_drag_in_region

    def select_and_random_click(self, n=1):
        self.button.find_and_click_button_random()
        time.sleep(random.uniform(0.15, 0.4))
        self.click_and_drag_in_region.random_click(n)

    def select_and_random_drag(self, n=1):
        self.button.find_and_click_button_random()
        time.sleep(random.uniform(0.15, 0.4))
        self.click_and_drag_in_region.random_drag(n)

