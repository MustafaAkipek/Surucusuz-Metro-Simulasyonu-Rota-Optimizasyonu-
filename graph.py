import matplotlib.pyplot as plt
import networkx as nx

G = nx.Graph() # Create a graph

# Add nodes
G.add_nodes_from([
    ("K1", {"name": "Kızılay", "hat": "Kırmızı Hat"}),
    ("K2", {"name": "Ulus", "hat": "Kırmızı Hat"}),
    ("K3", {"name": "Demetevler", "hat": "Kırmızı Hat"}),
    ("K4", {"name": "OSB", "hat": "Kırmızı Hat"}),
    ("M1", {"name": "AŞTİ", "hat": "Mavi Hat"}),
    ("M2", {"name": "Kızılay", "hat": "Mavi Hat"}),
    ("M3", {"name": "Sıhhiye", "hat": "Mavi Hat"}),
    ("M4", {"name": "Gar", "hat": "Mavi Hat"}),
    ("T1", {"name": "Batıkent", "hat": "Turuncu Hat"}),
    ("T2", {"name": "Demetevler", "hat": "Turuncu Hat"}),
    ("T3", {"name": "Gar", "hat": "Turuncu Hat"}),
    ("T4", {"name": "Keçiören", "hat": "Turuncu Hat"})
])

G.add_edges_from([
    ("K1", "K2", {"weight": 4}),
    ("K2", "K3", {"weight": 6}),
    ("K3", "K4", {"weight": 8}),
    ("M1", "M2", {"weight": 5}),
    ("M2", "M3", {"weight": 3}),
    ("M3", "M4", {"weight": 4}),
    ("T1", "T2", {"weight": 7}),
    ("T2", "T3", {"weight": 9}),
    ("T3", "T4", {"weight": 5}),
    ("K1", "M2", {"weight": 2}),
    ("K3", "T2", {"weight": 3}),
    ("M4", "T3", {"weight": 2})
])

pos = {
    "K1": (4.5, 6.6),
    "K2": (3.0, 5.0),
    "K3": (3.0, 3.4),
    "K4": (3.0, 0.8),
    "M1": (8.0, 6.6),
    "M2": (6.5, 5.0),
    "M3": (6.5, 3.4),
    "M4": (6.5, 1.8),
    "T1": (0.5, 5.0),
    "T2": (0.5, 3.4),
    "T3": (0.5, 1.8),
    "T4": (0.5, 0.2)
}

pos_node_attributes = {}
for node, (x, y) in pos.items():
    pos_node_attributes[node] = (x - 0.5 , y + 0.2)    

node_labels = {n:(d["name"], d["hat"]) for n, d in G.nodes(data=True)}
edge_labels = {(u, v): d["weight"] for u, v, d in G.edges(data=True)}

nx.draw(G, pos=pos, with_labels=True,
        node_color = "red", node_size = 1500,
        font_color = "white", font_size = 20, font_family = "Times New Roman", font_weight="bold",
        edge_color = "lightgray",
        width = 5)


nx.draw_networkx_labels(G, pos = pos_node_attributes, labels = node_labels, font_color = "black", font_size = 10, font_family = "Times New Roman", font_weight="bold")
nx.draw_networkx_edge_labels(G, pos = pos, edge_labels = edge_labels, label_pos = 0.5)
plt.show()