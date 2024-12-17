import sys
print("Wklej tekst i naciśnij Enter dwukrotnie, aby zakończyć:")
tekst = sys.stdin.read()
tablica = tekst.strip().split('\n')

registery = []
for i in range(0, 3):
    registery.append(int(tablica[i][12:]))

# Poprawiamy kod odczytu programu:
instrukcja = tablica[4][9:]  # Usuń "Program: " przed split
instrukcje = instrukcja.split(',')

for i in range(len(instrukcje)):
    try:
        instrukcje[i] = int(instrukcje[i])  # Konwertuj na liczby całkowite
    except ValueError:
        continue

dane = {"instrukcja":[], "operand":[]}
for i in range(len(instrukcje)):
    if i % 2 == 0:
        dane["instrukcja"].append(instrukcje[i])
    else:
        dane["operand"].append(instrukcje[i])

for i in range(len(dane["instrukcja"])):
    operand = dane["operand"][i]
    match dane["instrukcja"][i]:
        case 0:
            wynik = registery[0] // (2 ** operand)