def dist_manhattan(origem, destino):
    x1, y1 = origem
    x2, y2 = destino
    return abs((x1 - x2) + (y1 - y2))

def dest_euclidiana(origem, destino):
    x1, y1 = origem
    x2, y2 = destino
    return (((x1 - x2) ** 2) + ((y1 - y2) ** 2)) ** (1 / 2)

def menor_dist(lst_origens, lst_destinos):
    import sys
    menorD = sys.maxsize # <= infinito
    menores = []
    for v in lst_origens:
        for w in lst_destinos:
            d = dist_manhattan(v, w)
            if (d < menorD):
                menorD = d
                menores = [v, w]
    return menores

lst_origens = [(1,1), (1,2), (2,1), (2,2)]
lst_destinos = [(400,400), (4,5), (5,4), (5,5)]

print(menor_dist(lst_origens, lst_destinos))
