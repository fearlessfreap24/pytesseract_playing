import pytesseract
import cv2
from PIL import Image
import os
import re
import time as t

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

basehight = 560
img = Image.open("./IMG_6493.PNG")
hpercent = (basehight/ float(img.size[1]))
wpercent = int((float(img.size[0]) * float(hpercent)))
img = img.resize((wpercent, basehight), Image.ANTIALIAS)
img.save("./resized_IMG_6493.PNG")

img = cv2.imread("./resized_IMG_6493.PNG")
# img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

h_img, w_img, _ = img.shape
find_medal_name = re.compile("Maverick", re.IGNORECASE)
find_medal_status = re.compile(r"\.394")
image_text = pytesseract.image_to_string(img)
medal = find_medal_name.search(image_text)
if medal:
    medal_status = find_medal_status.search(image_text[medal.start()-50:medal.start()])
    print(f"Found {medal.group(0)}, start = {medal.start()}, end = {medal.end()}")
    if medal_status:
        print(image_text.index(medal_status.group(0)))
    else:
        print(image_text[medal.start()-50:medal.start()])
else:
    print(image_text)

# boxes = pytesseract.image_to_boxes(img)

# for b in boxes.splitlines():
#     b = b.split(" ")
#     x, y, w, h = int(b[1]), int(b[2]), int(b[3]), int(b[4])
#     cv2.rectangle(img, (x, h_img-y), (w, h_img-h), (0,0,255), 2)


# cv2.imshow('Result', img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
# os.remove("./resized_IMG_6493.PNG")

