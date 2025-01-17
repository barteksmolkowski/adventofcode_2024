import numpy as np

Dane = [
    "1,0,1~1,2,1",
    "0,0,2~2,0,2",
    "0,2,3~2,2,3",
    "0,0,4~0,2,4",
    "2,0,5~2,2,5",
    "0,1,6~2,1,6",
    "1,1,8~1,1,9" # z lewej należy odczytać (x czy y) i do odpoiedniej tabeli (xz lub yz)
]                 # wprowadzić na odpowiednim wierszu (z) (różnica* "#") 
# xxxxxxx
# 0 0 0 9z
# 0 0 0 8z   xxxxx     yyyyy
# 0 0 0 7z   0 1 0z    1 1 1z
# 0 0 0 6z   0 1 2     0 1 2
# 0 0 0 5z
# 0 0 0 4
# 0 0 0 3
# 0 0 0 2
# 0 0 0 1
# 0 0 0 0

# yyyyyyy
# 0 0 0 9z
# 0 0 0 8z
# 0 0 0 7z
# 0 0 0 6z
# 0 0 0 5z
# 0 0 0 4
# 0 0 0 3
# 0 0 0 2
# 0 0 0 1
# 0 0 0 0

def OdczytajDane(Danetxt):
    tab1, tab2 = {}, {}
    for i in range(len(Danetxt)):
        grupy = Danetxt[i].split("~")
        Nowatab = list(map(int, grupy[0].split(',')))
        Nowatab2 = list(map(int, grupy[1].split(',')))

        tab1[Nowatab[2]] = (Nowatab[0], Nowatab[1])
        tab2[Nowatab2[2]] = (Nowatab2[0], Nowatab2[1])
    
    return tab1, tab2

def StwórzTab(slownik):
    wys = max(slownik.keys())
    tabX, tabY = [], []
    for i in slownik.keys():
        tabX.append(slownik[i][0])
        tabY.append(slownik[i][1])
    szerX, szerY = max(tabX), max(tabY)
    tab1 = np.zeros((wys, szerX + 1))
    tab2 = np.zeros((wys, szerY + 1))

    return tab1, tab2

tablica1, tablica2 = OdczytajDane(Dane)
print(tablica1)
print("\n")
print(tablica2); print("\n")
tablica1, tablica2 = StwórzTab(tablica1), StwórzTab(tablica2)
for i in range(len(tablica1)):
    print(tablica1[i])
print("\ndruga:")
for i in range(len(tablica2)):
    print(tablica2[i])
