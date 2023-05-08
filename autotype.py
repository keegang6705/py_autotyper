import pyautogui 
import time
print("open file...")
txt = open(r"C:\\path_to_text_file\\text.txt", "r")
print("prepare for autotyping...")
time.sleep(5)
print("start typing...")
for c in txt:
   pyautogui.typewrite(c, interval=0.05)
   pyautogui.press("enter")
print("end typing")
