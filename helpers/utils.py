import qrcode
from io import BytesIO
from django.core.files.base import ContentFile
from PIL import Image, ImageDraw

def generate_qr_code(url, filename):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(url)
    qr.make(fit=True)

    qr_img = qr.make_image(fill='black', back_color='white')
    canvas = Image.new('RGB', (qr_img.pixel_size, qr_img.pixel_size), 'white')
    draw = ImageDraw.Draw(canvas)
    canvas.paste(qr_img)

    buffer = BytesIO()
    canvas.save(buffer, format='PNG')
    buffer.seek(0)

    return ContentFile(buffer.getvalue(), name=filename)
