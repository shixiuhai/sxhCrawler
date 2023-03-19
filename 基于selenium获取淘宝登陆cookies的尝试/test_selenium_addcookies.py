from selenium import webdriver
from lxml import etree
from selenium.webdriver.common.by import By
import time
import re
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from urllib import parse
import random
import logging

'''format=%(asctime)s具体时间 %(filename)s文件名 %(lenvelname)s日志等级 %(message)s具体信息
   datemt=%a星期 %d日期 %b月份 %Y年份 %H:%M:%S时间'''
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(filename)s %(levelname)s %(message)s',
                    datefmt='%a %d %b %Y %H:%M:%S', filename='1688spider.log', filemode='w')

option = webdriver.ChromeOptions()
# 无头模式
# option.add_argument('--headless')
# 允许root模式允许google浏览器
option.add_argument('--no-sandbox')
# option.add_argument('--headless')
option.add_experimental_option(
    "excludeSwitches", ['enable-automation', 'enable-logging'])
# 打开无痕浏览模式
# option.add_argument("--incognito")
# 关闭开发者模式
option.add_argument('--disable-blink-features=AutomationControlled')
driver = webdriver.Chrome(
    executable_path=r"C:\Users\15256\Documents\Redis-x64-5.0.14.1\chromedriver.exe",
    chrome_options=option)
