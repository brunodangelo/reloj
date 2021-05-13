import os
import time
import datetime

while(True):
    os.system('cls')
    hora_actual=datetime.datetime.now()
    print("Son las {}:{}:{} del {}/{}/{}".format(hora_actual.hour, hora_actual.minute, hora_actual.second,hora_actual.day,hora_actual.month,hora_actual.year))
    time.sleep(1)
