osrodki = {
    "powietrze": 343,
    "woda": 1500
}

print("Obslugiwane osrodki to:")
for name in osrodki:
    print(name)

t = input("Podaj czas po ktorym dzwiek powrocil do zrodla w s: ")
osr = input("Podaj nazwe osrodka lub predkosc dzwieku w osrodku: ")

if osr in osrodki:
    osr = osrodki[osr]

def licz(t, osr):
    x = osr * t/2
    return x

x = licz(float(t), float(osr))
print("Odleglosc wynosi:", x, "m")


