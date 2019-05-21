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
    src_path, 'photo{}.jpg'.format(i)) for i in range(1, 17)]

images = []
for i in TEST_IMAGE_PATHS:
    old_image = Image.open(i)
    new_size = tuple(2*x for x in old_image.size)
    new_image = old_image.resize(new_size, Image.ANTIALIAS)
    images.append(new_image)





CORRECT_LICENSE = ['171NVX75', 'ZH247640', '819KXH75', 'DU748BH', 'SHD3164', 'KI43GC', 'LJ465H2', '325J521',
                   'ZG2877J', 'BEJ5345', 'SK253CL', 'ZG655UR', 'ZG7871S', 'ZG829I', 'VŽ0909MD', 'ZG884AM', 'RI681GN',
                    'RI373KI', 'ZG877TF', 'ZG637LV','ZG4513R','PE59FT','ZG5715AK','ZG4269AC','MA398AG','066A007','EDAL551','BJ100EE','KC538AG','ZD539CH','ZG3585AI']



  # Define config parameters.
  # '-l eng'  for using the English language
  # '--oem 1' sets the OCR Engine Mode to LSTM only.
  #
  #  There are four OCR Engine Mode (oem) available
  #  0    Legacy engine only.
  #  1    Neural nets LSTM engine only.
  #  2    Legacy + LSTM engines.
  #  3    Default, based on what is available.
  #
  #  '--psm 3' sets the Page Segmentation Mode (psm) to auto.
#  Other important psm modes will be discussed in a future post.  

config0 = (' --psm 6 --oem 1 load_system_dawg F load_freq_dawg F')
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
predictions = []
for imPath in TEST_IMAGE_PATHS:
    total = total + 1

    im = cv2.imread(imPath)
    gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)

    # Apply dilation and erosion to remove some noise
    kernel = np.ones((1, 1), np.uint8)
    gray = cv2.dilate(gray, kernel, iterations=1)
    gray = cv2.erode(gray, kernel, iterations=1)

    ima = cv2.adaptiveThreshold(
        gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 2)

    

    text1 = re.sub(r'\W+', '', pytesseract.image_to_string(gray, config=config0))
    text2 = re.sub(r'\W+', '', pytesseract.image_to_string(gray, config=config1))
    text3 = re.sub(r'\W+', '', pytesseract.image_to_string(gray, config=config2))
    text4 = re.sub(r'\W+', '', pytesseract.image_to_string(gray, config=config3))
    text5 = re.sub(r'\W+', '', pytesseract.image_to_string(gray, config=config4))
    text6 = re.sub(r'\W+', '', pytesseract.image_to_string(gray, config=config5))
    text7 = re.sub(r'\W+', '', pytesseract.image_to_string(gray, config=config6))
    text8 = re.sub(r'\W+', '', pytesseract.image_to_string(gray, config=config7))

    predictions.append(text1)
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


w=10
h=5
fig=plt.figure(figsize=(8, 8))
columns = 4
rows = 4
for i in range(1, len(images)+1):
    img = images[i-1]
    ax=fig.add_subplot(rows, columns, i)
    predict = predictions[i-1]
    ax.set_title(predict)
    plt.imshow(img)
plt.show()