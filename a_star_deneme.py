import heapq

def a_star(graph, cost, heuristic, start, goal):
    open_list = []  # Öncelikli kuyruk (heapq kullanılarak oluşturulur)
    heapq.heappush(open_list, (0 + heuristic[start], 0, start, []))  # (f yani g + h, g, düğüm, yol)
    visited_list = set()  # Ziyaret edilen düğümleri tutuyoruz (set ile önceden ziyaret edilip edilmediğini kontrol edebiliyoruz)
    
    while open_list:
        _, g, current, path = heapq.heappop(open_list)  # En düşük f değerine sahip düğümü çıkar(en öncelikli düğümü yani)
        
        if current in visited_list:
            continue  # Eğer düğüm zaten ziyaret edildiyse atla
        
        path = path + [current]  # Yolu güncelle
        
        if current == goal:
            return path, g  # Hedef düğüme ulaştıysak yolu ve toplam maliyeti döndür
        
        visited_list.add(current)  # Düğümü listeye ekle (ziyaret edildi olarak eklendi)
        
        for neighbor in graph.get(current, []):  # Mevcut düğümün komşularını dolaş
            if neighbor in visited_list:
                continue  # Komşu zaten ziyaret edildiyse atlanır
            
            new_g = g + cost.get((current, neighbor), float('inf'))  # Yeni maliyeti hesapla
            f = new_g + heuristic[neighbor]  # f = g + h hesaplaması
            heapq.heappush(open_list, (f, new_g, neighbor, path))  # Yeni düğümü kuyruğa ekle
    
    return None, float('inf')  # Eğer hedefe ulaşılamıyorsa None döndür

# Graf tanımlamaları
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

# Düğümler arası maliyetler (Örnek değerler)
cost = {
    ('A', 'B'): 2, ('A', 'C'): 3,
    ('B', 'D'): 4, ('B', 'E'): 2, ('B', 'F'): 3,
    ('C', 'G'): 5,
    ('F', 'H'): 1,
    ('G', 'I'): 2
}

# Heuristic değerleri rastgele olarak atadım
heuristic = {
    'A': 6, 'B': 4, 'C': 5,
    'D': 3, 'E': 2, 'F': 4, 'G': 3,
    'H': 1, 'I': 0  # I hedef düğüm olduğu için 0 verdim
}

start, goal = 'A', 'I'
path, total_cost = a_star(graph, cost, heuristic, start, goal)
print(f"En kısa yol: {path}, Toplam maliyet: {total_cost}")