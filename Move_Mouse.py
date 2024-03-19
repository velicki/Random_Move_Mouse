import threading
import pyautogui as pag
import random
import time
import keyboard
import sys

exit_flag = False

def capture_input():
    global exit_flag
    while True:
        if keyboard.is_pressed('q'):
            print('Key "q" is pressed. EXIT program!')
            exit_flag = True
            break
        time.sleep(0.1)

print('To STOP program press "q"')

input_thread = threading.Thread(target=capture_input)
input_thread.daemon = True
input_thread.start()

while not exit_flag:
    x = random.randint(500,800)
    y = random.randint(200,600)
    t = round(random.uniform(0.2,2.0), 1)
    t_sleep = round(random.uniform(0.5,2.0), 1)

    print(f'x coordinate is {x}, y coordinate is {y}, time/speed of moving is {t}, and time sleep is {t_sleep}')

    pag.moveTo(x,y,t)
    time.sleep(t_sleep)

sys.exit()


    
