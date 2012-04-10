from flask import Flask, render_template, request
from socketio import socketio_manage
#from flask.wrappers import Response

from socketapp import EventNamespace

app = Flask(__name__)

@app.route('/')
def index():
    print '\n/////////////////////////////////'
    return render_template('index.html')
    
#@app.route('/socket.io/1/<session>')
@app.route('/socket.io/1/websocket/<session>')
def socketio_service(session):
    retval = socketio_manage(request.environ, {'/event': EventNamespace},request)
    #return Response(retval)

