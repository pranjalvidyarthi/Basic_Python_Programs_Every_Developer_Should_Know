# QR Code generator using python
import qrcode

qr = qrcode.make("https://www.youtube.com/@pranjaltechnology")

qr.show()
