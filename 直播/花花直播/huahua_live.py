import json
import requests
import time
class HH:
    def __init__(self) -> None:
        self.cookies = {
            'acw_tc': '2f61f26916792967548221899e4bb6bc2d6e27fe5a01b622e348e3beba72cb',
        }
        self.headers = {
            'Host': 'api.appbocai.com',
            # 'Cookie': 'acw_tc=2f61f26916792967548221899e4bb6bc2d6e27fe5a01b622e348e3beba72cb',
            'version': '864',
            'channel': 'wandoujia',
            'platform': '2',
            'authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHRlbmQiOiIiLCJ1aWQiOjEwMDM2MzYxNzcsImxvZ2luVHlwZSI6InFxIiwidW5vIjoxMDAzNjM2MTc3LCJpcCI6IjExMS4yLjkxLjM4IiwiaXNzIjoiZmxhc2h3aGFsZS10ZWNoIiwic291cmNlIjoid2FuZG91amlhIiwiZGV2aWNlSWQiOiIiLCJ2ZXJzaW9uIjoiODY0IiwicGxhdGZvcm0iOiIyIiwidGltZXN0YW1wIjoxNjc5Mjk3MTc1NTIzfQ.jTbAYDGUHaIJVNB4qfXV0Rkkm-Kt-rHkVXUY_ZkjUyc',
            'content-type': 'application/json; charset=UTF-8',
            'user-agent': 'okhttp/4.2.2',
        }
        
    def get_anchor(self):
        page=1
        while True:
            json_data = {
                'pageIndex': page,
                'subTab': 0,
                'tab': 0,
                'pageSize': 20,
            }
            response=requests.post('https://api.appbocai.com/huahua/live/roomList', cookies=self.cookies, headers=self.headers, json=json_data)
            if response.json()["data"]!=None:
                resp=response.json()["data"]
                for item in resp[1::]:
                    print(item)
            else:
                break
            time.sleep(10)
            
                    
    def writeAnchorTxt(self,anchorList:list,path="/home/sh/huahua/all")->None:
        returnList=json.dumps(anchorList,ensure_ascii=False)
        # 将数据写入文件
        fileName=int(time.time())
        #with open("./%s"%fileName,'w',encoding='utf-8') as f:
        #    f.write(returnList)
        with open(path+"/%s"%fileName,'w',encoding='utf-8') as f:
            f.write(returnList)
            
if __name__ == "__main__":
    obj=HH()
    obj.get_anchor()