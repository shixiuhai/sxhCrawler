# 1. 把excel里的除第一行外所有的单元格的数据放入到python的列表中
# 怎么读取excel
# a=["a","a","b","c"]
# b_set={"a","b","c"}
# result={}
# for key in (b_set):
#     result[key]=a.count(key)


    
import pandas as pd
workbook=pd.read_excel("袜子批发.xlsx",sheet_name="Sheet1")
str_list=[]
# 遍历所有单元格并打印它们的值
for i in range(len(workbook.index)):
    if i==0:
        continue
    for j in range(len(workbook.columns)):
        if pd.isna(workbook.iloc[i,j]):
            continue
        else:
            str_list.append(workbook.iloc[i,j])
# print(str_list)        
str_set=set(str_list)
str_result={}
for str_key in str_set:
    str_result[str_key]=str_list.count(str_key)
print(str_result)

key_list=[]
value_list=[]
for key in str_result.keys():
    key_list.append(key)
    value_list.append(str_result[key])


data={"名称":key_list,
      "次数":value_list}
dataFrame= pd.DataFrame(data)
dataFrame.to_excel("out.xlsx")




    
# https://juejin.cn/s/pandas%E9%81%8D%E5%8E%86%E5%8D%95%E5%85%83%E6%A0%BC%E6%95%B0%E6%8D%AE

# 构建dateframe格式

# pip3 install pandas 网络安装
# 2. 统计列表里的字符串有多少类 使用python集合实现
# 3. 创建字典，遍历集合 通过 集合中的元素和list 的count 统计每个字符串出现的次数
# 4. 打印出字典