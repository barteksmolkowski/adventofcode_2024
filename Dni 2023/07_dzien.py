gry = {
    "32T3K": "765",
    "T55J5": "684",
    "KK677": "28",
    "KTJJT": "220",
    "QQQJT": "483"
}

def PoliczZnaki(tekst):
    znaki = {}
    for i in tekst:
        if i not in znaki:
            znaki[i] = 1
        else:
            znaki[i] += 1
    return znaki

def Rozpoznaj(gra):
    znaki = PoliczZnaki(gra)
    wartosci = sorted(znaki.values(), reverse=True)
    
    match wartosci:
        case [5]: 
            return 6
        case [3, 2]: 
            return 5
        case [4, 1]:
            return 4
        case [3, 1, 1]:
            return 3
        case [2, 2, 1]:
            return 2
        case [2, 1, 1, 1]:
            return 1
        case _:
            return 0

AlfabetWartosci = list("AKQJT98765432")

def Wartosc(gra1, gra2):
    rodzaj1, rodzaj2 = Rozpoznaj(gra1), Rozpoznaj(gra2)
    
    if rodzaj1 != rodzaj2:
        return 1 if rodzaj1 > rodzaj2 else -1
    
    for karta1, karta2 in zip(gra1, gra2):
        wartosc1 = AlfabetWartosci.index(karta1)
        wartosc2 = AlfabetWartosci.index(karta2)
        if wartosc1 != wartosc2:
            return 1 if wartosc1 > wartosc2 else -1
    
    return 0

gry_lista = list(gry.keys())

for i in range(len(gry_lista)):
    for j in range(i + 1, len(gry_lista)):
        if Wartosc(gry_lista[i], gry_lista[j]) < 0:
            gry_lista[i], gry_lista[j] = gry_lista[j], gry_lista[i]

ranking = {}
for i in range(len(gry_lista)):
    ranking[gry_lista[i]] = i + 1

wynik = 0
for gra in gry_lista:
    poczatkowa_wygrana = int(gry[gra])
    wygrana_po_mnozeniu = poczatkowa_wygrana * ranking[gra]
    print(f"Gra: {gra}, Układ: {Rozpoznaj(gra)}, Miejsce: {ranking[gra]}, Wygrana: {wygrana_po_mnozeniu}")
    wynik += wygrana_po_mnozeniu

print(f"Łączna wygrana: {wynik}")
