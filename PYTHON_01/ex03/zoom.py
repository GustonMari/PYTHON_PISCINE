from PIL import Image

# def ft_zoom(image, zoom_factor) -> Image:
#     width, height = image.size
#     zoomed_width = int(width * zoom_factor)
#     zoomed_height = int(height * zoom_factor)

#     zoomed_image = image.resize((zoomed_width, zoomed_height))

#     print("Pixel Content:")
#     pixels = zoomed_image.load()
#     # for y in range(zoomed_height):
#     #     for x in range(zoomed_width):
#     #         r, g, b = pixels[x, y]
#     #         print(f"Pixel at ({x}, {y}): RGB({r}, {g}, {b})")
#     return zoomed_image

def ft_zoom(img, zoom):
    """Zoom on the center of the image"""
    x = img.width / 2
    y = img.height / 2
    w, h = img.size
    zoom2 = zoom * 2
    img = img.crop((x - w / zoom2, y - h / zoom2, 
                    x + w / zoom2, y + h / zoom2))
    return img.resize((w, h), Image.LANCZOS)