import sys
import cv2
import os
import numpy as np
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes
import hashlib

def encrypt(path,key_name):
    mode = AES.MODE_CBC    
    keySize = 32
    ivSize = AES.block_size if mode == AES.MODE_CBC else 0
    imageOrig = cv2.imread(path)
    rowOrig, columnOrig, depthOrig = imageOrig.shape
    minWidth = (AES.block_size + AES.block_size) // depthOrig + 1
    imageOrigBytes = imageOrig.tobytes()
    #text = input("Enter the text to use as the AES key: ")
    key = hashlib.sha256(key_name.encode()).digest()[:16]
    key_hex = key.hex()

    print(key_hex)
    iv=b'MyFixedKey123456'
    cipher = AES.new(key, AES.MODE_CBC, iv) if mode == AES.MODE_CBC else AES.new(key, AES.MODE_ECB)
    imageOrigBytesPadded = pad(imageOrigBytes, AES.block_size)
    ciphertext = cipher.encrypt(imageOrigBytesPadded)
    paddedSize = len(imageOrigBytesPadded) - len(imageOrigBytes)
    void = columnOrig * depthOrig - ivSize - paddedSize
    ivCiphertextVoid = iv + ciphertext + bytes(void)
    imageEncrypted = np.frombuffer(ivCiphertextVoid, dtype = imageOrig.dtype).reshape(rowOrig + 1, columnOrig, depthOrig)
    cv2.imwrite(r"C:\Users\karth\OneDrive\Desktop\Mini Project\aes_gui_trail.png", imageEncrypted)
    return key_hex
#encrypt(r"C:\Users\karth\OneDrive\Desktop\Mini Project\RSA\c1.jpg")
