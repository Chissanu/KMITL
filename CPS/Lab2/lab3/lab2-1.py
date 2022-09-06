import serial
from datetime import datetime
import time
import keyboard
SampleTime = '500' # in milli second
# Sampling Tin
timelist = [0]
dlist = [0]
index = 0
with serial. Serial('COM8',9600) as serArd:
    print(f"The Arduino board is connect through {serArd.port}")
    time. sleep(2)
    serArd.reset_input_buffer()
    if (serArd.writable()):
        serArd.write(SampleTime.encode())
        print(serArd.readline().decode().rstrip())
    while not keyboard.is_pressed('q'):
        if (serArd.inWaiting() > 0):
            rec_time = datetime.now().strftime('%H:%M: %S.%f')
            timelist.append(float(rec_time[8:]))
            index += 1
            myData = serArd.readline().decode().rstrip()
            try:
                myData = float(myData)
                distance = myData*178*(10**-4)
                dlist.append(float(distance))
                if distance > 20:
                    print("Clear")
                else:
                    timepass = timelist[index] - timelist[index -1]
                    change = dlist[index] - dlist[index - 1]
                    if change > 1:
                        print(str(round((change/abs(timepass)), 2)), "cm/s backwards" )
                    if change < -1:
                        print(str(round(abs(change) / abs(timepass), 2)), "cm/s forwards")
                    else:
                        print(0, "cm/s")
            except:
                print("No data")
