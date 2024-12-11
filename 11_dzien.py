tab = [125, 17]
n_tab = []

def usun_poprzednie():
    print("\n" * 10)

def update():
    local_n_tab = []
    for i in tab:
        if i == 0:
            local_n_tab.append(1)
        elif len(str(i)) % 2 == 0:
            srodek = len(str(i)) // 2
            lewa = int(str(i)[:srodek])
            prawa = int(str(i)[srodek:])
            local_n_tab.append(lewa)
            local_n_tab.append(prawa)
        else:
            local_n_tab.append(i * 2024)
    return local_n_tab
x = 1
while x <= 25:
    tab = update()
    usun_poprzednie()
    print(f"Liczba {x}: ")
    print(tab)
    x += 1
print(f"\nDługość wyniku: {len(tab)}")

