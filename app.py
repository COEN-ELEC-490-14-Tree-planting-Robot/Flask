from flask import Flask, render_template, request
from flask_socketio import SocketIO
from flask_socketio import SocketIO, emit
import os
import sys
import json
import time
import logging
from watchdog.observers import Observer
from watchdog.events import LoggingEventHandler
from watchdog.events import FileSystemEventHandler
app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret'
socketio=SocketIO(app)

@socketio.on('connect')
def ws_connect():
    print('socket connected')
        
@socketio.on('disconnect')
def ws_disconnect():
    print('socket disconnected')
    
@socketio.on('wb-navi-commands')
def wb_navigate(command):
    if command == 'w':
        print(command)
    elif command == 'a':
        print(command)
    elif command == 's':
        print(command)
    elif command == 'd':
        print(command)
    elif command == 'p':
        print(command)
    elif command == 'a':
        print(command)
    elif command == 'm':
        print(command)

@socketio.on('cam-wb')
@app.route('/cam-wb', methods=['POST'])
def receiveCamWB():
    uri = request.form['uri']
    print(uri)
    socketio.emit('cam-wb',{'data' : uri})
    return 'success-cam'


@socketio.on('gps-wb')
@app.route('/gps-wb', methods=['POST'])
def receiveGPSWB():
    gps = request.form['gps']
    print(gps)
    socketio.emit('gps-wb',{'data' : gps})
    return 'success-gps'



@app.route('/', methods=["POST","GET"])
def home():
    return render_template("index.html")

class MyFileChangeHandler(FileSystemEventHandler):
    #@socketio.on('map-change')
    def dispatch(self, event):
        if "gps" in event.src_path:
            print ("gps has changed at :" + event.src_path)
            # open file and read gps
            with open('static/files/gps/gps.txt', 'rb') as f:
                gps = f.readline()
            socketio.emit('gps-change', {'data': gps.decode()})
        elif "controls" in event.src_path:
            # open file and read controls
            with open('static/files/controls/controls.txt', 'rb') as f:
                control = f.readline()
            print ("controls has changed at :" + event.src_path)
            socketio.emit('control-change', {'data': control.decode()})
        elif "E:/school/490/website\Flask\static\maps" in event.src_path:
            print ("map has changed at :" + event.src_path)
            socketio.emit('map-change')
        elif "cam-wb" in event.src_path:
            print ("cam changed at : " + event.src_path)
            socketio.emit('cam-change')
        else:
            print(event.src_path)

        

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S')
    path = "E:/school/490/website"
    event_handler = MyFileChangeHandler()
    observer = Observer()
    observer.schedule(event_handler, path, recursive=True)
    observer.start()
    socketio.run(app, debug=False)
