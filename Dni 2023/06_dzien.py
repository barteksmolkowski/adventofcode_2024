czasy = [(42, 284), (68, 1005), (69, 1122), (85, 1341)]

def licz_mozliwe_rozwiazania(czasy):
    total_sposoby = 1
    for idx, (WRczas, rekord) in enumerate(czasy):
        print(f"\nWyścig {idx + 1}: Czas = {WRczas} ms, Rekordowy dystans = {rekord} mm")
        
        sposoby = 0
        for czas_przycisku in range(WRczas + 1):
            prędkość = czas_przycisku
            czas_na_ruch = WRczas - czas_przycisku
            dystans = prędkość * czas_na_ruch

            print(f"  Przytrzymaj: {czas_przycisku} ms, Prędkość: {prędkość} mm/ms, "
                f"Czas ruchu: {czas_na_ruch} ms, Dystans: {dystans} mm")

            if dystans > rekord:
                print(f"    -> Dystans {dystans} mm przekracza rekord!")
                sposoby += 1
        
        print(f"Liczba sposobów na pobicie rekordu w wyścigu {idx + 1}: {sposoby}")
        total_sposoby *= sposoby
    
    return total_sposoby

wynik = licz_mozliwe_rozwiazania(czasy)
print(f"\nŁączna liczba możliwych sposobów na pobicie rekordów we wszystkich wyścigach: {wynik}")