import requests

headers = {
    'authority': 'widget.1688.com',
    'accept': '*/*',
    'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8',
    # 'cookie': 'SameSite=none; lid=tb80111606; ali_ab=2409:8a28:6ab9:3100:ed07:b541:4c1b:24db.1678108184784.2; cna=su2QHDAXHR4BASQJiijj0y+z; keywordsHistory=%E8%A2%9C%E5%AD%90; ali_apache_track=c_mid=b2b-345151005463a30|c_lid=tb80111606|c_ms=1; t=3f67e5167347da1dd1edcce6a6d4f268; cookie2=1ea63cc2b74976be8dbc2d1e6c3fbc1f; __cn_logon_id__=tb80111606; __last_loginid__=tb80111606; __cn_logon__=true; __cn_userid__=3451510054; firstRefresh=1678969978545; is_identity=buyer; ali_apache_tracktmp=c_w_signed=Y; _m_h5_c=369b2519664468c92fd4047fdc1d6a2c_1678979737717%3B9ab54e834bee6e4eb239a135f326bd36; __mwb_logon_id__=tb80111606; aliwwLastNum=0; _m_h5_tk=636a1abdc95613abddd194871239ac10_1678980098048; _m_h5_tk_enc=54449c2332c202d7836154756b511821; mwb=ng; lastRefresh=1679054107917; _csrf_token=1679058295571; xlly_s=1; alicnweb=touch_tb_at%3D1679058298325%7Clastlogonid%3Dtb80111606%7Cshow_inter_tips%3Dfalse; cookie1=U%2BGWz3AsFiX%2BQb4KVw17j51DAUP9jxfiN9Dd%2FomAUJ8%3D; cookie17=UNQyQxMqUdx1nQ%3D%3D; sgcookie=E100DddPKZ0Qm0fObwcRXtOBjfuim6oDiLWznNQCG%2BwiuN92Juq1PKYZzuJMzZEdblfkqStBO2DGHRhJf92MdpevzSoSusqprKNKbXkscQriKY0%3D; _tb_token_=710be73131be3; sg=641; csg=c9774b23; unb=3451510054; uc4=nk4=0%40FY4GsvRHfRNKE%2BdeKAb%2BBBGjXEuT&id4=0%40UgP5GPE5h%2FvopPV87sbnzzVDsqDJ; _nk_=tb80111606; last_mid=b2b-345151005463a30; _is_show_loginId_change_block_=b2b-345151005463a30_false; _show_force_unbind_div_=b2b-345151005463a30_false; _show_sys_unbind_div_=b2b-345151005463a30_false; _show_user_unbind_div_=b2b-345151005463a30_false; __rn_alert__=false; isg=BAQEvqS4POP9Bog-KInyAw_31YL2HSiHs1D_7R6-OE0OSYITRC3JFjYoieGR1mDf; tfstk=cXdlBsOXHLWSalhpc31Sso1ap4T5aCDPVBR2gqatasdP28v1zsfL3RR56qj-f0yC.; l=fB_5pERlNOhjvliTBO5aKurza77tPUdfH1PzaNbMiIEGC6AvM79OpStQ2rKwTTKRR8Xli18H4037e599Trt8JbMmndLhMXXwmgieBecJLyvP.; aliwwLastRefresh=1679058746634',
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
    'callback': 'jQuery3600825913373777599_1678969977563',
    'namespace': 'getAliRankCateData',
    'widgetId': 'getAliRankCateData',
    'methodName': 'execute',
    'cateLevel': '1',
    'parentId': '0',
    # '_tb_token_': '710be73131be3',
    '_': '1679058744844',
}

response = requests.get('https://widget.1688.com/front/getJsonComponent.json', params=params,  headers=headers).text
print(response)