osrodki = {
    "powietrze": 343,
    "woda": 1500
}

osr = input("Podaj nazwe osrodka lub predkosc dzwieku w osrodku: ")
f = input("Podaj czestotliwosc emisji: ")
f1 = input("Podaj czestotliwosc zwrotna: ")

if osr in osrodki:
    osr = osrodki[osr]

def licz(osr, f, f1):
    vo = (osr*f1)/f - osr
    return vo

x = licz(float(osr), float(f), float(f1))
print("Predkosc detektora wynosi:", x, "m/s")

