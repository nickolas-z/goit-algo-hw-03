import os
from helpers.helpers import print_header, print_footer

import os
import shutil
import argparse

def copy_and_sort_files(src_dir, dest_dir="dist"):
    try:
        # Створення директорії призначення, якщо вона не існує
        if not os.path.exists(dest_dir):
            os.makedirs(dest_dir)
        
        # Рекурсивне читання директорії
        for root, dirs, files in os.walk(src_dir):
            for file in files:
                file_path = os.path.join(root, file)
                file_ext = os.path.splitext(file)[1].lower()  # Отримання розширення файлу
                if file_ext:
                    ext_dir = os.path.join(dest_dir, file_ext[1:])  # Назва піддиректорії на основі розширення
                else:
                    ext_dir = os.path.join(dest_dir, "no_extension")
                
                # Створення директорії для відповідного типу файлів
                if not os.path.exists(ext_dir):
                    os.makedirs(ext_dir)
                
                # Копіювання файлу у відповідну директорію
                dest_file_path = os.path.join(ext_dir, file)
                shutil.copy2(file_path, dest_file_path)
                print(f"Copied: {file_path} to {dest_file_path}")
                
    except Exception as e:
        print(f"Error: {e}")

def main():
    # Парсинг аргументів командного рядка
    parser = argparse.ArgumentParser(description="Copy and sort files by extension.")
    parser.add_argument("src_dir", help="Source directory to copy files from.")
    parser.add_argument("dest_dir", nargs="?", default="dist", help="Destination directory to copy files to (default is 'dist').")
    
    args = parser.parse_args()

    # Виклик функції копіювання та сортування
    # Перший аргумент - директорія, з якої копіювати файли
    copy_and_sort_files(args.src_dir, args.dest_dir)


# Перед запуском програми потрібно згенерувати файли за допомогою file_generator.py
if __name__ == "__main__":
    main()
