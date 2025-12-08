# Разработайте класс, реализующий буфер текстового редактора. Класс должен предоставлять методы:
# добавления строки s в конец буфера
# удаления n последних символов из буфера
# отмены последней операции
# вывода текста всего буфера
# вывод последнего символа буфера

# class BufferException(Exception):
#     pass


class BufferExeption(Exception):
    pass


class EditorBuffer:
    """
    Implements simple buffer.
    """

    def __init__(self):
        self._buffer = []
        self._history_stack = []

    def add_str_to_the_end(self, s: str) -> None:
        if self._buffer:
            self._history_stack.append(self._buffer.copy())

        for c in s:
            self._buffer.append(c)

    def remove_last_n_symbols(self, n: int) -> None:
        if self._buffer:
            self._history_stack.append(self._buffer.copy())

        if n > len(self._buffer):
            raise BufferExeption()

        self._buffer = self._buffer[:-n]

    def cancel_operation(self) -> None:
        if len(self._history_stack) > 0:
            self._buffer = self._history_stack[0]

    def get_buffer(self) -> str:
        return "".join(self._buffer)

    def print_buffer(self) -> None:
        print(self.get_buffer())

    def get_last_char(self) -> str:
        if not self._buffer:
            raise BufferExeption("Buffer is empty!")

        return self._buffer[-1]
