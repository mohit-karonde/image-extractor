import  cv2
import  numpy as np
img = cv2.imread("resources/IMG_3458-01.jpeg")
img = cv2.resize(img,(640,480))

cv2.imshow("image", img)


print("shape==",img.shape)
print("size==",img.size)
print("datatype++",img.dtype)
print("imagtype",type(img))

#lets split image into differant chnnel

print(cv2.split(img))


b, g, r = cv2.split(img)
"""
cv2.imshow("B",b)
cv2.imshow("G",g)
cv2.imshow("R",r)
"""

img1 = cv2.merge((b,g,r))
cv2.imshow("BGR",img1)

img2 = cv2.merge((r, g, b))
cv2.imshow("RGB",img2)

img3 = cv2.merge((g, b, r))
cv2.imshow("GBR",img3)


cv2.waitKey(10000)
cv2.destroyAllWindows()