cookies = [{'domain': '.1688.com', 'expiry': 1694769484, 'httpOnly': False, 'name': 'tfstk', 'path': '/', 'sameSite': 'Lax', 'secure': False, 'value': 'c_blBN1SSg-WwrzdhTT7SbfPJRxPZrZyFw7VuSMeonzl21_ViPiqbvHaiLe_UD1..'}, {'domain': '.1688.com', 'expiry': 1679822287, 'httpOnly': False, 'name': 'is_identity', 'path': '/', 'sameSite': 'Lax', 'secure': False, 'value': 'buyer'}, {'domain': '.1688.com', 'expiry': 1679822287, 'httpOnly': False, 'name': 'aliwwLastRefresh', 'path': '/', 'sameSite': 'Lax', 'secure': False, 'value': '1679217487732'}, {'domain': '.1688.com', 'httpOnly': False, 'name': 'mwb', 'path': '/', 'sameSite': 'Lax', 'secure': False, 'value': 'ng'}, {'domain': '.1688.com', 'expiry': 1679822286, 'httpOnly': False, 'name': 'firstRefresh', 'path': '/', 'sameSite': 'Lax', 'secure': False, 'value': '1679217486703'}, {'domain': '.1688.com', 'expiry': 1679289481, 'httpOnly': False, 'name': 'last_mid', 'path': '/', 'sameSite': 'None', 'secure': True, 'value': 'b2b-345151005463a30'}, {'domain': '.1688.com', 'httpOnly': False, 'name': '__cn_logon_id__', 'path': '/', 'sameSite': 'Lax', 'secure': False, 'value': 'tb80111606'}, {'domain': '.1688.com', 'httpOnly': True, 'name': 'uc4', 'path': '/', 'sameSite': 'None', 'secure': True, 'value': 'id4=0%40UgP5GPE5h%2FvopPV87sbnzf8cqwZE&nk4=0%40FY4GsvRHfRNKE%2BdeKAb%2BBqEZanqS'}, {'domain': '.1688.com', 'expiry': 1679224688, 'httpOnly': False, 'name': '_show_user_unbind_div_', 'path': '/', 'sameSite': 'Lax', 'secure': False, 'value': 'b2b-345151005463a30_false'}, {'domain': '.1688.com', 'httpOnly': False, 'name': 'unb', 'path': '/', 'sameSite': 'None', 'secure': True, 'value': '3451510054'}, {'domain': '.1688.com', 'expiry': 1694769484, 'httpOnly': False, 'name': 'l', 'path': '/', 'sameSite': 'Lax', 'secure': False, 'value': 'fBrWhCeVNNpWHQCkBOfwFurza77tIIRAguPzaNbMi9fPOB7p5chdW1MyNpA9CnGVFsvyR3o-P8F6BeYBqsVidj4KuQIXdpMmngzr905..'}, {'domain': '.1688.com', 'httpOnly': False, 'name': '__mwb_logon_id__', 'path': '/', 'sameSite': 'Lax', 'secure': False, 'value': 'tb80111606'}, {'domain': '.1688.com', 'expiry': 1679822266, 'httpOnly': False, 'name': '_m_h5_tk', 'path': '/', 'sameSite': 'None', 'secure': True, 'value': '98162fe66cb0984c93172076f87831d1_1679224666310'}, {'domain': '.1688.com', 'expiry': 1713777481, 'httpOnly': False, 'name': 'ali_apache_track', 'path': '/', 'sameSite': 'Lax', 'secure': False, 'value': 'c_mid=b2b-345151005463a30|c_lid=tb80111606|c_ms=1'}, {'domain': '.1688.com', 'httpOnly': True, 'name': 'csg', 'path': '/', 'sameSite': 'None', 'secure': True, 'value': '4985d3d7'}, {'domain': '.1688.com', 'httpOnly': True, 'name': 'sgcookie', 'path': '/', 'sameSite': 'None', 'secure': True, 'value': 'E1008MgSWIwrwokjGCvsNl1u2zn73%2B50Bu2ldISMI7M286O0ny0r1f7oql70hw%2FBvucf5ATdjHf6WJi7Zqz%2FhDMp0MCPBiGxGRc8L62JRncCOUg%3D'}, {'domain': '.1688.com', 'httpOnly': True, 'name': 'cookie17', 'path': '/', 'sameSite': 'None', 'secure': True, 'value': 'UNQyQxMqUdx1nQ%3D%3D'}, {'domain': '.1688.com', 'expiry': 1679224688, 'httpOnly': False, 'name': '_show_force_unbind_div_', 'path': '/', 'sameSite': 'Lax', 'secure': False, 'value': 'b2b-345151005463a30_false'}, {'domain': '.1688.com', 'httpOnly': True, 'name': 'cookie1', 'path': '/', 'sameSite': 'None', 'secure': True, 'value': 'U%2BGWz3AsFiX%2BQb4KVw17j51DAUP9jxfiN9Dd%2FomAUJ8%3D'}, {'domain': '.1688.com', 'expiry': 1713777491, 'httpOnly': False, 'name': 'alicnweb', 'path': '/', 'sameSite': 'Lax', 'secure': False, 'value': 'touch_tb_at%3D1679217471072%7Clastlogonid%3Dtb80111606'}, {'domain': '.1688.com', 'httpOnly': False, 'name': '_csrf_token', 'path': '/', 'sameSite': 'None', 'secure': True, 'value': '1679217481442'}, {'domain': '.1688.com', 'expiry': 1679224689, 'httpOnly': False, 'name': '__rn_alert__', 'path': '/', 'sameSite': 'Lax', 'secure': False, 'value': 'false'}, {'domain': '.1688.com', 'expiry': 1679224688, 'httpOnly': False, 'name': '_show_sys_unbind_div_', 'path': '/', 'sameSite': 'Lax', 'secure': False, 'value': 'b2b-345151005463a30_false'}, {'domain': '.1688.com', 'expiry': 1679224688, 'httpOnly': False, 'name': '_is_show_loginId_change_block_', 'path': '/', 'sameSite': 'Lax', 'secure': False, 'value': 'b2b-345151005463a30_false'}, {'domain': '.1688.com', 'expiry': 1713777468, 'httpOnly': False, 'name': 'cna', 'path': '/', 'sameSite': 'None', 'secure': True, 'value': 'O8GdHMyBOXICASe8CIUukYlA'}, {'domain': '.1688.com', 'httpOnly': False, 'name': '__cn_logon__', 'path': '/', 'sameSite': 'Lax', 'secure': False, 'value': 'true'}, {'domain': '.1688.com', 'expiry': 1710753481, 'httpOnly': False, 'name': 'lid', 'path': '/', 'sameSite': 'None', 'secure': True, 'value': 'tb80111606'}, {'domain': '.1688.com', 'expiry': 1679303867, 'httpOnly': False, 'name': 'xlly_s', 'path': '/', 'sameSite': 'None', 'secure': True, 'value': '1'}, {'domain': '.1688.com', 'httpOnly': False, 'name': 'sg', 'path': '/', 'sameSite': 'None', 'secure': True, 'value': '641'}, {'domain': '.1688.com', 'httpOnly': False, 'name': '_tb_token_', 'path': '/', 'sameSite': 'None', 'secure': True, 'value': '7e85b9b509e56'}, {'domain': '.1688.com', 'httpOnly': False, 'name': 't', 'path': '/', 'sameSite': 'None', 'secure': True, 'value': 'd2b7a2195096dbb3e2263c7c904aa947'}, {'domain': '.1688.com', 'expiry': 1694769486, 'httpOnly': False, 'name': 'isg', 'path': '/', 'sameSite': 'None', 'secure': True, 'value': 'BGho0Zq6mB2Nt7SZAbKVL0DhOVZ6kcyb9-TjOSKZtOPWfQjnyqGcK_73cRWNzYRz'}, {'domain': '.1688.com', 'httpOnly': False, 'name': 'ali_apache_tracktmp', 'path': '/', 'sameSite': 'Lax', 'secure': False, 'value': 'c_w_signed=Y'}, {'domain': '.1688.com', 'expiry': 1679822266, 'httpOnly': False, 'name': '_m_h5_tk_enc', 'path': '/', 'sameSite': 'None', 'secure': True, 'value': '2d655479d2b87923811cfd4e78f933b2'}, {'domain': '.1688.com', 'expiry': 1679822286, 'httpOnly': False, 'name': 'lastRefresh', 'path': '/', 'sameSite': 'Lax', 'secure': False, 'value': '1679217486703'}, {'domain': '.1688.com', 'httpOnly': False, 'name': '_nk_', 'path': '/', 'sameSite': 'None', 'secure': True, 'value': 'tb80111606'}, {'domain': '.1688.com', 'httpOnly': True, 'name': 'cookie2', 'path': '/', 'sameSite': 'None', 'secure': True, 'value': '1e276dc2818a8969861af51fe3c7f46a'}]

driver.get("https://www.1688.com/")
for cookie in cookies:
    driver.add_cookie(cookie_dict=cookie)
time.sleep(3)
driver.get("https://www.1688.com/")
time.sleep(100)
