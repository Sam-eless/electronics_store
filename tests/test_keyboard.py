import pytest
from electronics_store.keyboard import Keyboard


def test_change_lang():
    """Проверяет метод изменения языка клавиатуры"""
    kb = Keyboard('Dark Project KD87A', 9600, 5)
    assert kb.language == "EN"
    kb.change_lang()
    assert kb.language == "RU"
    kb.change_lang()
    assert kb.language == "EN"
