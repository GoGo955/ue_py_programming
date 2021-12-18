"""
Helper module containing used functions
"""
import glob
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
    return pytesseract.image_to_string(path)


def print_images_text() -> None:
    """
    Function prints out text read from images from pics folder.
    """
    for pic in glob.glob('pics/*'):
        print(f'Text read from {pic} is:')
        print(read_text_from_image(pic))
        print(20 * '*')
