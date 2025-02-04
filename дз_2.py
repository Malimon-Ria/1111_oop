class Cat:
    print('Hi')
    count_of_cats = 0
    def __init__(self,name,height = 75, color1 = 'ginger', color2 = 'black', toy = 'mouse'):
        self.name = name
        self.color= color1
        self.height = 75
        self.toy = toy
        Cat.count_of_cats += 1
        print('Hi! I`m a Cat ))')

    def grow_up(self,grow):
        if self.height + grow < 75:
            self.height += grow

    def info(self):
        print(f'Name  : {self.name}')
        print(f'Height  : {self.height}')
        print(f'Color  : {self.color}')
        print(f'Favourite toy  : {self.toy}')

    def __str__(self):
        return f'Name  : {self.name}\n'

    def __len__(self):
        return self.height

print(Cat.count_of_cats)


cat1 = Cat('Рыжик')
# print(cat1.name)
cat1.grow_up(80)
# print(cat1.height)

cat2 = Cat('Пушок',height = 75, toy = 'rope')
# print(cat2.name)
# cat2.height =65
# print(cat2.height)

cat1.info()
cat2.info()
print(Cat.count_of_cats)

print(len(cat2))
