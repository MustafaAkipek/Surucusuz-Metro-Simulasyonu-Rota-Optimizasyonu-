import matplotlib.pyplot as plt # Grafik çizimi için kullanıldı
import networkx as nx # Graph' ı görselleştirmek için kullanıldı

G = nx.Graph() # Graph oluşturuldu

def show_graph(G):
    # Düğümler eklendi
    G.add_nodes_from([
        ("K1", {"name": "Kızılay", "line": "Kırmızı Hat"}),
        ("K2", {"name": "Ulus", "line": "Kırmızı Hat"}),
        ("K3", {"name": "Demetevler", "line": "Kırmızı Hat"}),
        ("K4", {"name": "OSB", "line": "Kırmızı Hat"}),
        ("M1", {"name": "AŞTİ", "line": "Mavi Hat"}),
        ("M2", {"name": "Kızılay", "line": "Mavi Hat"}),
        ("M3", {"name": "Sıhhiye", "line": "Mavi Hat"}),
        ("M4", {"name": "Gar", "line": "Mavi Hat"}),
        ("T1", {"name": "Batıkent", "line": "Turuncu Hat"}),
        ("T2", {"name": "Demetevler", "line": "Turuncu Hat"}),
        ("T3", {"name": "Gar", "line": "Turuncu Hat"}),
        ("T4", {"name": "Keçiören", "line": "Turuncu Hat"})
    ])

    # Kenarlar eklendi
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
        
        ("K1", "M2", {"weight": 2}), # Aktarma bulunuyor
        ("K3", "T2", {"weight": 3}), # Aktarma bulunuyor
        ("M4", "T3", {"weight": 2})  # Aktarma bulunuyor
    ])

    # Hat renkleri
    line_colors = {
        "Kırmızı Hat": "red", 
        "Mavi Hat": "blue",
        "Turuncu Hat": "orange"
    }

    # Kenar renklerini belirle
    edge_colors = []
    for u, v, d in G.edges(data=True):
        line_u = G.nodes[u]["line"]
        line_v = G.nodes[v]["line"]
        if line_u == line_v:
            edge_colors.append(line_colors[line_u])  # Hattın rengi(ör: hattın özelliği kırmızı ise kırmızı rengini listeye ekleyecek)
        else:
            edge_colors.append("gray")  # Aktarma noktaları gri olsun

    # Düğümlerin konumları
    pos = {
        "K1": (5.5, 6.6),
        "K2": (5.0, 5.0),
        "K3": (5.0, 3.4),
        "K4": (5.0, 0.2),
        "M1": (6.5, 6.6),
        "M2": (6.0, 5.0),
        "M3": (6.0, 3.4),
        "M4": (5.8, 1.8),
        "T1": (4.0, 5.0),
        "T2": (4.0, 3.4),
        "T3": (4.0, 1.8),
        "T4": (4.0, 0.2)
    }

    pos_node_attributes = {} # Düğümlerin etiketlerini düzenlemek için kullanılacak özellikler
    for node, (x, y) in pos.items(): # Düğümlerin etiketlerinin konumlarını düzenler
        pos_node_attributes[node] = (x + 0.150 , y + 0.150) # Düğüm etiketlerini konumunu düzenler(sağ üst köşede olacak şekilde)

    node_labels = {n: (d.get("name", ""), d.get("line", "")) for n, d in G.nodes(data=True)} # Düğümlerin etiketlerini çağırmak için kullanıldı(etiket yoksa boş string döndürecek)
    edge_labels = {(u, v): d.get("weight", "") for u, v, d in G.edges(data=True)} # Kenarların etiketlerini çağırmak için kullanıldı(ağırlık yoksa boş string döndürecek)

    # Graf çizimi
    nx.draw(G, pos=pos, with_labels=True,
            node_color="pink", node_size=1500,
            font_color="black", font_size=12, font_family="Times New Roman", font_weight="bold",
            edge_color=edge_colors,  # Kenar renklerini ekledik!
            width=5)


    # Düğümlerin etiketleri ve kenarların etiketleri çizildi
    nx.draw_networkx_labels(G, pos = pos_node_attributes, labels = node_labels, font_color = "black", font_size = 10, font_family = "Times New Roman", font_weight="bold")
    nx.draw_networkx_edge_labels(G, pos = pos, edge_labels = edge_labels, label_pos = 0.5)

    # Grafik gösterildi
    plt.show()