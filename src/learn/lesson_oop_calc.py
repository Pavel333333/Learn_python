import abc
from functools import singledispatchmethod
from abc import abstractmethod

# Реализуйте класс Calculator, в котором будет один метод, для вычисления суммы двух чисел.
# Реализуйте еще один класс, который будет наследоваться от класса Calculator
# и перегрузите метод для вычисления суммы двух чисел, чтобы он делал конкатенацию двух строк.


class Calculator:

    @singledispatchmethod
    def format(self, *args):
        if all(isinstance(arg, str) for arg in args):
            return Concatenator().format(*args)

    @format.register
    def summa(self, *args: int):
        return sum(args)


class Concatenator(Calculator):

    @singledispatchmethod
    def format(self, *args):
        if all(isinstance(arg, int) for arg in args):
            return super().format(*args)

    @format.register
    def summa(self, *args: str):
        return ''.join(args)


c = Calculator()
print(c.format(3, 5, 8))
print(c.format('3', '5', '8'))

cc = Concatenator()
print(cc.format(3, 5, 8))
print(cc.format('3', '5', '8'))

# Реализуйте абстрактный класс Animals, создайте класс Cat,
# который будет наследоваться от класса Animals и реализуйте метод voice.


class Animals(abc.ABC):

    @abstractmethod
    def voice(self):
        pass

    def eat(self):
        print(f'{self} ест')


class Cat(Animals):

    def voice(self):
        print(f'Кот мяукает')


vasya = Cat()
vasya.voice()

# Прочитайте статью и выполните действия, которые в ней прописаны

class Parent:

    def __init__(self):
        self.parent_attribute = 'I am a parent'

    def parent_method(self):
        print('Back in my day...')


class Child(Parent):

    def __init__(self):
        super().__init__()
        self.child_attribute = 'I am a child'


child = Child()

print(child.child_attribute)
print(child.parent_attribute)
child.parent_method()


class B:
    def b(self):
        print('b')
class C:
    def c(self):
        print('c')
class D(B, C):
    def d(self):
        print('d')


d = D()
d.b()
d.c()
d.d()


class B:
    def x(self):
        print('x: B')


class C:
    def x(self):
        print('x: C')


class D(B, C):
    pass


d = D()
d.x()
print(D.mro())


class Tokenizer:
    def __init__(self, text):
        print('Start Tokenizer.__init__()')
        self.tokens = text.split()
        print('End Tokenizer.__init__()')


class WordCounter(Tokenizer):
    def __init__(self, text):
        print('Start WordCounter.__init__()')
        super().__init__(text)
        self.word_count = len(self.tokens)
        print('End WordCounter.__init__()')


class Vocabulary(Tokenizer):
    def __init__(self, text):
        print('Start init Vocabulary.__init__()')
        super().__init__(text)
        self.vocab = set(self.tokens)
        print('End init Vocabulary.__init__()')


class TextDescriber(WordCounter, Vocabulary):
    def __init__(self, text):
        print('Start init TextDescriber.__init__()')
        super().__init__(text)
        print('End init TextDescriber.__init__()')


td = TextDescriber('row row row your boat')
print('--------')
print(td.tokens)
print(td.vocab)
print(td.word_count)

# Реализуйте класс Dog. Придумайте, какие переменные будет принимать данный класс
# и какие методы будут реализованы. Реализуйте в этом классе паттерн Singleton


class Dog:

    __instance__ = None

    def __new__(cls, *args, **kwargs):
        if cls.__instance__ is None:
            cls.__instance__ = super(Dog, cls).__new__(cls)
        return cls.__instance__

    def __init__(self):
        if not hasattr(self, '_initialized'):
            print('Создание новой собачки.')
            self._initialized = True
        else:
            print('Нельзя завести другую собачку, она должна быть единственной.')


dog1 = Dog()
print(dog1)
dog2 = Dog()
print(dog2)
dog3 = Dog()
print(dog3)
print(dog1 is dog3)
print(dog1 is dog2)
print(dog2)


class People:
    a = 5


p = People()
p2 = People()
print(p.__dict__)
p.a = 3
print(p.__dict__)
print(p2.__dict__)
print(p.a)
print(p2.a)
print(People.__dict__)
People.a = 1
print(p.__dict__)
print(p2.__dict__)
print(People.a)
print(p.a)
print(p2.a)
print(People.__dict__)


# Напишите класс, который принимает список людей с интерфейсом добавления новых
# и при итерации возвращал имена людей


class PeopleList:

    def __init__(self, initial=None):
        if initial is None:
            initial = []
        self._list = list(initial)

    def append(self, value):
        self._list.append(value)

    def __setitem__(self, key, value):
        self._list[key] = value

    def __getitem__(self, item):
        return self._list[item]

    def __iter__(self):
        return iter(self._list)

    def user_input(self):
        while True:
            user_input = input("Введите список людей (или 'exit' для выхода): ")
            user_input = user_input.split(', ')
            if user_input[0].lower() == 'exit':
                break
            if isinstance(user_input, list):
                self._list.extend(user_input)
            else:
                self.append(user_input)
        print(f"Текущий список: {self._list}")

    @property
    def list(self):
        return self._list


people = PeopleList()
people.user_input()
people.append('Кузнецов')
print(people._list)
people[3] = 'Васнецов'
print(people._list)

for name in people._list:
    print(name)


# Напишите класс, содержит 3 любые атрибута и
# при изменении логгировать всё в консоль (при изменении старое->новое)


class ChangeLogger:

    def __init__(self, name_attr):
        self.name = name_attr
        self.value = None

    def __get__(self, instance, owner):
        return self.value

    def __set__(self, instance, value):
        if self.value is not None:
            old_value = self.value
            self.value = value
            print(f'{self.name}: старое значение {old_value} стало {value}')
        else:
            print(f'у {self.name} новое значение {value}')


class ThreeAttrs:
    at1 = ChangeLogger('at1')
    at2 = ChangeLogger('at2')
    at3 = ChangeLogger('at3')


log = ThreeAttrs()
log.at1 = 10
log.at1 = 20
log.at2 = 'abc'
log.at3 = [1, 2, 3]
log.at3 = [4, 5, 6]


class Forest:

    name = 'Лес'

    def poly(self):
        return f'{self.name} цветёт'


class Tree(Forest):

    def poly(self):
        return f'{self.name} цветёт'


class Flower(Forest):

    def poly(self):
        return f'{self.name} цветёт'


forest = Forest()
tree = Tree()
tree.name = 'Ель'
flower = Flower()
flower.name = 'Ромашка'
print(forest.poly())
print(tree.poly())
print(flower.poly())

lst = [forest, tree, flower]

for elem in lst:
    print(elem.poly())








