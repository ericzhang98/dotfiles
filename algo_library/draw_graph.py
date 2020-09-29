def draw(weights):
    import networkx as nx
    G = nx.Graph()
    for v in weights:
        G.add_node(v)
    for v in weights:
        for u, w in weights[v].items():
            G.add_edge(v, u, weight=w)

    import matplotlib.pyplot as plt
    pos = nx.spring_layout(G, seed=0)
    labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_nodes(G, pos, node_size=500)
    nx.draw_networkx_labels(G, pos, font_size=20, font_family="sans-serif")
    nx.draw_networkx_edges(G, pos, edgelist=G.edges(data=True), width=1)
    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
    plt.show()
