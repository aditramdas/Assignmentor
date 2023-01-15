from PIL import Image, ImageDraw, ImageFont

# Create a blank image with a white background
image = Image.new("RGB", (300, 100), (255, 255, 255))

# Create an ImageDraw object
draw = ImageDraw.Draw(image)

# Define the text you want to convert to handwriting
text = "Hello, World!"

# Define the font and font size
font = ImageFont.truetype("Inkfree.ttf", 36)

# Draw the text on the image
draw.text((10, 10), text, font=font, fill=(0, 0, 0))

# Save the image as a PNG file
image.save("handwriting.png")
