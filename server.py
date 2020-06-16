from flask import Flask
from flask_socketio import SocketIO, send
from logs import globallog

app = Flask(__name__, static_url_path='')
socketio = SocketIO(app)


@socketio.on('hello')
def handle_message(message):
    globallog.info('received message: ' + message)
    send(f'echo: {message}')


@app.route('/')
def root():
    globallog.info('Returning index.html')
    return app.send_static_file('index.html')


if __name__ == '__main__':
    socketio.run(app)
