#30-sentabr 2021-yil
#FinalExam Foundation
#6-savol Kichkina shaxzoda

from aylana import Aylana
from shaxzoda import Shaxzoda

t = int(input())
for test in range(t):
    x1, y1, x2, y2 = map(int, input().split())
    sh = Shaxzoda(x1, y1, x2, y2)
    n = int(input())
    k = 0
    for i in range(n):     #Bu for aylana kiritilgandan birdaniga kesish kesmasligini hisoblab ketadi (har siklda aylana yangitdan o'qiladi, saqlab qolinmaydi)
        x, y, r = map(int, input().split())
        aylana = Aylana(x, y, r)
        if sh.kesibUtadimi(aylana):
            k += 1
    print(k)