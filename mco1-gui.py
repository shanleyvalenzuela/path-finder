import networkx as nx
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import ttk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from csintsy_mco1 import heuristic_search, get_heuristic

labels = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'AA', 'AB', 'AC', 'AD', 'AE', 'AF', 'AG', 'AH', 'AI', 'AJ', 'AK', 'AL', 'AM', 'AN', 'AO', 'AP', 'AQ', 'AR', 'AS', 'AT', 'BA', 'BB', 'BC', 'BD']
adjacency_matrix = [
    #A,B,C,D,E,F,G,H,I,J,K,L,M,AA,AB,AC,AD,AE,AF,AG,AH,AI,AJ,AK,AL,AM,AN,AO,AP,AQ,AR,AS,AT,BA,BB,BC,BD
    [0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,49],  # A
    [0,0,0,0,0,0,75,0,83,0,0,70,0,0,0,0,0,0,1,1,0,0,1,1,0,0,0,0,0,1,0,0,0,0,0,0,0],  # B
    [0,0,0,0,0,0,0,280,0,0,0,0,52,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],  # C
    [0,0,0,0,0,0,140,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],  # D
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,36,0,0],  # E
    [0,0,0,0,0,0,180,190,0,0,0,200,110,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],  # F
    [0,75,0,140,0,180,0,0,97,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],  # G
    [0,0,280,0,0,190,0,0,0,0,0,0,400,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,110,0,0,0,0,0,0,0,0],  # H
    [0,83,0,0,0,0,97,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,51,0,0],  # I
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,39],  # J
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,140],  # K
    [0,70,0,0,0,200,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,61,0,0],  # L
    [0,0,52,0,0,110,0,400,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],  # M
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0],  # AA
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0],  # AB
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0],  # AC
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,19],  # AD
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0],  # AE
    [0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],  # AF
    [0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],  # AG
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0],  # AH
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0],  # AI
    [0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],  # AJ
    [0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],  # AK
    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],  # AL
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0],  # AM
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0],  # AN
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0],  # AO
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,110,0],  # AP
    [0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],  # AQ
    [0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],  # AR
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0],  # AS
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0],  # AT
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,1,1,0,0,0,1,1,0,0,0,0,1,0,0,1,0,0],  # BA
    [0,0,0,0,1,0,0,0,1,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,1,1],  # BB
    [0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,1,0,1,0,0,0,0,0,0,0,0,0,1,0,0,0,0,1,0,1,0,0],  # BC
    [1,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0]  # BD
]
G = nx.DiGraph()
for i, src in enumerate(labels):
    for j, dst in enumerate(labels):
        weight = adjacency_matrix[i][j]
        if weight > 0:
            G.add_edge(src, dst, weight=weight)

def run_gui():
    def draw_graph(path=None):
        ax.clear()
        pos = {
            "A": (12, -5), "B": (-3, 1), "C": (-12, -1), "D": (-6, 0), "E": (3, -3), "F": (-8, -7),
            "G": (-6, -2), "H": (-13, -6), "I": (-1, -2), "J": (12, 0), "K": (10, 0), "L": (-4, -6), "M": (-8, -1),
            "AA": (-2, -7), "AB": (3, 4), "AC": (-1, -7), "AD": (15, -3), "AE": (0, -7),
            "AF": (-7, 3), "AG": (-5.5, 3), "AH": (4, 4), "AI": (5, 4), "AJ": (-4, 3),
            "AK": (-2.5, 3), "AL": (12, -7), "AM": (6, 4), "AN": (7, 4), "AO": (1, -7),
            "AP": (-15, -4), "AQ": (-1, 3), "AR": (12, 4), "AS": (8, 4), "AT": (2, -7),
            "BA": (5, 0), "BB": (2, -1), "BC": (1, -5), "BD": (9, -2)
        }

        node_colors = []
        for node in G.nodes():
            if node in ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M"]:
                node_colors.append("lightgreen")  # Food stalls
            elif node in ["AA", "AB", "AC", "AD", "AE", "AF", "AG", "AH", "AI", "AJ", "AK", "AL", "AM", "AN", "AO", "AP", "AQ", "AR", "AS", "AT"]:
                node_colors.append("deepskyblue")  # Entrances
            else:
                node_colors.append("white")  # Main connectors (e.g., BB, BD, BA, BC)

        nx.draw(G, pos, ax=ax, with_labels=True, node_color=node_colors, edgecolors='black', node_size=400)

        nx.draw_networkx_edge_labels(
            G,
            pos,
            edge_labels={(u, v): d['weight'] for u, v, d in G.edges(data=True)},
            ax=ax,
            font_color='black',
            bbox=None 
        )

        if path:
            path_edges = list(zip(path, path[1:]))
            nx.draw_networkx_nodes(G, pos, nodelist=path, node_color='yellow', edgecolors='black', ax=ax)
            nx.draw_networkx_edges(G, pos, edgelist=path_edges, edge_color='yellow', width=3, ax=ax)


        canvas.draw()

    def find_path():
        start = start_var.get()
        end = end_var.get()
        try:
            heuristic = get_heuristic(end)
            path = heuristic_search(start, end)
            draw_graph(path)
        except nx.NetworkXNoPath:
            draw_graph()
            print(f"No path between {start} and {end}")

    window = tk.Tk()
    window.title("Graph Path Finder")

    frame = tk.Frame(window)
    frame.pack()

    tk.Label(frame, text="Start:").grid(row=0, column=0)
    start_var = tk.StringVar(value=labels[0])
    start_menu = ttk.Combobox(frame, textvariable=start_var, values=labels)
    start_menu.grid(row=0, column=1)

    tk.Label(frame, text="End:").grid(row=0, column=2)
    end_var = tk.StringVar(value=labels[-1])
    end_menu = ttk.Combobox(frame, textvariable=end_var, values=labels)
    end_menu.grid(row=0, column=3)

    tk.Button(frame, text="Find Path", command=find_path).grid(row=0, column=4)

    fig, ax = plt.subplots(figsize=(10, 7))
    canvas = FigureCanvasTkAgg(fig, master=window)
    canvas.get_tk_widget().pack()
    draw_graph()

    window.mainloop()

if __name__ == '__main__':
    run_gui()
