from PIL import Image
import numpy as np


def ft_load(path: str) -> np.ndarray:
    """
    DESCRIPTION :
    Function that loads an image, prints its format, and its pixels
    content in RGB format.

    OUTPUT :
    A 3D array representing the image's pixels in RGB:
    The first dimension represents the height (number of rows).
    The second dimension represents the width (number of columns).
    The third dimension represents the RGB color channels for each pixel.

    ACCESSING ELEMENTS:
    To access a specific pixel and its RGB values:
    pixels_array[x, y] = RGB tuple for the pixel at position (x, y).
    pixels_array[x, y, 0] = red value of the pixel at (x, y).
    pixels_array[x, y, 1] = green value of the pixel at (x, y).
    pixels_array[x, y, 2] = blue value of the pixel at (x, y).
    """
    pixels = []
    my_image = Image.open(path)
    width = my_image.width
    height = my_image.height
    try:
        if my_image.format not in ["JPEG", "JPG"]:
            raise AssertionError("Format not supported")
        else:
            print(f"IMAGE FORMAT : {my_image.format}")
            # ASSERTION ERROR SUR LE FORMAT
            # Extracting the pixel data into a list
            pixels = list(my_image.getdata())
            # Converting list into NumPy array,
            # Reshaping it from a 1D array to a 3D array
            # 3: indicates that each pixel has 3 values:
            # One for each color channel: Red, Green, and Blue.
            pixels = np.array(pixels).reshape(height, width, 3)
            print(f"The shape of image is : {pixels.shape}")
    except AssertionError as e:
        print(e)
        exit(1)

    return pixels
