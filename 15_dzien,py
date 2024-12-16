tablica = [
    list("##########"),
    list("#..O..O.O#"),
    list("#......O.#"),
    list("#.OO..O.O#"),
    list("#..O@..O.#"),
    list("#O#..O...#"),
    list("#O..O..O.#"),
    list("#.OO.O.OO#"),
    list("#....O...#"),
    list("##########")
]

zasady = "<vv>^<v^>v>^vv^v>v<>v^v<v<^vv<<<^><<><>>v<vvv<>^v^>^<<<><<v<<<v^vv^v>^"\
         "vvv<<^>^v^^><<>>><>^<<><^vv^^<>vvv<>><^^v>^>vv<>v<<<<v<^v>^<^^>>>^<v<v"\
         "><>vv>v^v^<>><>>>><^^>vv>v<^^^>>v^v^<^^>v^^>v^<^v>v<>>v^v^<v>v^^<^^vv<"\
         "<<v<^>>^^^^>>>v^<>vvv^><v<<<>^^^vv^<vvv>^>v<^^^^v<>^>vvvv><>>v^<<^^^^^"\
         "^><^><>>><>^^<<^^v>>><^<v>^<vv>>v>>>^v><>^v><<<<v>>v<v<v>vvv>^<><<>^><"\
         "^>><>^v<><^vvv<^^<><v<<<<<><^v<<<><<<^^<v<^^^><^>>^<v^><<<^>>^v<v^v<v^"\
         ">^>>^v>vv>^<<^v<>><<><<v<<v><>v<^vv<<<>^^v^>^^>>><<^v>>v^v><^^>>^<>vv^"\
         "<><^^>^^^<><vvvvv^v<v<<>^v<v>v<<^><<><<><<<^^<<<^<<>><<><^^^>^^<>^>v<>"\
         "^^>vv<^v^v<vv>^<><v<^v>^^^>>>^^vvv^>vvv<>>>^<^>>>>>^<<^v>^vvv<>^<><<v>"\
         "v^^>>><<^^<>>^v^<v^vv<>v^<<>^<^v^v><^<<<><<^<v><v<>vv>>v><v^<vv<>v^<<^"

kierunki = {"^": (-1, 0), ">": (0, 1), "v": (1, 0), "<": (0, -1)}

def ZnajdzGracza():
    for i in range(len(tablica)):
        for j in range(len(tablica[i])):
            if tablica[i][j] == "@":
                return i, j
    return None

def czy_mozna_ruch(x, y, nx, ny):
    if 0 <= nx < len(tablica) and 0 <= ny < len(tablica[0]):
        return tablica[nx][ny] in [".", "O"]
    return False

def ruch(x, y, kierunek):
    dx, dy = kierunki[kierunek]
    nx, ny = x + dx, y + dy
    
    if czy_mozna_ruch(x, y, nx, ny):
        if tablica[nx][ny] == ".":
            tablica[nx][ny], tablica[x][y] = "@", "."
            return True
        
        elif tablica[nx][ny] == "O":
            nnx, nny = nx + dx, ny + dy
            if czy_mozna_ruch(nx, ny, nnx, nny) and tablica[nnx][nny] == ".":
                tablica[nnx][nny], tablica[nx][ny] = "O", "@"
                tablica[x][y] = "."
                return True
    return False

def oblicz_gps():
    suma_gps = 0
    for i in range(len(tablica)):
        for j in range(len(tablica[i])):
            if tablica[i][j] == "O":
                gps = i * 100 + j
                suma_gps += gps
    return suma_gps

for krok in zasady:
    x, y = ZnajdzGracza()
    if x is not None and y is not None and krok in kierunki:
        ruch(x, y, krok)

print("Suma GPS:", oblicz_gps())

