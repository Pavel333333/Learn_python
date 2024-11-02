from functools import total_ordering
from copy import deepcopy, copy


class MeansOfTransport:

    def __init__(self, brand, color):
        self.__brand = brand
        self.__color = color

    def show_brand(self):
        print(self.__brand)

    def show_color(self):
        print(self.__color)

    @property
    def brand(self):
        return self.__brand

    @brand.setter
    def brand(self, value):
        self.__brand = value

    @brand.deleter
    def brand(self):
        del self.__brand

    @property
    def color(self):
        return self.__color

    @color.setter
    def color(self, value):
        self.__color = value

    @color.deleter
    def color(self):
        del self.__color


class Moped(MeansOfTransport):
    def __init__(self, brand, color, wheels_number):
        super().__init__(brand, color)
        self.__wheels_number = wheels_number

    @staticmethod
    def way_time(way, speed):
        return way / speed


@total_ordering
class Car(MeansOfTransport):
    car_drive = 4

    def __new__(cls, *args, **kwargs):
        instance = super().__new__(cls)
        print('Метод __new__ отработал')
        return instance

    def __init__(self, brand, color, wheels_number, seat_number, length):
        super().__init__(brand, color)
        self.__wheels_number = wheels_number
        self._seat_number = seat_number
        self._length = length
        self.index = 0

    @property
    def wheels_number(self):
        return self.__wheels_number

    @wheels_number.setter
    def wheels_number(self, value):
        self.__wheels_number = value

    @classmethod
    def car_drive_print(cls):
        print(cls.car_drive)

    def __eq__(self, other):
        if not isinstance(other, Car):
            return NotImplemented
        return self.brand == other.brand

    def __lt__(self, other):
        if not isinstance(other, Car):
            return NotImplemented
        return self._seat_number < other._seat_number

    def __pos__(self):
        if self.wheels_number != 4:
            return f'у машины не может быть столько колёс: {self.wheels_number} '
        return self.wheels_number

    def __neg__(self):
        return f'Экземпляр класса Car не может быть отрицательным, так как мы не в Зазеркалье'

    def __abs__(self):
        if self.brand == 'lada':
            return 'у Вас определённо хороший вкус, ведь Lada это absолютно лучшая машина'
        return 'можно было бы выбрать машину получше'

    def __round__(self, n=None):
        if self.brand == 'uaz':
            return 'Уазик нельзя округлить, он всегда квадратный'
        elif self.brand == 'lada':
            return f'нашу любимую {self.brand} трогать лучше не надо'
        return f'{self.brand} итак круглый, куда его ещё круглее'

    def __add__(self, other):
        if not isinstance(other, int):
            return 'второе слагаемое должно быть целочисленным'
        return 'ejd849j3d. А какой результат ты хотел получить прибавляя число к машине ?!'

    def __sub__(self, other):
        if not isinstance(other, int):
            return 'вычитаемое должно быть целочисленным'
        return 'а что ты хочешь отнять у машины ? у неё нету ничего ненужного. если только в багажнике посмотреть...'

    def __or__(self, other):
        if not isinstance(other, Car):
            return 'после | поставь объект класса Car. Иначе из чего мне выбирать ?'
        if self.brand == 'lada' or self.brand == 'uaz':
            return f'без вариантов, только {self.brand}'
        return f'не знаю, сам решай, что лучше {self.brand} или {other.brand}. моё мнение ты знаешь.'

    def __radd__(self, other):
        return self.__add__(other)

    def __iadd__(self, other):
        return 'что за мания, прибавлять числа к машине. что я должен посчитать ?'

    def __int__(self):
        print(f'у этого объекта колёс: {self.wheels_number}, посадочных мест {self._seat_number}, итого:')
        return self.wheels_number + self._seat_number

    def __str__(self):
        return f'{self.brand}, {self.color}, {self.wheels_number}, {self._seat_number}, {self._length}'

    def __hash__(self):
        h = hash(self.brand) + hash(self.color) + hash(self.wheels_number) + hash(self._seat_number)
        print('выводим сумму хэшей аргументов объекта')
        return h

    def __bool__(self):
        if self.brand == 'lada' or self.brand == 'uaz':
            return True
        return False

    def __getattr__(self, item):
        return f'в этом объекте нет атрибута {item}'
    
    def __setattr__(self, key, value):
        super().__setattr__(key, value)

    def __len__(self):
        return self._length

    def __getitem__(self, item):
        lst = self.__str__().split(', ')
        if not isinstance(item, int):
            return 'в индекс надобно вводить сугубо целочисленное значение'
        if abs(item) >= len(lst):
            return f'в данном объекте меньше атрибутов, чем {item}'
        return lst[item]

    def __setitem__(self, key, value):
        match key:
            case 0:
                self.brand = value
            case 1:
                self.color = value
            case 2:
                self.wheels_number = value
            case 3:
                self._seat_number = value
            case 4:
                self._length = value

    def __delitem__(self, key):
        if key == 0:
            del self._MeansOfTransport__brand
        elif key == 1:
            del self.color
        elif key == 2:
            del self._Car__wheels_number
        elif key == 3:
            del self._seat_number
        elif key == 4:
            del self._length

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < len(self):
            result = self[self.index]
            self.index += 1
            return result
        else:
            raise StopIteration

    def __reversed__(self):
        lst = self.__str__().split(', ')
        return lst[::-1]

    def __contains__(self, item):
        lst = self.__str__().split(', ')
        if item in lst:
            return True
        return False

    def __instancecheck__(self, instance):
        if instance == self.__class__:
            return True
        return False

    def __subclasscheck__(self, subclass):
        if subclass in self.__dir__():
            return True
        return False

    def __call__(self, *args, **kwargs):
        if self.brand == 'lada' or self.brand == 'uaz':
            return 'поздравляем, это хороший выбор!'
        return 'подумайте хорошенько над своим выбором :\\'

    def __enter__(self):
        return 'карета подана, извольте'

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('не беспокойтесь о закрытии двери, я сам это сделаю')

    def __copy__(self):
        return self

    def __deepcopy__(self, memodict={}):
        new_object = Car(self.brand, self.color, self.wheels_number, self._seat_number, self._length)
        return new_object


