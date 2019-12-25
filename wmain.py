osrodki = {
    "powietrze": 343,
    "woda": 1500
}

print("Obslugiwane osrodki to:")
for name in osrodki:
    print(name)

n = input("Podaj ilosc dokonanych pomiarow: ")
osr = input("Podaj nazwe osrodka lub predkosc dzwieku w osrodku: ")
inter = input("Podaj okres fali: ")

if osr in osrodki:
    osr = osrodki[osr]


def licz(t, osr):
    x = osr * t/2
    return x

czasy = []
odleg = []
predkosci =[]

i = 0
while (i < int(n)):
    t = input("Podaj czas po ktorym dzwiek powrocil do zrodla w s: ")
    czasy.append(float(t))
    x = licz(float(t), float(osr))
    odleg.append(x)
    i += 1

j = 0
while j < int(n)-1:
    t1 = czasy[j]
    t2 = czasy[j+1]
    rt = -t1/2 + float(inter) + t2/2
    print(rt)
    speed = (odleg[j] - odleg[j+1])/rt
    predkosci.append(speed)
    j+=1

print(odleg)
print(czasy)
print(predkosci)

