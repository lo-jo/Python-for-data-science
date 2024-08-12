from load_image import ft_load
from PIL import Image
import matplotlib.pyplot as plt
import numpy as np


def zoom_image(image: np.ndarray) -> Image:
    """
    Zooms the given image and displays it.

    Args:
        image (np.ndarray): The image to be zoomed,
        represented as a NumPy array.
    """
    try:
        # crop_box: left, upper, right, bottom
        crop_box = (400, 100, 800, 500)
        zoomed_img = image.crop(crop_box)

        # getbands: Returns a tuple containing the name of each band
        # ex. on an RGB image returns ("R", "G", "B").
        num_channels = len(zoomed_img.getbands())

        # Draw scale on the image
        # convert the image zoomed_img to grayscale "L" shape
        truc = zoomed_img.convert("L")

        # matplotlib: lib for data visualization
        # ply: sets Axis Range in Matplotlib
        plt.imshow(truc, cmap='gray')
        plt.title("Zoomed image")
        plt.savefig('zoomed_img.jpg')

        return zoomed_img, zoomed_img.size, num_channels

    except Exception as e:
        print(f"Error: {e}")
        return None


def main():
    image_path = "animal.jpeg"

    # Load image
    image = ft_load(image_path)
    if image is not None:
        print(image)
        # Convert the NumPy array back to an image
        # (by converting the data type of the array image
        # to unsigned 8-bit integers) ensuring that the array
        # elements are in the correct range and data type expected
        # by PIL when creating the image object
        sliced_image = Image.fromarray(image.astype('uint8'))

        # Zoom image
        zoomed_img, zoomed_img_size, num_channels = zoom_image(sliced_image)
        if zoomed_img is not None:
            print("Image Information:")
            print(f"\nZoomed image size: {zoomed_img_size}")
            print(f"Number of channels: {num_channels}")
            print(f"\nNew shape after slicing: {zoomed_img.size}")

            # Retrieving and displaying pixels array and zoomed image
            zoom_image_pixel_content = np.array(zoomed_img)
            print("Zoomed image pixel content:")
            print(zoom_image_pixel_content)


if __name__ == "__main__":
    main()
