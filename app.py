from flask import Flask, render_template
from flask_socketio import SocketIO
from flask_socketio import SocketIO, emit
import sys
import time
import logging
from watchdog.observers import Observer
from watchdog.events import LoggingEventHandler
import os
import sys
import json

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


@app.route('/', methods=["POST","GET"])
def home():
    return render_template("index.html")



if __name__ == "__main__":

    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s - %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S')
    path = "/Users/yanghaocheng/Desktop/h/pcode/"
    event_handler = LoggingEventHandler()
    observer = Observer()
    observer.schedule(event_handler, path, recursive=True)
    observer.start()
    socketio.run(app, debug=True)
    
