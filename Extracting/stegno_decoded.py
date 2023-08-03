from PIL import Image
import numpy as np

# Function to convert binary to decimal
def binary_to_decimal(binary):
    decimal = 0
    for bit in binary:
        decimal = decimal * 2 + int(bit)
    return decimal

# Function to convert decimal to binary
def decimal_to_binary(decimal):
    binary = bin(decimal)[2:]
    return '0' * (8 - len(binary)) + binary
def extract_data_from_image(image_path):
    output_file=r"C:\Users\karth\OneDrive\Desktop\Mini Project\decoded.txt"
    image = Image.open(image_path)
    pixels = np.array(image)

    # Extract binary data from image pixels
    binary_string = ""
    for i in range(pixels.shape[0]):
        for j in range(pixels.shape[1]):
            for k in range(pixels.shape[2]):
                pixel = pixels[i][j][k]
                pixel_binary = format(pixel, '08b')
                binary_string += pixel_binary[-1]

    # Convert binary string to bytes
    binary_data = bytearray()
    for i in range(0, len(binary_string), 8):
        byte = binary_to_decimal(binary_string[i:i+8])
        binary_data.append(byte)

    # Write binary data to output file
    with open(output_file, 'wb') as file:
        file.write(binary_data)

    print("Binary data has been successfully extracted from the image.")
#extract_data_from_image(r"C:\Users\karth\Downloads\CISCDjango\CISC\static\Images\steg.jpg" )