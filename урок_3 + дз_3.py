import random

class Student:
    def __init__(self,name):
        self.name = name
        self.progress = 10
        self.gladness = 50
        self.alive = True
        self.money = 600

    def money(self):
        money = 600
        while self.money == 0:
            self.money= max(0)
            print(f'В мене закінчились гроші...потрібно йти на роботу!')

    def work(self):
        self.money += 100
        self.gladness -= 1
        self.progress +=1
        print('Я попрацював і заробив 100')


    def study(self):
        self.progress += 1
        self.gladness -= 0.05
        print('Я навчаюсь у IT STEP')

    def chill(self):
        if self.money >= 50:
            self.gladness += 1
            self.progress -= 0.5
            self.money -= 50
            print('Я сьогодні гарно відпочив')
        else:
            print('Грошей нема, треба йти працбвати...')
            self.work()

    def sleep(self):
        self.gladness += 1
        print('Я втомився, і пішов спати...')

    def is_alive(self):
        if self.gladness <0:
            print('В мене дипрєшн, я пішов...')
            self.alive = False
        elif self.progress < 0:
            print('Нічого не лізе в голову..THE END')
            self.alive = False
        elif self.progress > 30 :
            print('Я достроково завершив IT STEP,і пішов працювати')
            self.alive = False

    def info(self):
        print(f'Задоволення - {self.gladness}')
        print(f'Прогрес - {self.progress}')
        print(f'Гроші - {self.money}$')

    def live(self,day):
        print()
        print(f' ----- День №{day+1} -----')
        print(f'Привіт, я {self.name},і я сьогодні: ')
        rnd = random.randint(1,3)
        if rnd == 1:
            self.study()
        elif rnd == 2:
            self.sleep()
        elif rnd == 3:
            self.chill()
        self.info()
        self.is_alive()



student = Student("Jorik")
for day in range(365):
    if student.alive == False:
        break
    student.live(day)