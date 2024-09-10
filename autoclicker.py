import pyautogui
from pynput import keyboard

MOUSE_BUTTON = 'left'  # Mouse button to click
CLICK_INTERVAL = 0.1  # Time between clicks in seconds

def on_press(key):
    if key == keyboard.Key.z:
        return False  # Stop the listener

def autoclicker():
    listener = keyboard.Listener(on_press=on_press)
    listener.start()
    
    while True:
        pyautogui.click(button=MOUSE_BUTTON)
        if not listener.is_alive():
            break

autoclicker()
