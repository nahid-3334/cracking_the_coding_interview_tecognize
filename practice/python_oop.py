class Person:
    def __init__(self,name:str ,age :int ,salary:None): #init constructor,self deaflt parameter 
        self.name=name #self class intnace obje/current obj
        self.age=age
        self.salary=salary # __ private encapsulation
    def get_name(self):
        return self.name
    def get_age(self):
        return self.age
    def get_salary(self):
        return self.salary
    def get_summary(self):
        return f"Name :{self.name} Age :{self.age} Salary: {self.salary}"

person_list=[Person("Nahid",24,20000),
            Person("Sakib",22,40000),
            Person("Jakib",23,50000),
            Person("Kamrul",26,40000),
            Person("Tanbir",25,60000)]
#print(obj.name,obj.age,obj._Person__salary) # usee _classname to acces private data
for person in person_list :
        print(person.get_summary())
class Student(Person):
    def __init__(self ,name:str ,age :int ,salary:None, email :str,student_id :int):
        super().__init__(name,age,salary)
        self.email = email
        self.id = student_id
    def get_summary(self):
        return f"Name :{self.name} Age :{str(self.age)} email: {self.email}, id:{str(self.id)}"
    def __str__(self):
         return self.get_summary()
    

#task polymorphism,""
student=Student("Apu",18,10000,"apu@gmail.com",101)
print(student)

class Teacher(Person):
    def __init__(self,name:str ,age :int ,salary:None,email :str,teacher_id :int):
        super().__init__(name,age,salary)
        self.email = email
        self.id = teacher_id
    def get_summary(self):
        return f"Name :{self.get_name()} Age :{str(self.get_age())} email: {self.email}, id:{str(self.id)}"
    def __repr__(self):
            return self.get_summary()

teacher=Teacher("Mokammel",38,100000,"mokammel@gmail.com",100)
print(teacher)