class Human:
    def __init__(self,name,house,car=None,job=None):
        self.name = name
        self.house = house
        self.car = car
        self.job = job
        self.money = 1000
        self.gladness = 50

    def shoping(self):
        pass

    def work(self):
        pass

    def eat(self):
        pass

    def chill(self):
        pass

    def cleaning(self):
        pass

    def info(self):
        pass

    def live(self):
        pass
    def is_alive(self):
        if self.money < 0:
            return False
        return True

class Car:
    def __init__(self,model):
        self.model = model
        self.fuel = 60
        self.state = 100
    def drive(self, length):
        rahod =length * 0.1
        if self.fuel - rahod <0:
            print('Подорож неможлива не вистачає пального!')
        else:
            self.fuel -= rahod
            self.state -= length * 0.01
            print(f'Ми проїхали {length}km, витратили {rahod}l пального')

    def add_fuel(self,fuel):

    def __str__(self):
        pass

class Job:
    def __init__(self,name,salary):
        self.name = name
        self.salary  = salary
    def __str__(self):
        return f'Робота: {self.name},зарпатня - {self.salary}$'

class House:
    def __init__(self):
        self.pollution = 0
        self.food = 0

    def __str__(self):
        print(f'Будинок: запас їжі - {self.food}, забрудненність - {self.pollution}')