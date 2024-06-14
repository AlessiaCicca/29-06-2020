import networkx as nx

from database.DAO import DAO


class Model:
    def __init__(self):
        self.grafo = nx.Graph()
        self.match=DAO.getMatch()
        self.dict={}
        self._idMap = {}
        for v in self.match:
            self._idMap[v.MatchID] = v
        self._solBest = []
        self._costBest = 0
        self._idMapMese = {"Gennaio":1,"Febbraio":2,"Marzo":3,"Aprile":4,"Maggio":5,"Giugno":6,"Luglio":7,"Agosto":8,
                           "Settembre":9,"Ottobre":10,"Novembre":11,"Dicembre":12}




    def creaGrafo(self, mese,minuti):
        self.nodi = DAO.getNodi(self._idMapMese[mese])
        self.grafo.add_nodes_from(self.nodi)

        self.addEdges(minuti)
        return self.grafo

    def addEdges(self, minuti ):
         self.grafo.clear_edges()
         allEdges = DAO.getConnessioni(minuti)
         for connessione in allEdges:
             nodo1 = self._idMap[connessione.m1]
             nodo2 = self._idMap[connessione.m2]
             if nodo1 in self.grafo.nodes and nodo2 in self.grafo.nodes:
                 if self.grafo.has_edge(nodo1, nodo2) == False:
                     #peso = DAO.getPeso(forma, anno, connessione.v1, connessione.v2)
                     self.grafo.add_edge(nodo1, nodo2, weight=connessione.peso)

    def getNumNodes(self):
        return len(self.grafo.nodes)

    def getNumEdges(self):
        return len(self.grafo.edges)
    def connessione(self):
        for arco in self.grafo.edges:
            self.dict[arco]=self.grafo[arco[0]][arco[1]]["weight"]
        dictOrder=list(sorted(self.dict.items(), key=lambda item: item[1], reverse=True))

        return dictOrder[0]

    def getBestPath(self,codm1,codm2):
       m1=self._idMap[int(codm1)]
       m2 = self._idMap[int(codm2)]
       dizio=[]
       for cammino in list(nx.all_simple_paths(self.grafo,m1,m2)):
           peso=0
           for i in range(0,len(cammino)-1):
               peso+=self.grafo[cammino[i]][cammino[i+1]]["weight"]
           dizio.append((cammino,peso))
       dictOrder = (sorted(dizio, key=lambda x: x[1], reverse=True))
       for cam,peso in dictOrder:
           print(cam,peso)
           if self.ammissibile(cam):
               return cam,peso
    def ammissibile(self, listanodi):
        okay=True
        lista=[]
        for i in range( len(listanodi) - 1):
            nodoIarco=listanodi[i]
            nodoFarco=listanodi[i+1]
            if (((nodoIarco.TeamHomeID==nodoFarco.TeamHomeID) and (nodoIarco.TeamAwayID==nodoFarco.TeamAwayID))
                or ((nodoIarco.TeamHomeID==nodoFarco.TeamAwayID) and (nodoIarco.TeamAwayID==nodoFarco.TeamHomeID))):
                okay=False
        for i in range( len(listanodi) - 1):
            if listanodi[i] not in lista:
                lista.append(listanodi[i])
            else:
                okay=False
        return okay






