import os

from core.download_video import download_video
from core.config import dir_path
from core.read_csv import read_csv_data
from core.log import Logger, sys

'''
第二段根据./data/SavaData.csv里的数据下载视频
'''
log_dir_path = Logger().path()
log = 'down2local.log'
log_path = os.path.join(log_dir_path, log)
sys.stdout = Logger(log_path)

result = read_csv_data()
download_video(result, dir_path)
