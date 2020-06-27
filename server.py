from flask import Flask, request
from flask_socketio import SocketIO

from gameadapter import GameAdapter
from logs import GLOBAL_LOG
from socketio_notifier import SocketIoNotifier

app = Flask(__name__, static_url_path='', static_folder='ui/dist')
socketio = SocketIO(app)
clients = []
commands = []


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


if __name__ == '__main__':
    notifier = SocketIoNotifier(app, socketio)
    with GameAdapter(notifier, commands):
        socketio.run(app)
