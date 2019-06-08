from teachable import main
import sys
from flask import Flask, render_template
from multiprocessing import Process
import time

app = Flask(__name__)

def f():
    sys.exit(main(sys.argv))

@app.route('/')
def start():
    global p
    p = Process(target=f, args=('--keyboard'))
    p.start()
    return render_template('layout.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)

