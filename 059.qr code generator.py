# QR Code generator using python
import qrcode
data = input('Enter data for QR code:  ')
qr = qrcode.make(data)
qr.show()