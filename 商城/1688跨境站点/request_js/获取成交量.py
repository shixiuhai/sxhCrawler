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
    '_bl_uid': 'm0lL0fdjhbgkj176tbL3lg26ywL0',
    '_csrf_token': '1679361045356',
    '_m_h5_tk': '8078ca4873e9451464851b2c3aeacd75_1679384935913',
    '_m_h5_tk_enc': '11b41d29eb383418ec4eee694335bd49',
    'alicnweb': 'touch_tb_at%3D1679382415008%7Clastlogonid%3Dtb80111606',
    'tfstk': 'cfLNBgaSXV3aOoOxewb2LbNWxMOFZFIc4y5Ajxd_Dd5TpBSGiSwAt93RT_FUnGf..',
    'l': 'fBQjVxA4NjmdJ8P8BOfwFurza77OIIRAguPzaNbMi9fPOUjB5LINW1M_TWp6CnGVFsFHJ3o-P8F6BeYBqijrQ2EQLUjDYhDmnmOk-Wf..',
    'isg': 'BEVFkaF4jd3kp6keAqxj8gETVIF_AvmUGqeezkeqD3yL3mVQDlJGZNH47AIonhFM',
}

headers = {
    'authority': 'detail.1688.com',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8',
    'cache-control': 'max-age=0',
    # 'cookie': 'ali_ab=111.2.91.38.1678161716466.4; cna=AbGRHJxN6koCAW8CWyaOFU9H; lid=tb80111606; last_mid=b2b-345151005463a30; __last_loginid__=tb80111606; is_identity=buyer; aliwwLastNum=0; aliwwLastRefresh=1678953729515; cookie2=1b0448f1ce30484930268601ddbe4d18; sgcookie=E100DC85bOZVfIoWOZBBJsHzPU%2FGD3m%2B0I%2BixpzIuvvwrMkJIX71ifgMadX%2F7dIvzoi9Mmj5xzgPpMQSKCNSSNXN6rrj3sUJA8WDCHVdWoIyKuw%3D; t=52bc5c276688e72126801bd9a41c4cc4; _tb_token_=fe76e5ee767a5; __cn_logon__=false; xlly_s=1; __mwb_logon_id__=undefined; mwb=ng; _bl_uid=m0lL0fdjhbgkj176tbL3lg26ywL0; _csrf_token=1679361045356; _m_h5_tk=8078ca4873e9451464851b2c3aeacd75_1679384935913; _m_h5_tk_enc=11b41d29eb383418ec4eee694335bd49; alicnweb=touch_tb_at%3D1679382415008%7Clastlogonid%3Dtb80111606; tfstk=cfLNBgaSXV3aOoOxewb2LbNWxMOFZFIc4y5Ajxd_Dd5TpBSGiSwAt93RT_FUnGf..; l=fBQjVxA4NjmdJ8P8BOfwFurza77OIIRAguPzaNbMi9fPOUjB5LINW1M_TWp6CnGVFsFHJ3o-P8F6BeYBqijrQ2EQLUjDYhDmnmOk-Wf..; isg=BEVFkaF4jd3kp6keAqxj8gETVIF_AvmUGqeezkeqD3yL3mVQDlJGZNH47AIonhFM',
    'referer': 'https://food.1688.com/',
    'sec-ch-ua': '"Google Chrome";v="111", "Not(A:Brand";v="8", "Chromium";v="111"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-site',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36',
}

params = {
    'spm': 'a260c.14127409.jtqvgucl.2.62b874beaEZM5G',
}

response = requests.get('https://detail.1688.com/offer/644699678066.html', params=params, cookies=cookies, headers=headers)