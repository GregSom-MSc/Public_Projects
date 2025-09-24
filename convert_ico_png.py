# ***File to convert PNG to ICO***************
# ********************* SGMS *****************
# Remember to install:
# pip install pillow


import sys
from PIL import Image
import os


def convert_to_ico(input_file, output_file=None):
    try:
        # Open the image
        img = Image.open(input_file)

        # If no output file provided, use same name with .ico
        if not output_file:
            base = os.path.splitext(input_file)[0]
            output_file = base + ".ico"

        # Save as ICO with multiple sizes
        img.save(output_file, sizes=[
                 (16, 16), (32, 32), (48, 48), (64, 64), (128, 128), (256, 256)])
        print(f"✅ Converted '{input_file}' → '{output_file}'")

    except Exception as e:
        print(f"❌ Error: {e}")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(
            "Usage: python convert_to_ico.py input_image.png [output_icon.ico]")
    else:
        input_file = sys.argv[1]
        output_file = sys.argv[2] if len(sys.argv) > 2 else None
        convert_to_ico(input_file, output_file)
