import csv
import math
class grafo:
   def __init__(self, matriz,ids):
    self.matriz = matriz
    self.ids = ids


def lerCSV(caminho):
    matriz = []
    with open(caminho) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        ids = csv_reader.__next__()
        ids.pop(0)
        for row in csv_reader:
            aux = []
            for a in row[1:]:
                if(a=="i"):
                    aux.append(math.inf)
                else:
                    aux.append(int(a))
            matriz = matriz + [aux]
    return grafo(matriz, ids)


def floydWarshal(grafo):
    d = []
    p = []
    for i in grafo.matriz:
        d.append([math.inf]*len(grafo.matriz))
        p.append([-1]*len(grafo.matriz))
    
    for i in range(len(grafo.matriz)):
        for j in range(len(grafo.matriz)):
            if(i == j):
                d[i][i] = 0
            elif(grafo.matriz[i][j] != math.inf):
                d[i][j] = grafo.matriz[i][j]
                
    for k in range(len(grafo.matriz)):
        for i in range(len(grafo.matriz)):
            for j in range(len(grafo.matriz)):
                if(d[i][j]> d[i][k] + d[k][j]):
                    d[i][j] = d[i][k] + d[k][j]
                    p[i][j] = k
                    
    print(d)
    print(p)
    printDistances(d, p, grafo)


def printDistances(distance, previous, grafo):
    for i in range (len(distance)):
        print("\n**********************************************")
        print("Distancias a partir do vertice ", grafo.ids[i], end="\n\n")
        for j in range (len(distance)):
            if(i == j):
                continue

            print("Vertice", grafo.ids[i],"=>",grafo.ids[j],"=", distance[i][j], end="\n\n")
            x = i
            print(grafo.ids[x], " => ", end="")
            while(previous[x][j] != -1):
                print(grafo.ids[previous[x][j]], " => ", end="")
                x = previous[x][j]
            print(grafo.ids[j])
            print("-----------------------------------------------")




grafo = lerCSV("Ativ 11\Atividade 11 - Grafo.csv")
floydWarshal(grafo)