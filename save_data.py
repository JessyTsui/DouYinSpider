from core.read_excel import read_excel_data
from core.config import path
from core.output_csv import output_csv
from core.douyin_spider import douyin_spider
from core.final_res import generate_res
from core.log import Logger, sys, os

'''
第一段根据Excel的需求URL去抖音接口里抓到真实视频URL，然后存到./data/SaveData.csv里
'''

log_dir_path = Logger().path()
log = 'sava_csv.log'
log_path = os.path.join(log_dir_path, log)
sys.stdout = Logger(log_path)

datalist = read_excel_data(path)
url, key, id = douyin_spider(datalist)
result = generate_res(url, key, id)
output_csv(result)
