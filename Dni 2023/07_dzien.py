gry = {
    "32T3K": "765",
    "T55J5": "684",
    "KK677": "28",
    "KTJJT": "220",
    "QQQJA": "483"
}

def PoliczZnaki(tekst):
    znaki = {}
    for i in tekst:
        if i not in znaki:
            znaki[i] = 1
        else:
            znaki[i] += 1
    print(znaki)

def Rozpoznaj(gra):
    
    return nazwa # Same5, Same4, Full (11122), trójka, para, różne