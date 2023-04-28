"""excel实现同一个单元格子内不同元素换行"""
import pandas as pd

data = pd.DataFrame({"Text1": ["1\n1_1\n1-2","2","3"],
                     "Text2": ["4","5\n5_1","6"],
                     "Text3": ["7","8","9"],
                     "Text4": ["11","12","13"]})

df = pd.DataFrame(data, columns = ['Text1', 'Text2','Text4', 'Text4']) 
print(df.to_excel("1.xlsx"))