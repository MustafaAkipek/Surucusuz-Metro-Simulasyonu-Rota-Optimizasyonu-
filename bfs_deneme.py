from collections import deque

def bfs(graph, start, goal):
    queue = deque([(start, [start])])  # (Şu anki düğüm, o noktaya kadar olan yol)
    visited = set()  # Ziyaret edilen düğümleri takip etmek için(set ile önceden ziyaret edilip edilmediğini kontrol edebiliyoruz)


    while queue:
        node, path = queue.popleft()  # Kuyruğun başındaki düğümü al

        if node == goal:  
            return path  # Hedefe ulaştıysak, gidilen yolu döndür

        if node not in visited:
            visited.add(node)  # Eğer düğüm daha önce ziyaret edilmediyse düğümü ziyaret edildi olarak ekle

            for neighbor in graph.get(node, []):  # Komşuları gez
                if neighbor not in visited:
                    queue.append((neighbor, path + [neighbor]))  # Eğer komşu daha önceden ziyaret edilmemiş ise komşuyu kuyruğa ekle

    return None  # Hedefe ulaşılamazsa None döndür

graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E', 'F'],
    'C': ['G'],
    'D': [],
    'E': [],
    'F': ['H'],
    'G': ['I'],
    'H': [],
    'I': []
}

start_node = 'A'
goal_node = 'I'
path = bfs(graph, start_node, goal_node)
print("En kısa yol:", path)
