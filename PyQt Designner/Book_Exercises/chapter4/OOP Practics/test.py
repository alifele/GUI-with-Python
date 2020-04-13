class Dog():
    def __init__(self,name, age):
        self.name = name
        self.age = age


class Cat():
    def __init__(self, name, age):
        self.Name = name
        self.Age = age


class Animal(Dog, Cat):

    def __init__(self,name,age, color, Name, Age):
        Cat.__init__(self,Name, Age)
        Dog.__init__(self, name, age)

        self.color = color



dog = Dog('ali', 12)
print(dog.name)
animal = Animal('dog', 12 ,'red', 'cat', 42)
print(animal.name)
