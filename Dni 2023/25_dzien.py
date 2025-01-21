from typing import List, Optional

tablica = [
    "jqt: rhn xhk nvd",
    "rsh: frs pzl lsr",
    "xhk: hfx",
    "cmg: qnr nvd lhk bvb",
    "rhn: xhk bvb hfx",
    "bvb: xhk hfx",
    "pzl: lsr hfx nvd",
    "qnr: nvd",
    "ntq: jqt hfx bvb xhk",
    "nvd: lhk",
    "lsr: lhk",
    "rzs: qnr cmg lsr rsh",
    "frs: qnr lhk lsr"
]

def StwórzSłownik(tablica: List[str]):
    slownik = {}
    PraweElementy = set()
    elementyStartowe = []

    for wiersz in tablica:
        try:
            LewyElement, rozdzielenie = wiersz.split(": ")
            elementyStartowe.append(LewyElement)
            wyjścia = rozdzielenie.split(" ")
            slownik[LewyElement] = wyjścia
            
            for wyjscie in wyjścia:
                PraweElementy.add(wyjscie)
        except ValueError:
            print(f"Błąd w formatowaniu wiersza: '{wiersz}'")
            continue

    return slownik, PraweElementy, elementyStartowe

def ZnajdzStarty(tablica: List[str]):
    slownik, PraweElementy, elementyStartowe = StwórzSłownik(tablica)
    
    Starty = []
    for element in elementyStartowe:
        if element not in PraweElementy:
            Starty.append(element)
    
    return Starty

def dfs_generuj_trasy(dlugosc: int):
    slownik, PraweElementy, elementyStartowe = StwórzSłownik(tablica)
    trasy = ZnajdzStarty(tablica)
    
    trasy = [[start] for start in trasy]

    for _ in range(dlugosc - 1):
        NoweTrasy = []
        for trasa in trasy:
            OstatniElement = trasa[-1]
            if OstatniElement not in slownik:
                continue
            sasiedzi = slownik[OstatniElement]
            for sasiad in sasiedzi:
                NowaTrasa = trasa + [sasiad]
                NoweTrasy.append(NowaTrasa)
        trasy = NoweTrasy
    
    return trasy

def WyznaczGłówneWartości(liczba, wynik):
    cyfra = 0
    for _ in range(5):
        wartości = []
        for i in range(len(wynik)):
            wartości.append(wynik[i][cyfra])

        wartości = list(set(wartości))
        cyfra += 1

        if len(wartości) == liczba:
            return wartości

def PodzielNaGrupy(wyniki, wartości):
    grupy = {}
    for wartość in wartości:
        for wynik in wyniki:
            if wartość in wynik:
                if wartość not in grupy:
                    grupy[wartość] = []
                grupy[wartość].append(wynik)
    
    for klucz in grupy:
        złączone = []
        for lista in grupy[klucz]:
            złączone.extend(lista)
        grupy[klucz] = list(set(złączone))
    
    return grupy

wynik = dfs_generuj_trasy(5)

wartości = WyznaczGłówneWartości(3, wynik)

grupy = PodzielNaGrupy(wynik, wartości)

for i in range(len(tablica)):
    print(tablica[i])

for klucz, wartosci in grupy.items():
    print(f"Grupa: {klucz}")
    print(f"  Liczba elementów: {len(wartosci)}")
    print(f"  Elementy: {', '.join(sorted(wartosci))}")
    print("=" * 40)