import cv2
import time
import pyautogui
import numpy as np
import keyboard

image = cv2.imread('1.jpg')
height, width, channels = image.shape
print(f"Разрешение: {width}x{height}")
Y = 500
X = int((width * Y) / height)

resized_image = cv2.resize(image, (X, Y))


gray_image = cv2.cvtColor(resized_image, cv2.COLOR_BGR2GRAY)
# Бинарный 

_, binary_image = cv2.threshold(gray_image, 128, 255, cv2.THRESH_BINARY)


binary_array = np.where(binary_image == 0, 0, 1)


#print(binary_array)
'''

binary_image = np.zeros_like(gray_image)

for i in range(gray_image.shape[0]):
    for j in range(gray_image.shape[1]):
        if gray_image[i, j] > 200:
            binary_image[i, j] = 0  # белый
        elif gray_image[i, j] > 150:
            binary_image[i, j] = 1  # светло-серый
        elif gray_image[i, j] > 100:
            binary_image[i, j] = 2  # темно-серый
        else:
            binary_image[i, j] = 3  # черный


print(binary_image)
'''


def on_press_w(event):
    x = 200#700
    y = 100#320
    xi = x
    h = 3

    icop = 0
    if event.name == 'w':
        for i in binary_array:
            for i2 in i:
                if i2 == 0:
                    time.sleep(0.01)
                    print(1)
                    #pyautogui.mouseDown(button='left')
                    pyautogui.click(x, y, _pause=False)
                    #pyautogui.moveTo(x, y, _pause=False) 
                #elif i2 != 0:
                    #pyautogui.mouseUp(button='left')

                #icop = i2    
                x += h
            x = xi
            y += h

keyboard.on_press(on_press_w)

keyboard.wait('esc')

              
'''
                if i2 != icop:
                    if i2 == 1:
                        pyautogui.click(528, 441, _pause=False)
                    if i2 == 2:
                        pyautogui.click(535, 441, _pause=False)
                    if i2 == 3:
                        pyautogui.click(486, 441, _pause=False)
'''
