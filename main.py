#не работает, если источник видео используется ещё где-то

#я ебал производительность питона, буду переписывать на плюсах

import pyvirtualcam #pip install pyvirtualcam
import cv2          #pip install opencv-python
import numpy as np
import random

#порог цвета
def threshold(val, a = 128):
    if val > a:
        return 255
    return 0

cap = cv2.VideoCapture(0)
ret, img = cap.read()


#consts
height, width = len(img), len(img[0])
divider = 12 # степень зашакаливанья

dHeight, dWidth = height // divider, width // divider


with pyvirtualcam.Camera(width=dWidth, height=dHeight, fps=20) as cam:
    print(f'Using virtual camera: {cam.device}')
    while True:
        ret, img = cap.read()
        frame = np.zeros((cam.height, cam.width, 3), np.uint8) # RGB
        for i in range(dHeight):
            for j in range(dWidth):
                
                #просто шакаливанье
                frame[i][j][0] = img[i * divider][j * divider][2] #R
                frame[i][j][1] = img[i * divider][j * divider][1] #G
                frame[i][j][2] = img[i * divider][j * divider][0] #B

                #уже преколы
                #if img[i * divider][j * divider][2] > 100:
                #    frame[i][j][0] = img[i * divider][j * divider][2]
                #    frame[i][j][2] = img[i * divider][j * divider][0] / 2
                #if img[i * divider][j * divider][0] < 200:
                #    frame[i][j][1] += img[i * divider][j * divider][1] / 2
                #    frame[i][j][2] += img[i * divider][j * divider][0]
                #frame[i][j][0] += random.randint(0, 5)
                #frame[i][j][1] += random.randint(0, 5)
                #frame[i][j][2] += random.randint(0, 5)


        cam.send(frame)
        cam.sleep_until_next_frame()
