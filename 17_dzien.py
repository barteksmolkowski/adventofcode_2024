import sys

print("Wklej tekst i naciśnij Enter dwukrotnie, aby zakończyć:")
tekst = sys.stdin.read()
tablica = tekst.strip().split('\n')

registery = []
for i in range(0, 3):
    try:
        registery.append(int(tablica[i][12:]))
    except ValueError:
        print(f"Błąd w odczycie rejestru {tablica[i]}")
        sys.exit()

instrukcje = tablica[4][9:].split(',')

for i in range(len(instrukcje)):

    try: instrukcje[i] = int(instrukcje[i])
    except ValueError: continue
        

dane = {"instrukcja":[], "operand":[]}
for i in range(len(instrukcje)):
    dane["instrukcja"].append(instrukcje[i]) if i % 2 == 0 else dane["operand"].append(instrukcje[i])

for i in range(len(dane["instrukcja"])):
    operand = dane["operand"][i]
    match dane["instrukcja"][i]:
        case 0:  # A //= 2^operand
            wynik = registery[0] // (2 ** operand)
            registery[0] = wynik
        case 1:  # A *= operand
            wynik = registery[0] * operand
            registery[0] = wynik
        case 2:  # A += B
            wynik = registery[0] + registery[1]
            registery[0] = wynik
        case 3:  # C -= A + B
            wynik = registery[2] - (registery[0] + registery[1])
            registery[2] = wynik
        case 4:  # suma A, B, C
            wynik = registery[0] + registery[1] + registery[2]
            print(f"Suma Rejestrów: {wynik}")
        case 5:  # A //= operand
            wynik = registery[0] // operand
            registery[0] = wynik
        case 7:  # C ^= operand
            wynik = registery[2] ^ operand
            registery[2] = wynik

print("\nWartości rejestrów po wykonaniu programu:")
print(f"Register A: {registery[0]}")
print(f"Register B: {registery[1]}")
print(f"Register C: {registery[2]}")