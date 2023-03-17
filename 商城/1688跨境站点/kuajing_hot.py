import requests
import logging
import time
import json
import pymysql
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s-%(levelname)s-%(message)s')
class KJ:
    def __init__(self,host="127.0.0.1",port="3306",user="root",passwd="123456",database="push") -> None:
        self.headers = {
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
        # mysql初始化
        self.host=host
        self.port=port
        self.user=user
        self.passwd=passwd
        self.database=database
        # 标题级别初始化
        self.cate_level=1
        try:
            self.db=pymysql.connect(host=self.host,port=int(self.port),user=self.user,passwd=self.passwd,database=self.database)
        except Exception as error:
            print("连接数据库失败")
            logging.error("连接数据库失败")
        # 初始标题级别
        # self.cateIdList=[]
    # 如果列表没有元素会返回 ""
    def getListOne(self,data:list)->str:
        if len(data)>0:
            return data[0]
        else:
            return ""
    
    def getgoodsIndex(self,parentId:int,cateLevel:int)->list:
        params = {
            'callback': 'jQuery3600825913373777599_1678969977563',
            'namespace': 'getAliRankCateData',
            'widgetId': 'getAliRankCateData',
            'methodName': 'execute',
            'cateLevel': '%s'%cateLevel,
            'parentId': '%s'%parentId,
            # '_tb_token_': 'e6e1b1eaea59',
            '_': '%s'%(int(time.time())*1000),
        }
        try:
            return json.loads(
                requests.get(url="https://widget.1688.com/front/getJsonComponent.json",
                params=params,headers=self.headers).text.
                replace("jQuery3600825913373777599_1678969977563","").replace("(","").
                replace(")","").replace(" ","").replace("，",","))["content"]["result"]
        except Exception as error:
            logging.error("获取索引出现错误，错误是%s"%error)
            return []
        
    def getgoodsList(self,cateId:int,pageNo:int)->list:
        params = {
            'callback': 'jQuery36008223910503795178_1678971098945',
            'namespace': 'getAliRankDataByCateId',
            'widgetId': 'getAliRankDataByCateId',
            'methodName': 'execute',
            'cateId': '%s'%cateId,
            'cateLevel': '1',
            'type': 'hot',
            'pageNo': '%s'%pageNo,
            'pageSize': '20',
            '_': '%s'%(int(time.time())*1000),
        }
        try:
            return json.loads(
                    requests.get(url="https://widget.1688.com/front/getJsonComponent.json",
                    params=params,headers=self.headers).text.
                    replace("jQuery36008223910503795178_1678971098945","").replace("(","").
                    replace(")","").replace(" ","").replace("，",","))["content"]["result"]
        except Exception as error:
            logging.error("获取该页商品数据出现错误，错误是%s"%error)
            return []
    # 入数据库
    def insertMysql(self,sql:str)->None:
        try:
            cursor=self.db.cursor()
            cursor.execute(sql)
            # 插入执行必须要提交事务
            self.db.commit()
            cursor.close()
        # pymysql.err.OperationalError: (2003, "Can't connect to MySQL server on '183.134.60.170' (timed out)")
        except Exception as error:
            logging.error("插入数据库出错，错误是%s"%error)
            # print(error.__str__())
            if "Can't connect to MySQL" in error.__str__():
                self.db=pymysql.connect(host=self.host,port=int(self.port),user=self.user,passwd=self.passwd,db=self.db)
    
    # 爬取信息
    def spider(self):
        # 获取一级标题信息
        
        pass
if __name__ == '__main__':
    obj=KJ()
    print(obj.getgoodsIndex(4))
    print(obj.getgoodsList(97,3))