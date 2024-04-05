import qrcode as QR
import image

qr = QR.QRCode(version=15, box_size=10, border=5)


data = "https://nikhil-jaiz.github.io/Resume/"
qr.add_data(data)

qr.make(fit=True)

img = qr.make_image(fill_color="black", back_color="white")


img.save("My_QR.png")