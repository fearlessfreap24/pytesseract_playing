from tkinter.messagebox import NO
from typing import Any, List
import cv2
import os
import numpy as np
import datetime as dt

def cut_images(cols: int = 1, rows:int = 1, image: Any = "") -> List:
    images = []
    height = image.shape[0]//(rows)
    width = image.shape[1]//(cols)
    for x in range(0, rows):
        for y in range(0, cols):
            print(f"top right = {x}, {y}, height {(x+1)*height}, width {(y+1)*width}")
            sub_image = image[x*height:(x+1)*height, y*width:(y+1)*width]
            images.append(sub_image)

    return images


if __name__ == "__main__":
    image = cv2.imread(os.path.join(os.getenv("userprofile"), "missions", "wcp", "caboose_cropped.png"))
    print(image.shape[0], image.shape[1])
    images = cut_images(6, 2, image)
    for i in range(len(images)):
        save_folder = os.listdir(os.path.join(os.getenv("userprofile"), "missions", "wcp"))
        save_file = f"caboose_{i}.png"
        now = dt.datetime.now()
        if save_file in save_folder:
            save_file = f"{save_file.split('.')[0]}_{now.year}{now.month}{now.day}{now.hour}{now.minute}.{save_file.split('.')[1]}"
        cv2.imwrite(os.path.join(os.getenv("userprofile"), "missions", "wcp", save_file), images[i])