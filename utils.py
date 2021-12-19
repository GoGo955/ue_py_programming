"""
Helper module containing used functions
"""
import glob
import cv2
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'


def read_text_from_image(path: str) -> str:
    """
    Function returns text from given image.
    Parameters:
        path (str): image's path
    Returns:
        string from image
    """
    conv_img = clean_img(path)
    return pytesseract.image_to_string(conv_img)


def clean_img(path: str):
    """
    docstr
    """
    img = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
    # img_converted = cv2.threshold(cv2.GaussianBlur(img, (5, 5), 0), 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]
    # img_converted = cv2.threshold(cv2.bilateralFilter(img, 5, 75, 75), 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]
    # img_converted = cv2.threshold(cv2.medianBlur(img, 3), 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]
    # img_converted = cv2.adaptiveThreshold(cv2.GaussianBlur(img, (5, 5), 0), 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 31, 2)
    # img_converted = cv2.adaptiveThreshold(cv2.bilateralFilter(img, 9, 75, 75), 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 31, 2)
    img_converted = cv2.adaptiveThreshold(cv2.medianBlur(img, 3), 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 31, 2)
    return img_converted

def print_images_text() -> None:
    """
    Function prints out text read from images from pics folder.
    """
    for pic in glob.glob('pics/*'):
        print(f'Text read from {pic} is:')
        print(read_text_from_image(pic))
        print(20 * '*')
