
import redis #导入redis模块 

connection = redis.Redis(host='192.168.1.125',port=6379) #连接redis server 
print(connection.ping()) #测试是否连接成功