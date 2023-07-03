from PIL import Image
import os
import numpy as np
import pimp_image


def load_image(file_path: str):
    """Load an image from file path"""
    try:
        image = Image.open(file_path)

        return image
    except IOError:
        print("Unable to load image")
        return None

def print_image_info(image):
    """Print information about the image"""
    if image:
        width, height = image.size
        channels = len(image.getbands())

        print("Image Information:")
        print(f"Size: {width} x {height} pixels")
        print(f"Number of Channels: {channels}")
        np_image = np.array(image)
        print("The shape of image is:",np_image.shape)
        # for x in np_image:
        #     print(x)

def display_image(array):
    """Display the image"""
    # Convert the array to an image
    image = Image.fromarray(array)

    # Display the image
    image.show()

def ft_load(path: str):

    image = load_image(path)
    np_image = np.array(image)
    # print_image_info(image)
    # display_image(image)
    return np_image