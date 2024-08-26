# This script renames all the graphic files by main title extracted by OCR
#
# Author: Jan Elznic <jan@elznic.com>
# Homepage: https://janelznic.cz
# GitHub: https://github.com/janelznic/python-ocr-bulk-file-rename-by-main-title
# Version: 1.0

import cv2, easyocr, os, re, unicodedata
from PIL import Image, ImageDraw, ImageFont
import numpy as np

# Source directory path
source_dir = "./img"

# Objects
ocr = easyocr.Reader(['en'])


# Split filename and extension
def split_filename(file_path):
    filename, extension = os.path.splitext(file_path)
    return filename, extension

# Removes forbidden characters in filename
def sanitize_filename(filename):
    # Removes diacritics
    normalized_filename = unicodedata.normalize('NFKD', filename).encode('ascii', 'ignore').decode('ascii')

    # Replaces spaces with dashes
    sanitized_filename = normalized_filename.replace(" ", "-")

    # Removes remaining forbidden characters
    sanitized_filename = re.sub(r'[<>:"/\\|?!,.*]', '', sanitized_filename)

    # Slice to 255 characters
    max_length = 255
    sanitized_filename = sanitized_filename[:max_length]

    return sanitized_filename

def get_text_size(image_path, bbox):
    # Calculates the size of the text within the specified bounding box
    image = Image.open(image_path)
    draw = ImageDraw.Draw(image)
    
    # Get the text from the bounding box
    (top_left, top_right, bottom_right, bottom_left) = bbox
    width = int(np.linalg.norm(np.array(top_right) - np.array(top_left)))
    height = int(np.linalg.norm(np.array(bottom_left) - np.array(top_left)))

    return width * height

def extract_main_title(image_path):
    results = ocr.readtext(image_path)

    if not results:
        return "No text found in the image."

    # Search for text with the largest size
    max_size = 0
    main_title = ""

    for bbox, text, prob in results:
        text_size = get_text_size(image_path, bbox)
        if text_size > max_size:
            max_size = text_size
            main_title = text

    if main_title:
        return main_title
    else:
        return "No main title found."


# Browse files in source directory
for full_filename in os.listdir(source_dir):

  # Get file path
  file_path = os.path.join(source_dir, full_filename)

  # Check if the file is ordinary file or directory
  if os.path.isfile(file_path):
    filename, extension = split_filename(full_filename)

    main_title = extract_main_title(file_path)
    new_filename = sanitize_filename(main_title) + extension

    # Get a new file name with full path and keep filename extension
    new_file_path = os.path.join(source_dir, new_filename)

    # Rename file
    os.rename(file_path, new_file_path)

    print(f"File {full_filename} renamed to: {new_filename}")
