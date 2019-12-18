"""
写操作
"""
import pymysql

# 链接数据库
db = pymysql.connect(host='localhost',
                     port=3306,
                     user='root',
                     password='123456',
                     database='stu',
                     charset='utf8')
# 生产游标对象   (操作数据库执行spl语句获取结果的对象)
cur = db.cursor()

# 利用游标对象执行各种sql语句
# 写操作  -->    commit  rollback
try:
    sql = "insert into class_1 values(7,'yun',18,'w',96)"
    cur.execute(sql)
    db.commit()  # 提交结果
except Exception as e:
    print(e)
    db.rollback()  # 回滚 没有写入数据库的操作召回

# u关闭游标和数据库
cur.close()
db.close()
