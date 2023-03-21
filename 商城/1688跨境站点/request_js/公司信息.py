import requests

cookies = {
    'ali_ab': '111.2.91.38.1678161716466.4',
    'cna': 'AbGRHJxN6koCAW8CWyaOFU9H',
    'lid': 'tb80111606',
    'last_mid': 'b2b-345151005463a30',
    '__last_loginid__': 'tb80111606',
    'is_identity': 'buyer',
    'aliwwLastNum': '0',
    'aliwwLastRefresh': '1678953729515',
    'cookie2': '1b0448f1ce30484930268601ddbe4d18',
    'sgcookie': 'E100DC85bOZVfIoWOZBBJsHzPU%2FGD3m%2B0I%2BixpzIuvvwrMkJIX71ifgMadX%2F7dIvzoi9Mmj5xzgPpMQSKCNSSNXN6rrj3sUJA8WDCHVdWoIyKuw%3D',
    't': '52bc5c276688e72126801bd9a41c4cc4',
    '_tb_token_': 'fe76e5ee767a5',
    '__cn_logon__': 'false',
    'xlly_s': '1',
    '__mwb_logon_id__': 'undefined',
    'mwb': 'ng',
    '_csrf_token': '1679361045356',
    'alicnweb': 'touch_tb_at%3D1679375887948%7Clastlogonid%3Dtb80111606',
    '_m_h5_tk': '8078ca4873e9451464851b2c3aeacd75_1679384935913',
    '_m_h5_tk_enc': '11b41d29eb383418ec4eee694335bd49',
    'tfstk': 'cDPGBSA5DRk1Aq1YAlG1ajLBQB2NaGSZbSPTTwH6-WbTYT3q7sX6LLlOpwmFVGJf.',
    'l': 'fBQjVxA4NjmdJknaKO5Churza77OXIdb8sPzaNbMiIEGa6w5VEyjFNCsCWbphdtjgT5VZetr24w81dhWWlU38xssMFXarOKCGx9M8eM3N7AN.',
    'isg': 'BBoam22vKgwWDqa_4fXkw1Kaa8A8S54lSd5R7ySSOK1hl7vRDNkUNO6hY2MLRxa9',
}

headers = {
    'authority': 'h5api.m.1688.com',
    'accept': '*/*',
    'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8',
    # 'cookie': 'ali_ab=111.2.91.38.1678161716466.4; cna=AbGRHJxN6koCAW8CWyaOFU9H; lid=tb80111606; last_mid=b2b-345151005463a30; __last_loginid__=tb80111606; is_identity=buyer; aliwwLastNum=0; aliwwLastRefresh=1678953729515; cookie2=1b0448f1ce30484930268601ddbe4d18; sgcookie=E100DC85bOZVfIoWOZBBJsHzPU%2FGD3m%2B0I%2BixpzIuvvwrMkJIX71ifgMadX%2F7dIvzoi9Mmj5xzgPpMQSKCNSSNXN6rrj3sUJA8WDCHVdWoIyKuw%3D; t=52bc5c276688e72126801bd9a41c4cc4; _tb_token_=fe76e5ee767a5; __cn_logon__=false; xlly_s=1; __mwb_logon_id__=undefined; mwb=ng; _csrf_token=1679361045356; alicnweb=touch_tb_at%3D1679375887948%7Clastlogonid%3Dtb80111606; _m_h5_tk=8078ca4873e9451464851b2c3aeacd75_1679384935913; _m_h5_tk_enc=11b41d29eb383418ec4eee694335bd49; tfstk=cDPGBSA5DRk1Aq1YAlG1ajLBQB2NaGSZbSPTTwH6-WbTYT3q7sX6LLlOpwmFVGJf.; l=fBQjVxA4NjmdJknaKO5Churza77OXIdb8sPzaNbMiIEGa6w5VEyjFNCsCWbphdtjgT5VZetr24w81dhWWlU38xssMFXarOKCGx9M8eM3N7AN.; isg=BBoam22vKgwWDqa_4fXkw1Kaa8A8S54lSd5R7ySSOK1hl7vRDNkUNO6hY2MLRxa9',
    'referer': 'https://detail.1688.com/',
    'sec-ch-ua': '"Google Chrome";v="111", "Not(A:Brand";v="8", "Chromium";v="111"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'script',
    'sec-fetch-mode': 'no-cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36',
}

params = {
    'jsv': '2.4.11',
    'appKey': '12574478',
    't': '1679382065844',
    'sign': '12203cd04042d62d54aee4aedf4a7765',
    'api': 'mtop.alibaba.alisite.cbu.server.ModuleAsyncService',
    'v': '1.0',
    'type': 'jsonp',
    'valueType': 'string',
    'dataType': 'jsonp',
    'timeout': '10000',
    'callback': 'mtopjsonp4',
    'data': '{"componentKey":"wp_pc_shop_basic_info","params":"{\\"memberId\\":\\"b2b-3417629197bf224\\"}"}',
}

response = requests.get(
    'https://h5api.m.1688.com/h5/mtop.alibaba.alisite.cbu.server.moduleasyncservice/1.0/',
    params=params,
    cookies=cookies,
    headers=headers,
)