def check_salary(text):
    param = input(f'Укажите размер {text} сотрудника')
    while True:
        try:
            param = float(param)
            if text == 'оклада':
                if param < minimum_wage:
                    param = input(
                        f'Размер оклада не может быть меньше МРОТ. МРОТ = {minimum_wage}')  # не учитывается случай, когда работник трудоустроен по договору ГПХ
                    # TODO: enable verification for the GPC agreement
                else:
                    print(f'Размер {text} сотрудника = {param}')
                    return param
            elif text == 'премии':
                if param < 0:
                    param = input('Премия не может быть отрицательной!')
                else:
                    print(f'Размер {text} сотрудника = {param}')
                    return param
        except ValueError:
            param = input(f'Укажите размер {text} сотрудника')


def data_output(worker):
    print(f'Полное имя сотрудника: {worker.get_full_name()}')
    print(f'Доход сотрудника, учитывая премию, равен {worker.get_total_income()} р.')


class Worker:
    def __init__(self, name, surname, position, income):
        self.name = name
        self.surname = surname
        self.full_name = [name, surname]
        self.position = position
        self._income = income

    def get_salary(self):
        return self._income


class Position(Worker):
    def get_full_name(self):
        return ' '.join(self.full_name)

    def get_total_income(self):
        return sum(self._income.values())


minimum_wage = 12792
a = Worker(input('Введите имя сотрудника').title(), input('Введите фамилию сотрудника').title(),
           input('Укажите должность сотрудника сотрудника').title(),
           {'wages': check_salary('оклада'), "bonus": check_salary('премии')})
a = Position(a.name, a.surname, a.position,
             a.get_salary())  # если я правильно понял, то некорректно обращаться к защищенному атрибуту и требуется создать метод для его получения
data_output(a)

b = Worker(input('Введите имя сотрудника').title(), input('Введите фамилию сотрудника').title(),
           input('Укажите должность сотрудника сотрудника').title(),
           {'wages': check_salary('оклада'), "bonus": check_salary('премии')})
b = Position(b.name, b.surname, b.position, b.get_salary())
data_output(b)
