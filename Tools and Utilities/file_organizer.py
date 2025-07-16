# This is a basic file organizer script in Python.
# It categorizes files in a specified folder into subfolders based on their file types.
# It will automitically log files as they are moved.
import os
import shutil
import logging

# Define file type categories
FILE_TYPES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif"],
    "Documents": [".pdf", ".docx", ".txt", ".xlsx"],
    "Videos": [".mp4", ".mov", ".avi"],
    "Music": [".mp3", ".wav"],
    "Archives": [".zip", ".rar", ".tar", ".gz"],
    "Scripts": [".py", ".js", ".html", ".css"]
}

# Convert bytes to human-readable format
def format_size(size_bytes):
    if size_bytes < 1024:
        return f"{size_bytes} B"
    elif size_bytes < 1024 ** 2:
        return f"{size_bytes / 1024:.2f} KB"
    else:
        return f"{size_bytes / (1024 ** 2):.2f} MB"

# Log each move in a clean, readable format
def log_move(filename, src, dst, size_bytes):
    size_str = format_size(size_bytes)
    dst_folder = os.path.basename(os.path.dirname(dst))
    logging.info(f"• '{filename}' → '{dst_folder}' folder ({size_str})")

# Set up logging with a folder-specific log file and header
def setup_logging(folder_path):
    folder_name = os.path.basename(os.path.normpath(folder_path))
    log_filename = f"file_organizer_log_{folder_name}.txt"
    logging.basicConfig(
        filename=log_filename,
        level=logging.INFO,
        format="%(asctime)s - %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S"
    )
    logging.info(f"Organizing folder: {folder_name}")

# Organize files in the folder
def organize_folder(folder_path):
    setup_logging(folder_path)

    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)

        if os.path.isfile(file_path):
            _, ext = os.path.splitext(filename)
            size_bytes = os.path.getsize(file_path)
            moved = False

            for category, extensions in FILE_TYPES.items():
                if ext.lower() in extensions:
                    category_folder = os.path.join(folder_path, category)
                    os.makedirs(category_folder, exist_ok=True)
                    new_path = os.path.join(category_folder, filename)
                    shutil.move(file_path, new_path)
                    log_move(filename, file_path, new_path, size_bytes)
                    moved = True
                    break

            if not moved:
                other_folder = os.path.join(folder_path, "Others")
                os.makedirs(other_folder, exist_ok=True)
                new_path = os.path.join(other_folder, filename)
                shutil.move(file_path, new_path)
                log_move(filename, file_path, new_path, size_bytes)

# Insert your folder path here
organize_folder("folder-path")
