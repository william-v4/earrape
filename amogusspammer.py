from os import system
from multiprocessing import Process as process
from time import sleep
from wave import open as openwav


def play(): 
    system('aplay amogus.wav')

amogus = 0
repeat = 0

while True: 
    if amogus == 0 and repeat == 4: 
        system('mpv amogussfx.ogg')
        amogus = 1
    process(target=play)
    process(target=play).start()
    sleep(0.5)
    repeat += 1
    print(repeat)