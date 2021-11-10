with open('text.txt', 'w') as file:
    file.write('Hello world!')

file = open('text.txt', 'w')

import time

def timer(time_sec):
    while time_sec:
        min, sec = divmod(time_sec, 60)
        timeformat = '{:02d}:{:02d}'.format(min,sec)
        print(timeformat, end='\r')
        time.sleep(1)
        time_sec -= 1

    print("stop")

timer(40)