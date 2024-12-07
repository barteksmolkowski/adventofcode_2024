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

for klucz, wartosci in tabela.items():
    liczby = list(wartosci)  # Tworzymy listę z tupli
    print(f"Sprawdzam klucz {klucz} z wartościami {liczby}")  # Debugowanie, wyświetlamy klucz i liczby

    match len(liczby):
        case 2:
            if liczby[0] + liczby[1] == klucz:
                print(f"{liczby[0]} + {liczby[1]} = {klucz}")
            elif liczby[0] * liczby[1] == klucz:
                print(f"{liczby[0]} * {liczby[1]} = {klucz}")
        case 3:
            if liczby[0] + liczby[1] + liczby[2] == klucz:
                print(f"{liczby[0]} + {liczby[1]} + {liczby[2]} = {klucz}")
            elif liczby[0] + liczby[1] * liczby[2] == klucz:
                print(f"{liczby[0]} + {liczby[1]} * {liczby[2]} = {klucz}")
            elif liczby[0] * liczby[1] + liczby[2] == klucz:
                print(f"{liczby[0]} * {liczby[1]} + {liczby[2]} = {klucz}")
            elif liczby[0] * liczby[1] * liczby[2] == klucz:
                print(f"{liczby[0]} * {liczby[1]} * {liczby[2]} = {klucz}")
        case 4:
            if liczby[0] + liczby[1] + liczby[2] + liczby[3] == klucz:
                print(f"{liczby[0]} + {liczby[1]} + {liczby[2]} + {liczby[3]} = {klucz}")
            elif liczby[0] + liczby[1] + liczby[2] * liczby[3] == klucz:
                print(f"{liczby[0]} + {liczby[1]} + {liczby[2]} * {liczby[3]} = {klucz}")
            elif liczby[0] + liczby[1] * liczby[2] + liczby[3] == klucz:
                print(f"{liczby[0]} + {liczby[1]} * {liczby[2]} + {liczby[3]} = {klucz}")
            elif liczby[0] + liczby[1] * liczby[2] * liczby[3] == klucz:
                print(f"{liczby[0]} + {liczby[1]} * {liczby[2]} * {liczby[3]} = {klucz}")
            elif liczby[0] * liczby[1] + liczby[2] + liczby[3] == klucz:
                print(f"{liczby[0]} * {liczby[1]} + {liczby[2]} + {liczby[3]} = {klucz}")
            elif liczby[0] * liczby[1] + liczby[2] * liczby[3] == klucz:
                print(f"{liczby[0]} * {liczby[1]} + {liczby[2]} * {liczby[3]} = {klucz}")
            elif liczby[0] * liczby[1] * liczby[2] + liczby[3] == klucz:
                print(f"{liczby[0]} * {liczby[1]} * {liczby[2]} + {liczby[3]} = {klucz}")
            elif liczby[0] * liczby[1] * liczby[2] * liczby[3] == klucz:
                print(f"{liczby[0]} * {liczby[1]} * {liczby[2]} * {liczby[3]} = {klucz}")

