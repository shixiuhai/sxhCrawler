import requests
import logging
import time
import json
import pymysql
logging.basicConfig(level=logging.INFO,filename="./kuajing.log",
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
    # sql 的增 删 改 
    def exec_mysql(self,sql:str)->None:
        try:
            cursor=self.db.cursor()
            cursor.execute(sql)
            # 插入执行必须要提交事务
            self.db.commit()
            cursor.close()
        # pymysql.err.OperationalError: (2003, "Can't connect to MySQL server on '183.134.60.170' (timed out)")
        except Exception as error:
            logging.error("执行语句出错，错误是%s"%error)
            # print(error.__str__())
            if "Can't connect to MySQL" in error.__str__():
                self.db=pymysql.connect(host=self.host,port=int(self.port),user=self.user,passwd=self.passwd,db=self.db)
    
    # sql 插入 返回 插入id
    def exec_mysql_id(self,sql:str)->int:
        try:
            cursor=self.db.cursor()
            cursor.execute(sql)
            insertId=self.db.insert_id()
            # 插入执行必须要提交事务
            self.db.commit()
            cursor.close()
            return insertId
        # pymysql.err.OperationalError: (2003, "Can't connect to MySQL server on '183.134.60.170' (timed out)")
        except Exception as error:
            logging.error("执行语句出错，错误是%s"%error)
            # print(error.__str__())
            if "Can't connect to MySQL" in error.__str__():
                self.db=pymysql.connect(host=self.host,port=int(self.port),user=self.user,passwd=self.passwd,db=self.db)
            return 0
    
    # sql的查询
    def select_mysql(self,sql:str)->list:
        try:
            cursor=self.db.cursor()
            cursor.execute(sql)
            return list(cursor.fetchall())
        except Exception as error:
            logging.error("查询语句出错，错误是%s"%error)
            # print(error.__str__())
            if "Can't connect to MySQL" in error.__str__():
                self.db=pymysql.connect(host=self.host,port=int(self.port),user=self.user,passwd=self.passwd,db=self.db)
            return []
        
    # 保存标题到数据库
    def save_cate(self,taskId):
        fistCateInformation=self.get_goods_cate(parentId=0,cateLevel=1)
        if fistCateInformation!={}:
            for fistCateItem in fistCateInformation["cate"]["result"]:
                cateName=fistCateItem["cateName"]
                cateId=fistCateItem["cateId"]
                parentId=fistCateInformation["parentId"]
                # sql插入一级标题
                createdTime=time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                time.sleep(0.2)
                self.exec_mysql("insert into 1688_kj_commodity_index \
                                 (parent_id,cate_id,cate_name,created_time,cate_level,task_id)\
                                 values ('%s','%s','%s','%s','%s','%s')"%(parentId,cateId,cateName,createdTime,1,taskId))
                
                secondCateInformation=self.get_goods_cate(parentId=cateId,cateLevel=2)
                if secondCateInformation!={}:
                    for secondCateItem in secondCateInformation["cate"]["result"]:
                        cateName=secondCateItem["cateName"]
                        cateId=secondCateItem["cateId"]
                        parentId=secondCateInformation["parentId"]
                        # print(parentId,cateId,cateName)
                        # sql插入二级标题
                        time.sleep(0.2)
                        self.exec_mysql("insert into 1688_kj_commodity_index \
                                 (parent_id,cate_id,cate_name,created_time,cate_level,task_id)\
                                 values ('%s','%s','%s','%s','%s','%s')"%(parentId,cateId,cateName,createdTime,2,taskId))
                
                        threeCateInformation=self.get_goods_cate(parentId=cateId,cateLevel=3)
                        if threeCateInformation!={}:
                            for threeCateItem in threeCateInformation["cate"]["result"]:
                                cateName=threeCateItem["cateName"]
                                cateId=threeCateItem["cateId"]
                                parentId=threeCateInformation["parentId"]
                                # print(parentId,cateId,cateName)
                                # sql插入三级标题
                                time.sleep(0.2)
                                self.exec_mysql("insert into 1688_kj_commodity_index \
                                 (parent_id,cate_id,cate_name,created_time,cate_level,task_id)\
                                 values ('%s','%s','%s','%s','%s','%s')"%(parentId,cateId,cateName,createdTime,3,taskId))
                                
                                fourCateInformation=self.get_goods_cate(parentId=cateId,cateLevel=4)
                                if fourCateInformation!={}:
                                    for fourCateItem in fourCateInformation["cate"]["result"]:
                                        cateName=fourCateItem["cateName"]
                                        cateId=fourCateItem["cateId"]
                                        parentId=fourCateItem["parentId"]    
                                        print(parentId,cateId,cateName)
                                        time.sleep(0.2)
                                        # sql插入四级标题
                                        self.exec_mysql("insert into 1688_kj_commodity_index \
                                        (parent_id,cate_id,cate_name,created_time,cate_level,task_id)\
                                        values ('%s','%s','%s','%s','%s','%s')"%(parentId,cateId,cateName,createdTime,4,taskId))
    
    # 从mysql中查询所有的最后一级标题信息
    def get_last_cate(self,taskId)->list:
        result=self.select_mysql("SELECT id,cate_name,cate_id,cate_level,task_id \
                                FROM 1688_kj_commodity_index  WHERE cate_id NOT IN \
                                ( SELECT parent_id FROM 1688_kj_commodity_index) and task_id=%s"%taskId)
        return result
        
    # 定义一共创建任务的方法
    def created_task(self,tasktype:int=2)->int:
        # 任务创建时间
        createdTime=time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        if tasktype==1:
            describe="手动爬取任务："
            yourInput=input("请输入你对任务的描述")
            describe=describe+yourInput
            # 创建任务
            taskId=self.exec_mysql_id("insert into 1688_kj_commodity_task (created_time,type,task_describe) values ('%s','%s','%s')"%(createdTime,tasktype,describe))
            if taskId==0:
                logging.error("爬取任务启动失败")
            else:
                self.spider(taskId=taskId)
        if tasktype==2:
            describe="自动爬取任务"
            taskId=self.exec_mysql_id("insert into 1688_kj_commodity_task (created_time,type,task_describe) values ('%s','%s','%s')"%(createdTime,tasktype,describe))
            if taskId==0:
                logging.error("爬取任务启动失败")
            else:
                self.spider(taskId=taskId)
                
    # 定义一个保存到商品信息表的方法
    def save_commodity(self,item:dict):
        # qmarks = ', '.join(['%s'] * len(item))
        # columns = ', '.join(item.keys())
        self.exec_mysql("insert into 1688_kj_commodity (`index_id`, `cate_level`, `cate_id`, `cate_name`, `gmt_create`, `offer_picurl`, `price`, `good_subject`, `offer_id`, `offer_url`, `created_time`, `total_page`, `task_id`, `rank`) \
                        values ('%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s')"\
                        %(item["index_id"],item["cate_level"],item["cate_id"],item["cate_name"],item["gmt_create"],item["offer_picurl"],item["price"],item["subject"],item["offer_id"],item["offer_url"],item["created_time"],item["total_page"],item["task_id"],item["rank"]))
    
    # 定义一个获取商品信息表的方法
    def get_commodity(self):
        pass
    
    # 定义一个保存到商品详情表的方法
    def save_detail(self,item:dict):
        pass
    
    # 定义一个爬取商品信息的方法
    def spider_goods_list(self,indexId,cateName,cateId,cateLevel,taskId):
        try:
            # 第一类是hot 
            resp=self.get_goods_list(cateLevel=cateLevel,cateId=cateId,pageNo=1,rankType="hot")
            if resp!={}:
                totalPage=int(resp["page"]["total"]/resp["page"]["pageSize"] )
                for pageNo in range(1,totalPage+1):
                    time.sleep(0.3)
                    try:
                        resp=self.get_goods_list(cateLevel=cateLevel,cateId=cateId,pageNo=pageNo,rankType="hot")
                        # 从resp里提取商品信息
                        for oneItem in resp["result"]:
                            try:
                                gmtCreate=oneItem["gmt_create"]
                                offerPicurl=oneItem["offerPicUrl"]
                                price=oneItem["price"]
                                subject=oneItem["subject"]
                                offerId=oneItem["offerId"]
                            except Exception as error:
                                logging.error("提取数据搓洗错误错误是%s"%error)
                                continue
                            offerUrl="https://detail.1688.com/offer/"+str(offerId)+".html"
                            createdTime=time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                            totalPage=totalPage
                            indexId=indexId
                            cateName=cateName
                            cateId=cateId
                            cateLevel=cateLevel
                            taskId=taskId
                            rank=1
                            item={"index_id":indexId,
                                "cate_level":cateLevel,
                                "cate_id":cateId,
                                "cate_name":cateName,
                                "gmt_create":gmtCreate,
                                "offer_picurl":offerPicurl,
                                "price":price,
                                "subject":subject,
                                "offer_id":offerId,
                                "offer_url":offerUrl,
                                "created_time":createdTime,
                                "total_page":totalPage,
                                "task_id":taskId,
                                "rank":rank}
                            # 存库
                            self.save_commodity(item=item)
                    except Exception as error:
                        print(error)
                        logging.error("爬取页面出现错误,错误是%s"%error)
                        continue
            
            # 第二类是rising
            resp=self.get_goods_list(cateLevel=cateLevel,cateId=cateId,pageNo=1,rankType="rising")
            if resp!={}:
                totalPage=int(resp["page"]["total"]/resp["page"]["pageSize"] )
                for pageNo in range(1,totalPage+1):
                    time.sleep(0.3)
                    try:
                        resp=self.get_goods_list(cateLevel=cateLevel,cateId=cateId,pageNo=pageNo,rankType="rising")
                        # 从resp里提取商品信息
                        for oneItem in resp["result"]:
                            try:
                                gmtCreate=oneItem["gmt_create"]
                                offerPicurl=oneItem["offerPicUrl"]
                                price=oneItem["price"]
                                subject=oneItem["subject"]
                                offerId=oneItem["offerId"]
                            except Exception as error:
                                logging.error("提取数据搓洗错误错误是%s"%error)
                                continue
                            offerUrl="https://detail.1688.com/offer/"+str(offerId)+".html"
                            createdTime=time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                            totalPage=totalPage
                            indexId=indexId
                            cateName=cateName
                            cateId=cateId
                            cateLevel=cateLevel
                            taskId=taskId
                            rank=2
                            item={"index_id":indexId,
                                "cate_level":cateLevel,
                                "cate_id":cateId,
                                "cate_name":cateName,
                                "gmt_create":gmtCreate,
                                "offer_picurl":offerPicurl,
                                "price":price,
                                "subject":subject,
                                "offer_id":offerId,
                                "offer_url":offerUrl,
                                "created_time":createdTime,
                                "total_page":totalPage,
                                "task_id":taskId,
                                "rank":rank}
                            # 存库
                            self.save_commodity(item=item)
                    except Exception as error:
                        print(error)
                        logging.error("爬取页面出现错误，错误是%s"%error)
                        continue
        except Exception as error:
            logging.error("获取商品信息出现错误，错误是%s"%error)

                    
                    
                    
                
    # 爬取信息，目前考虑到最多四级目录
    def spider(self,taskId):
        # 保存所有标题信息到index表
        self.save_cate(taskId)
        # 从index获取最后一级标题信息
        lastCateList=self.get_last_cate(taskId)
        if len(lastCateList)!=0:
            for lastCateItem in lastCateList:
                # id,cate_name,cate_id,cate_level,task_id
                indexId=lastCateItem[0]
                cateName=lastCateItem[1]
                cateId=lastCateItem[2]
                cateLevel=lastCateItem[3]
                taskId=lastCateItem[4]
                # 进行爬取任务
                self.spider_goods_list(indexId,cateName,cateId,cateLevel,taskId)
                
                                        
if __name__ == '__main__':
    obj=KJ()
    # print(obj.get_last_cate(14))
    obj.created_task()
    #print(obj.get_last_cate())
    # obj.spider_goods_list(5389,'机械门锁',1033168,3,1)
    # print(obj.created_task())
    # print(obj.get_goods_cate(2,2))
    # obj.spider()
    #obj.save_cate(1)
    # print(obj.getgoodsIndex(4))
    # print(obj.get_goods_list(2,97,3))