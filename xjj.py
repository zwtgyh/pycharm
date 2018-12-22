import pymysql
import time
start = time.perf_counter()
config = dict(host='localhost', user='root', password='zhangwentao123',
             cursorclass=pymysql.cursors.DictCursor
             )
conn = pymysql.Connect(**config)
conn.autocommit(1)
cursor = conn.cursor()
#####################################
import pandas as pd
df = pd.read_csv('/home/zwt/Desktop/201801.csv',encoding='utf-8',usecols=[0,1,2,3,4,5,6,7,8,9,10],parse_dates=['TradingDate'])
# df.head()
##################################
def make_table_sql(df):
    columns = df.columns.tolist()
    types = df.ftypes
    make_table = []
    for item in columns:
        if 'int' in types[item]:
            char = item + ' INT'
        elif 'float' in types[item]:
            char = item + ' FLOAT'
        elif 'object' in types[item]:
            char = item + ' VARCHAR(225)'
        elif 'datetime' in types[item]:
            char = item + ' DATETIME'
        make_table.append(char)
    return ','.join(make_table)
def csv_to_mysql(db_name, table_name, df):
    cursor.execute('CREATE DATABASE IF NOT EXISTS {}'.format(db_name))
    conn.select_db(db_name)
    cursor.execute('CREATE TABLE IF NOT EXISTS {}({})'.format(table_name, make_table_sql(df)))
    df['TradingDate'] = df['TradingDate'].astype('str')
    values = df.values.tolist()
    s = ','.join(['%s' for _ in range(len(df.columns))])
    cursor.executemany('INSERT INTO {} VALUES ({})'.format(table_name, s), values)
df2 = df.astype(object).where(pd.notnull(df), None)
#csv_to_mysql(db_name = 'xjj', table_name = 'test', df = df2)
# cursor.close()
# conn.close()
# ###完成
# cursor.execute('select * from test where TradingDate between "2018-01-01 00:00:00" and "2018-01-10 00:00:00"')
# data = cursor.fetchall()
#
#
#
#
# StockCode = df.iloc[:,1]                   #取出股票代码那一列数据
# StockCode_arry = StockCode.values          #以列表显示
# StockCode_arry2 = set(StockCode_arry)      #以集合显示来剔除重复项
# len(StockCode_arry2)                       #查看长度
# fff = list(StockCode_arry2)                #列表

for i in range(76456):
    x = df['StockCode'][i]
    xx = x.astype(str)
    csv_to_mysql(db_name='xjj', table_name='StockCode{}'.format(xx), df = df2[i:i+1])
end = time.perf_counter()
print(end-start)