tabela = { 
    190: (10, 19),
    3267: (81, 40, 27),
    83: (17, 5),
    156: (15, 6),
    7290: (6, 8, 6, 15),
    161011: (16, 10, 13),
    192: (17, 8, 14),
    21037: (9, 7, 18, 13),
    292: (11, 6, 16, 20)
}

# Funkcja do generowania wszystkich możliwych kombinacji operatorów (+ i *)
def generuj_wyrazenia(wartosci):
    operatory = ['+', '*']
    n = len(wartosci)
    
    # Liczba kombinacji operatorów to 2^(n-1), gdzie n to liczba liczb w krotce
    kombinacje = []
    # Generujemy wszystkie możliwe ciągi operatorów dla (n-1) miejsc
    for i in range(2 ** (n - 1)): 
        wyrazenie = str(wartosci[0])
        binarna_kombinacja = bin(i)[2:].zfill(n - 1)  # Zamieniamy na binarną reprezentację
        for j in range(n - 1):
            operator = operatory[int(binarna_kombinacja[j])]  # Wybieramy operator na podstawie 0 lub 1
            wyrazenie += f" {operator} {wartosci[j + 1]}"
        kombinacje.append(wyrazenie)
    
    return kombinacje

# Funkcja do sprawdzania, które kombinacje dają wynik równy kluczowi
def sprawdz_kombinacje(tabela):
    for klucz, wartosci in tabela.items():
        print(f"Sprawdzam klucz {klucz} z wartościami {wartosci}")
        
        wyrazenia = generuj_wyrazenia(wartosci)
        
        # Sprawdzamy wszystkie kombinacje
        znaleziono = False  # Flaga, czy znaleziono kombinację
        for wyrazenie in wyrazenia:
            try:
                wynik = eval(wyrazenie)
                if wynik == klucz:
                    print(f"Znaleziono: {wyrazenie} = {wynik}")
                    znaleziono = True
            except ZeroDivisionError:  # Obsługuje ewentualne dzielenie przez 0
                continue
        
        if not znaleziono:
            print(f"Brak pasujących kombinacji dla klucza {klucz}")
        print("-" * 30)

# Uruchomienie funkcji
sprawdz_kombinacje(tabela)
