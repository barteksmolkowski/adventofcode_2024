przeplywy = [
    "px{a<2006:qkq,m>2090:A,rfg}",
    "pv{a>1716:R,A}",
    "lnx{m>1548:A,A}",
    "rfg{s<537:gd,x>2440:R,A}",
    "qs{s>3448:A,lnx}",
    "qkq{x<1416:A,crn}",
    "crn{x>2662:A,R}",
    "in{s<1351:px,qqz}",
    "qqz{s>2770:qs,m<1801:hdj,R}",
    "gd{a>3333:R,R}",
    "hdj{m>838:A,pv}"
]

wejscia = [
    "{x=787,m=2655,a=1222,s=2876}",
    "{x=1679,m=44,a=2067,s=496}",
    "{x=2036,m=264,a=79,s=2244}",
    "{x=2461,m=1339,a=466,s=291}",
    "{x=2127,m=1623,a=2188,s=1013}"
]

def OdczytPrzeplywu(przeplyw):
    przeplyw = list(przeplyw)
    kierunek = ''.join(przeplyw[:przeplyw.index("{")])

    przeplyw = list(przeplyw)
    
    kierunek = ''.join(przeplyw[:przeplyw.index("{")])
    
    przeplyw = przeplyw[przeplyw.index("{") + 1:]
    
    przeplyw = ''.join(przeplyw[:-1])
    
    warunki = przeplyw.split(',')
    
    KoncowyWarunek = []

    for warunek in warunki:
        if ':' in warunek:
            czesc_warunku, przeplyw_docelowy = warunek.split(':')
            KoncowyWarunek.append((czesc_warunku, przeplyw_docelowy))
        else:
            KoncowyWarunek.append((warunek, ''))

    return kierunek, KoncowyWarunek

print(OdczytPrzeplywu("qqz{s>2770:qs,m<1801:hdj,R}"))

def Odczyt(wejscie):
    x, m, a, s = 0, 0, 0, 0
    liczba = 0
    wynik = 0
    linia = list(wejscie)
    
    for i in range(len(linia)):
        try:
            liczba = liczba * 10 + int(linia[i])
        except ValueError:
            match wynik:
                case 0: x = liczba
                case 1: m = liczba
                case 2: a = liczba
                case 3: s = liczba
                   
            liczba = 0
            wynik += 1
    
    if wynik == 3:
        s = liczba

    return x, m, a, s

def Przeplyw(x, m, a, s):
    for i in range(len(przeplywy)):
        przeplyw = przeplywy[i]
