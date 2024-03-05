import pyqrcode
from pyqrcode import QRCode
s = str(input("What would you like to display in your QR code? "))
qrCode = pyqrcode.generate(s)
qrCode.svg("myqr.png", scale = 8)
