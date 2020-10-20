# pylint: disable=W0201
import logging

import pytest
from coolname import generate_slug

from . import test_mocks as mock
from .doorcards import factory as doordeck_factory
from .doorcards.boss import Boss
from .gamestate import GameState
from .heroes.hero import Hero
from .heroes.singlesymbol import SingleSymbol
from .symbol import Symbol
from .table import Table


async def print_emitter(msg):
    print(msg)


class TestTable:
    def setup_method(self):
        heroname = generate_slug()
        self.hero = Hero(heroname, 'ranger', [SingleSymbol(Symbol.sword)])

        boss = Boss([Symbol.jump], 10)
        deck = doordeck_factory.deal_deck(9, 1, boss)
        deck.put_on_top(mock.enemy(Symbol.sword))

        state = GameState(deck, [self.hero], logging=logging)

        self.table = Table(state, print_emitter, logging=logging)

    @pytest.mark.asyncio
    async def test_draw(self):
        assert len(self.hero.hand) == 0
        assert len(self.hero.deck) == 1
        await self.table.draw_card(self.hero)
        assert len(self.hero.hand) == 1
        assert len(self.hero.deck) == 0

    @pytest.mark.asyncio
    async def test_play(self):
        assert len(self.hero.hand) == 0
        self.hero.draw_card()
        assert len(self.hero.hand) == 1
        await self.table.play_card(self.hero, self.hero.hand[0])
        assert len(self.hero.hand) == 0

    @pytest.mark.asyncio
    async def test_discard(self):
        assert len(self.hero.hand) == 0
        self.hero.draw_card()
        assert len(self.hero.hand) == 1
        await self.table.discard_card(self.hero, self.hero.hand[0])
        assert len(self.hero.hand) == 0
