import qrcode
import qrcode.constants
import Visual


def generate_qr_code(text, file_name):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=4,
    )
    qr.add_data(text)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    img.save(file_name)


text = ""
file_name = Visual.title + ".jpg"  # ver cómo enlazar con tkinter


generate_qr_code(text, file_name)
print(f"QR code saved as {file_name}")
