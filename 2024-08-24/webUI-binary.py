import streamlit as st
import redis
from dotenv import load_dotenv
import os
import json
import pandas as pd
from streamlit_autorefresh import st_autorefresh


load_dotenv()
st_autorefresh()

redis_conn = redis.Redis(host=os.environ['REDIS_HOST'], port=6379,password=os.environ['REDIS_PASSWORD'])
bytes_list = redis_conn.lrange('501教室/老師桌燈',-5,-1)
st.write(bytes_list)
st.title("訓練通教室")
st.header("感測器:blue[cool] :sunglasses:")