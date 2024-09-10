import pyautogui

def main():
    pyautogui.moveTo(1384, 84)
    pyautogui.sleep(0.1)
    pyautogui.click()

    pyautogui.moveTo(1200, 660)
    pyautogui.sleep(0.1)
    pyautogui.click()

    pyautogui.sleep(0.2)
    pyautogui.moveTo(600, 84)
    pyautogui.click()
    pyautogui.typewrite('https://allstatesugarbowl.org/news/2024/9/9/manning-stars.aspx')
    pyautogui.press('enter')
    pyautogui.sleep(7)

    pyautogui.moveTo(350, 700)
    pyautogui.click()
    pyautogui.sleep(1.5)

    pyautogui.moveTo(306, 43)
    pyautogui.click()

if __name__ == '__main__':
        pyautogui.sleep(5)
        while pyautogui.pixel(700, 550) == (249, 251, 253):
             main()