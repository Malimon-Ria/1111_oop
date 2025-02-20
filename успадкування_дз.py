class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_info(self):
        return f"{self.name}, {self.age} років"

class M(Animal):
    def __init__(self, name, age, fur_type):
        super().__init__(name, age)
        self.fur_type = fur_type
    def get_info(self):
        return f"{super().get_info()}, шерсть: {self.fur_type}"

class B(Animal):
    def __init__(self, name, age, wing_span):
        super().__init__(name, age)
        self.wing_span = wing_span
    def get_info(self):
        return f"{super().get_info()}, розмах крил {self.wing_span}см"

class C(M):
    def __init__(self, name, age, fur_type):
        super().__init__(name, age, fur_type)
        self.fur_type = "коротка шерсть"

class D(M):
    def __init__(self, name, age, fur_type):
        super().__init__(name, age, fur_type)
        self.fur_type = "довга шерсть"

class S(B):
    def __init__(self, name, age, wing_span):
        super().__init__(name, age, wing_span)

class E(B):
    def __init__(self, name, age, wing_span):
        super().__init__(name, age, wing_span)

animals = [
    C("кіт", 3, "Коротка шерсть"),
    D("пес", 5, "довга шерсть"),
    S("горобець", 1, 15),
    E("орел", 7, 200)
]

for animal in animals:
    print(animal.get_info())
