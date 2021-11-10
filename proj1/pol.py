class Duck:
    def sound(self):
        print('Quack Quack')

class Dog:
    def sound(self):
        print('Gav Gav')

for animal in Duck(), Dog():
    animal.sound()