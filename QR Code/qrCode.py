# Imports library for QR Code
import qrcode

# Takes user input for the text to be converted into QR Code image
user_input = str(input("Type your text here for QR Code Generation: "))

# Creates the QR Code
img = qrcode.make(user_input)

# Saves the QR Code as JPG (image) file
img.save("QRcode.jpg")