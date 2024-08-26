# python-ocr-bulk-file-rename-by-main-title

## About
This script renames all the graphic files in directory by main title (recognized by text size) extracted by OCR

## To do
* [x] Removes diacritics and special characters excluding parentheses
* [x] Replaces whitespaces in filenames with dashes
* [x] Slice filenames to 255 characters
* [ ] Iterate and rename file names when the title is same as in previous file with _1, _2, _3 etc.
* [ ] Improve main title text content recognition logic

## Author
* Maintainer: [Jan Elznic](https://janelznic.cz), <jan@elznic.com>
* GitHub repo: [https://github.com/janelznic/python-ocr-bulk-file-rename-by-main-title](https://github.com/janelznic/python-ocr-bulk-file-rename-by-main-title)

## Requirements
Python3 and higher.

## Config
Edit ```source_dir``` path in ```index.py``` file.

## Run
```python index.py```

## License
MIT © Jan Elznic – [Homepage](https://janelznic.cz) – [GitHub](https://github.com/janelznic) – [LinkedIn](https://linkedin.com/in/janelznic/)
