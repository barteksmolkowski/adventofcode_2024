tablica = [
    "Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green",
    "Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue",
    "Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red",
    "Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red",
    "Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green"
]

# Ustalamy limity
maks_red = 12
maks_green = 13
maks_blue = 14

mozliwe_gry = []

# Iterujemy przez każdą grę
for i in range(len(tablica)):
    tekst = tablica[i][7:] 
    
    red, green, blue = 0, 0, 0
    
    zestawy = tekst.split(";")
    
    for zestaw in zestawy:
        elementy = zestaw.split(",")
        for el in elementy:
            liczba, kolor = el.strip().split(" ")
            liczba = int(liczba)
            
            if kolor == "red":
                red += liczba
            elif kolor == "green":
                green += liczba
            elif kolor == "blue":
                blue += liczba
    
    if red <= maks_red and green <= maks_green and blue <= maks_blue:
        mozliwe_gry.append(i + 1)

print(mozliwe_gry)
