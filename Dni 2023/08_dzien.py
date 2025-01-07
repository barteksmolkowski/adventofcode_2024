tablica = [
    "RL",
    "",
    "AAA = (BBB, CCC)",
    "BBB = (DDD, EEE)",
    "CCC = (ZZZ, GGG)",
    "DDD = (DDD, DDD)",
    "EEE = (EEE, EEE)",
    "GGG = (GGG, GGG)",
    "ZZZ = (ZZZ, ZZZ)"
]

def odczytanieDanych(tablica):
    instrukcja = tablica[0]
    ruchy = {}
    
    for i in range(2, len(tablica)):
        if tablica[i]:
            elementy = tablica[i].split(" = ")
            if len(elementy) == 2:
                klucz = elementy[0]
                wartosci = elementy[1].strip("()").split(", ")
                ruchy[klucz] = wartosci
    
    return instrukcja, ruchy

def OdczytajRuch(komorka, ruch, instrukcja, ruchy):
    NazwaRuchu = instrukcja[ruch % len(instrukcja)]
    if NazwaRuchu == "R":
        return ruchy[komorka][1]
    elif NazwaRuchu == "L":
        return ruchy[komorka][0]
    else:
        raise ValueError("Nieznany kierunek w instrukcji!")

def PoliczRuchy(instrukcja, ruchy):
    komorka = "AAA"
    ruch = 0
    while komorka != "ZZZ":
        komorka = OdczytajRuch(komorka, ruch, instrukcja, ruchy)
        ruch += 1
    return ruch

instrukcja, ruchy = odczytanieDanych(tablica)
LiczbaRuchow = PoliczRuchy(instrukcja, ruchy)
print(f"Liczba ruchów wymagana do przejścia labiryntu wynosi: {LiczbaRuchow}")