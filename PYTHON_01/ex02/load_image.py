from PIL import Image
import os
import numpy as np

# def ft_load(path: str) -> list:
def ft_load(path: str):
    """Load an image and return it as a numpy array"""
    # path = "ksjdk.mpeg"
    if not path.endswith(".jpg") | path.endswith(".jpeg"):
        raise TypeError("Only .jpg files are supported")
    assert os.path.exists(path), "File does not exist"
    try:
        image = Image.open(path)

        # Print the image format
        # print("Image format:", image.format)
        
        np_image = np.array(image)
        print("The shape of image is:",np_image.shape)
        for x in np_image:
            print(x)
        # Get the pixel data
        pixels = image.load()

        # Print the pixel content in RGB format
        # width, height = image.size
        # for y in range(height):
        #     for x in range(width):
        #         r, g, b = pixels[x, y]
        #         print(f"Pixel at ({x}, {y}): RGB({r}, {g}, {b})")

        # Show the image
        # image.show()
    except FileNotFoundError:
        print("File not found!")
    except AssertionError as error:
        print(error)
    return np_image