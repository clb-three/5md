from threading import Thread
import asyncio
from flask import Flask
from flask_socketio import SocketIO, send
from logs import globallog
from core.main import GameLoop
import time

app = Flask(__name__, static_url_path='')
socketio = SocketIO(app)

commands = []
gameloop = GameLoop()


@socketio.on('hello')
def handle_message(message):
    globallog.info('received message: ' + message)
    send(f'echo: {message}')


@socketio.on('command')
def handle_message(cmd):
    globallog.info(f'queue command: {cmd}')
    commands.append(cmd)
    send(f'queued command')


@app.route('/')
def root():
    globallog.info('Returning index.html')
    return app.send_static_file('index.html')


shouldrun = True


def get_command():
    globallog.info('waiting for command')
    while shouldrun and not any(commands):
        time.sleep(1 / 100)
    if not shouldrun:
        return 'quit'
    globallog.info('getting command')
    return commands.pop()


if __name__ == '__main__':
    loop = asyncio.new_event_loop()
    t = Thread(target=gameloop.loop, args=(get_command,))
    t.start()
    socketio.run(app)
    shouldrun = False
    t.join()
