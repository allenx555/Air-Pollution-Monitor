#!/usr/bin/python3
import requests
from pushbullet import Pushbullet
from datetime import datetime


url = "http://www.pm25.in/api/querys/pm2_5.json?city=chengdu&token=5j1znBVAsnSf5xQyNQyq&stations=no"
r = requests.get(url)
response_dict = r.json()

for i in response_dict:
    m = i.get('aqi')
    if m <= 50:
        n = "\n空气质量不错，开窗通风吧"
    elif m >= 150:
        n = "\n空气质量很糟糕， 快关窗户为自己续一秒"
a = str(response_dict).replace("[{"," ").replace("}]","").replace(",","\n").replace("'","") + n

pb = Pushbullet("o.6OvO8m6uoRoxjkD4v8ll9TuHrNWTg9RA")

dt = datetime.now()
t = dt.strftime("%Y-%m-%d %H:%M")

push = pb.push_note(t+" 成都的空气污染", a)
