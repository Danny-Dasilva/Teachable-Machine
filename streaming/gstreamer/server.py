from classify import streaming

# import required modules
from flask import Flask, render_template, Response 

import socket 
import io 
app = Flask(__name__) 
@app.route('/') 
def go(): 
   """Video streaming .""" 
   return "Hello World!"

@app.route('/stream') 
def index(): 
   """Video streaming .""" 
   return render_template('index.html') 

@app.route('/video_feed') 
def video_feed(): 
   """Video streaming route. Put this in the src attribute of an img tag.""" 
   return Response(streaming(), 
                   mimetype='multipart/x-mixed-replace; boundary=frame') 
if __name__ == '__main__': 
	app.run(host='0.0.0.0', debug=True, threaded=True) 