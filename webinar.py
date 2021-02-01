class Phone:
    def __init__(self, phone_model):  # конструктор класса
        self.phone = phone_model
        self._loading()  # сразу будет писать loading при создании класса; _loading - инкапсуляция защищенная, позволяет скрыть
        # эту функцию от пользователя
        self._serial_number = 651687913  # скрыли, но для того чтобы пользователь мог увидеть параметр используем функцию get_serial_number
        self.__serial_number = 651648464  # приватная инкапсуляция

    def call(self):
        print('call')

    def _loading(self):
        print(self.phone, 'loading...')

    def get_serial_number(self):  # используем функцию, чтобы можно было вывести скрытое значение serial number
        return self._serial_number

    def get_serial_number1(self):  # используем функцию, чтобы можно было вывести скрытое значение serial number
        return self.__serial_number


my_phone1 = Phone('nokia')  # есть стандартные классы, например: list, int и т.д.
print(my_phone1.phone)
my_phone2 = Phone('dfdfg')
print(my_phone2.phone)
# print(my_phone1.get_serial_number())
# my_phone1._serial_number = 0  # инкапсуляция не защищает от изменения!!!
# print(my_phone1.get_serial_number())
# print(my_phone1.get_serial_number1())
# my_phone1.__serial_number = 0  # __blabla защищает от изменения, но не достаточно. можно изменить object._ClassName__attr
# print(my_phone1.get_serial_number1())
# my_phone1._Phone__serial_number = 0  # object._ClassName__attr изменили все равно. в питоне инкапсуляция не строгая, т.к. значени можно изменить
# print(my_phone1.get_serial_number1())


# my_phone2 = Phone('samsung')
# print(my_phone1.phone)
# print(my_phone2.phone)
# my_phone1.loading()
# my_phone1.call()  # все равно что list.append() or str.split()

class SmartPhone(Phone):  # в скобках наследуемый класс

    def sms(self):
        print('sms sending')

    def email(self):
        print('email sending')


# sphone = SmartPhone('nokia6600')
# sphone.call()  # функция была наследована от Phone
# sphone.sms()

class IPhone(SmartPhone):

    def __init__(self, phone_model):
        super().__init__(phone_model)  # обращение к родительскому init, если мы создаем новый init
        print('show logo')

    def player(self):
        print('music')

    def browser(self):
        super().sms()  # теперь при серфинге отправляется СМС
        print('serfing')

    def sms(self):
        print('Imessege sending')  # переопределение метода - теперь этот метод будет работать по-новому для этого класса


# iphone = IPhone('iphone 6')
# iphone.player()
# iphone.browser()
# iphone.sms()

class NextGenPhone(IPhone):
    pass


# Множественные наследования

class Player:
    def player(self):
        print('player')

    def qwe(self):
        print('player won')

class Navigator:
    def navigator(self):
        print('navigator')

    def qwe(self):
        print('navigator won')

class Mphone(Player, Navigator):  # наслудется сразу от двух классов
    def mphone(self):
        print('mphone')

# mphone = Mphone()
# mphone.player()
# mphone.mphone()
# mphone.navigator()
# mphone.qwe()  # при наличии одинаковых методов в наследуемых классах, то забираются методы из первого класса,
              # а потом дополняется методами из второго класса то кто первый тот и папа.


# Полиморфизм!

class Auto:
    def auto_start(self, param1, param2=None):
        if param2 is not None:  # перегрузка метода, разное количество переменных разный класс
            print(param1 + param2)
        else:
            print(param1)

# a = Auto()
# a.auto_start(10)
# a.auto_start(10, 20)

class MyAuto:
    x = 0  # не стоит создавать переменные внутри класса. можно создать внутри метода
    def __init__(self, y):
        self.y = y


# a = MyAuto(10)
# b = MyAuto(20)
# a.__class__.x = 10
# MyAuto.x = 100000
# print(b.x)
# print(a.x)
