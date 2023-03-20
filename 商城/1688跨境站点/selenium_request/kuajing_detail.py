from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import logging
# set log config
logging.basicConfig(level=logging.INFO,filename="./kuajing_detail.log",
                    format='%(asctime)s-%(levelname)s-%(message)s')

# 定义一共解析链接的类，实现任意网站的链接解析，支持登陆渲染
class ParseLink:
    def __init__(self,
                url:str,
                executablePath:str=r"C:\Users\15256\Documents\Redis-x64-5.0.14.1\chromedriver.exe",
                timeOut:int=10,
                ) -> None:
        # 创建一共option对象
        self.option = webdriver.ChromeOptions()
        # 设置爬取页面超市时间
        self.timeOut=timeOut
        # 指定的webdriver路径
        self.executablePath=executablePath
        # self.option.add_argument('--no-sandbox')
        # 设置无头模式
        # self.option.add_argument('--headless')
        # 设置关闭开发者模式防止被检测
        self.option.add_experimental_option("excludeSwitches", ['enable-automation', 'enable-logging'])
        self.option.add_argument('--disable-blink-features=AutomationControlled')
        # 开启无痕模式
        # self.option.add_argument("--incognito")
        self.broser=webdriver.Chrome(executable_path=self.executablePath,chrome_options=self.option)
        # 定义一个wait对象
        self.wait=WebDriverWait(self.broser,self.timeOut)
        # 传入url
        self.url=url
        # 添加cookies
        cookies = [{'domain': '.1688.com',  'name': 'tfstk',   'value': 'c_blBN1SSg-WwrzdhTT7SbfPJRxPZrZyFw7VuSMeonzl21_ViPiqbvHaiLe_UD1..'}, {'domain': '.1688.com',   'name': 'is_identity',  'value': 'buyer'}, {'domain': '.1688.com',  'name': 'aliwwLastRefresh',  'value': '1679217487732'}, {'domain': '.1688.com',  'name': 'mwb',  'value': 'ng'}, {'domain': '.1688.com',  'name': 'firstRefresh',  'value': '1679217486703'}, {'domain': '.1688.com',  'name': 'last_mid',  'value': 'b2b-345151005463a30'}, {'domain': '.1688.com', 'name': '__cn_logon_id__',  'value': 'tb80111606'}, {'domain': '.1688.com',  'name': 'uc4', 'value': 'id4=0%40UgP5GPE5h%2FvopPV87sbnzf8cqwZE&nk4=0%40FY4GsvRHfRNKE%2BdeKAb%2BBqEZanqS'}, {'domain': '.1688.com', 'name': '_show_user_unbind_div_',  'value': 'b2b-345151005463a30_false'}, {'domain': '.1688.com',  'name': 'unb',  'value': '3451510054'}, {'domain': '.1688.com',  'name': 'l',  'value': 'fBrWhCeVNNpWHQCkBOfwFurza77tIIRAguPzaNbMi9fPOB7p5chdW1MyNpA9CnGVFsvyR3o-P8F6BeYBqsVidj4KuQIXdpMmngzr905..'}, {'domain': '.1688.com',  'name': '__mwb_logon_id__', 'value': 'tb80111606'}, {'domain': '.1688.com',  'name': '_m_h5_tk',  'value': '98162fe66cb0984c93172076f87831d1_1679224666310'}, {'domain': '.1688.com',   'name': 'ali_apache_track',  'value': 'c_mid=b2b-345151005463a30|c_lid=tb80111606|c_ms=1'}, {'domain': '.1688.com', 'name': 'csg',  'value': '4985d3d7'}, {'domain': '.1688.com',  'name': 'sgcookie',  'value': 'E1008MgSWIwrwokjGCvsNl1u2zn73%2B50Bu2ldISMI7M286O0ny0r1f7oql70hw%2FBvucf5ATdjHf6WJi7Zqz%2FhDMp0MCPBiGxGRc8L62JRncCOUg%3D'}, {'domain': '.1688.com',  'name': 'cookie17',  'value': 'UNQyQxMqUdx1nQ%3D%3D'}, {'domain': '.1688.com','name': '_show_force_unbind_div_',  'value': 'b2b-345151005463a30_false'}, {'domain': '.1688.com',  'name': 'cookie1',  'value': 'U%2BGWz3AsFiX%2BQb4KVw17j51DAUP9jxfiN9Dd%2FomAUJ8%3D'}, {'domain': '.1688.com',  'name': 'alicnweb',   'value': 'touch_tb_at%3D1679217471072%7Clastlogonid%3Dtb80111606'}, {'domain': '.1688.com', 'name': '_csrf_token', 'value': '1679217481442'}, {'domain': '.1688.com',  'name': '__rn_alert__',  'value': 'false'}, {'domain': '.1688.com',  'name': '_show_sys_unbind_div_',  'value': 'b2b-345151005463a30_false'}, {'domain': '.1688.com', 'name': '_is_show_loginId_change_block_', 'value': 'b2b-345151005463a30_false'}, {'domain': '.1688.com',  'name': 'cna', 'value': 'O8GdHMyBOXICASe8CIUukYlA'}, {'domain': '.1688.com',  'name': '__cn_logon__',  'value': 'true'}, {'domain': '.1688.com',  'name': 'lid', 'value': 'tb80111606'}, {'domain': '.1688.com',   'name': 'xlly_s',   'value': '1'}, {'domain': '.1688.com',  'name': 'sg',   'value': '641'}, {'domain': '.1688.com', 'name': '_tb_token_',    'value': '7e85b9b509e56'}, {'domain': '.1688.com',  'name': 't', 'value': 'd2b7a2195096dbb3e2263c7c904aa947'}, {'domain': '.1688.com',   'name': 'isg',    'value': 'BGho0Zq6mB2Nt7SZAbKVL0DhOVZ6kcyb9-TjOSKZtOPWfQjnyqGcK_73cRWNzYRz'}, {'domain': '.1688.com',  'name': 'ali_apache_tracktmp',    'value': 'c_w_signed=Y'}, {'domain': '.1688.com',   'name': '_m_h5_tk_enc',    'value': '2d655479d2b87923811cfd4e78f933b2'}, {'domain': '.1688.com',   'name': 'lastRefresh',    'value': '1679217486703'}, {'domain': '.1688.com',  'name': '_nk_',   'value': 'tb80111606'}, {'domain': '.1688.com', 'name': 'cookie2',  'value': '1e276dc2818a8969861af51fe3c7f46a'}]
        # 访问页面
        self.broser.get(self.url)
        for cookie in cookies:
            self.broser.add_cookie(cookie_dict=cookie)
        # 刷新页面
        self.broser.refresh()
    # 定义一个解析页面的方法
    # condition 页面加载成功判断条件
    # locator 是定位器，通过配置查询条件和参数来获取一共或者多个节点
    def scrape_page(self,condition,locator):
        logging.info("scraping %s"%self.url)
        try:
            self.broser.get(self.url)
            self.wait.until(condition(locator))
        except TimeoutException:
            logging.error("error occurred while scraping %s",self.url,exc_info=True)
    
    def scrape_items_by_css_select(self,selectCss):
        return self.broser.find_elements(By.CSS_SELECTOR,selectCss)
    
    def scrape_item_by_css_select(self,selectCss):
        return self.broser.find_element(By.CSS_SELECTOR,selectCss)
    
    def scrape_items_by_css_name(self,selectCss):
        return self.broser.find_elements(By.CLASS_NAME,selectCss)
    
    def scrape_item_by_css_name(self,selectCss):
        return self.broser.find_element(By.CLASS_NAME,selectCss)
    
    def scrape_items_by_path(self,selectXpath):
        return self.broser.find_elements(By.XPATH,selectXpath)
    
    def scrape_item_by_path(self,selectXpath):
        return self.broser.find_element(By.XPATH,selectXpath)
        
    def close_broser(self):
        self.broser.close()

