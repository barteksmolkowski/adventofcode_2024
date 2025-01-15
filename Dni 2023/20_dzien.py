import re

dane = [
    "broadcaster -> cz, gm, jn, ts",
    "%nr -> hq",
    "%xk -> sn",
    "%cl -> xk",
    "%mj -> dq, qr",
    "%gm -> lk, cl",
    "%mv -> lz, rr",
    "&qr -> cz, sp, lb, xt, fx",
    "%xt -> vl",
    "&dd -> rx",
    "%rv -> qr",
    "%ts -> lz, nk",
    "%vl -> zj, qr",
    "%qm -> db, lk",
    "%sn -> lp",
    "%xc -> lz",
    "%jn -> sz, ft",
    "%vg -> lk, ks",
    "%hq -> ft, lh",
    "&lz -> gx, xn, jq, fb, ts, rr",
    "%nk -> mv, lz",
    "&nx -> dd",
    "&sp -> dd",
    "%jj -> qr, mj",
    "%sz -> nr, ft",
    "%rn -> qm",
    "%cz -> xt, qr",
    "%fr -> ft",
    "%vb -> lz, xn",
    "%fb -> vb",
    "%hd -> lz, xc",
    "%gx -> fb",
    "%db -> mh, lk",
    "&ft -> jx, nx, lh, pc, nr, jn, kr",
    "%qc -> pl, ft",
    "%fx -> bz",
    "%jx -> kr",
    "%pl -> ft, fr",
    "%lh -> jx"
]

SlownikWartosci = {}

for linia in dane:
    linia = linia.lstrip()
    
    match linia[0]:
        case "b":
            linia = linia[15:]
            wartosci = linia.split(",")
            Nwartosci = [w.strip() for w in wartosci]
         
            for wartosc in Nwartosci:
                SlownikWartosci[wartosc] = 1

        case "%":
            czynnik = linia[1]
            zmiany = linia[(linia.index(">")) + 1:].split(",")
            zmiany = [z.strip() for z in zmiany]
            
            for zmiana in zmiany:
                if zmiana == "inv" and zmiana not in SlownikWartosci:
                    SlownikWartosci[zmiana] = []
                
                if zmiana != "inv":
                    SlownikWartosci[zmiana] = 2 if SlownikWartosci.get(czynnik, 0) in [0, 1] else 1
                else:
                    SlownikWartosci[zmiana].append(czynnik)

        case "&":
            czynnik = linia[1]
            zmiany = linia[(linia.index(">")) + 1:].split(",")
            zmiany = [z.strip() for z in zmiany]

            for zmiana in zmiany:
                if czynnik in SlownikWartosci and isinstance(SlownikWartosci[czynnik], list):
                    wszystkie_wysokie = True
                    for wejscie in SlownikWartosci[czynnik]:
                        if SlownikWartosci.get(wejscie, 0) != 2:
                            wszystkie_wysokie = False
                            break
                    SlownikWartosci[zmiana] = 1 if wszystkie_wysokie else 2

print("Stan wartości po przetworzeniu danych:")
for klucz, wartosc in SlownikWartosci.items():
    print(f"{klucz}: {wartosc}")

liczba_niskich_impulsow = sum(1 for v in SlownikWartosci.values() if v == 2)
liczba_wysokich_impulsow = sum(1 for v in SlownikWartosci.values() if v == 1)

print(f"Liczba niskich impulsów: {liczba_niskich_impulsow}")
print(f"Liczba wysokich impulsów: {liczba_wysokich_impulsow}")

iloczyn = liczba_niskich_impulsow * liczba_wysokich_impulsow
print(f"Iloczyn niskich i wysokich impulsów: {iloczyn}")
