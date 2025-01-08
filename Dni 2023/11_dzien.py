tablica = [
    "...#......",
    ".......#..",
    "#.........",
    "..........",
    "......#...",
    ".#........",
    ".........#",
    "..........",
    ".......#..",
    "#...#....."
]

def rozszerzTab(tablica):
    NowaTab = []

    for wiersz in tablica:
        NowaTab.append(wiersz)
        if "#" not in wiersz:
            NowaTab.append("." * len(wiersz))

    rozszerzona_tablica = [] 

    for wiersz in NowaTab:
        nowy_wiersz = ""
        
        for j in range(len(wiersz)):
            nowy_wiersz += wiersz[j]
            
            kolumna_pusta = True
            for w in NowaTab:
                if w[j] != ".":
                    kolumna_pusta = False
                    break
            
            if kolumna_pusta:
                nowy_wiersz += "."
            
        rozszerzona_tablica.append(nowy_wiersz)
    
    return rozszerzona_tablica

def PoliczSumeMozliwosci(Punkty):
    mozliwosci = []
    suma = 0
    
    if len(Punkty) < 2:
        return mozliwosci
    
    for i in range(len(Punkty)):
        for j in range(i + 1, len(Punkty)):
            x1, y1 = Punkty[i]
            x2, y2 = Punkty[j]

            odleglosc = abs(x1 - x2) + abs(y1 - y2)
            suma += odleglosc
            print(f"Od punktu ({x1}, {y1}) do punktu ({x2}, {y2}) odległość wynosi {odleglosc}")

    return suma

def OdczytajPunkty(tablica):
    punkty = []
    for i in range(len(tablica)):
        for j in range(len(tablica[i])):
            if tablica[i][j] == "#":
                punkty.append((i, j))
    return punkty

tablica = rozszerzTab(tablica)
punkty = OdczytajPunkty(tablica)
wynik = PoliczSumeMozliwosci(punkty)

print(f"Suma punktów wynosi: {wynik}")