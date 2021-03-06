import cv2
from os.path import join as j
from os import getenv


def get_crop_numbers(top: int, left:int, bottom:int, right:int, padding: tuple) -> dict:
    item_width = right - left
    item_height = bottom - top
    padding_width = padding[0] // 2
    padding_height = padding[1] // 2
    crop_numbers = {}
    crop_numbers["left"] = left - padding_width
    crop_numbers["width"] = left + item_width + padding_width
    crop_numbers["top"] = top - padding_height
    crop_numbers["height"] = top + item_height + padding_height
    return crop_numbers


def get_from_center(mid_h:int, mid_v: int, square:int) -> tuple:
    top = mid_v - (square//2)
    left = mid_h - (square//2)
    top_h = top + square
    left_w = left + square
    return (top, top_h, left, left_w)

if __name__ == "__main__":
    image_path = r"/home/dylan/Downloads"
    image_name = "blanco-sp-sign.jpg"
    images = {"brown2": get_from_center(535, 171, 150)}
    print(j(image_path, image_name))
    image = cv2.imread(j(image_path, image_name))
    for img in images:
        # img_nums = get_crop_numbers(images[img][0], images[img][1],
        # #     images[img][2], images[img][3], (200,200))
        cropped_image = image[images[img][0]:images[img][1], images[img][2]:images[img][3]] # [top:top + height, left:left + width]
        cv2.imshow("Cropped", cropped_image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        cv2.imwrite(j(image_path, f"{img}.jpg"), cropped_image)
        # print(images[img])