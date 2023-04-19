import qrcode
features=qrcode.QRCode(version=1,
               error_correction=qrcode.constants.ERROR_CORRECT_H,
               box_size=10,
               border=4)
features.add_data("this is rajan code")
features.make(fit=True)
imag=features.make_image(fill_color="purple",back_color='white')
imag.save('code.png')



