import sys
import os
import re
from progress.bar import IncrementalBar
from datetime import datetime


def check_filename(path):  # Функция проверяет задан путь к файлу или к папке. Также используется при проверке всех файлов в папке
    return re.match(filename_pattern, path)


def search_for_pattern(path):  # Функция ищет заданный шаблон логе
    with open(path, 'r') as f:
        for line in f:
            if re.match(search_pattern, line):
                errors_log.write(line)
        progress_bar.next()
    f.close()


def make_filenames_list(path):  # Функция заполняет список файлов, которые подходят заданному шаблону (Я ищу файлы .log)
    filenames_list = []
    for filename in os.listdir(path):
        if check_filename(filename):
            filenames_list.append(filename)
    return filenames_list


if len(sys.argv) == 1:
    print("Path to file or folder must be here :\\")
    raise SystemExit
else:
    ms = datetime.now().microsecond
    filename_pattern = r'.*\.log'
    search_pattern = r'Error.*'
    errors_log = open("errors_log" + str(ms), "w")
    root = sys.argv[1]
    progress_bar = IncrementalBar('Countdown', max=1)
    if len(sys.argv) == 3:
        search_pattern = sys.argv[2]
    if check_filename(root):
        search_for_pattern(root)
        errors_log.close()
        progress_bar.finish()
        raise SystemExit

    filenames = make_filenames_list(root)
    progress_bar.max = len(filenames)
    print("Selected files: ", end='')
    print(filenames)
    for file in filenames:
        search_for_pattern(os.path.join(root, file))
    errors_log.close()
    progress_bar.finish()

