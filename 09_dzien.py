pamiec = "2333133121414131402"
nowa_pamiec = ""
x = 0

for i in range(len(pamiec)):
    length = int(pamiec[i])
    if i % 2 == 0:
        nowa_pamiec += f"{x}" * length  
        x += 1
    else:
        nowa_pamiec += "." * length

tablica = list(nowa_pamiec)

def znajdz_pierwsza_kropke():
    for i, el in enumerate(tablica):
        if el == ".":
            return i
    return None

def znajdz_ostatnia_liczbe():
    for i in range(len(tablica) - 1, -1, -1):
        if tablica[i].isdigit():
            return i
    return None

while True:
    pierwsza_kropka = znajdz_pierwsza_kropke()
    ostatnia_liczba = znajdz_ostatnia_liczbe()
    
    if pierwsza_kropka is None or ostatnia_liczba is None or pierwsza_kropka >= ostatnia_liczba:
        break

    tablica[pierwsza_kropka], tablica[ostatnia_liczba] = tablica[ostatnia_liczba], tablica[pierwsza_kropka]

    print("".join(tablica))
    input("Naciśnij Enter, aby kontynuować...")

