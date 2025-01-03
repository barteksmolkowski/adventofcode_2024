tablica = [
    "1abc2",
    "pqr3stu8vwx",
    "a1b2c3d4e5f",
    "treb7uchet"
]

liczba = 0
L_tablica = []

for i in range(len(tablica)):
    L_cyfry = []
    for j in range(len(tablica[i])):
        try:
            liczba = int(tablica[i][j])
            L_cyfry.append(liczba)
        except ValueError:
            continue
    match len(L_cyfry):
        case 1:
            L_tablica.append(int(str(L_cyfry[0]) * 2))
        case _:
            L_tablica.append(int(str(L_cyfry[0]) + str(L_cyfry[-1])))

print("Wynikowe wartości kalibracyjne:", L_tablica)
print("Suma wartości kalibracyjnych:", sum(L_tablica))
