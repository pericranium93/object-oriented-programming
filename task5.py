class Stationery:
    def __init__(self, title_of_stationery):
        self.title = title_of_stationery

    def draw(self):
        print(self.title, 'drawning')


class Pen(Stationery):
    def draw(self):
        print('Pen drawning')


class Pencil(Stationery):
    def draw(self):
        print('Pencil drawning')


class Handle(Stationery):
    def draw(self):
        print('Handle drawning')


a = Stationery('tassel')
a.draw()

b = Pen('pen')
b.draw()

c = Pencil('pencil')
c.draw()

d = Handle('handle')
d.draw()
