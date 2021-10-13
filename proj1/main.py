class Person:
    arms_count = 2
    def greet(self):
        print(f'Hi {self.name}')
    def __init__(self):
        self.name = 'Test'
    def __str__(self):
        return f'Person<name={self.name}>'
    def __eq__(self, other):
        return self.name==other.name
me = Person()
you = Person()

print(me,you)
print(me.__eq__(you))
#
# me.greet()
# you.greet()
# print(me.arms_count, you.arms_count)
#
# me.arms_count = 2
# print(me.arms_count, you.arms_count)
#
# me.name = 'Nick'
# you.name = 'Sasha'
# print(me.name, you.name)
#
# me.age = 12
# print(me.age)

