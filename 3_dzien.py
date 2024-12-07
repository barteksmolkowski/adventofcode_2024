a = 4
b = 0
liczba1 = 0
liczba2 = 0

instrukcja = input("Podaj komendę mul(X,Y), aby pomnożyć liczby X i Y: ")

if instrukcja[:4] == "mul(":
    while True:
        try:
            if b == 0:
                x = int(instrukcja[a])
                liczba1 = liczba1 * 10 + x
            else:
                y = int(instrukcja[a])
                liczba2 = liczba2 * 10 + y
            a += 1
        except ValueError:
            if b == 0:
                a += 1
                b = 1
            else:
                print(f"Wynik to: {liczba1 * liczba2}")
                break