def SprawdzOdbicie(tablica):
    n = len(tablica)
    
    for col in range(n):
        for i in range(len(tablica[0]) // 2):
            if tablica[col][i] == tablica[col][len(tablica[0]) - i - 1]:
                print(f"Kolumnowe odbicie w kolumnach {i+1} i {len(tablica[0]) - i}")
                return 0


    for row in range(n // 2):
        if tablica[row] == tablica[n - row - 1]:
            print(f"Poziome odbicie między wierszami {row+1} i {n-row-1}")
            return 

    return 0

def RozdzielTab(tablice):
    NoweTablice = []
    tablica = []
    
    for rzad in tablice:
        if rzad.strip(" "):
            tablica.append(rzad)
        else:
            if tablica:
                NoweTablice.append(tablica)
                tablica = []
    
    if tablica:
        NoweTablice.append(tablica)
    
    return NoweTablice

tablice = [
    "#.##..##.",
    "..#.##.#.",
    "##......#",
    "##......#",
    "..#.##.#.",
    "..##..##.",
    "#.#.##.#.",
    " ",
    "#...##..#",
    "#....#..#",
    "..##..###",
    "#####.##.",
    "#####.##.",
    "..##..###",
    "#....#..#"
]

tablice = RozdzielTab(tablice)

for i, t in enumerate(tablice):
    print(f"Sprawdzam odbicie w grupie {i+1}...")
    SprawdzOdbicie(t)