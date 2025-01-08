import itertools

tablica = [
    "???.### 1,1,3",
    ".??..??...?##. 1,1,3",
    "?#?#?#?#?#?#?#? 1,3,1,6",
    "????.#...#... 4,1,1",
    "????.######..#####. 1,6,5",
    "?###???????? 3,2,1"
]

def OdczytajWiersz(wiersz):
    wiersz, liczbyStr = wiersz.split(" ")
    liczby = list(map(int, liczbyStr.split(",")))
    return wiersz, liczby

def Generuj(dlugosc):
    return list(itertools.product([0, 1], repeat=dlugosc))

def SprawdzMozl(wiersz, liczby):
    liczbaLen = 0
    numerIdx = 0

    for znak in wiersz + ".":
        if znak == "#":
            liczbaLen += 1
        elif liczbaLen > 0:
            if numerIdx >= len(liczby) or liczby[numerIdx] != liczbaLen:
                return False
            numerIdx += 1
            liczbaLen = 0

    return numerIdx == len(liczby)

def UzupelnijWiersz(wiersz, liczby):
    suma_liczb = sum(liczby)
    liczba_hash = wiersz.count("#")
    roznica = suma_liczb - liczba_hash

    if roznica <= 0:
        return wiersz if SprawdzMozl(wiersz, liczby) else None

    zmiany = Generuj(wiersz.count("?"))
    mozliwosci = []

    for zmiana in zmiany:
        tekst = ""
        idx = 0
        for znak in wiersz:
            if znak == "?":
                tekst += "#" if zmiana[idx] == 1 else "."
                idx += 1
            else:
                tekst += znak

        if SprawdzMozl(tekst, liczby):
            mozliwosci.append(tekst)

    return mozliwosci

for i in range(len(tablica)):
    wiersz, liczby = OdczytajWiersz(tablica[i])
    wynik = UzupelnijWiersz(wiersz, liczby)

    print(f"Wiersz {wiersz}, Liczby: {liczby}")
    if wynik:
        print(f"   Możliwe uzupełnienia: {wynik}")
    else:
        print("   Brak możliwych uzupełnień.")