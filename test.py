import time, os

now = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())


path = "./log/{}/".format(now)
log = 'down2local.log'
log_path = os.path.join(path, log)
print(log_path)
print(path)