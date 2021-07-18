#Modified by smartbuilds.io
#Date: 27.09.20
#Desc: This web application serves a motion JPEG stream
# main.py
# import the necessary packages
from flask import Flask, render_template, Response, request,url_for,redirect
from camera import VideoCamera
import time
import threading
import os
from index import Arduino_sensor

pi_camera = VideoCamera(flip=False) # flip pi camera if upside down.

def get_data():
    dht11 = Arduino_sensor('/dev/ttyACM0',9600,50)
    dht11_data = dht11.read_data()
    hum_value = dht11_data[0]
    tem_value = dht11_data[1]
    return hum_value,tem_value


# App Globals (do not edit)
app = Flask(__name__)
@app.route('/login',methods = ['POST', 'GET'])
def login_index ():
    return render_template('login.html')
def login():
   if request.method == 'POST':
      lname = request.form['lname']
      return redirect(url_for('main',name = lname))
   else:
      lname = request.args.get('lname')
      return redirect(url_for('main',name = lname))
    
def index_login(): 
    while True: 
        fname =  request.args.get('fname')
        lname =  request.args.get('lname')
        planttype = request.args.get('planttype')
        return fname, lname, planttype

@app.route('/main/<name>')
def index():
    while True:
        timeNow = time.asctime( time.localtime(time.time()) )
        hum_value,tem_value = get_data()
        fname,lname,planttype = index_login()
        return render_template('index.html',hum_value = hum_value,tem_value = tem_value,time_value = timeNow,fname = fname, lname = lname, planttype = planttype ) #you can customze index.html here

def gen(camera):
    #get camera frame
    while True:
        frame = camera.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')

@app.route('/video_feed')
def video_feed():
    return Response(gen(pi_camera),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':

    app.run(host='0.0.0.0', debug=False)
    


