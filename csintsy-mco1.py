from collections import OrderedDict, deque
import heapq

letter_names = OrderedDict([
    ("A", "Andrew - Br. Andrew Gonzales Hall"),
    ("B", "Bloemen - Br. Alphonsus Bloemen Hall"),
    ("C", "Connon - Br. Gabriel Connon Hall"),
    ("D", "Faculty Center"),
    ("E", "Gokongwei - John Gokongwei Sr. Hall"),
    ("F", "Henry Sy Sr. Hall"),
    ("G", "St. Joseph Hall"),
    ("H", "St. La Salle Hall"),
    ("I", "St. Miguel Febres Cordero Hall"),
    ("J", "Razon - Enrique M. Razon Sports Center"),
    ("K", "Science & Technology Research Center"),
    ("L", "Velasco - Urbano J. Velasco Hall"),
    ("M", "Yuchengco - Don Enrique T. Yuchengco Hall"),
    ("AA", "24 Chicken"),
    ("AB", "Ate Rica's Bacsilog"),
    ("AC", "Bab"),
    ("AD", "The Barn"),
    ("AE", "BBQ Nation"),
    ("AF", "Chef Bab's House of Sisig"),
    ("AG", "Colonel's Curry"),
    ("AH", "Good Munch"),
    ("AI", "Gyuniku"),
    ("AJ", "Happy N' Healthy (Bloemen)"),
    ("AK", "The Hungry Pita"),
    ("AL", "Kitchen City"),
    ("AM", "Kuya Mel Kitchen"),
    ("AN", "Lumpia.natics"),
    ("AO", "Master Chop"),
    ("AP", "McDonald's"),
    ("AQ", "Mongolian Master"),
    ("AR", "Perico's Grill"),
    ("AS", "Tapa Loca"),
    ("AT", "Tori Box"),
    ("BA", "Agno Food Court"),
    ("BB", "Agno St."),
    ("BC", "EGI Taft Tower"),
    ("BD", "Fidel A. Reyes St.")
])
adjacency_list = [
   
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


# === BFS with Distance Tracking ===
def blind_search(start, end):
    keys = list(letter_names.keys())
    index_map = {k: i for i, k in enumerate(keys)}
    visited = set()
    queue = deque([([start], 0)])  # (path, total_distance)

    while queue:
        path, total_dist = queue.popleft()
        current = path[-1]

        if current == end:
            print("Path:", " → ".join(path))
            print("Total Distance:", total_dist, "meters")
            print("Steps:", len(path) - 1)
            return

        if current not in visited:
            visited.add(current)
            cur_idx = index_map[current]

            for next_idx, weight in enumerate(adjacency_list[cur_idx]):
                if weight > 0:
                    neighbor = keys[next_idx]
                    if neighbor not in visited:
                        queue.append((path + [neighbor], total_dist + weight))

    print("No path found.")

# --------------- HEURISTIC SEARCH ---------------------
def build_weighted_graph():
    """
    Build a weighted adjacency list graph from the adjacency matrix.
    """
    graph = {}
    keys = list(letter_names.keys())
    n = len(keys)

    for i in range(n):
        src = keys[i]
        graph[src] = []
        for j in range(n):
            weight = adjacency_list[i][j]
            if weight > 0:
                dst = keys[j]
                graph[src].append((dst, weight))
    return graph

def get_heuristic(goal):
    heuristic_values = [
        5.0, 4.5, 3.0, 3.0, 3.0, 4.8, 3.0, 5.0, 3.0, 4.0, 3.0, 3.0, 3.0,
        4.7, 3.9, 4.0, 4.0, 3.0, 4.0, 5.0, 4.0, 3.0, 4.9, 4.8, 4.2, 4.0,
        4.0, 3.0, 4.2, 3.0, 4.0, 3.0, 3.9, 3.0, 3.0, 3.0, 3.0
    ]
    keys = list(letter_names.keys())
    return {key: heuristic_values[i] for i, key in enumerate(keys)}

def heuristic_search(start, goal):
    graph = build_weighted_graph()
    heuristics = get_heuristic(goal)

    open_set = []
    heapq.heappush(open_set, (heuristics[start], start))  # (f, node)

    g = {start: 0}
    h = {start: heuristics[start]}
    f = {start: g[start] + h[start]}
    parent = {start: None}
    closed_set = set()

    while open_set:
        # Get the node in open_set with lowest f value
        current_f, current = heapq.heappop(open_set)

        if current == goal:
            # Reconstruct path from goal to start
            path = []
            while current is not None:
                path.insert(0, current)
                current = parent[current]
            print("Path:", " → ".join(path))
            print("Steps:", len(path) - 1)
            print("Total cost:", g[goal])
            return

        closed_set.add(current)

        for neighbor, cost in graph.get(current, []):
            if neighbor in closed_set:
                continue

            tentative_g = g[current] + cost

            if neighbor not in g or tentative_g < g[neighbor]:
                parent[neighbor] = current
                g[neighbor] = tentative_g
                h[neighbor] = heuristics.get(neighbor, float('inf'))
                f[neighbor] = g[neighbor] + h[neighbor]
                heapq.heappush(open_set, (f[neighbor], neighbor))

    print("No path found.")

if __name__ == "__main__":
    dlsu_number = 13  # campus buildings
    food_number = 20  # food stalls
    letters_list = list(letter_names.keys())
    places_list  = list(letter_names.values())

    # Select campus building
    while True:
        print("\u001b[42m\nWhere are you?\u001b[0m\u001b[32m")
        for i in range(dlsu_number):
            print(f"[{i+1}] {places_list[i]}")
        try:
            option = int(input("\n\u001b[0mYour option: "))
        except ValueError:
            print("\u001b[31mInvalid input! Please enter a number.\u001b[0m")
            continue
        if option < 1 or option > dlsu_number:
            print("\u001b[31mInvalid Input!\u001b[0m")
        else:
            start = letters_list[option - 1]
            break

    # Select food stall
    while True:
        print("\u001b[44m\nWhere do you want to eat?\u001b[0m\u001b[34m")
        for i in range(food_number):
            print(f"[{i+1}] {places_list[dlsu_number + i]}")
        try:
            option = int(input("\n\u001b[0mYour option: "))
        except ValueError:
            print("\u001b[31mInvalid input! Please enter a number.\u001b[0m")
            continue
        if option < 1 or option > food_number:
            print("\u001b[31mInvalid Input!\u001b[0m")
        else:
            end = letters_list[dlsu_number + option - 1]
            break

    print("\u001b[43m\nYour shortest route using BLIND search:\u001b[0m")
    blind_search(start, end)

    print("\u001b[45m\nYour shortest route using HEURISTIC search:\u001b[0m")
    heuristic_search(start, end)

    print("\u001b[0m")  # reset colors
