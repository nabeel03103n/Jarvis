# importing the libraries
import cv2
import pytesseract

# setting the path of pytesseract exe
# you have to write the location of
# on which your tesseract was installed
pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

# Now we will read the image in our program
# you have to put your image path in place of photo.jpg
img = cv2.imread('code.jpg')

# Our image will read as BGR format,
# So we will convert in RGB format because
# tesseract can only read in RGB format
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# For getting the text and number from image
print(pytesseract.image_to_string(img))

# For displaying the original image
cv2.imshow("result", img)
cv2.waitKey(0)
