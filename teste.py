import pyautogui, time
time.sleep(20) 
texto = open('texto.txt', encoding='utf-8')
for frase in texto:
    pyautogui.typewrite(frase)
    pyautogui.press('enter')
  