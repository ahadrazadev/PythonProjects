import qrcode

Qrcode = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_L,
                       box_size=10,border=2)

Qrcode.add_data("https://github.com/ahadrazadev")
Qrcode.make(fit=True)

image = Qrcode.make_image(fill_color="black", back_color="white")
image.save("customqrcode.png")