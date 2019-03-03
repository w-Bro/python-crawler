import pymysql

conn = pymysql.connect(host='localhost', user='root', password='root', database='test', port=3306)

cursor = conn.cursor()

# insert into user(id, username, age, password) values(2, 'bbb', 20, '111111')
# sql = """
# insert into user(id, username, age, password) values(null, %s, %s, %s)
# """
# username = 'spider'
# age = 21
# password = '12345'
# cursor.execute(sql, (username, age, password))
# conn.commit()

# 查找数据：
# fetchone():每次只获取一条数据
# fectchall():接收全部的返回数据
# fetchmany(size):获取指定条数的数据

# select username, age from user where id=1
sql = """
select * from user
"""
# cursor.execute(sql)
# while True:
#     result = cursor.fetchone()
#     if result:
#         print(result)
#     else:
#         break

sql = """
delete from user where id=1
"""
cursor.execute(sql)
# 插入、删除、更新都要执行commit
conn.commit()

sql = """
update user set username='aaa' where id=2
"""
cursor.execute(sql)
conn.commit()
conn.close()
