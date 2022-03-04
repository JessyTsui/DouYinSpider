import csv
from .config import csv_path, EnsureExist, csv_file_name


def read_csv_data():
    EnsureExist(csv_path)
    with open(csv_path + csv_file_name, 'r', encoding="utf-8-sig") as file:
        reader = csv.reader(file)
        fieldnames = next(reader)
        res = []
        csv_reader = csv.DictReader(file, fieldnames=fieldnames)
        for row in csv_reader:
            d = {}
            for k, v in row.items():
                d[k] = v
            res.append(d)
    return res
