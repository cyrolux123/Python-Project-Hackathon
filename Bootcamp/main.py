import sys
import os
from subprocess import call, run, PIPE

VALID_IMAGES = [".jpg", ".gif", ".png", ".tga", ".tif", ".bmp"]

def create_directory(path):
    if not os.path.exists(path):
        os.makedirs(path)

def check_path(path):
    return os.path.exists(path)

def process_image(path, filename, directory_path, count):
    ext = os.path.splitext(filename)[1]

    if ext.lower() not in VALID_IMAGES:
        return count, 1

    create_directory(directory_path)

    image_file_name = os.path.join(path, filename)
    filename = ''.join(e for e in os.path.splitext(filename)[0] if e.isalnum() or e == '-')
    text_file_path = os.path.join(directory_path, filename)

    result = run(["tesseract", image_file_name, text_file_path], stdout=PIPE, stderr=PIPE, universal_newlines=True)

    if result.returncode == 0:  # Successful execution
        count += 1
        print(f"{count} {'file' if count == 1 else 'files'} completed")
    else:
        print(f"Error converting {image_file_name}: {result.stderr.strip()}")

    return count, 0

def main(path):
    path = os.path.abspath(path)

    if not check_path(path):
        print (f"No directory found at {path}")
        return

    directory_path = os.path.join(path, 'converted-text')
    count = 0
    other_files = 0

    print(f"Scanning {path} for valid image files...")

    for filename in os.listdir(path):
        count, other_files_increment = process_image(path, filename, directory_path, count)
        other_files += other_files_increment

    if count + other_files == 0:
        print(f"No valid image files found at {path}")
    else:
        print(f"{count} / {count + other_files} files converted")

if __name__ == '__main__':
    main('C:\\Users\\Asus\\Downloads\\Plagiarism-checker-Python-master\\Plagiarism-checker-Python-master\\Bootcamp')  # Escape the backslashes
