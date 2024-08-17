
#  1個按鍵雨一個LED,按鍵壓一下LED亮-->開 , 按鍵再壓一下LED熄滅-->關
#  並且顯示日期時間

import signal
from gpiozero import Button,LED
from datetime import datetime

def user_release():
    print("使用者按下放開")
    led.toggle()

    now=datetime.now()
    now_str=now.strftime("%Y-%m-%d %H:%M:%S")
    print(now_str)

    if led.is_lit:
        print('燈是開的\n\n')
    else:
        print('燈是關的\n')


if __name__ == '__main__':
    button = Button(pin=18)
    button.when_released = user_release 

    led=LED(pin=25)

    signal.pause()