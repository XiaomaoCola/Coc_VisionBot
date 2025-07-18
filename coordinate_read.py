import pyautogui
import time

print("Move your mouse. Press Ctrl+C to quit.")
try:
    while True:
        x, y = pyautogui.position()
        print(f"X: {x}  Y: {y}", end="\r")
        time.sleep(0.05)
except KeyboardInterrupt:
    print("\nDone.")