import sys

print("Wklej tekst i naciśnij Enter dwukrotnie, aby zakończyć:")
tekst = sys.stdin.read()
tablica = tekst.strip().split('\n')

registery = []
for i in range(0, 3):
    try:
        registery.append(int(tablica[i][12:]))
    except ValueError:
        print(f"Błąd w odczycie rejestru {tablica[i]}")
        sys.exit()

instrukcja, instrukcje = tablica[4][9:]
instrukcje = instrukcja.split(',')

for i in range(len(instrukcje)):

    try: instrukcje[i] = int(instrukcje[i])
    except ValueError: continue
        

dane = {"instrukcja":[], "operand":[]}
for i in range(len(instrukcje)):
    dane["instrukcja"].append(instrukcje[i]) if i % 2 == 0 else dane["operand"].append(instrukcje[i])

for i in range(len(dane["instrukcja"])):

    operand = dane["operand"][i]

    match dane["instrukcja"][i]:
        case 0:
            wynik = registery[0] // (2 ** operand)
            print(f"Instrukcja 0: Rejestr A: {registery[0]} // 2^{operand} = {wynik}")

        case 1:
            wynik = registery[0] * operand
            print(f"Instrukcja 1: Rejestr A: {registery[0]} * {operand} = {wynik}")

        case 2:
            wynik = registery[0] + registery[1]
            print(f"Instrukcja 2: Rejestr A: {registery[0]} + Rejestr B: {registery[1]} = {wynik}")

        case 3:
            wynik = registery[2] - operand
            print(f"Instrukcja 3: Rejestr C: {registery[2]} - {operand} = {wynik}")

        case 4:
            wynik = registery[0] + registery[1] + registery[2]
            print(f"Instrukcja 4: Rejestr A + B + C = {wynik}")

        case 5:
            tekst = f"Instrukcja 5: Rejestr A: {registery[0]} / {operand} = {wynik}"
            tekst_blad = "Instrukcja 5: Błąd, dzielenie przez zero."
            wynik = registery[0] / operand; print(tekst) if operand != 0 else print(tekst_blad)

        case 6:
            wynik = registery[1] % operand
            print(f"Instrukcja 6: Rejestr B: {registery[1]} % {operand} = {wynik}")

        case 7:
            wynik = registery[2] ** operand
            print(f"Instrukcja 7: Rejestr C: {registery[2]} ^ {operand} = {wynik}")

        case _:
            print(f"Nieznana instrukcja: {dane['instrukcja'][i]}")
