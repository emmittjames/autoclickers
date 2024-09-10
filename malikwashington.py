
import pyautogui
import time
import random
import pyperclip
import math

def script(math):

    # Chrome profile button
    pyautogui.moveTo(1384, 84)
    pyautogui.click()

    time.sleep(0.2)

    # Chrome guest button
    pyautogui.moveTo(1150, 580)
    pyautogui.click()

    time.sleep(0.2)

    # Put in link
    pyautogui.typewrite('biletnikoffaward.com/fan-vote/')

    time.sleep(0.1) 

    # Press enter
    pyautogui.press('enter')

    time.sleep(2)

    # ctrl+f
    pyautogui.hotkey('command', 'f')

    time.sleep(0.1)

    # Search for Malik Washington
    pyautogui.typewrite('Malik Washington')

    time.sleep(0.1)

    # Select Malik Washington
    pyautogui.moveTo(360, 565)
    pyautogui.click()

    time.sleep(0.5)

    # Press enter
    pyautogui.press('enter')

    time.sleep(0.5)

    if math:
        # ctrl+f
        pyautogui.hotkey('command', 'f')

        time.sleep(0.1)

        # Search for math problem
        pyautogui.typewrite('Answer this')

        time.sleep(0.1)

        # Highlight math problem
        pyautogui.moveTo(267, 295)
        pyautogui.mouseDown()
        pyautogui.moveTo(350, 295)
        pyautogui.mouseUp()

        time.sleep(0.1)

        # Copy math problem to clipboard
        pyautogui.hotkey('command', 'c')

        time.sleep(0.1)

        clipboard = pyperclip.paste()
        answer = solve_math(clipboard)

        time.sleep(0.1)

        # Select math problem
        pyautogui.moveTo(360, 335)
        pyautogui.click()
        
        time.sleep(0.1)

        # Type answer
        pyautogui.typewrite(str(answer))

        time.sleep(0.1)

        # Press enter
        pyautogui.press('enter')

    time.sleep(1.5)

    # Exit
    pyautogui.moveTo(315, 45)
    pyautogui.click()

def solve_math(input):
    try:
        # Extract the expression (excluding the "=" sign)
        expression = input.split('=')[0].strip()

        # Use eval() to evaluate the expression
        result = eval(expression)

        # Print the input and the result
        print(input, result)

        global prev
        global errors
        global successes

        if result == prev:
            errors+=1
        else:
            prev = result
            successes+=1

        return result

    except Exception as e:
        # Catch any exceptions and print an error message
        print(f"An error occurred: {e}")
        errors+=1
        return 10

successes = 1
errors = 0
prev = ""
start_time = time.time()

time.sleep(2)

if False:
    for i in range(0, 50):
        for j in range(0, 6):
            print("Iteration:",j)
            script(math=True)
            sleep_time = random.randint(1, 99)
            time.sleep(1)
        print("================================================\nSuccesses:", successes, " | Errors:", errors, " | Total:", successes+errors, "\n================================================")
        time.sleep(120)

if True:
    for i in range(0, 1000):
        script(math=True)
        sleep_time = random.randint(1, 80)
        time.sleep(sleep_time)
        if sleep_time < 10:
            end_time = time.time()
            time_elapsed = int((end_time-start_time)/60)
            ratio = time_elapsed/successes
            print("================================================\nSuccesses:", successes, "| Errors:", errors, "| Total:", successes+errors, "| Time elapsed (mins):", time_elapsed, "| Time (mins)/successes:", ratio, "\n================================================")

#1-80 = 0.9857
#1-75 = 1.1219
#1-70 = 0.9984
#1-65 = 1.0715
#1-60 = 1.0278 

        

# display_coordinates()

def display_coordinates():
    try:
        while True:
            x, y = pyautogui.position()
            print(f"X: {x}, Y: {y}", end='\r')
            time.sleep(0.1)
    except KeyboardInterrupt:
        print("\nCoordinate display stopped.")