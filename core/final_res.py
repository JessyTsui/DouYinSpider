def generate_res(url, key, id):
    result = []
    for i in range(len(url)):
        dic = {"url": url[i], "关键词": key[i], "id": id[i]}
        result.append(dic)
    return result
