import random

def losuj():
    return [
        random.randint(1, 12),  # czerwone
        random.randint(1, 13),  # zielone
        random.randint(1, 14),  # niebieskie
    ]

gry = 12 * 13 * 14
udane_gry = set()  # Użyj zestawu, aby uniknąć duplikatów
max_proby = 50000  # Limit prób, aby uniknąć nieskończonej pętli
proby = 0

while len(udane_gry) < gry and proby < max_proby:
    gra = tuple(losuj())  # Tupla jest hashowalna, więc może być użyta w zestawie
    udane_gry.add(gra)
    proby += 1

print(f"Wygenerowano {len(udane_gry)} unikalnych gier w {proby} próbach")