l = Car('lada', 'red', 5, 5, 5)
l2 = Car('bmw', 'white', 4, 8, 6)
l3 = Car('mersedes', 'black', 4, 6, 7)
l4 = Car('uaz', 'green', 4, 10, 4)
v = 'lada'

print(l != l2)
print(l == v)
print(l <= l2)
print(+l)
print(+l2)
print(-l)
print(abs(l))
print(abs(l3))
print(round(l2, 3))
print(round(l3))
print(round(l4))
print(l + '3')
print(l + 3)
print(l3 - '3')
print(l3 - 3)
print(l3 | '3')
print(l | l3)
print(l2 | l3)
print(3 + l)
l3 += 3
print(l3)
l3 = Car('mersedes', 'black', 4, 6, 7)
print(int(l2))
print(str(l3))
print(hash(l3))
print(bool(l), bool(l2), bool(l4))
print(l3.engine)
l3.engine = 'мотор'
print(l3.engine)
print(len(l))
print(l2['3'])
print(l2[5])
print(l2[0])
l3[0] = 'Mersedes'
print(str(l3))
del l3[2]
print(l3)
for i in l:
    print(i)
print(reversed(l2))
print('uaz' in l4)
print('toyota' in l4)
print(isinstance(l2, Car))
print(isinstance(v, Car))
print(issubclass(Car, MeansOfTransport))
print(issubclass(MeansOfTransport, Car))
print(l())
print(l2())
with l as car_voice:
    print(car_voice)
copy_l2 = copy(l2)
copy_l2[4] = 5
print(copy_l2[4])
print(l2[4])
copy_l4 = deepcopy(l4)
copy_l4[3] = 7
print(copy_l4[3])
print(l4[3])

