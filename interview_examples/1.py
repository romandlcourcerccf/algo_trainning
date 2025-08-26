from abc import ABC, abstractmethod

Написать декоратор

def timer(func):

    def wrapper(*args, **kwargs):
        print('Measure time!!')
        func(*args, **kwargs)
        return func

    return wrapper


Написать абстрактнвй класс 
class MyAbstClass(ABC):

    '''

    '''

    @abstractmethod
    def add(self, a : int, b: int) -> int:
        pass

class MyClass(MyAbstClass):

    '''
    '''

    @timer
    def add(self, a : int, b: int) -> int:
        return a + b
    


c = MyClass()
c.add(2,3)