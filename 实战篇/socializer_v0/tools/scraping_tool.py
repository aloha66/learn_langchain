# 导入所需的库
import json
import requests
import time


# 定义爬取微博用户信息的函数
def scrape_weibo(url: str):
    """爬取相关鲜花服务商的资料"""
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36",
        "Referer": "https://weibo.com",
    }
    cookies = {
        "cookie": """SINAGLOBAL=3149173157742.6553.1699669090765; UOR=,,www.baidu.com; ULV=1711592260506:8:1:1:6169753048074.416.1711592260498:1707235814567; XSRF-TOKEN=2i4tTtU0lsPd3MmdU-OdWgxh; SUB=_2A25LF4VmDeRhGeNM6FcZ9C_IyjqIHXVobJiurDV8PUNbmtAGLVPXkW9NTjzSeQdmSHcqR9NSUStfCqWNRooKijmw; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WWion3NDHRPfVFXYJeGOz6r5NHD95Qfeoef1hBpSh2cWs4Dqc_29G-7dK5LxKML1-2L1hBLxKBLBonL1h5LxKBLB.2L1-zLxKBLB.2L12zLxKBLBonL1h5LxKBLB.2L1-zLxKqL1heL1h-t; ALF=02_1715175990; WBPSESS=y7nadm9Cx5aIkEy5JvmlnV6_4sHu_DQ4ECe38gpoj0gVUGjNsVO5MvbDzKHPxs_de2LIeVGUhDWp2kVuPC2Re23OnJUmjjMKGD-cWbGSy6Y2gLOA62Q0AxNWHa2s9eLckNQeICynlsKp6Aief7GQCw=="""
    }
    response = requests.get(url, headers=headers, cookies=cookies)
    time.sleep(3)  # 加上3s 的延时防止被反爬
    return response.text


# 根据UID构建URL爬取信息
def get_data(id):
    url = "https://weibo.com/ajax/profile/detail?uid={}".format(id)
    html = scrape_weibo(url)
    response = json.loads(html)

    return response
