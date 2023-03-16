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
import time
params = {
    'callback': 'jQuery3600825913373777599_1678969977563',
    'namespace': 'getAliRankCateData',
    'widgetId': 'getAliRankCateData',
    'methodName': 'execute',
    'cateLevel': '2',
    'parentId': '4',
    # '_tb_token_': 'e6e1b1eaea59',
    '_': '%s'%int(time.time())*1000,
}

response = requests.get('https://widget.1688.com/front/getJsonComponent.json', params=params, headers=headers)

print(response.text)