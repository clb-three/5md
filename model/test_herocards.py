# pylint: disable=W0201
import pytest

from . import test_mocks as mock
from .heroes.complaint import Complaint
from .heroes.multisymbol import MultiSymbol
from .heroes.singlesymbol import SingleSymbol
from .symbol import Symbol


class TestSingleSymbol():
    def setup_method(self):
        self.enemy = mock.enemy(Symbol.sword, Symbol.arrow)
        assert self.enemy.is_dead() is False

    def test_kill_single(self):
        SingleSymbol(Symbol.arrow).play(self.enemy)
        assert self.enemy.is_dead() is False
        SingleSymbol(Symbol.sword).play(self.enemy)
        assert self.enemy.is_dead() is True

    def test_miss_single(self):
        with pytest.raises(Complaint):
            SingleSymbol(Symbol.shield).play(self.enemy)
        assert self.enemy.is_dead() is False

    def test_attacktwice_single(self):
        SingleSymbol(Symbol.sword).play(self.enemy)
        with pytest.raises(Complaint):
            SingleSymbol(Symbol.sword).play(self.enemy)


class TestMultiSymbol():
    def setup_method(self):
        self.enemy = mock.enemy(Symbol.sword, Symbol.arrow)
        assert self.enemy.is_dead() is False

    @pytest.mark.xfail  # take this off when you implement it
    def test_instantkill_multi(self):
        MultiSymbol(Symbol.sword, Symbol.arrow).play(self.enemy)
        assert self.enemy.is_dead() is True

    @pytest.mark.xfail  # take this off when you implement it
    def test_slowkill_multi(self):
        assert MultiSymbol(Symbol.sword, Symbol.jump).play(self.enemy)
        assert self.enemy.is_dead() is False
        assert MultiSymbol(Symbol.arrow, Symbol.shield).play(self.enemy)
        assert self.enemy.is_dead() is True

    @pytest.mark.xfail  # take this off when you implement it
    def test_attacktwice_multisymbol(self):
        MultiSymbol(Symbol.sword, Symbol.jump).play(self.enemy)
        assert self.enemy.is_dead() is False
        with pytest.raises(Complaint):
            MultiSymbol(Symbol.sword, Symbol.jump).play(self.enemy)
        assert self.enemy.is_dead() is False

    @pytest.mark.xfail  # take this off when you implement it
    def test_miss_multisymbol(self):
        with pytest.raises(Complaint):
            MultiSymbol(Symbol.shield, Symbol.arrow).play(self.enemy)
