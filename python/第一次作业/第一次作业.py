"""
将2012_2021.csv文件中的数据,整理到excel中; 要求:

根据年份创建对应的sheet,
将年份对应的数据保存到对应的sheet中,
使用面向对象实现
文件打开编码格式:utf-8-sig
"""

import pandas as pd
import openpyxl


class DataToExcel:
    def __init__(self, csv_file):
        self.csv_file = csv_file

    def read_csv(self):
        return pd.read_csv(self.csv_file, encoding='utf-8-sig')

    def save_to_excel(self):
        data = self.read_csv()
        with pd.ExcelWriter('output.xlsx', engine='openpyxl') as writer:
            has_sheets = False
            for year, group_data in data.groupby('年份', sort=False):
                has_sheets = True
                group_data.to_excel(writer, sheet_name=str(year), index=False)
            if not has_sheets:
                # 如果没有任何工作表创建，需要添加一个默认的工作表
                pd.DataFrame().to_excel(writer, sheet_name='Sheet1')


# 使用方法
csv_handler = DataToExcel(r'C:\Users\XCF\Desktop\驭风计划\第一次作业\题目1数据.csv')
csv_handler.save_to_excel()
