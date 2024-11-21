import osmnx as ox
import matplotlib.pyplot as plt

if __name__ == "__main__":

    print(ox.__version__)
    G_full = ox.graph_from_place(
        "Garching, Bavaria, Germany", network_type="drive", simplify=False
    )
    G_simple = ox.simplify_graph(G_full, edge_attrs_differ="name")

    gdf_nodes, gdf_edges = ox.graph_to_gdfs(G_simple)

    fig, ax = ox.plot_graph(G_full)
    plt.savefig("Garching-OSMNX-full.pdf")
    fig, ax = ox.plot_graph(G_simple)
    plt.savefig("Garching-OSMNX-simple.pdf")
