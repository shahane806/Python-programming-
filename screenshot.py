import pyautogui

if __name__ == '__main__':
    snap = pyautogui.screenshot()
    snap.save('snapshot.png')
