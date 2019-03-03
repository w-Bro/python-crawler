import pytesseract
from PIL import Image


def main():
    pytesseract.pytesseract.tesseract_cmd = r'D:\python\Tesseract-OCR\tesseract.exe'
    while True:
        image = Image.open('./captcha_image/BlackOverlap Captcha Image.jpg')
        text = pytesseract.image_to_string(image)
        print(text)
        break


if __name__ == '__main__':
    main()