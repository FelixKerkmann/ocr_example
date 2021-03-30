# This is a sample Python script.

# Press Umschalt+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import cv2
import pytesseract

# after the installation you have to set the path directly to the executable (Windows)
pytesseract.pytesseract.tesseract_cmd = r'C:\Users\felix.kerkmann\AppData\Local\Programs\Tesseract-OCR\tesseract.exe'

img_path_1 = "pdf_bild_test.jpg"
img_path_2 = "pdf_bild_test.png"
img_path_3 = "fallnummer_test.png"
img_path_4 = "fallnummer_test2.png"
img_path_5 = "fallnummer_test3.png"

numbers = "0123456789"

# turns the picture into a string
def picturetotext(path):

    img = cv2.imread(path)
    return pytesseract.image_to_string(img)

# extracts all substrings beginning with 00
def extractfnr(text):

    count = text.count("00")
    nrs = list(range(count))
    index = 0
    start = 0
    end = len(text)

    while count != 0:
        # extract Fallnummer
        beg = text.find("00", start, end)
        endspace = text.find(" ", beg, end)
        endnewline = text.find("\n", beg, end)
        endfn = min(endspace, endnewline)
        nr = text[beg:endfn]
        if nr.isnumeric() and len(nr) == 10:
            nrs[index] = nr
        else:
            nrs.remove(nrs[-1])

        count = count - 1
        index = index + 1
        start = beg+11

    return nrs


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    text = picturetotext(img_path_5)
    fnrs = extractfnr(text)
    print(fnrs)


# See PyCharm help at https://www.jetbrains.com/help/pycharm/

