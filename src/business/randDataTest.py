from db import *

HEAD_CODE = '999999'
HEAD_NAME = '全国'
REGION_CODE = '210963'
REGION_NAME = '上海区'
CENTER_CODE = '210901'
CENTER_NAME = '上海'
BRANCH_CODE = '210448'
BRANCH_NAME = '上海市闵行区诸翟'
SUB_CODE = '021203'
SUB_NAME = '上海市闵行区纪鹤'
K_CODE = 'K0000001'
K_NAME = '大客户001号测试者'
STORE_CODE = 'ST0000001'
STORE_NAME = '店铺001号测试者'

ORG_TYPE_LIST = ['HEAD', 'REGION_MANAGE', 'TRANSFER_CENTER', 'BRANCH', 'SUB_DEPARTMENT', 'CUSTOMER', 'STORE']
FIRST_TAB_TYPE = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
SECOND_TAB_TYPE = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
THIRD_TAB_TYPE = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']


class RandDataTest:

    def __init__(self, db):
        self.db = db
        self.columnList = []
        self.dimColumns = []
        self.buzColumns = []

    def getTableInfo(self, tableName: str):
        cursor = self.db.cursor()
        cursor.execute(
            "select * from information_schema.columns where table_name = %s", tableName)
        for data in cursor.fetchall():
            print(data)
            if data[3] == 'id':
                continue
            self.columnList.append((data[3], data[7]))
            if data[3].endswith('code') or data[3].endswith('name') or data[3].endswith('type') or data[3] in (
                    'rpt_date'):
                self.dimColumns.append((data[3], data[7]))
            else:
                self.buzColumns.append((data[3], data[7]))
        dbApi.close(self.db)
        return self.columnList, self.dimColumns, self.buzColumns

    '''
        为列赋值
    '''

    def initDataForColumns(self, rpt_date: str, sum_type: str):
        preColumnList = []


if __name__ == '__main__':
    rdt = RandDataTest(dbApi.connect('bigdata_mutiple'))
    columns, dimColumns, buzColumns = rdt.getTableInfo(tableName='t_app_store_analysis_total_store_m')
    print('*' * 20)
    print(columns)
    print(dimColumns)
    print(buzColumns)
