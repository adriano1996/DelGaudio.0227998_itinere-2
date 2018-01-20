# prova_in_itinere_2

DESCRIZIONE ALGORITMO
La funzione camminiMinBFS restituisce i cammini minimi tra tutte le coppie di vertici del grafo, ma a differenza della normale visita in ampiezza, prende in input due vertici, tra i quali trova il cammino più breve.
La funzione mediumNode restituisce una lista dove sono presenti tutti i medi dei cammini più brevi tra ogni coppia di nodi del grafo, richiamando la funzione camminiMinBFS per ogni coppia di vertici.
La funzione mediodeimedi, data come input la lista dei medi trovata tramite mediumNode, calcola la moda, ovvero il nodo che è medio per il maggior numero di cammini, dando la soluzione del problema assegnato.
La funzione prova è  la funzione per far partire tutto il programma, passandogli in input un grafo come dizionario.

ANALISI TEMPI DI ESECUZIONE TEORICA
La funzione camminiMinBFS ha tempo di esecuzione O(n+m).
La funzione mediumNode ha tempo di esecuzione O(n*3(n+m)).
La funzione mediodeimedi ha tempo di esecuzione O(n*2).
La funzione prova ha quindi costo O(n*3(n+m)+ n*2).

TEMPI SPERIMENTALE 
graf : ~0.00028776376761460184 sec
graf2: ~7.450686717630381e-05 sec
graf3: ~0.0003364213135256573 sec

Notiamo che più il grafo ha nodi più tempo impiega l'algoritmo mentre il numero di archi è poco influente.
L'algortmo va quindi bene per grafi con molti archi 
