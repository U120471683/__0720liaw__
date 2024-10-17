import paho.mqtt.client as mqtt
import redis

connection = redis.Redis(host='192.168.1.125',port=6379) #连接redis server 
print(connection.ping()) #测试是否连接成功

def on_message(mosq, obj, msg):
    topic = msg.topic
    message = msg.payload.decode('utf-8')
    redis_conn.rpush(topic,message)
    print(f"topic={topic},message:{message}")

if __name__ == '__main__':

    print('1')
    client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
    client.on_message = on_message

    client.connect('127.0.0.1')
    client.subscribe('501教室/老師桌燈',qos=2)
    print('1')
    client.loop_forever()