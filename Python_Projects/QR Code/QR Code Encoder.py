# QR Code Encoder - Project created by Sonia Li

# Install necessary libraries
pip install pyqrcode pypng opencv-python

# Importing libraries
from PIL import Image
import pyqrcode
import png
import matplotlib.pyplot as plt

# Generates a QR code image using the provided data and saves it to the given image path.
def generate_qr_code(data, image_path, scale=6):  # The scale parameter controls the size of the QR code image.
    url = pyqrcode.create(data)
    url.png(image_path, scale=scale)

# Displays the QR code image located at the given image path using matplotlib.
def display_qr_code(image_path):
    qr_image = Image.open(image_path)
    plt.imshow(qr_image)
    plt.axis('off')
    plt.show()

def main():
    # Get input data from the user
    data = input("Please enter the data to encode as a QR code: ")

    # Generate and save the QR code image
    generate_qr_code(data, "qrcode.png")

    print("Here your QR code!")

    # Display the QR code image
    display_qr_code("qrcode.png")

if __name__ == '__main__':   # execute only if run as a script
    main()
