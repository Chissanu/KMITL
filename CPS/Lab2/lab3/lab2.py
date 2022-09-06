import serial
from datetime import datetime
import time
import keyboard

SampleTime = '500'

with serial.Serial('COM8',9600) as serArd:
    print(f"The arduino board is connected through {serArd.port}")
    time.sleep(2)
    serArd.reset_input_buffer()
    
    dList = []
    tList = []
    
    if (serArd.writable()):
        serArd.write(SampleTime.encode())
        print(serArd.readline().decode().rstrip())
    while not keyboard.is_pressed('q'):
        if serArd.inWaiting() > 0:
            rec_time = datetime.now().strftime('%H:%M:%S.%f')
            myData = serArd.readline().decode().rstrip()
            try:
                myData = float(myData)
                cm = str(round(myData / 57, 2))
                dList.append(cm)
                tList.append(int(rec_time[6:8]))
                #print(f"The distance is {cm}cm : {rec_time}")
            except:
                print("No data")
            
            if abs(float(dList[0])) < 6:
                if len(dList) == 1:
                    pass
                else:
                    prev = dList[0]
                    prevTime = tList[0]
                    cur = float(serArd.readline().decode().rstrip())
                    cur = str(round(cur / 57, 2))
                    curTime = datetime.now().strftime('%H:%M:%S.%f')
                    curTime = int(curTime[6:8])
                    
                    temp = prev - int(cur)
                    divTime = curTime - prevTime
                    
                    print(prevTime)
                    #print(divTime)
                    # if cur > prev:
                    #     print("Going forward")
                    #     print(f"Going forward at {abs(float(cur))/(divTime)}cm/s")
                    # elif cur < prev:
                    #     print("Going backward")
                    # else:
                    #     print("Still")
                    #print(f"Prev time: {prev}, current time is {cur}")
                    dList.pop(0)
            else:
                print("Clear")
                dList = []