from fake_useragent import UserAgent
import os

ua = UserAgent()
headers = {
    'authority': 'www.douyin.com',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'accept-encoding': 'utf-8',
    'User-Agent': ua.chrome
}

# 这是抓包到的API接口，悠着点用
API_url = 'https://www.douyin.com/web/api/v2/aweme/iteminfo/?item_ids='

# 这是cos的配置东西，想上传的话用自己的key
secret_id = '111'
secret_key = '222'
region = 'ap-333'
bucket = 'mira-444'

def IsExist(path):
    # 判断路径是否存在
    return os.path.isdir(path)


def EnsureExist(path):
    # 确保路径存在，不存在则新建一个
    if not IsExist(path):
        os.makedirs(path)



dir_path = "./抖音视频下载/"  # 输出目录
# dir_path = input("请输入视频保存目录：")  # 输出目录

csv_path = "./data/" # 抓取到的真实视频地址保存成的csv
csv_file_name = 'SaveData.csv'

# path = '/Users/jessytsui/Desktop/douyin.xlsw'
path = './测试.xlsx'
# path = input("请输入需求Excel目录: ")

