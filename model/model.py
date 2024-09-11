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
            self._id_Map_Stati[s.CCcode] = s

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
        return len(self._grafo.neighbors(nodo))

    def get_num_comp_conn(self):
        return nx.number_connected_components(self._grafo)





