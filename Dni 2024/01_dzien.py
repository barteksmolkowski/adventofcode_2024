prawa = [4, 3, 5, 3, 9, 3]
lewa = [3, 4, 2, 1, 3, 3]

prawa = sorted(prawa)
lewa = sorted(lewa)

wynik = 0

for i in range(len(prawa)):
    wynik += abs(prawa[i] - lewa[i])

print(wynik)