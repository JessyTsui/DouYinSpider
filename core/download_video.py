import time, requests
from .config import headers, EnsureExist

MAX_TRY_TIME = 5

def download_video(list, path):
    for i in range(len(list)):
        isSuccess = False
        trytime = 0

        video_url = list[i]['url']
        video_key = list[i]['关键词']
        video_title = list[i]['id'] + ".mp4"

        while(not isSuccess) and trytime < MAX_TRY_TIME:
            try:
                trytime += 1
                start = time.time()
                print("Trying {}time for ".format(trytime) + video_title)
                print(video_url)
                resp = requests.get(
                    url=video_url,
                    headers=headers, stream=True)

                file_path = path + video_key
                print("保存目录：", file_path)
                EnsureExist(file_path)
                with open(file_path + "/" + video_title, mode='wb') as file:
                    file.write(resp.content)
                    print('下载完毕')
                    end = time.time()
                    duration = end - start
                    print("花费时间：", duration, "秒")
                    print("\n")
                isSuccess = True
            except:
                print("Download error", video_title)

