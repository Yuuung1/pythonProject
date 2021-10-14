# gon = input('Введите количество гонщиков и кругов(через пробел): ').split()
gon = input().split()
n = int(gon[0])
m = int(gon[1])

kol1 = [None] * n
kol2 = [None] * m

class Driver:
    def __init__(self):
        t = 0
        obsh = 0
        # self.name = input('Введите имя гонщика: ')
        self.name = input()
        # secs = input('Введите кол-во секунд за каждый круг: ').split()
        secs = input().split()
        for g in range(0, m):
            obsh = obsh+int(secs[t])
            t+=1
        self.sec = obsh

    # def __lt__(self, other):
    #     return self.sec < other

e = 0
minsec = 100
winname = ''

for x in range(0,n):
    kol1[e] = Driver()
    if minsec > kol1[e].sec:
        minsec = kol1[e].sec
        winname = kol1[e].name
    # if (kol1[e].sec).__lt__(minsec):
    #     minsec = kol1[e].name
    e+=1

# print('Ответ:')
print(winname)
