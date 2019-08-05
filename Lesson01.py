class Animal:
    def __init__(self):
        self.name = None
        self.age = None

    def show_info(self):
        print('%s: %d' % (self.name, self.age))


animal1 = Animal()
animal1.name = 'Hoang'
animal1.age = 20
animal1.show_info()

