import cv2
import pytesseract
from pyautogui import screenshot
# from PIL import Image

screenshot(imageFilename="ReferenceImage.png")
# image = Image.open("ReferenceImage.png")
#
# imageBox = image.getbbox()
# croppedImage = image.crop(imageBox)
# croppedImage.save("Cropped_ReferenceImage.png")


img = cv2.imread("ReferenceImage.png")
print(type(img))

# Shape of the image
print("Shape of the image", img.shape)

# [rows, columns]
crop = img[50:180, 100:300]

# cv2.imshow('cropped', crop)
cv2.imwrite("cv2_cropped_ReferenceImage.png", crop)
converted_text = pytesseract.image_to_string(crop)
print(converted_text)
cv2.waitKey(0)
cv2.destroyAllWindows()

