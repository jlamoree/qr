import os
import sys

from PIL import Image
import pyzbar.pyzbar as pyzbar


def main():
    if len(sys.argv) > 1:
        filename = sys.argv[1]
    else:
        filename = os.getenv("IMAGE_FILE", "/data/image_file")

    if not os.path.exists(filename):
        sys.stderr.write(f"File '{filename}' not found.\n")
        exit(1)
    image = Image.open(filename)
    objects = pyzbar.decode(image, symbols=[pyzbar.ZBarSymbol.QRCODE])
    if len(objects):
        for o in objects:
            print(o.data.decode("UTF-8"))
    else:
        sys.stderr.write(f"No QR codes found in image '{filename}'.\n")
        exit(1)


if __name__ == "__main__":
    main()
