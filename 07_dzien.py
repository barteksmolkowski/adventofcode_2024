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

def generuj_wyrazenia(wartosci):
    operatory = ['+', '*']
    n = len(wartosci)
    
    kombinacje = []

    for i in range(2 ** (n - 1)): 
        wyrazenie = str(wartosci[0])
        binarna_kombinacja = bin(i)[2:].zfill(n - 1)

        for j in range(n - 1):
            operator = operatory[int(binarna_kombinacja[j])]
            wyrazenie += f" {operator} {wartosci[j + 1]}"

        kombinacje.append(wyrazenie)
    
    return kombinacje

def sprawdz_kombinacje(tabela):
    for klucz, wartosci in tabela.items():
        print(f"Sprawdzam klucz {klucz} z wartościami {wartosci}")
        
        wyrazenia = generuj_wyrazenia(wartosci)
        
        znaleziono = False
        for wyrazenie in wyrazenia:
            try:
                wynik = eval(wyrazenie)

                if wynik == klucz:
                    print(f"Znaleziono: {wyrazenie} = {wynik}")
                    znaleziono = True

            except ZeroDivisionError:
                continue
        
        if not znaleziono:
            print(f"Brak pasujących kombinacji dla klucza {klucz}")
            
        print("-" * 30)

sprawdz_kombinacje(tabela)
