# -*- coding=utf-8
from qcloud_cos import CosConfig
from qcloud_cos import CosS3Client
from qcloud_cos import CosServiceError
from qcloud_cos.cos_threadpool import SimpleThreadPool
from core.config import secret_id, secret_key, region, bucket
import sys
import os
import logging

from core.log import Logger

log_dir_path = Logger().path()
log = 'upload2cos.log'
log_path = os.path.join(log_dir_path, log)
sys.stdout = Logger(log_path)


logging.basicConfig(level=logging.INFO, stream=sys.stdout)

token = None
scheme = 'https'

config = CosConfig(Region=region, SecretId=secret_id, SecretKey=secret_key, Token=token, Scheme=scheme)
client = CosS3Client(config)

# key = '/lab/'  # 写死，让他们只能上传到lab后面的目录

def upload2cos(upload_dir):
    g = os.walk(upload_dir)
    pool = SimpleThreadPool()
    for path, dir_list, file_list in g:
        for file_name in file_list:
            srcKey = os.path.join(path, file_name)
            cosObjectKey = srcKey.strip('/')
            # 判断COS上文件是否存在
            exists = False
            try:
                response = client.head_object(Bucket=bucket, Key=cosObjectKey)
                exists = True
            except CosServiceError as e:
                if e.get_status_code() == 404:
                    exists = False
                else:
                    print("Error happened, reupload it.")
            if not exists:
                print("File %s not exists in cos, upload it", srcKey)
                pool.add_task(client.upload_file, bucket, cosObjectKey, srcKey)

    pool.wait_completion()
    result = pool.get_result()
    if not result['success_all']:
        print("Not all files upload sucessed. you should retry")

upload_dir = input("请输入上传到cos的文件目录")
upload2cos(upload_dir)