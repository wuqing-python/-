"""
练习:通过程序描述登录注册过程,将其各封装为一个函数

        def  login(name,passwd):
             pass
        def  register(name,passwd):
             pass
"""
#
#
# def register(name,passwd):
#     sql="select name from user  where name='%s'"%name
#     cur.execute(sql)
#     result = cur.fetch
#     try:
#         sql="insert into user (name,passwd)values "
#         cur.execute(sql,[name,passwd])
#         db.commit()
#         return True
#     except:
#         db.rollback()
#         return False