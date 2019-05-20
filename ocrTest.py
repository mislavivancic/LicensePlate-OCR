import cv2
import sys
import pytesseract
import numpy as np
from pytesseract import image_to_string
from PIL import Image
import os
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import re
from skimage import data
from skimage.filters import threshold_otsu


src_path = './images/'

TEST_IMAGE_PATHS = [os.path.join(
    src_path, 'photo{}.jpg'.format(i)) for i in range(1, 32)]

images = []
for i in TEST_IMAGE_PATHS:
    images.append(Image.open(i))

CORRECT_LICENSE = ['171NVX75', 'ZH247640', '819KXH75', 'DU748BH', 'SHD3164', 'KI43GC', 'LJ465H2', '325J521',
                   'ZG2877J', 'BEJ5345', 'SK253CL', 'ZG655UR', 'ZG7871S', 'ZG829I', 'VŽ0909MD', 'ZG884AM', 'RI681GN',
                    'RI373KI', 'ZG877TF', 'ZG637LV','ZG4513R','PE59FT','ZG5715AK','ZG4269AC','MA398AG','066A007','EDAL551','BJ100EE','KC538AG','ZD539CH','ZG3585AI']

config0 = (' --psm 6 --oem 3 load_system_dawg F load_freq_dawg F')
config1 = (' --psm 7 --oem 3 load_system_dawg F load_freq_dawg F')
config2 = (' --psm 8 --oem 3')
config3 = (' --psm 9 --oem 3')
config4 = (' --psm 10 --oem 3')
config5 = (' --psm 11 --oem 3')
config6 = (' --psm 12 --oem 3')
config7 = (' --psm 13 --oem 3')



#config = ('-c tessedit_char_whitelist=0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ --psm 6 ')

#-c tessedit_char_whitelist=0123456789abcdefghijklmnopqrstuvwxyz
total = 0
guess = 0
correctGuess = 0
for imPath in TEST_IMAGE_PATHS:
    total = total + 1

    im = cv2.imread(imPath)
    gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)

    ima = cv2.adaptiveThreshold(
        gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 2)

    #imgplot = plt.imshow(ima)
    # plt.show()

    text1 = re.sub(r'\W+', '', pytesseract.image_to_string(gray, config=config0))
    text2 = re.sub(r'\W+', '', pytesseract.image_to_string(gray, config=config1))
    text3 = re.sub(r'\W+', '', pytesseract.image_to_string(gray, config=config2))
    text4 = re.sub(r'\W+', '', pytesseract.image_to_string(gray, config=config3))
    text5 = re.sub(r'\W+', '', pytesseract.image_to_string(gray, config=config4))
    text6 = re.sub(r'\W+', '', pytesseract.image_to_string(gray, config=config5))
    text7 = re.sub(r'\W+', '', pytesseract.image_to_string(gray, config=config6))
    text8 = re.sub(r'\W+', '', pytesseract.image_to_string(gray, config=config7))
    #print (imPath," -> ",text)

    #print(imPath, " \n", re.sub(r'\W+', '', text1), "\n", re.sub(r'\W+', '',
    #                                                             text2), "\n", re.sub(r'\W+', '', text3), '\n',re.sub(r'\W+', '', text4), '\n'
    #                                                                 ,re.sub(r'\W+', '', text5), '\n',re.sub(r'\W+', '', text6), '\n'
    #                                                                     ,re.sub(r'\W+', '', text7), '\n',re.sub(r'\W+', '', text8),
    #                                                                          '\n', CORRECT_LICENSE[total-1])

    print(imPath, " \n", text1, "\n", text2, "\n", text3, '\n',text4,'\n',text5, '\n', text6, '\n',text7, '\n', text8,'\n',CORRECT_LICENSE[total-1])


    if  text1 == CORRECT_LICENSE[total-1]:
        correctGuess += 1
        print ("EQUAL")

    print()
    print("-------------------------------")
    print()

    #if text1:
    #    guess = guess + 1

print("All: ", total)
print("Guess: ", correctGuess)
print(correctGuess, "/", total, " = ", correctGuess/total)

imgplot = plt.imshow(im)