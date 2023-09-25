import pyautogui
#pausa de 2seg entre os comandos, para não dar erro
pyautogui.PAUSE = 2

#Abrir o sistema, ferramenta ou programa
pyautogui.press("win") #abrir o pesquisa windows
pyautogui.write("Instagram") #escrever no pesquisa
pyautogui.press("backspace") #macete para reconhecer o que foi digitado
pyautogui.press('enter') #abrir o programa

#preencher o login
import time
time.sleep(2)

pyautogui.click(x=925, y=293)
pyautogui.write("jubelasco21@gmail.com")

#preencher a senha
pyautogui.click(x=881, y=358)
pyautogui.write("soueubb1234!")

#clicar em fazer login
pyautogui.click(x=889, y=417)

#lembrando, que os pixels vão de acordo com o tamanho de sua tela