# 1. 把excel里的除第一行外所有的单元格的数据放入到python的列表中
# 怎么读取excel
import pandas as pd
workbook=pd.read_excel("袜子批发.xlsx",sheet_name="Sheet1")
# 遍历所有单元格并打印它们的值
for i in range(len(workbook.index)):
    for j in range(len(workbook.columns)):
        print(workbook.iloc[i,j])
# pip3 install pandas 网络安装
# 2. 统计列表里的字符串有多少类 使用python集合实现
# 3. 创建字典，遍历集合 通过 集合中的元素和list 的count 统计每个字符串出现的次数
# 4. 打印出字典