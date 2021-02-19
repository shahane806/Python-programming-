import pyautogui

# position of the mouse courser
# pos = pyautogui.position()
# print(pos)

# size of the screen
# siz = pyautogui.size()
# print(siz)


# on the sreen if the element is in the screen then it return 0 or 1 false or true

# screen = pyautogui.onScreen(1180, 400)
# print(screen)

# pyautogui.PAUSE = 2
# pyautogui.moveTo(100, 200)  # Move to X and Y position
# pyautogui.PAUSE = 2
# pyautogui.moveTo(10, 10)

# Quick quiz
# continuously printing the mouse position

# while True:
#     pos = pyautogui.position()
#     print(pos)


# mouse movement
'''
move or moveTo
'''
# pyautogui.move(100, 70)
# pyautogui.moveTo(10, 70)
# pyautogui.moveTo(100, 100, 2, pyautogui.easeInQuad)  # start slow, end fast
# pyautogui.moveTo(100, 100, 2, pyautogui.easeOutQuad)  # start fast, end slow
# pyautogui.moveTo(100, 100, 2, pyautogui.easeInOutQuad)
# start and end fast, slow in middle
# pyautogui.moveTo(100, 100, 2, pyautogui.easeInBounce)  # Bounce at end
# pyautogui.moveTo(100, 100, 2, pyautogui.easeInElastic)
# rubber band at the end

'''
mouse drags
'''

# pyautogui.drag(20, 20)
# pyautogui.dragTo(100, 100, button='left')


'''
mouse clicks
'''
# pyautogui.click()  # single click

# pyautogui.doubleClick(230, 333, 2, button='left')
# pyautogui.tripleClick(230, 333)
# pyautogui.rightClick(230, 333)
# pyautogui.leftClick(230, 333)


'''
mouse fun
'''
# pyautogui.mouseDown(230, 333, button='left', duration=2)
# pyautogui.mouseUp(230, 333, button='left', duration=2)

'''
mouse scroll
'''
# pyautogui.scroll(111)  #Positive number for Up Scroll
# pyautogui.scroll(-111)    #Negative number for Down Scroll

# pyautogui.hscroll(3)
# pyautogui.vrscroll()#does not support to windows


'''
keyboard function
'''

# pyautogui.write('hello',interval=0.10)
# pyautogui.press('enter')


# pyautogui.keyDown('shiftleft') #toggle key
# pyautogui.press('h', presses=5)
# pyautogui.press('e', presses=5)
# pyautogui.press('l', presses=5)
# pyautogui.press('l', presses=5)
# pyautogui.press('o', presses=5)

# pyautogui.keyUp('shiftleft') #unlock key

# pyautogui.hotkey('ctrl', 't') #hotkey is used for presses multi keys


'''
message box
'''
# pyautogui.alert(text='Text', title='alert', button='ok')
# pyautogui.confirm(text='input', title='inputbox', buttons=['ok', 'cancel'])
# pyautogui.prompt(text='input', title='inputbox', default='username')
# password = pyautogui.password(
#     text='Enter your password', title='Password', mask='?')
# print(password)

'''
screenshot
'''
# var = pyautogui.screenshot()
# var.save('my_screenshot.png')

# var = pyautogui.screenshot('my_screen.png', region=(0, 0, 500, 400))
