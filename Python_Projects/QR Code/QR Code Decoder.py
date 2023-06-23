# QR Code Decoder - Project created by Sonia Li

# Install necessary libraries
pip install pyqrcode pypng opencv-python

# Importing libraries
from PIL import Image
from google.colab import files
import cv2
import numpy as np
import matplotlib.pyplot as plt

def qr_decode():

    def read_qrcode():
        # Upload the QR code image file
        uploaded = files.upload()

        # Read the QR code image
        image_path = next(iter(uploaded))
        img = cv2.imread(image_path)
        return img

    try: # Check error by using try-except statement:
        # Call the QR code decoding function
        img = read_qrcode()

        # Create a QR code detector and detect QR code in the image
        det = cv2.QRCodeDetector()
        val, pts, st_code = det.detectAndDecode(img) # By default, detecting QR code in an image requires these three arguments

        while not val:
          print("No QR code detected. Please try again.")
          img = read_qrcode()
          val, pts, st_code = det.detectAndDecode(img)

        else:
          print(f"The result of your QR code is: {val}")

          # Display the QR code image
          plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
          plt.axis('off')
          plt.title("QR Code Image:")
          plt.show()

    except Exception as e:
      print("Error: Failed to read the QR code image file. Please try again")
      print(e)
      qr_decode()

# Call the qr_decode function
if __name__ == '__main__':
  qr_decode()
