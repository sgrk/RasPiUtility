# -*- coding: utf-8 -*-
#!/usr/bin/env python3
from twitter import *
from datetime import datetime

def get_CPU_Temp(self):
    f = open("/sys/class/thermal/thermal_zone0/temp","r")
    temp=int(f.read())
    f.close()
    temp=temp/1000
    return temp
if __name__ == "__main__":
    time = datetime.now().strftime('%H:%M:%S')
    temp=str(get_CPU_Temp())
    txt="raspberry pi CPU temp:{0}°C({1})".format(temp,time)
    print(txt)