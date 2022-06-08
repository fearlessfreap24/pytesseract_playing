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
    

if __name__ == "__main__":
    image_path = r"C:\Users\dylan\missions\blanco"
    image_name = "TAC-made Blanco County Seal.png"
    images = {"seal": (353, 318, 1056, 1054)}
    image = cv2.imread(j(image_path, image_name))
    for img in images:
        img_nums = get_crop_numbers(images[img][0], images[img][1],
            images[img][2], images[img][3], (200,200))
        cropped_image = image[img_nums["top"]:img_nums["height"], \
            img_nums["left"]:img_nums["width"]] # [top:top + height, left:left + width]
        cv2.imshow("Cropped", cropped_image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        cv2.imwrite(j(image_path, f"{img}.jpg"), cropped_image)