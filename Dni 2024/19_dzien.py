import sys

# Wczytaj dane
dane = sys.stdin.read().strip().split("\n")

# Oddzielne grupy
fragmenty = []
elementy = []

for linia in dane:
    if ',' in linia:
        fragmenty.extend(x.strip() for x in linia.split(","))
    else:
        elementy.append(linia.strip())

# Wyniki
print("Ciągi z przecinkami:", fragmenty)
print("Długie ciągi:", elementy)

def znajdz_podciagi(fragmenty, elementy):
    liczba_dopasowan = 0
    # Tworzymy kopię fragmentów, żeby modyfikować
    fragmenty_copy = fragmenty.copy()

    # Dla każdego długiego ciągu
    for slowo in elementy:
        znalezione = False
        
        for fragment in fragmenty_copy:
            # Jeśli fragment jest częścią długiego słowa
            if fragment in slowo:
                znalezione = True
                fragmenty_copy.remove(fragment)  # Usuwamy fragment po dopasowaniu
                break

        if znalezione:  # Jeśli znaleziono dopasowanie
            liczba_dopasowan += 1  # Zliczamy słowo z dopasowaniem

    return liczba_dopasowan

# Wywołanie funkcji
liczba_dopasowan = znajdz_podciagi(fragmenty, elementy)

# Wypisanie wyników
print(f"Liczba długich ciągów, które mają dopasowanie: {liczba_dopasowan}")
