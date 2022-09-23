# importing Libraries
import cv2
from matplotlib import pyplot as plt
import numpy as np

# set path



drive.mount('/content/drive', force_remount=True)
!ls
"/content/drive/My Drive/Required Files"

Mounted
at / content / drive
car.jpg
frames
'Ice Car.mp4'
cars.xml
haarcascade_russian_plate_number.xml

# import dependencies
% matplotlib
inline
import os

data = os.listdir('../content/drive/My Drive/Required Files')
data

['cars.xml',
 'haarcascade_russian_plate_number.xml',
 'car.jpg',
 'Ice Car.mp4',
 'frames']

lic_data = cv2.CascadeClassifier('../content/drive/My Drive/Required Files/haarcascade_russian_plate_number.xml')


def plt_show(image, title="", gray=False, size=(100, 100)):
    temp = image
    if gray == False:
        temp = cv2.cvtColor(temp, cv2.COLOR_BGR2RGB)
        plt.title(title)
        plt.imshow(temp, cmap='gray')
        plt.show()


def detect_number(img):
    temp = img
    gray = cv2.cvtColor(temp, cv2.COLOR_BGR2GRAY)
    number = lic_data.detectMultiScale(img, 1.2)
    print("number plate detected:" + str(len(number)))
    for numbers in number:
        (x, y, w, h) = numbers
        roi_gray = gray[y:y + h, x:x + w]
        roi_color = img[y:y + h, x:x + h]
        cv2.rectangle(temp, (x, y), (x + w, y + h), (0, 255, 0), 3)

    plt_show(temp)


# Take input of car image with number plate
img = cv2.imread("../content/drive/My Drive/Required Files/car.jpg")
plt_show(img)
detect_number(img)

number
plate
detected: 1

plt.subplot(1, 1, 1), plt.imshow(img)

(< matplotlib.axes._subplots.AxesSubplot at 0x7f25db51bdd8 >,
 < matplotlib.image.AxesImage at 0x7f25db4c82e8 >)

import cv2 as cv
from google.colab.patches import cv2_imshow

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2_imshow(gray)

import numpy as np

kernel = np.ones((5, 5), np.uint8)
erosion = cv2.erode(img, kernel, iterations=1)

plt.subplot(1, 1, 1), plt.imshow(erosion)
plt.title('Morphological Transformation/Erosion'), plt.xticks([]), plt.yticks([])
plt.show()

import imutils

image = img
ratio = image.shape[0] / 500.0
orig = image.copy()
image = imutils.resize(image, height=500)

# convert the image to grayscale, blur it, and find edges
# in the image
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
gray = cv2.GaussianBlur(gray, (5, 5), 0)
edged = cv2.Canny(gray, 75, 200)

# show the original image and the edge detected image
print("STEP 1: Edge Detection")
cv2_imshow(image)
cv2_imshow(edged)

satisfied: Pillow in / usr / local / lib / python3
.6 / dist - packages(7.0
.0)
Requirement
already
satisfied: pytesseract in / usr / local / lib / python3
.6 / dist - packages(0.3
.7)
Requirement
already
satisfied: Pillow in / usr / local / lib / python3
.6 / dist - packages(
from pytesseract) (7.0.0)

img = cv2.resize(img, (620, 480))
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # convert to grey scale

gray = cv2.bilateralFilter(gray, 13, 15, 15)

edged = cv2.Canny(gray, 30, 200)  # Perform Edge detection
cv2_imshow(edged)

contours = cv2.findContours(edged.copy(), cv2.RETR_TREE,
                            cv2.CHAIN_APPROX_SIMPLE)
contours = imutils.grab_contours(contours)
contours = sorted(contours, key=cv2.contourArea, reverse=True)[:10]
screenCnt = None

for c in contours:
    # approximate the contour
    peri = cv2.arcLength(c, True)
    approx = cv2.approxPolyDP(c, 0.018 * peri, True)
    # if our approximated contour has four points, then
    # we can assume that we have found our screen
    if len(approx) == 4:
        screenCnt = approx
        break

if screenCnt is None:
    detected = 0
    print("No contour detected")
else:
    detected = 1

if detected == 1:
    cv2.drawContours(img, [screenCnt], -1, (0, 0, 255), 3)

# Masking the part other than the number plate
mask = np.zeros(gray.shape, np.uint8)
new_image = cv2.drawContours(mask, [screenCnt], 0, 255, -1, )
new_image = cv2.bitwise_and(img, img, mask=mask)
cv2_imshow(new_image)

# Now crop
(x, y) = np.where(mask == 255)
(topx, topy) = (np.min(x), np.min(y))
(bottomx, bottomy) = (np.max(x), np.max(y))
Cropped = gray[topx:bottomx + 1, topy:bottomy + 1]

plt.imshow(Cropped, cmap='gray');

# Read the number plate
text = pytesseract.image_to_string(Cropped, config='--psm 11')
print("Detected license plate Number is:", text)

