from python_imagesearch import imagesearch
import time
import keyboard
import pyautogui

while True:

    time.sleep(0.5)

    canavar_1 = imagesearch.imagesearch("mtn_1.png")
    canavar_2 = imagesearch.imagesearch("mtn_2.png")
    canavar_3 = imagesearch.imagesearch("mtn_3.png")
    canavar1_x = canavar_1[0]
    canavar1_y = canavar_1[1]
    canavar2_x = canavar_2[0]
    canavar2_y = canavar_2[1]
    canavar3_X = canavar_3 [0]
    canavar3_y = canavar_3[1]
    print (canavar_1)
    print (canavar_2)
    print (canavar_3)


if canavar1_x != -1:
  pyautogui.moveTo(canavar1_x+30, canavar1_y+60)
  time.sleep(0.4)
  pyautogui.click (canavar_1_x+30, canavar1_y+60)
  time.sleep(35)

if canavar2_x != -1:
   pyautogui.moveTo(canavar2_x+30, canavar2_y+60)
   time.sleep(0.4)
   pyautogui.click(canavar2_x+30,canavan2_y+60)
   time.sleep(35)

if canavar3_x != -1:
  pyautogui.moveTo(canavar3_x+30, canavar3_y+68)
  time.sleep(0.4)
  pyautogul.click (canavar3_x+30,canavar3_y+60)
  time.sleep(35)

  if canavar1_x == -1 and canavar2_x == -1:
   if canavar3_x == -1:
      keyboard.press ("e")
      keyboard.release("e")
      keyboard.press("e")
      time.sleep(0.3)
      keyboard.release("e")
      time.sleep(0.5)
      keyboard.press("g")
      keyboard.release("g")

      keyboard.press("g")
      time.sleep(1.5)
      keyboard.release("g")
      time.sleep(0.5)
      keyboard.press("t")
      keyboard.release("t")

      keyboard.press("t")
      time.sleep(0.7)
      keyboard.release("t")
      time.sleep(0.5)
      keyboard.press("f")
      keyboard.release("f")

      keyboard.press("f")
      time.sleep(0.5)
      keyboard.release("f")
      time.sleep(0.5)
