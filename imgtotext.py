from PIL import Image
import pytesseract
pytesseract.pytesseract.tesseract_cmd = r'C:\Users\gauth\AppData\Local\Programs\Tesseract-OCR\tesseract.exe'
image1=Image.open('1.png')
text=pytesseract.image_to_string(image1)
print(text)
