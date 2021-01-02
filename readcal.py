from PIL import Image
import pytesseract
pytesseract.pytesseract.tesseract_cmd = r'C:\Users\gauth\AppData\Local\Programs\Tesseract-OCR\tesseract.exe'
image1=Image.open('2.png')
text=pytesseract.image_to_string(image1)
a, b, c=text.split()
a=int(a)
b=int(b)

if c=="+":
    print(a+b)
elif c=="-":
    print(a-b)
elif c=="*":
    print(a*b)
elif c=="/":
    print(a/b)
elif c=="**":
    print(a**b)
elif c=="//":
    print(a//b)

