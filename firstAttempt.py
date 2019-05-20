import cv2
import numpy as np
import pytesseract
from PIL import Image
from pytesseract import image_to_string
import os

src_path = './images/'

TEST_IMAGE_PATHS = [ os.path.join(src_path, 'photo{}.jpg'.format(i)) for i in range(1, 13) ]

images = []
for i in TEST_IMAGE_PATHS:
    images.append(Image.open(i))
i = 1
detections = []
for image in images:
    imageName = 'image{}'.format(i)
    detectedText = pytesseract.image_to_string(image) 
    detections.append(imageName + ' --> ' + detectedText)
    i += 1

for det in detections:
    print (det)
