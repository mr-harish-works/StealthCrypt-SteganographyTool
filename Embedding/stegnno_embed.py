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

def hide_data_in_image(file_path,imp):
    #imp=r"C:\Users\karth\OneDrive\Desktop\Mini Project\cover1.jpg"
    opath=r"C:\Users\karth\OneDrive\Desktop\Mini Project\gui_trail_steg.png"

    image = Image.open(imp)
    pixels = np.array(image)
    
    # Read binary data from file
    with open(file_path, 'rb') as file:
        binary_data = file.read()
    
    # Convert binary data to binary string
    binary_string = ''.join(format(byte, '08b') for byte in binary_data)
    # Check if image has enough capacity to hide binary data
    if len(binary_string) > pixels.size:
        raise ValueError("Image does not have enough capacity to hide binary data.")
    binary_index = 0
    for i in range(pixels.shape[0]):
        for j in range(pixels.shape[1]):
            for k in range(pixels.shape[2]):
                if binary_index < len(binary_string):
                    pixel = pixels[i][j][k]
                    pixel_binary = format(pixel, '08b')
                    pixel_binary = pixel_binary[:-1] + binary_string[binary_index]
                    pixels[i][j][k] = binary_to_decimal(pixel_binary)
                    binary_index += 1

    # Save the modified image to output path
    modified_image = Image.fromarray(pixels)
    modified_image.save(opath)
    print("Successful")
#hide_data_in_image(r"C:\Users\karth\Downloads\kailash\aes27txt_trail.txt")