reguly = [
    (47, 53),(97, 13),(97, 61),
    (97, 47),(75, 29),(61, 13),
    (75, 53),(29, 13),(97, 29),
    (53, 29),(61, 53),(97, 53),
    (61, 29),(47, 13),(75, 47),
    (97, 75),(47, 61),(75, 61),
    (47, 29),(75, 13),(53, 13)]

aktualizacje = [
    [75, 47, 61, 53, 29],
    [97, 61, 53, 29, 13],
    [75, 29, 13],
    [75, 97, 47, 61, 53],
    [61, 13, 29],
    [97, 13, 75, 29, 47]]

def wszyst_mozliwosci(tablica):
    nowatablica = []
    for a in range(len(tablica)):
        for b in range(a + 1, len(tablica)):
            nowatablica.append((tablica[a], tablica[b]))
    return nowatablica

def poprawnosc_aktualizacji(tablica):
    pary = wszyst_mozliwosci(tablica)
    for i in range(len(pary)):
        para = pary[i]
        if para not in reguly:
            return False
    return True

def program():
    for i in range(len(aktualizacje)):
        if poprawnosc_aktualizacji(aktualizacje[i]) == True:
            print("tak")
        else:
            print("nie")

program()