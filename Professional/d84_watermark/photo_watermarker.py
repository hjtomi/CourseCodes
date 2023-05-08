import tkinter.filedialog as fd
from PIL import Image


path = fd.askopenfilename(initialdir="/",
                          title="Select file",
                          filetypes=(('png files', "*.png"), ('All file', '*.*')))


# Load the image and the watermark
image = Image.open(path)
watermark = Image.open("watermark.png")

# Resize the watermark to fit the image
image_width, image_height = image.size
scaling_factor = 0.1

if image_width < image_height:
    watermark_size = int(image_width * scaling_factor)
else:
    watermark_size = int(image_height * scaling_factor)

watermark = watermark.resize((watermark_size, watermark_size))

# Blend the images
position = (image.width - watermark.width, image.height - watermark.height)
image.paste(watermark, position, watermark)

# Save the result
image.save("watermarked_image.png")
