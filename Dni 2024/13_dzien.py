def znajdz_minimalny_koszt(x_a, y_a, x_b, y_b, x_p, y_p, max_nacisniecia=100):
    min_koszt = float('inf')
    najlepsze_a, najlepsze_b = None, None

    for a in range(max_nacisniecia + 1):
        for b in range(max_nacisniecia + 1):

            if a * x_a + b * x_b == x_p and a * y_a + b * y_b == y_p:
                koszt = 3 * a + b
                print(koszt)
                if koszt < min_koszt:
                    min_koszt = koszt
                    najlepsze_a, najlepsze_b = a, b

    if min_koszt == float('inf'):
        return None, None, None
    return najlepsze_a, najlepsze_b, min_koszt

xa, ya = 94, 34
xb, yb = 22, 67
xp, yp = 8400, 5400

a, b, koszt = znajdz_minimalny_koszt(xa, ya, xb, yb, xp, yp)

if a is not None:
    print(f"Znaleziona optymalna solucja: Naciśnij A {a} razy, B {b} razy. Całkowity koszt: {koszt} tokenów.")
else:
    print("Brak rozwiązania dla tej maszyny.")
