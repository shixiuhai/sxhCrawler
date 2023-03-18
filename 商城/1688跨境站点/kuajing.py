import requests
import logging
import time
import json
import pymysql
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s-%(levelname)s-%(message)s')
class KJ:
    def __init__(self,host="127.0.0.1",port="3306",user="root",passwd="sxh.200008",database="goods") -> None:
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
        # # 标题级别初始化
        # self.cateLevel=1
        # # 初始化parenteid
        # self.parentId=0
        try:
            self.db=pymysql.connect(host=self.host,port=int(self.port),user=self.user,passwd=self.passwd,database=self.database)
        except Exception as error:
            print("连接数据库失败")
            logging.error("连接数据库失败")
        # 初始标题级别
        # self.cateIdList=[]
    # 如果列表没有元素会返回 ""
    def get_list_one(self,data:list)->str:
        if len(data)>0:
            return data[0]
        else:
            return ""
    
    # 获取标题
    def get_goods_cate(self,parentId:int,cateLevel:int)->dict:
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
            return {
                "parentId":parentId,
                "cate":json.loads(
                requests.get(url="https://widget.1688.com/front/getJsonComponent.json",
                params=params,headers=self.headers).text.
                replace("jQuery3600825913373777599_1678969977563","").replace("(","").
                replace(")","").replace(" ","").replace("，",","))["content"]
            }
        except Exception as error:
            logging.error("获取索引出现错误，错误是%s"%error)
            return {}
        
    # 获取每页所有商品信息
    # rankType hot rising
    def get_goods_list(self,cateLevel:int,cateId:int,pageNo:int,rankType:str)->dict:
        params = {
            'callback': 'jQuery36008223910503795178_1678971098945',
            'namespace': 'getAliRankDataByCateId',
            'widgetId': 'getAliRankDataByCateId',
            'methodName': 'execute',
            'cateId': '%s'%cateId,
            'cateLevel': '%s'%cateLevel,
            'type': '%s'%rankType,
            'pageNo': '%s'%pageNo,
            'pageSize': '20',
            '_': '%s'%(int(time.time())*1000),
        }
        try:
            return json.loads(
                    requests.get(url="https://widget.1688.com/front/getJsonComponent.json",
                    params=params,headers=self.headers).text.
                    replace("jQuery36008223910503795178_1678971098945","").replace("(","").
                    replace(")","").replace(" ","").replace("，",","))["content"]
        except Exception as error:
            logging.error("获取该页商品数据出现错误，错误是%s"%error)
            return {}
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
    
    # 保存标题到数据库
    def save_cate(self):
        fistCateInformation=self.get_goods_cate(parentId=0,cateLevel=1)
        if fistCateInformation!={}:
            for fistCateItem in fistCateInformation["cate"]["result"]:
                cateName=fistCateItem["cateName"]
                cateId=fistCateItem["cateId"]
                parentId=fistCateInformation["parentId"]
                # sql插入一级标题
                createdTime=time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                time.sleep(0.2)
                self.insertMysql("insert into 1688_kj_commodity_index \
                                 (parent_id,cate_id,cate_name,created_time,cate_level)\
                                 values ('%s','%s','%s','%s','%s')"%(parentId,cateId,cateName,createdTime,1))
                
                secondCateInformation=self.get_goods_cate(parentId=cateId,cateLevel=2)
                if secondCateInformation!={}:
                    for secondCateItem in secondCateInformation["cate"]["result"]:
                        cateName=secondCateItem["cateName"]
                        cateId=secondCateItem["cateId"]
                        parentId=secondCateInformation["parentId"]
                        # print(parentId,cateId,cateName)
                        # sql插入二级标题
                        time.sleep(0.2)
                        self.insertMysql("insert into 1688_kj_commodity_index \
                                 (parent_id,cate_id,cate_name,created_time,cate_level)\
                                 values ('%s','%s','%s','%s','%s')"%(parentId,cateId,cateName,createdTime,2))
                
                        threeCateInformation=self.get_goods_cate(parentId=cateId,cateLevel=3)
                        if threeCateInformation!={}:
                            for threeCateItem in threeCateInformation["cate"]["result"]:
                                cateName=threeCateItem["cateName"]
                                cateId=threeCateItem["cateId"]
                                parentId=threeCateInformation["parentId"]
                                # print(parentId,cateId,cateName)
                                # sql插入三级标题
                                time.sleep(0.2)
                                self.insertMysql("insert into 1688_kj_commodity_index \
                                                (parent_id,cate_id,cate_name,created_time,cate_level)\
                                                values ('%s','%s','%s','%s','%s')"%(parentId,cateId,cateName,createdTime,3))
                                
                                fourCateInformation=self.get_goods_cate(parentId=cateId,cateLevel=4)
                                if fourCateInformation!={}:
                                    for fourCateItem in fourCateInformation["cate"]["result"]:
                                        cateName=fourCateItem["cateName"]
                                        cateId=fourCateItem["cateId"]
                                        parentId=fourCateItem["parentId"]    
                                        print(parentId,cateId,cateName)
                                        time.sleep(0.2)
                                        # sql插入四级标题
                                        self.insertMysql("insert into 1688_kj_commodity_index \
                                                        (parent_id,cate_id,cate_name,created_time,cate_level)\
                                                        values ('%s','%s','%s','%s','%s')"%(parentId,cateId,cateName,createdTime,4))
    
    # 从mysql中查询所有的最后一级标题信息
    def get_last_good(self):
        pass
    
    # 定义一个保存到商品信息表的方法
    def save_commodity(self):
        pass
    
    # 定义一共获取商品信息表的方法
    def get_commodity(self):
        pass
    
    # 定义一共保存到商品详情表的方便
    def save_detail(self):
        pass
    
    # 爬取信息，目前考虑到最多四级目录
    def spider(self):
        pass
        
                                                                         
                
if __name__ == '__main__':
    obj=KJ()
    # print(obj.get_goods_cate(2,2))
    # obj.spider()
    obj.save_cate()
    # print(obj.getgoodsIndex(4))
    # print(obj.get_goods_list(2,97,3))