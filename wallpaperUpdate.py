import requests
import ctypes
import os

# Retrieve image from API
image_url1 = "https://pixabay.com/api/?key=40439767-62fcf0a43d2a3a3b9856f80eb&q=yellow+flowers&image_type=photo&pretty=true"
image_url = "https://picsum.photos/1024/768"
response = requests.get(image_url)
image_path = "temp_image.jpg"

# Save the image locally
with open(image_path, "wb") as f:
    f.write(response.content)

# Set the image as wallpaper
SPI_SETDESKWALLPAPER = 20
ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, os.path.abspath(image_path), 3)

# Delete the temporary image file
os.remove(image_path)
