
import paho.mqtt.client as mqtt
import redis
from dotenv import load_dotenv
import os
from tools import file
import json



load_dotenv()


redis_conn = redis.Redis(host=os.environ['REDIS_HOST'], port=6379,password=os.environ['REDIS_PASSWORD'])
render_redis_conn = redis.Redis.from_url(os.environ['RENDER_REDIS'])

def on_message(mosq, obj, msg):
    topic = msg.topic
    message = msg.payload.decode('utf-8')
    redis_conn.rpush(topic,message)
    
    render_redis_conn.rpush(topic,message)
    #print(f"topic={topic},message:{message}")
    message_dict=json.loads(s=message)
    print(message_dict)
    create_log_file()

if __name__ == '__main__':
    client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
    client.username_pw_set(username=os.environ['MQTT_USERNAME'],password=os.environ['MQTT_PASSWORD'])
    client.on_message = on_message
    client.connect(os.environ['MQTT_SERVER'])
    client.subscribe('501教室/老師桌燈',qos=2)
    client.loop_forever()