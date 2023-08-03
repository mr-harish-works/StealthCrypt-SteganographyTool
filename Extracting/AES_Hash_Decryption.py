import sys
import cv2
import numpy as np
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes
import hashlib
def decrypt(key):
        key = hashlib.sha256(key.encode()).digest()[:16]
        key = key.hex()

        mode = AES.MODE_CBC
        keySize = 32
        ivSize = AES.block_size if mode == AES.MODE_CBC else 0
        imageEncrypted = cv2.imread(r"C:\Users\karth\OneDrive\Desktop\Mini Project\detect_aes.jpg")
        key = bytes.fromhex(key)
        rowEncrypted, columnOrig, depthOrig = imageEncrypted.shape 
        rowOrig = rowEncrypted - 1
        encryptedBytes = imageEncrypted.tobytes()
        iv = b'MyFixedKey123456'
        imageOrigBytesSize = rowOrig * columnOrig * depthOrig
        paddedSize = (imageOrigBytesSize // AES.block_size + 1) * AES.block_size - imageOrigBytesSize
        encrypted = encryptedBytes[ivSize : ivSize + imageOrigBytesSize + paddedSize]
        cipher = AES.new(key, AES.MODE_CBC, iv) if mode == AES.MODE_CBC else AES.new(key, AES.MODE_ECB)
        decryptedImageBytesPadded = cipher.decrypt(encrypted)
        decryptedImageBytes = unpad(decryptedImageBytesPadded, AES.block_size)
        decryptedImage = np.frombuffer(decryptedImageBytes, imageEncrypted.dtype).reshape(rowOrig, columnOrig, depthOrig)
        cv2.imwrite(r"C:\Users\karth\OneDrive\Desktop\Mini Project\nonsteg11_33_59decry.png", decryptedImage)
        cv2.waitKey()
        cv2.destroyAllWindows()
   
#text=input("ENTER THE KEY : ")
#key_digest = hashlib.sha256(text.encode()).digest()[:16]
#aes_key = key_digest.hex()
#decrypt(aes_key)