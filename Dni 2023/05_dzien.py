def zamiana(tablica, liczba):
    for start1, start2, dlugosc in tablica:
        wejscie = [i for i in range(start1, start1 + dlugosc)]
        wynik = [i for i in range(start2, start2 + dlugosc)]
        
        if liczba in wejscie:
            indeks = wejscie.index(liczba)
            print(f"jest zmiana z {liczba} na {wynik[indeks]}")
            return wynik[indeks]
    print(f"bez zmian, pozostaje: {liczba}")
    return liczba  # Jeśli liczba nie jest w żadnym zakresie, zwracamy ją bez zmian.

# Dane wejściowe:
seeds = [79, 14, 55, 13]

seed_to_soil_map = [
    (50, 98, 2),
    (52, 50, 48)
]
soil_to_fertilizer_map = [
    (0, 15, 37),
    (37, 52, 2),
    (39, 0, 15)
]
fertilizer_to_water_map = [
    (49, 53, 8),
    (0, 11, 42),
    (42, 0, 7),
    (57, 7, 4)
]
water_to_light_map = [
    (88, 18, 7),
    (18, 25, 70)
]
light_to_temperature_map = [
    (45, 77, 23),
    (81, 45, 19),
    (68, 64, 13)
]
temperature_to_humidity_map = [
    (0, 69, 1),
    (1, 0, 69)
]
humidity_to_location_map = [
    (60, 56, 37),
    (56, 93, 4)
]

# Iteracyjna konwersja każdego numeru nasion
def znajdz_lokalizacje(seeds):
    najnizsza_lokalizacja = float('inf')  # Użyjemy tego, żeby znaleźć minimalny wynik
    
    for seed in seeds:
        # Przejdź przez kolejne mapy
        soil = zamiana(seed_to_soil_map, seed)
        fertilizer = zamiana(soil_to_fertilizer_map, soil)
        water = zamiana(fertilizer_to_water_map, fertilizer)
        light = zamiana(water_to_light_map, water)
        temperature = zamiana(light_to_temperature_map, light)
        humidity = zamiana(temperature_to_humidity_map, temperature)
        location = zamiana(humidity_to_location_map, humidity)
        
        # Znajdź najniższą lokalizację
        print(f"znaleziono lokację dla {seed} która wynosi: {location}\n")
        najnizsza_lokalizacja = min(najnizsza_lokalizacja, location)
    
    return najnizsza_lokalizacja

# Oblicz i wyświetl wynik
najnizsza_lokalizacja = znajdz_lokalizacje(seeds)
print("Najniższa lokalizacja:", najnizsza_lokalizacja)
