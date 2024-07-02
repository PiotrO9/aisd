import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()

G.add_nodes_from([1,2,3,4,5,6])

G.add_edge(2, 1)
G.add_edge(2, 3)
G.add_edge(1, 2)
G.add_edge(1, 3)
G.add_edge(1, 5)
G.add_edge(3, 2)
G.add_edge(3, 1)
G.add_edge(3, 5)
G.add_edge(3, 4)
G.add_edge(5, 1)
G.add_edge(5, 3)
G.add_edge(5, 4)
G.add_edge(5, 6)
G.add_edge(4, 3)
G.add_edge(4, 5)
G.add_edge(4, 6)
G.add_edge(6, 4)
G.add_edge(6, 5)

nx.draw(G, with_labels=True)
print(nx.to_numpy_array(G))

tmp = nx.to_dict_of_dicts(G)

for wierzcholek, sasiedzi in tmp.items():
    print(f'{wierzcholek}: {", ".join(map(str, sasiedzi))}')

plt.savefig("zad1.png")

