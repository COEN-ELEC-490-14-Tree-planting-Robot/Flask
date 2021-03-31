from flask import Flask, render_template, request
from flask_socketio import SocketIO
from flask_socketio import SocketIO, emit
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



if __name__ == "__main__":
    socketio.run(app, debug=False)
