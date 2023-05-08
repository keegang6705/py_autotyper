import pyautogui 
import time
#var
path = r"C:\\path_to_text_file\\text.txt"
delay_before_start = 3
type_interval = 0.05

print("open file...")
txt = open(path, "r")
print("prepare for autotyping...")
time.sleep(delay_before_start)
print("start typing...")
for c in txt:
   pyautogui.typewrite(c, interval=type_interval)
   pyautogui.press("enter")
print("end typing")
