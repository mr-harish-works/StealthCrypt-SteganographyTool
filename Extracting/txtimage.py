import base64
  
def txt_to_image():  
    file = open(r"C:\Users\karth\OneDrive\Desktop\Mini Project\decoded.txt", 'rb')
    byte = file.read()
    file.close()
    decodeit = open(r"C:\Users\karth\OneDrive\Desktop\Mini Project\detect_aes.jpg", 'wb')  
    decodeit.write(base64.b64decode((byte)))
    decodeit.close()
#txt_to_image()