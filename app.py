from teachable import main
import sys
from multiprocessing import Process
import time
from Cam.apps import run_server
from Cam.classify import render_gen


def f():
    sys.exit(main(sys.argv))


def l():
    run_server(render_gen)



if __name__ == '__main__':
    global p
    p = Process(target=f)
    p.start()
    global r
    r = Process(target=l)
    r.start()
    