if __name__ == '__main__':
    print("开始")
    obj=ParseLink(url="https://detail.1688.com/offer/699297425649.html?spm=a262or.11066112.rankhot.dcr10166t0.45b73722sDBn5I")
    obj.scrape_page(condition=EC.visibility_of_element_located,locator=(By.XPATH,'//*[@id="hd_0_container_0"]/div[1]/div[2]/div/div[1]/div[3]/div/div[2]/a/div'))
    print(obj.scrape_item_by_path('//*[@id="hd_0_container_0"]/div[1]/div[2]/div/div[1]/div[3]/div/div[2]/a/div').text)
    
    # select 是 css节点
    # obj.scrape_page(condition=EC.visibility_of_element_located,locator=(By.CSS_SELECTOR,'#hd_0_container_0 > div:nth-child(1) > div:nth-child(2) > div > div:nth-child(1) > div:nth-child(3) > div > div:nth-child(2) > a > div'))
    # print(obj.scrape_item_by_css_select('#hd_0_container_0 > div:nth-child(1) > div:nth-child(2) > div > div:nth-child(1) > div:nth-child(3) > div > div:nth-child(2) > a > div').text)
    #hd_0_container_0 > div:nth-child(1) > div:nth-child(2) > div > div:nth-child(1) > div:nth-child(3) > div > div:nth-child(2) > a > div
   

    
    
        
        
        