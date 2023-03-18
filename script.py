# En los juegos de suma cero, las estrategias minmax inducen equilibrios de Nash

def gt(x, y):
    return x >= y

def lt(x, y):
    return x <= y

def comp(L, R, player):
    func = gt if player == 0 else lt
    return L if func(L[0], R[0]) else R

def solve(util, N, player):
    # Caso base 
    if N == 2:
        left_node = util[0], "L"
        right_node = util[1], "R"
        return comp(left_node, right_node, player)

    H = N // 2

    next_player = (player + 1) % 2

    L = solve(util[0:H], H, next_player)
    R = solve(util[H:N], H, next_player)
    
    chosen = comp(L, R, player) 

    utility = chosen[0]
    path = ("L" if chosen == L else "R") + chosen[1]

    return utility, path 

def test():
    minmax = lambda u: solve(u, len(u), 0)[1]

    a = range(1, 17)

    ans = minmax(a) 

    print(ans)

    b = []
    b.extend(list(map(int, "091001")))
    b.extend(list(map(int, "201911468")))
    b.append(10324)

    ans = minmax(b) 

    print(ans)

test()