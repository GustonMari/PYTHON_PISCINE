import numpy as np
import load_image

def ft_invert(array):
    """Invert the colors of an image array"""
    if array is None:
        return None
    new_array = (255 - array)
    load_image.display_image(new_array)
    return 255 - array

def ft_red(array):
    """Keep only the red channel of an image array"""
    if array is None:
        return None
    result = np.zeros_like(array)
    result[:, :, 0] = array[:, :, 0]
    load_image.display_image(result)
    return result

def ft_green(array):
    """Keep only the green channel of an image array"""
    if array is None:
        return None
    result = np.zeros_like(array)
    result[:, :, 1] = array[:, :, 1]
    load_image.display_image(result)
    return result

def ft_blue(array):
    """Keep only the blue channel of an image array"""
    if array is None:
        return None
    result = np.zeros_like(array)
    result[:, :, 2] = array[:, :, 2]
    load_image.display_image(result)
    return result

def ft_grey(array):
    """Convert an image array to grayscale"""
    if array is None:
        return None
    gray = np.zeros_like(array)
    gray[:, :, 0] = 0.2989 * array[:, :, 0] + 0.5870 * array[:, :, 1] + 0.1140 * array[:, :, 2]
    gray[:, :, 1] = gray[:, :, 0]
    gray[:, :, 2] = gray[:, :, 0]
    load_image.display_image(gray)
    return gray.astype(np.uint8)