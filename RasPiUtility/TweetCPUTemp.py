#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from twitter import *
from datetime import datetime

def get_CPU_Temp():
    f = open("/sys/class/thermal/thermal_zone0/temp","r")
    temp=int(f.read())
    f.close()
    temp=temp/1000
    return temp
if __name__ == "__main__":
    time = datetime.now().strftime('%H:%M:%S')
    temp=str(get_CPU_Temp())   
    txt="raspberry pi CPU temp:{0}°C({1})".format(temp,time)
 
    consumer_key    = "[Consumer Key]"
    consumer_secret = "[Consumer Secret]"
    access_token    = "[Access Token]"
    access_secret   = "[Access Token Secret]"
 
    twitter = Twitter(auth=OAuth(
    access_token, access_secret, consumer_key, consumer_secret)
    )
    twitter.statuses.update(status=txt)