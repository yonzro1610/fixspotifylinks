import pyperclip
import keyboard

def test():
    print(pyperclip.paste())
    
keyboard.add_hotkey('ctrl+v', test)