import networkx as nx

from database.DAO import DAO


class Model:

    def __init__(self):
        self._grafo = nx.Graph()

    def costruisci_grafo(self, anno):
        self._grafo.clear()

        self._stati = DAO.getAllStati(anno)
        self._id_Map_Stati = {}
        for s in self._stati:
            self._id_Map_Stati[s.CCode] = s

        self._confini = DAO.getAllConfini(self._id_Map_Stati, anno)

        self._grafo.add_nodes_from(self._stati)
        for c in self._confini:
            self._grafo.add_edge(c.s1, c.s2)

    def get_num_nodi(self):
        return len(self._grafo.nodes)

    def get_num_archi(self):
        return len(self._grafo.edges)

    def get_nodi(self):
        return list(self._grafo.nodes)

    def get_num_confinanti(self, nodo):
        return len(list(self._grafo.neighbors(nodo)))

    def get_num_comp_conn(self):
        return nx.number_connected_components(self._grafo)

    def get_raggiungibili_DFS(self, nodo):
        albero = nx.dfs_tree(self._grafo, nodo)
        ragg = list(albero.nodes)
        ragg.remove(nodo)

        return ragg

    def get_raggiungibili_BFS(self, nodo):
        albero = nx.bfs_tree(self._grafo, nodo)
        ragg = list(albero.nodes)
        ragg.remove(nodo)

        return ragg

    def get_raggiungibili_ricorsione(self, nodo):
        visitati = []
        self.visita_ricorsiva(nodo, visitati)
        visitati.remove(nodo)

        return visitati

    def visita_ricorsiva(self, nodo, visitati):
        visitati.append(nodo)

        for vicino in self._grafo.neighbors(nodo):
            if vicino not in visitati:
                self.visita_ricorsiva(vicino, visitati)

        pass



