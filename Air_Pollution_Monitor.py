#!/usr/bin/python3
import requests
from pushbullet import Pushbullet
from datetime import datetime


url = "http://www.pm25.in/api/querys/pm2_5.json?city=chengdu&token=5j1znBVAsnSf5xQyNQyq&stations=no"
r = requests.get(url)
response_dict = r.json()
a = str(response_dict).replace("[{"," ").replace("}]","").replace(",","\n").replace("'","")

pb = Pushbullet("o.6OvO8m6uoRoxjkD4v8ll9TuHrNWTg9RA")

dt = datetime.now()
t = dt.strftime("%Y-%m-%d %H:%M")

push = pb.push_note(t+" 成都的空气污染", a)
