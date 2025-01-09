def Ascii(tablica):
    suma = 0
    for i in range(len(tablica)):
        wynik = 0
        for znak in tablica[i]:
            wynik += ord(znak)
            wynik *= 17
            wynik %= 256
        suma += wynik
    return suma

tekst = "dm=4,rx=5,hh-,kms=8,qrqh=5,ptxhg-,ckhp=2,qq-,cdzffg=6,dzlzq-"

tablica = tekst.split(",")
wynik = Ascii(tablica)
print(wynik)