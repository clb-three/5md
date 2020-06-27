from flask import Flask, request
from flask_socketio import SocketIO

from gameloop import commands, gib
from logs import GLOBAL_LOG

app = Flask(__name__, static_url_path='')
socketio = SocketIO(app)
clients = []


@socketio.on('hello')
def handle_hello(message):
    GLOBAL_LOG.info('received message: %s', message)
    sid = request.sid
    clients.append(sid)
    GLOBAL_LOG.info('said hello to client: %s', message)
    socketio.send(f'echo: {message}')


@socketio.on('command')
def handle_command(cmd):
    GLOBAL_LOG.info('queue command: %s', cmd)
    commands.append(cmd)
    socketio.send('queued command')


@app.route('/')
def root():
    GLOBAL_LOG.info('Returning index.html')
    return app.send_static_file('index.html')


def echo_func(message):
    with app.app_context():
        socketio.emit('gameevent', message, broadcast=True)


if __name__ == '__main__':
    with gib(echo_func):
        socketio.run(app)
