
import os
import qrcode

def generate_qr(url, output_file, fill_color, back_color):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(url)
    qr.make(fit=True)

    img = qr.make_image(fill_color=fill_color, back_color=back_color)
    output_dir = os.getenv('QR_CODE_DIR', '.')
    os.makedirs(output_dir, exist_ok=True)
    img.save(os.path.join(output_dir, output_file))
    print(f"QR Code generated and saved as {os.path.join(output_dir, output_file)}")

if __name__ == "__main__":
    url = os.getenv('QR_DATA_URL', 'https://github.com/tk385')
    output_file = os.getenv('QR_CODE_FILENAME', 'github_qr.png')
    fill_color = os.getenv('FILL_COLOR', 'black')
    back_color = os.getenv('BACK_COLOR', 'white')
    generate_qr(url, output_file, fill_color, back_color)
