import os
import sys
import csv
sys.path.append(os.path.realpath('.'))
from .config import csv_path, EnsureExist, csv_file_name


def output_csv(datalist):
    EnsureExist(csv_path)
    csv_file = open(csv_path + csv_file_name, 'w', newline='', encoding='utf-8-sig')  # 解决中文乱码问题
    writer = csv.writer(csv_file)

    writer.writerow(["url", "关键词", "id"])
    for data in datalist:
        writer.writerow([data['url'], data['关键词'], data['id']])
    csv_file.close()
