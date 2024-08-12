import numpy as np
from PIL import Image
from load_image import ft_load
import matplotlib.pyplot as plt

if __name__ == "__main__":
    image_path = "animal.jpeg"
    # Loading the RGB pixels array
    pixels = ft_load(image_path)
    # One example of how the data is stored
    # pixels = np.array([[[255, 100, 0],[198, 250, 3],[85, 45, 78]],
    #                    [[25, 243, 46],[69, 58, 2],[86, 65, 210,]],
    #                    [[53, 8, 0],[0, 0, 0],[0, 0, 0]]
    #                    [[...], [...], [...]]])

    # Generating original image from pixels
    original_image = Image.fromarray(pixels.astype('uint8'))
    # Cutting image (left, top, right, down)
    crop_box = (400, 100, 800, 500)
    cropped_img = original_image.crop(crop_box)
    cropped_array = np.array(cropped_img)
    # The RGB values are converted to grayscale using
    # the NTSC formula: 0.299 ∙ Red + 0.587 ∙ Green + 0.114 ∙ Blue.
    # This formula closely represents the average person's relative
    # perception of the brightness of red, green, and blue light.
    gray_array = np.dot(cropped_array[..., :3], [0.299, 0.5870, 0.1140])
    # Simply put, numpy.newaxis is used to increase the dimension of
    # the existing array by one more dimension, when used once.
    # https://stackoverflow.com/questions/29241056/how-do-i-use-np-newaxis
    gray_array = gray_array[:, :, np.newaxis]
    print(f"The shape of image is: {gray_array.shape}")
    print(gray_array)
    # Saving the shape tuple of gray scale array
    original_shape = gray_array.shape
    # Getting the new shape of transpose image
    transpose_shape = (original_shape[1], original_shape[0], original_shape[2])
    # Creating numpy array empty with the transpose shape
    transposed_array = np.zeros(transpose_shape, dtype=cropped_array.dtype)
    # Transposing the image manually
    for i in range(original_shape[0]):
        for j in range(original_shape[1]):
            for k in range(original_shape[2]):
                transposed_array[j, i, k] = cropped_array[i, j, k]

    rotated_array = transposed_array.reshape(400, 400)
    print(f"New shape after Transpose: {rotated_array.shape}")
    print(rotated_array)
    # Performing change in data representation (casting)
    pixels_array_uint_8 = rotated_array.astype('uint8')
    # Creating image
    image = Image.fromarray(pixels_array_uint_8)
    # Converting image
    plt_image = image.convert("L")
    # matplotlib: lib for data visualization
    # ply: sets Axis Range in Matplotlib

    # Display data as an image, i.e., on a 2D regular raster.
    plt.imshow(plt_image, cmap='gray')
    plt.title("Rotate image")
    plt.savefig('rotated_img.jpg')
