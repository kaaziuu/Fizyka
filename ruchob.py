# # import json
#
# osrodki = {
#     "powietrze": 343,
#     "woda": 1500
# }
# # tab_js = json.dumps(osrodki)
# # with open('save.json', 'w') as f:
# #     f.write(tab_js)
#
#
# osr = input("Podaj nazwe osrodka lub predkosc dzwieku w osrodku: ")
# f = input("Podaj czestotliwosc emisji: ")
# f1 = input("Podaj czestotliwosc zwrotna: ")
#
# if osr in osrodki:
#     osr = osrodki[osr]

def licz(osr, f, f1):
    vo = (osr*f1)/f - osr
    return vo

# x = licz(float(osr), float(f), float(f1))
# print("Predkosc detektora wynosi:", x, "m/s")

