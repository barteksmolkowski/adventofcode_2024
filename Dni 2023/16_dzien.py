tablica = [
    list("/-\\"),
    list("|.|"),
    list("\\-/"),
]

def WyswietlTablice(tablica):
    for wiersz in tablica:
        print("".join(wiersz))

def Czujnik(x, y, ruch): # zwraca w jaki kierunek po lustrze trzeba iść
    ruchy = {1:(0, -1), 2:(1, 0), 3:(0, 1), 4:(-1, 0)}
    a, b = ruchy[ruch]
    blok = tablica[x + a][y + b]
    if blok == ".":
        return ruch
    elif a != 0:
        match blok:
            case "/":
                if ruch == 1:
                    return 2
                else:
                    return 4
            case "\\":
                if ruch == 1:
                    return 4
                else:
                    return 2
            case "-":
                return (2, 4)
            case "|":
                return ruch
    elif b != 0:
        match blok:
            case "/":
                if ruch == 2:
                    return 1
                else:
                    return 3
            case "\\":
                if ruch == 2:
                    return 3
                else:
                    return 1
            case "-":
                return (1, 3)
            case "|":
                return ruch

x, y, kierunek = 1, 1, 3
print(Czujnik(x, y, kierunek))