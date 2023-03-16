import requests


headers = {
    'authority': 'widget.1688.com',
    'accept': '*/*',
    'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8',
    'referer': 'https://kj.1688.com/',
    'sec-ch-ua': '"Google Chrome";v="111", "Not(A:Brand";v="8", "Chromium";v="111"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'script',
    'sec-fetch-mode': 'no-cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36',
}

params = {
    'callback': 'jQuery36008223910503795178_1678971098945',
    'namespace': 'getAliRankDataByCateId',
    'widgetId': 'getAliRankDataByCateId',
    'methodName': 'execute',
    'cateId': '97',
    'cateLevel': '1',
    'type': 'hot',
    'pageNo': '3',
    'pageSize': '20',
    '_': '1678971098956',
}
import time
for i in range(1000):
    time.sleep(3)
    response = requests.get('https://widget.1688.com/front/getJsonComponent.json', params=params, headers=headers)

    print(response.text)