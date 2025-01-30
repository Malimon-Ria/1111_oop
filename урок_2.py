class Student:
    print('Hi')
    count_of_student = 0
    def __init__(self,name, height = 160):
        self.name = name
        self.height= 160
        Student.count_of_student += 1
        print('Hi! I`m Student')

    def grow_up(self,grow):
        if self.height + grow < 220:
            self.height += grow

    def info(self):
        print(f'Name  : {self.name}')
        print(f'Height  : {self.height}')

    def __str__(self):
        return f'Name  : {self.name}\n'

    def __del__(self):
        print(f'{self.name} is dead :(')

    def __len__(self):
        return self.height

print(Student.count_of_student)


student1 = Student('Maria')
# print(student1.name)
student1.grow_up(1000000)
# print(student1.height)

student2 = Student('Ria',height = 170)
# print(student2.name)
# student2.height =170
# print(student2.height)

student1.info()
student2.info()
print(Student.count_of_student)

print(len(student2))
