from flask import Flask, request
from flask_socketio import SocketIO
from logs import globallog
from gameloop import commands, gib

app = Flask(__name__, static_url_path='')
socketio = SocketIO(app)
clients = []


@socketio.on('hello')
def handle_message(message):
    globallog.info('received message: ' + message)
    sid = request.sid
    clients.append(sid)
    globallog.info('said hello to client: ' + message)
    socketio.send(f'echo: {message}')


@socketio.on('command')
def handle_message(cmd):
    globallog.info(f'queue command: {cmd}')
    commands.append(cmd)
    socketio.send(f'queued command')


@app.route('/')
def root():
    globallog.info('Returning index.html')
    return app.send_static_file('index.html')


def echo_func(message):
    with app.app_context():
        socketio.emit('gameevent', message, broadcast=True)


if __name__ == '__main__':
    with gib(echo_func):
        socketio.run(app)
