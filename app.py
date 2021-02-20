from flask import Flask, render_template
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
    try:
        #Read
        f=open("test.txt", "r")
        data= f.read()
        _=int(json.loads(data).get("counter"))+int(1)
        tem={"counter":_ }
        print(tem)
        f.close()
        emit('user', tem, broadcast=True)
        
        #write
        fw= open("test.txt", "w", encoding='utf-8')
        fw.write(json.dump(tem))
        fw.close()
        emit('user', tem, broadcast=True)
        
        
    except Exception as e:
        fw=open("test.txt", "w", encoding='utf-8')
        fw.write(json.dump({"counter":0}))
        fw.close()
        emit('user', {"counter":0}, broadcast=True)
        
@socketio.on('disconnect')
def ws_disconnect():
    
    f=open("test.txt", "r")
    data= f.read()
    tem={"counter": int(json.loads(data).get("counter"))-int(1)}
    f.close()

    
    #write
    fw= open("test.txt", "r")
    fw.write(json.dump(tem))
    fw.close()
    emit('user', tem, broadcast=True)
    
    
@app.route('/', methods=["POST","GET"])

def home():
    f=open("test.txt", "r")
    data = f.read()
    data = {"counter": int(json.loads(data).get("counter"))}
    return render_template("index.html", data=data)

if __name__ == "__main__":
    socketio.run(app)
