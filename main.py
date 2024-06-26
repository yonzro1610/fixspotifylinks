import pyperclip
import keyboard
import time

def modify_spotify_url(url):
    parts = url.split('/')
    if len(parts) > 3 and 'intl-' in parts[3]:
        parts.pop(3)
    return '/'.join(parts)

def monitor_clipboard():
    recent_value = ""
    while True:
        time.sleep(0.5)
        clipboard_content = pyperclip.paste()
        if clipboard_content != recent_value:
            recent_value = clipboard_content
            modified_url = modify_spotify_url(clipboard_content)
            if modified_url != clipboard_content:
                pyperclip.copy(modified_url)
                print(f"Modified URL: {modified_url}")

def on_paste():
    clipboard_content = pyperclip.paste()
    modified_url = modify_spotify_url(clipboard_content)
    if modified_url != clipboard_content:
        pyperclip.copy(modified_url)
        print(f"Modified URL: {modified_url}")

if __name__ == "__main__":
    try:
        print("Monitoring clipboard for Spotify URLs...")
        keyboard.add_hotkey('ctrl+v', on_paste)
        monitor_clipboard()
    except KeyboardInterrupt:
        exit(1)