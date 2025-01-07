tablica = [
    [0, 3, 6, 9, 12, 15],
    [1, 3, 6, 10, 15, 21],
    [10, 13, 16, 21, 30, 45]
]

def ObliczRoznice(wiersz):
    NowyWiersz = []
    for i in range(1, len(wiersz)):
        a, b = wiersz[i], wiersz[i - 1]
        NowyWiersz.append(a - b)
    return NowyWiersz

def SprawdzZera(wiersz):
    return all(x == 0 for x in wiersz)

def BadajSekwencje(wiersz):
    LiczbaRoznic = 0
    suma = 0
    while LiczbaRoznic <= 25:
        print(f"Iteracja {LiczbaRoznic}, wiersz: {wiersz}")
        suma += wiersz[-1]
        if SprawdzZera(wiersz):
            print(f"Wiersz zawiera tylko zera po {LiczbaRoznic} iteracjach.")
            return suma
        wiersz = ObliczRoznice(wiersz)
        LiczbaRoznic += 1
    print(f"Osiągnięto limit iteracji, wiersz: {wiersz}")
    return suma

for i in range(len(tablica)):
    suma = BadajSekwencje(tablica[i])
    tablica[i].append(suma)

print(f"Po dodaniu pól nowa tablica to:\n{tablica}")