"""
pymysql使用流程
1. 建立数据库连接(db = pymysql.connect(...))
2. 创建游标对象(cur = db.cursor())
3. 游标方法: cur.execute("insert ....")
4. 提交到数据库或者获取数据 : db.commit()/db.fetchall()
5. 关闭游标对象 :cur.close()
6. 断开数据库连接 :db.close()
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
# 读操作  -->    fetch
sql = "select name,age,sex from class_1 where sex='m';"
cur.execute(sql)

# 遍历游标对象获取查询记录
for i in cur:
    print(i)

# u关闭游标和数据库
cur.close()
db.close()
