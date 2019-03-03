# SQL/mongodb
# table/collection 数据库表/集合
# row/document 数据记录行/文档
# column/field 数据字段/域
# primary key MongoDB自动将_id字段设置为主键

# 基本操作命令
# db: 查看当前数据库
# # show dbs: 查看所有数据库
# # use 数据库名：切换数据库，没有则创建
# # db.dropDatabase(): 删除当前指向的数据库
# # db.集合名.insert(value): 添加数据到指定的集合中
# # db.集合名.find(): 从指定的集合查找数据

import pymongo

# 获取连接mongodb的对象
client = pymongo.MongoClient('localhost', port=27017)
# 获取数据库（没有则创建）
db = client.test
# 获取数据库中的集合（也就是mysql中的表,没有则创建）
collection = db.qa
# 写入数据
# collection.insert({'username': 'aaa'})
# collection.insert_many([
#     {
#         "username": "aaa",
#         "age": 18
#     },
#     {
#         "username": "bbb",
#         "age": 19
#     }
# ])

# 查找数据
# cursor = collection.find()
# for x in cursor:
#     print(x)
# result = collection.find_one({"age": 18})
# print(result)

# 更新数据
# 第一个参数为条件，第二个参数为更改的数据
# collection.update_one({"username": "bbb"}, {"$set": {"username": "ccc"}})
# collection.update_many({"username": "aaa"}, {"$set": {"username": "bbb"}})

# 删除数据
# collection.delete_one({"username": "bbb"})
collection.delete_many({"username": "bbb"})