import exifread
from PIL import Image
import logging
#https://pypi.org/project/ExifRead/


def _read_img_and_correct_exif_orientation(path):
    im = Image.open(path)
    tags = {}
    with open(path, 'rb') as f:
        tags = exifread.process_file(f, details=False)
    if "Image Orientation" in tags.keys():
        orientation = tags["Image Orientation"]
        logging.basicConfig(level=logging.DEBUG)
        logging.debug("Orientation: %s (%s)", orientation, orientation.values)
        val = orientation.values
        if 2 in val:
            val += [4, 3]
        if 5 in val:
            val += [4, 6]
        if 7 in val:
            val += [4, 8]
        if 3 in val:
            logging.debug("Rotating by 180 degrees.")
            im = im.transpose(Image.ROTATE_180)
        if 4 in val:
            logging.debug("Mirroring horizontally.")
            im = im.transpose(Image.FLIP_TOP_BOTTOM)
        if 6 in val:
            logging.debug("Rotating by 270 degrees.")
            im = im.transpose(Image.ROTATE_270)
        if 8 in val:
            logging.debug("Rotating by 90 degrees.")
            im = im.transpose(Image.ROTATE_90)
    return im