from advanced_coding.buffer.buffer import EditorBuffer, BufferExeption
import pytest


def test_add_str_to_the_end():
    buffer = EditorBuffer()

    s1 = "qwerty1"

    buffer.add_str_to_the_end(s1)

    assert buffer.get_buffer() == s1


def test_remove_last_n_symbols():
    buffer = EditorBuffer()
    s1 = "qwerty123"
    s2 = "qwerty"

    buffer.add_str_to_the_end(s1)
    buffer.remove_last_n_symbols(3)

    assert buffer.get_buffer() == s2


def test_remove_last_n_symbols_more_then_exist():
    buffer = EditorBuffer()
    s1 = "qwerty123"

    buffer.add_str_to_the_end(s1)
    with pytest.raises(BufferExeption):
        buffer.remove_last_n_symbols(len(s1) + 1)


def test_cancel_operation():
    buffer = EditorBuffer()
    s1 = "qwerty123"
    s2 = "qwerty456"

    buffer.add_str_to_the_end(s1)
    assert buffer.get_buffer() == s1
    buffer.add_str_to_the_end(s2)
    assert buffer.get_buffer() == s1 + s2

    print(buffer._history_stack)

    buffer.cancel_operation()

    assert buffer.get_buffer() == s1


def test_get_buffer():
    buffer = EditorBuffer()
    s1 = "qwerty123"
    buffer.add_str_to_the_end(s1)
    assert buffer.get_buffer() == s1


def test_get_last_char():
    buffer = EditorBuffer()
    s1 = "qwerty123"
    buffer.add_str_to_the_end(s1)

    assert buffer.get_last_char() == "3"


def test_get_last_char_empty_buffer():
    with pytest.raises(BufferExeption):
        buffer = EditorBuffer()
        buffer.get_last_char()
