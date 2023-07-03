from PIL import Image
import os
import numpy as np
from zoom import ft_zoom

# def ft_load(path: str) -> list:
# def ft_load():
#     """Load an image and return it as a numpy array"""
#     path = "animal.jpeg"
#     if not path.endswith(".jpg") | path.endswith(".jpeg"):
#         raise TypeError("Only .jpg files are supported")
#     assert os.path.exists(path), "File does not exist"
#     try:
#         image = Image.open(path)

#         # Print the image format
#         # print("Image format:", image.format)
        
#         np_image = np.array(image)
#         print("The shape of image is:",np_image.shape)
#         for x in np_image:
#             print(x)
#         # Get the pixel data
#         pixels = image.load()

#     except FileNotFoundError:
#         print("File not found!")
#     except AssertionError as error:
#         print(error)
#     return np_image



def load_image():
    """Load an image from file path"""
    file_path = "animal.jpeg"
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

def display_image(image, zoom_factor):
    """Display the image after applying zoom"""
    if image:
        width, height = image.size
        zoomed_width = int(width * zoom_factor)
        zoomed_height = int(height * zoom_factor)

        zoomed_image = image.resize((zoomed_width, zoomed_height))

        print("Pixel Content:")
        # pixels = zoomed_image.load()
        # for y in range(zoomed_height):
        #     for x in range(zoomed_width):
        #         r, g, b = pixels[x, y]
        #         print(f"Pixel at ({x}, {y}): RGB({r}, {g}, {b})")
        zoomed_image = ft_zoom(image, zoom_factor)
    
        print("New shape after slicing: (400, 400, 1) or (400, 400)")
        print_image_info(zoomed_image)
        
        zoomed_image.show()

if __name__ == "__main__":
    zoom_factor = 4.0

    image = load_image()
    print_image_info(image)
    display_image(image, zoom_factor)