import sys

def bramka(input1, input2, rodzaj):
    match rodzaj:
        case "AND":
            return input1 & input2
        case "OR":
            return input1 | input2
        case "XOR":
            return input1 ^ input2

# Słownik na początkowe wartości kabli
wartosci_poczatkowe = {}
# Lista bramek logicznych
bramki = []

# Wczytywanie danych z wejścia
for linia in sys.stdin:
    linia = linia.strip()  # Usunięcie zbędnych spacji i znaków nowej linii
    if not linia:  # Pusta linia kończy sekcję wartości początkowych
        continue
    if ":" in linia:
        # Wczytujemy wartości wejściowe, np. "x00: 1"
        kabel, wartosc = linia.split(":")
        wartosci_poczatkowe[kabel.strip()] = int(wartosc.strip())
    elif "->" in linia:
        # Wczytujemy opis bramek logicznych, np. "ntg XOR fgs -> mjb"
        bramki.append(linia)

# Wyświetlenie danych (do celów testowych)
print("Początkowe wartości kabli:", wartosci_poczatkowe)
print("Bramki logiczne:", bramki)
n_wartosci = {}

rozdzielone_bramki = {}
for i in range(len(bramki)):
    rozdzielone_bramki.append(i)
    czesci = wejscie.split()
    input1 = czesci[0].strip()  # Pierwszy kabel wejściowy
    operator = czesci[1].strip()  # Operator logiczny (AND, OR, XOR)
    input2 = czesci[2].strip()  # Drugi kabel wejściowy    
    rozdzielone_bramki[i].append()

def logika():
    bramka_info = bramki[i]
    wejscie, wyjscie = bramka_info.split("->")
    wyjscie = wyjscie.strip()  # Kabel, gdzie zapisujemy wynik


