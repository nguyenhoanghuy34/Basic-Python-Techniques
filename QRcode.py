import qrcode

url = "https://www.facebook.com/someone"

qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,  # Kích thước mỗi ô vuông trong mã QR
    border=4, 
)

# Thêm dữ liệu vào mã QR
qr.add_data(url)
qr.make(fit=True)

img = qr.make_image(fill='black', back_color='white')

img.save("qr_code.png")
img.show()
