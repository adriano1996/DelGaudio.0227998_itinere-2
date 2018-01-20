"""
file name: prova_in_itinere_2

autori:
Del Gaudio Adrinao  0227998
Magnoni Flavia      0228318

V. python: 3,6

soluzione proposta per il problema n2 della prova in itinere di ingegneria degli algoritmi (2017/2018)
trova il nodo che è medio per la maggior parte dei cammini più brevi tra tutte le coppie di un grafo
"""


def camminiMinBFS(graph, inizio, fine):
    # mantiene traccia dei nodi esplorati
    explored = []
    # mantine traccia dei cammini da controllare
    queue = [[inizio]]
    # return lo stesso nodo in caso di cammino su se stesso
    if inizio == fine:
        return inizio

    # finchè ci sono cammini da controllare continua a fare il while
    while queue:
        path = queue.pop(0)
        node = path[-1]
        if node not in explored:
            adiacenti = graph[node]
            # esploro gli adiacenti, costruisco il nuovo cammino (new_path) e
            # lo inserisco in coda
            for X in adiacenti:
                new_path = list(path)
                new_path.append(X)
                queue.append(new_path)
                if X == fine:
                    return new_path

            # segna il nodo come esplorato
            explored.append(node)

    # in caso che il cammino non esista
    return "nessun cammino disponibile"

def mediumNode(graph):
    listOfMedium = []

    for s in graph:
        for d in graph:
            dist = camminiMinBFS(graph, s, d)
            l=[]
            if (len(dist)) % 2 == 1:
              for i in range (0, len(dist)):
                 l.append(dist[i])
                 a=int (len(l)/2)
              listOfMedium.append(l[a])
    print ('la lista dei medi è:',(listOfMedium))
    return listOfMedium




def mediodeimedi(list):
    #calcola la moda dei medi
    # param list: è la lista dei medi
    moda= None
    freq_mod= 0
    L=int(len(list))
    for i in range (0,L):
        cont=0
        for x in range(0,L):
            if list[i]==list[x]:
                cont+=1
        if cont> freq_mod:
            freq_mod= cont
            moda=list[i]
    return moda



if __name__ == '__main__':

   #grafo di prova dato come dizionario chiave: valore (il valore è la lista dei nodi adiacenti)
    graph = {'A': ['B', 'C', 'E'],
             'B': ['A', 'D', 'E'],
             'C': ['A', 'F', 'G'],
             'D': ['B','E','G','H'],
             'E': ['A', 'B', 'D'],
             'F': ['C'],
             'G': ['C','D','H'],
             'H': ['D','G']}


    A=mediumNode(graph)
    print ('il nodo medio per il maggior numero di coppie è:',mediodeimedi(A))





