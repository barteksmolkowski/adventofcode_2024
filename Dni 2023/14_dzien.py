# Tablica startowa
tablica = [
    list("O....#...."),
    list("O.OO#....#"),
    list(".....##..."),
    list("OO.#O....O"),
    list(".O.....O#."),
    list("O.#..O.#.#"),
    list("..O..#O..O"),
    list(".......O.."),
    list("#....###.."),
    list("#OO..#....")
]

def WyswietlTablice():
    for wiersz in tablica:
        print("".join(wiersz))

def Grawitacja(x, y):
    tekst = ""
    nX = x - 1
    if nX >= 0 and tablica[nX][y] == ".":
        tekst = f"Nowe pole: ({nX}, {y}), na nim jest: {tablica[nX][y]}" 
        tablica[x][y], tablica[nX][y] = ".", "O"
    return tekst

def kola():
    suma = 0
    for i in range(len(tablica)):
        for j in range(len(tablica[i])):
            if tablica[i][j] == "O":
                suma += 1
    return suma

def PoliczWartosc():
    suma = 0
    wartosc = 10
    for i in range(len(tablica)):
        kola = 0
        for j in range(len(tablica[i])):
            if tablica[i][j] == "O":
                kola += 1
        suma += wartosc * kola
        wartosc -= 1
    return suma

for _ in range(len(tablica)):
    for i in range(1, len(tablica)):
        for j in range(len(tablica[i])):
            if tablica[i][j] == "O":
                Ntekst = (Grawitacja(i, j))



WyswietlTablice()
print(f"Obciążenie wynosi: {PoliczWartosc()}")