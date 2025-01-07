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
    # Sprawdza, czy wiersz zawiera tylko zera
    return all(x == 0 for x in wiersz)

def BadajSekwencje(wiersz):
    # Iteracyjnie liczy różnice aż do osiągnięcia wiersza z samymi zerami
    LiczbaRoznic = 0
    while LiczbaRoznic <= 10:
        print(f"Iteracja {LiczbaRoznic}, wiersz: {wiersz}")
        if SprawdzZera(wiersz):
            print(f"Wiersz zawiera tylko zera po {LiczbaRoznic} iteracjach.")
            return LiczbaRoznic
        wiersz = ObliczRoznice(wiersz)
        LiczbaRoznic += 1
    print(f"Osiągnięto limit iteracji, wiersz: {wiersz}")
    return LiczbaRoznic

for i in range(len(tablica)):
    NowaLiczba = BadajSekwencje(tablica[i])
    tablica[i].append(NowaLiczba)

print(f"Po dodaniu pól nowa tablica to:\n{tablica}")