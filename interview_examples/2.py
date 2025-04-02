from abc import ABC, abstractmethod

def timer_f(rep : int):
    def timer(func):

        def wrapper(*args, **kwargs):
            for i in range(rep):
                func(*args, **kwargs)
            return func

        return wrapper
    return timer


class MyAbstClass(ABC):

    '''

    '''

    @abstractmethod
    def add(self, a : int, b: int) -> int:
        pass

class MyClass(MyAbstClass):

    '''
    '''

    @timer_f(5)
    def add(self, a : int, b: int) -> int:
        return a + b
    


c = MyClass()
c.add(2,3)