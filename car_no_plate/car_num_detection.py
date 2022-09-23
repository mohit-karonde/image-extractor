# Import dependencies
import cv2
import numpy as np
import matplotlib.pyplot as plt
#from matplotlib import inline
import pytesseract

    # Set tesseract path to where the tesseract exe file is located (Edit this path accordingly based on your own settings)
   # pytesseract.pytesseract.tesseract_cmd = r'D:\Program Files\Tesseract-OCR\tesseract.exe'


    # Read car image and convert color to RGB
    carplate_img = cv2.imread("resouces/car_image.png")

    carplate_img_rgb = cv2.cvtColor(carplate_img, cv2.COLOR_BGR2RGB)


    plt.imshow(carplate_img_rgb);


    # Function to enlarge the plt display for user to view more clearly
    def enlarge_plt_display(image, scale_factor):
        width = int(image.shape[1] * scale_factor / 100)
        height = int(image.shape[0] * scale_factor / 100)
        dim = (width, height)
        plt.figure(figsize = dim)
        plt.axis('off')
        plt.imshow(image)


    enlarge_plt_display(carplate_img_rgb, 1.2)


    # Import Haar Cascade XML file for Russian car plate numbers
    carplate_haar_cascade = cv2.CascadeClassifier('/car_no_plate/haar_cascades/haarcascade_russian_plate_number.xml')


    # Setup function to detect car plate
    def carplate_detect(image):
        carplate_overlay = image.copy()  # Create overlay to display red rectangle of detected car plate
        carplate_rects = carplate_haar_cascade.detectMultiScale(carplate_overlay, scaleFactor=1.1, minNeighbors=5)

        for x, y, w, h in carplate_rects:
            cv2.rectangle(carplate_overlay, (x, y), (x + w, y + h), (255, 0, 0), 5)

        return carplate_overlay

    detected_carplate_img = carplate_detect(carplate_img_rgb)
    enlarge_plt_display(detected_carplate_img, 1.2)


    # Function to retrieve only the car plate sub-image itself
    def carplate_extract(image):
        carplate_rects = carplate_haar_cascade.detectMultiScale(image, scaleFactor=1.1, minNeighbors=5)

        for x, y, w, h in carplate_rects:
            carplate_img = image[y + 15:y + h - 10, x + 15:x + w - 20]

        return carplate_img




    # Enlarge image for further image processing later on
    def enlarge_img(image, scale_percent):
        width = int(image.shape[1] * scale_percent / 100)
        height = int(image.shape[0] * scale_percent / 100)
        dim = (width, height)
        resized_image = cv2.resize(image, dim, interpolation = cv2.INTER_AREA)
        return resized_image

    # Display extracted car license plate image
    carplate_extract_img = carplate_extract(carplate_img_rgb)
    carplate_extract_img = enlarge_img(carplate_extract_img, 150)
    plt.imshow(carplate_extract_img);





    # Convert image to grayscale
    carplate_extract_img_gray = cv2.cvtColor(carplate_extract_img, cv2.COLOR_RGB2GRAY)
    plt.axis('off')
    plt.imshow(carplate_extract_img_gray, cmap = 'gray');

    # Apply median blur + grayscale
    carplate_extract_img_gray_blur = cv2.medianBlur(carplate_extract_img_gray,3) # Kernel size 3
    plt.axis('off')
    plt.imshow(carplate_extract_img_gray_blur, cmap = 'gray');

    # Display the text extracted from the car plate
    print(pytesseract.image_to_string(carplate_extract_img_gray_blur,config = f'--psm 8 --oem 3 -c tessedit_char_whitelist=ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'))


    for i in range(3,14):
        print(f'PSM: {i}')
        print(pytesseract.image_to_string(carplate_extract_img_gray_blur,config = f'--psm {i} --oem 3 -c tessedit_char_whitelist=ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'))


