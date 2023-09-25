import pyautogui

import time

time.sleep(3)
pixel = pyautogui.position() #pegar posição do seu mouse
print(pixel)

#lembrando, que os pixels vão de acordo com o tamanho de sua tela