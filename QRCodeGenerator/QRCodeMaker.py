import qrcode

QR = qrcode.QRCode(version=1,
                   box_size=20,
                   border=1,
                   error_correction=qrcode.constants.ERROR_CORRECT_L)

QR.add_data("https://github.com/JoeHamed")
QR.make()

QRCodeImage = QR.make_image(fill_color="black", back_color="white")
QRCodeImage.save("QRCodeImage.png")

# The version parameter is an integer from 1 to 40 that controls the size of the QR Code

# The error_correction parameter controls the error correction used for the QR Code.
# ERROR_CORRECT_L ---> About 7% or less errors can be corrected.
# ERROR_CORRECT_M ---> About 15% or less errors can be corrected (default).
# ERROR_CORRECT_Q ---> About 25% or less errors can be corrected.
# ERROR_CORRECT_H ---> About 30% or less errors can be corrected.

# The box_size parameter controls how many pixels each “box” of the QR code is.
