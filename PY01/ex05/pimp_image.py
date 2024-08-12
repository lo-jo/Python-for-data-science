import numpy as np
from load_image import show_image


def ft_invert(array: np.ndarray) -> np.ndarray:
    """Inverts the color of the image received."""
    inverted_array = 255 - array
    show_image(inverted_array, "Inverted")
    return inverted_array


def ft_red(array: np.ndarray) -> np.ndarray:
    """Applies a red filter to an RGB image."""
    red_filtered_array = array.copy()
    red_filtered_array[:, :, 1] = 0
    red_filtered_array[:, :, 2] = 0
    show_image(red_filtered_array, "Red")
    return red_filtered_array


def ft_green(array: np.ndarray) -> np.ndarray:
    """Applies a green filter to an RGB image."""
    green_filtered_array = array.copy()
    green_filtered_array[:, :, 0] = 0
    green_filtered_array[:, :, 2] = 0
    show_image(green_filtered_array, "Green")
    return green_filtered_array


def ft_blue(array: np.ndarray) -> np.ndarray:
    """Applies a blue filter to an RGB image."""
    blue_filtered_array = array.copy()
    blue_filtered_array[:, :, 0] = 0
    blue_filtered_array[:, :, 1] = 0
    show_image(blue_filtered_array, "Blue")
    return blue_filtered_array


def ft_grey(array: np.ndarray) -> np.ndarray:
    """Applies a gray filter to an RGB image."""
    gray_filtered_array = np.dot(array[..., :3], [0.299, 0.5870, 0.1140])
    show_image(gray_filtered_array, "Gray")
    return gray_filtered_array
