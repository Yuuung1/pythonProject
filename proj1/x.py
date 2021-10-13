class Person:
    arms_count = None
me = Person()
you = Person()

print(me.arms_count, you.arms_count)

me.arms_count = 2

print(me.arms_count, you.arms_count)