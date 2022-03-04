import requests
from .config import API_url, headers


def douyin_spider(datalist):
    KeyList = []
    IdList = []
    for i in range(len(datalist)):
        key = datalist[i]['关键词']
        KeyList.append(key)
        pre_id = datalist[i]['笔记链接']
        id = pre_id.split('/')[-1]
        print(id)
        IdList.append(id)
    UrlList = []
    for i in range(len(IdList)):
        url = API_url + IdList[i]  # 拼接url
        print(url)
        try:
            requests.packages.urllib3.disable_warnings()  # 消掉warning
            response = requests.get(url=url, headers=headers, verify=False, timeout=30)
            response_json = response.json()
            list = response_json['item_list']
            tmp = list[0]['video']['play_addr']['url_list']
            url = ''.join(tmp)
            UrlList.append(url)
        except:
            print("Error!", url, "something wrong")
    return UrlList, KeyList, IdList
