from flask import Flask, request
from flask_socketio import SocketIO

from logs import GLOBAL_LOG
from model.doorcards import factory as doorcard_factory
from model.gamestate import GameState
from model.heroes import factory as hero_factory
from model.table import Table

app = Flask(__name__, static_url_path='', static_folder='ui/dist')
socketio = SocketIO(app)
clients = []


def get_gameloop():
    heroes = {
        'benji': hero_factory.hero('benji', 'barbarian'),
        'austin': hero_factory.hero('austin', 'healer'),
    }
    # Draws the hero's initial hand
    for _ in range(0, 5):
        for hero in heroes.values():
            hero.draw_card()

    # Deal boss mat and door deck
    boss = doorcard_factory.create_boss()
    doordeck = doorcard_factory.deal_deck(
        boss.num_door_cards, len(heroes))

    game = GameState(heroes, doordeck,
                     doordeck.current_enemy, boss)
    return Table(game)


table = get_gameloop()


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
    socketio.send('queued command')
    message = table.process_command(cmd)
    socketio.emit('gameevent', str(message))


@app.route('/')
def root():
    GLOBAL_LOG.info('Returning index.html')
    return app.send_static_file('index.html')


if __name__ == '__main__':
    socketio.run(app)
