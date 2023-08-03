import pywt
import numpy as np
from PIL import Image

def Decompression_Process(path):
    # Load compressed image
    image = Image.open(path)
    pixels = np.array(image)

    # Crop the input image to an even number of pixels
    pixels = pixels[:pixels.shape[0]//2*2, :pixels.shape[1]//2*2, :]

    # Perform inverse DWT on each color channel
    coeffs = []
    for channel in range(3):
        cA, (cH, cV, cD) = pywt.dwt2(pixels[:, :, channel],"coif2")
        coeffs.append((cA, (cH, cV, cD)))

    

    # Perform inverse DWT on the thresholded coefficients to obtain the decompressed image
    output_pixels = np.zeros_like(pixels)
    for channel in range(3):
        cA, (cH, cV, cD) = coeffs[channel]
        output_pixels[:, :, channel] = pywt.idwt2((cA, (cH, cV, cD)),"coif2")

    # Add padding to match the size of the compressed image
    pad_width = [(0, pixels.shape[0] - output_pixels.shape[0]), (0, pixels.shape[1] - output_pixels.shape[1]), (0, 0)]
    output_pixels = np.pad(output_pixels, pad_width, mode="edge")

    # Save the decompressed image
    output_image = Image.fromarray(output_pixels.astype("uint8"))
    output_image.save(r"C:\Users\lyric\OneDrive\Desktop\decompressed.jpg")

Decompression_Process(path=r"C:\Users\lyric\OneDrive\Desktop\compressed.jpg")
