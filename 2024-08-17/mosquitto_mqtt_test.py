import paho.mqtt.client as mqtt

# MQTT 伺服器的地址和端口
broker = "localhost"
port = 1883
topic = "test/topic"

# 當連接到 MQTT 伺服器時呼叫的回調函數
def on_connect(client, userdata, flags, rc):# 這裡的訊息是為了讓程式能夠正常運行
    print(f"Connected with result code {rc}") # 訂閱主題 
    client.subscribe(topic) # 這裡的訂閱主題是為了讓程式能夠正常運行

# 當接收到 MQTT 訊息時呼叫的回調函數
def on_message(client, userdata, msg):
    print(f"Received message: {msg.payload.decode()} on topic {msg.topic}")# 這裡的訊息是為了讓程式能夠正常運行

# 當發佈訊息時呼叫的回調函數
def on_publish(client, userdata, mid):
    print(f"Message {mid} published.")

# 建立 MQTT 客戶端
client = mqtt.Client()
client.on_connect = on_connect # 設置連接回調函數# 設置接收訊息回調函數#
client.on_message = on_message # 設置發佈訊息回調函數 
client.on_publish = on_publish # 設置用戶名和密碼# client.username_pw_set(username, password)# 連接到 MQTT 伺服器

# 連接到 MQTT 伺服器
client.connect(broker, port, 60) # 60 是 keepalive 的值 (秒) # 這裡的連接是為了讓程式能夠正常運行#            

# 發佈訊息
client.loop_start() # 開始一個新的執行緒以處理網絡流量          
client.publish(topic, "Hello MQTT!")  # 發佈訊息    # 這裡的 QoS 是 0，表示最多發佈一次，不會有回應 # QoS 1 表示至少發佈一次，有回應 # QoS 2 表示僅發佈一次，有回應      
client.loop_stop() # 停止網絡流量執行緒

# 保持程式運行以接收訊息
try:
    while True:
        pass
except KeyboardInterrupt: # 按下 Ctrl+C 時關閉連接  # 這裡的關閉連接是為了讓程式能夠正常退出
    client.disconnect() # 斷開連接  # 這裡的斷開連接是為了讓程式能夠正常退出

