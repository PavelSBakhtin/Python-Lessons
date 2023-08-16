# Создайте три (или более) отдельных классов животных. Например рыбы, птицы и т.п.
# У каждого класса должны быть как общие свойства, например имя, так и специфичные для класса.
# Для каждого класса создайте метод, выводящий информацию специфичную для данного класса.


class Fish():
    def __init__(self, name, age, scales):
        self.name = name
        self.age = age
        self.scales = scales

    def swim(self):
        print("i'm swimming, oh, it's titan!")


class Dog():
    def __init__(self, name, age, breed):
        self.name = name
        self.age = age
        self.breed = breed

    def bark(self):
        print('Bark !!!')


class Raven():
    def __init__(self, name, age, color):
        self.name = name
        self.age = age
        self.color = color

    def fly_around_corpse(self):
        print('oooh, meat ...')


fish = Fish('Nemo', 2, 'silver')
dog = Dog('Spark', 5, 'pitbull')
bird = Raven('Qarasique', 6, 'white')

fish.swim()
dog.bark()
bird.fly_around_corpse()
