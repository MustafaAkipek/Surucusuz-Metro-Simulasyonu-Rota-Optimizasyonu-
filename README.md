# Sürücüsüz Metro Simülasyonu - Rota Optimizasyonu

## 1. Proje Başlığı ve Kısa Açıklama(Türkçe)
## Project Presentation(English, line 128-257)

Bu proje, sürücüsüz bir metro sistemini simüle ederek rota optimizasyonu sağlamaktadır. Belirtilen iki istasyon arasındaki en iyi rotayı belirlemek için farklı algoritmalar kullanılır. Kullanılan kütüphaneler ve algoritmalar şunlardır:

## 2. Kullanılan Teknolojiler ve Kütüphaneler
Proje Python programlama dili kullanılarak geliştirilmiştir. Aşağıdaki kütüphaneler ve veri yapıları kullanılmıştır:
- **heapq**: Öncelikli kuyruk yapısını kullanarak A* algoritmasında etkin yol bulma işlemi gerçekleştirilmiştir.
- **collections**: BFS algoritması için deque veri yapısı kullanılmıştır.
- **matplotlib**: Metro hatlarını ve istasyonları görselleştirmek için kullanılmıştır.
- **networkx**: Graf yapısını yönetmek ve analiz etmek için kullanılmıştır.

- **En az aktarmalı rota (BFS):** En az hat değişimini gerektiren rotayı bulur.
- **En hızlı rota (A\* Algoritması):** En kısa süreyi hesaplar.
- **En kısa maliyetli rota (Uniform Cost Search - UCS):** En az toplam yolculuk süreli rotayı bulur.

## 3. Algoritmaların Çalışma Mantığı
### BFS Algoritması
BFS (Breadth-First Search) algoritması, en kısa yol bulma işleminde kullanılmıştır. Algoritma şu şekilde çalışır:
1. Başlangıç düğümünden itibaren kuyruk veri yapısına (queue) eklenir.
2. Kuyruk boşalana kadar döngü devam eder.
3. Her iterasyonda bir düğüm çıkartılır ve komşu düğümler ziyaret edilir.
4. Ziyaret edilen her düğüm için mesafe güncellenir ve kuyrukta işlenmek üzere eklenir.
5. Hedef düğüme ulaşıldığında en kısa yol elde edilir.

### A* Algoritması
A* (A Star) algoritması, hem BFS hem de Dijkstra algoritmalarının birleşimi olarak çalışır ve daha optimize bir yol bulma algoritmasıdır.
1. **Başlangıç noktası**, öncelikli kuyruğa eklenir.
2. **G fonskiyonu (g(n))**: Başlangıçtan düğüme olan mesafeyi hesaplar.
3. **H fonksiyonu (h(n))**: Düğümden hedefe olan tahmini mesafeyi (heuristic) belirler.
4. **F fonksiyonu (f(n) = g(n) + h(n))**: En iyi tahmini mesafeyi belirler.
5. Öncelikli kuyrukta en düşük `f(n)` değerine sahip düğüm işleme alınır.
6. Hedefe ulaşıldığında en kısa ve en optimize yol belirlenmiş olur.

### UCS Algoritması
UCS (Uniform Cost Search) algoritması, ağırlıklı graflarda en kısa yolu bulmak için kullanılan bir yöntemdir. Aşağıdaki adımlarla çalışır:
1. Başlangıç düğümü bir öncelik kuyruğuna eklenir ve maliyet `0` olarak ayarlanır.
2. Kuyruktaki en düşük maliyetli düğüm işleme alınır.
3. İşlenen düğümün komşuları keşfedilir ve yeni maliyetler hesaplanarak kuyruğa eklenir.
4. Eğer hedef düğüme ulaşıldıysa, o ana kadar bulunan en düşük maliyetli yol belirlenmiş olur.

### Neden Bu Algoritmaları Kullandık?
- **BFS**, ağırlıksız graf yapılarında en kısa yolu garantili olarak bulduğu için tercih edilmiştir.
- **A***, ağırlıklı graf yapılarında daha hızlı ve optimize sonuçlar ürettiği için kullanılmıştır.
- **UCS**, ağırlıklı graflarda en düşük maliyetli yolu bulmada etkili olduğu için eklenmiştir.


## Özellikler ve Fonksiyonlar

- **Metro istasyon ve hat yönetimi**  
- **Rota optimizasyon algoritmaları:**  
- **BFS:** En az aktarmalı rota
- **A\***: En hızlı rota
- **UCS:** En kısa maliyetli rota
- **Grafiksel metro ağı görünteleme**  
- **Tkinter tabanlı kullanıcı arayüzü**

## Kullanılan Teknolojiler

- **Python**  
- **`collections`** (BFS için `defaultdict`, `deque`)
- **`heapq`** (A* ve UCS için)
- **`typing`** (Tip belirleme)
- **`tkinter`** (Grafik arayüz)
- **`networkx`** (Graf yapısı)
- **`matplotlib`** (Grafikleri görüntüleme)

## 4. Örnek Kullanım ve Test Sonuçları
Projedeki kod parçaları **a_star_deneme.py** ve **bfs_deneme.py** dosyalarında algoritmaların nasıl çalıştığı gösterilmektedir.

## Gereksinimler

Bu projeyi çalıştırmak için Python 3.x ve aşağıdaki kütüphaneler gereklidir:

```bash
pip install networkx matplotlib
```

## Kurulum

1. Depoyu klonlayın:

    ```bash
    git clone https://github.com/MustafaAkipek/Surucusuz-Metro-Simulasyonu-Rota-Optimizasyonu-.git
    cd Surucusuz-Metro-Simulasyonu-Rota-Optimizasyonu-
    ```

2. Gerekli bağımlılıkları yükleyin:

    ```bash
    pip install networkx matplotlib
    ```

## Kullanım

1. Simülasyonu başlatın:

    ```bash
    python MustafaAkipek_MetroSimulation.py
    ```

2. Tkinter GUI ekranda görünecektir.
3. Başlangıç ve varış istasyonlarını seçin.
4. Rota tipi belirleyin:
   - `En Az Aktarmalı` (BFS)
   - `En Hızlı` (A*)
   - `En Kısa Maliyetli` (UCS)
5. **"Rotayı Göster"** butonuna basın.
6. **"İstasyonları Göster"** butonu ile metro ağı grafiğini görüntüleyin.

## Ana Fonksiyonlar

**`MetroAgi` Sınıfı (`MustafaAkipek_MetroSimulation.py` içinde bulunur)**

- **`istasyon_ekle(idx, ad, hat)`:** Yeni istasyon ekler.
- **`baglanti_ekle(istasyon1_id, istasyon2_id, sure)`:** İki istasyon arası bağlantı ekler.
- **`en_az_aktarma_bul(baslangic_id, hedef_id)`:** BFS ile en az aktarmalı rotayı bulur.
- **`en_hizli_rota_bul(baslangic_id, hedef_id)`:** A* algoritması ile en hızlı rotayı hesaplar.
- **`en_kisa_maliyetli_rota_bul(baslangic_id, hedef_id)`:** UCS ile en düşük maliyetli rotayı bulur.

## Katkıda Bulunma

Projeye katkı sağlamak için:

1. Depoyu forklayın.
2. Yeni bir şube oluşturun.
3. Değişikliklerinizi yapın ve test edin.
4. Pull request gönderin.

## Lisans

Bu proje için belirli bir lisans belirtilmemiştir. Tüm haklar saklıdır.

## İletişim

Sorular ve destek için: **akipekmustafa23@gmail.com**


# Driverless Metro Simulation - Route Optimization

## Project Overview

This project simulates a driverless metro system and provides route optimization functionalities. It implements several pathfinding algorithms to determine the best route between two stations, considering factors like the least number of transfers, the fastest route (A* algorithm), and the shortest path based on cost (Uniform Cost Search). The project also includes a graphical representation of the metro network using `networkx` and `matplotlib`.  A Tkinter-based GUI allows users to select start and end stations and choose the route optimization criteria.

## Features and Functionality

*   **Station and Line Management:**  Adds and manages metro stations and lines.
*   **Route Optimization Algorithms:**
    *   **Least Transfers (BFS):**  Finds the route with the fewest line changes. Implemented in the `en_az_aktarma_bul` function in `MustafaAkipek_MetroSimulation.py`.
    *   **Fastest Route (A\*):**  Calculates the quickest route using the A\* algorithm. Implemented in the `en_hizli_rota_bul` function in `MustafaAkipek_MetroSimulation.py`.  Heuristic values are defined to guide the search, favoring transfer stations.  The `heuristic` dictionary in `MustafaAkipek_MetroSimulation.py` contains these values.
    *   **Shortest Path (UCS):** Finds the route with the minimum overall travel time (cost) using Uniform Cost Search algorithm. Implemented in the `en_kisa_maliyetli_rota_bul` function in `MustafaAkipek_MetroSimulation.py`.
*   **Graphical Representation:**  Visualizes the metro network, stations, and connections.  This is handled by the `metro_station_graph.py` file.
*   **Tkinter GUI:**  Provides a user-friendly interface to select stations and route types.

## Technology Stack

*   **Python:** Programming language.
*   **`collections`:** For `defaultdict` and `deque` (used in BFS).
*   **`heapq`:** For implementing priority queues (used in A\* and UCS).
*   **`typing`:** For type hinting.
*   **`tkinter`:** For the GUI.
*   **`networkx`:** For graph representation and visualization (`metro_station_graph.py`).
*   **`matplotlib`:** For plotting the graph (`metro_station_graph.py`).

## Prerequisites

*   Python 3.x
*   Install the required Python packages:

    ```bash
    pip install networkx matplotlib
    ```

## Installation Instructions

1.  Clone the repository:

    ```bash
    git clone https://github.com/MustafaAkipek/Surucusuz-Metro-Simulasyonu-Rota-Optimizasyonu-.git
    cd Surucusuz-Metro-Simulasyonu-Rota-Optimizasyonu-
    ```

2.  Install dependencies:

    ```bash
    pip install networkx matplotlib
    ```

## Usage Guide

1.  Run the simulation:

    ```bash
    python MustafaAkipek_MetroSimulation.py
    ```

2.  The Tkinter GUI will appear.

3.  Select a starting station from the "Başlangıç İstasyonu" dropdown.  Possible values include:

    *   `Kızılay(K1-Kırmızı Hat)`
    *   `Ulus(K2-Kırmızı Hat)`
    *   `Demetevler(K3-Kırmızı Hat)`
    *   `OSB(K4-Kırmızı Hat)`
    *   `AŞTİ(M1-Mavi Hat)`
    *   `Kızılay(M2-Mavi Hat)`
    *   `Sıhhiye(M3-Mavi Hat)`
    *   `Gar(M4-Mavi Hat)`
    *   `Batıkent(T1-Turuncu Hat)`
    *   `Demetevler(T2-Turuncu Hat)`
    *   `Gar(T3-Turuncu Hat)`
    *   `Keçiören(T4-Turuncu Hat)`

4.  Select a destination station from the "Varış İstasyonu" dropdown (using the same possible values as above).

5.  Choose a route type from the "Rota Tipi" dropdown:

    *   `En Az Aktarmalı` (Least Transfers - BFS)
    *   `En Hızlı` (Fastest Route - A\*)
    *   `En Kısa Maliyetli` (Shortest Path - UCS)

6.  Click the "Rotayı Göster" button.  A message box will display the calculated route and the total travel time (if applicable, A* and UCS will return the time, but BFS will not).

7.  To view the graphical representation of the metro network, click the "İstasyonları Göster" button. This will open a separate window showing the graph generated by `networkx` and `matplotlib`.

## API Documentation

The core functionality resides within the `MetroAgi` class in `MustafaAkipek_MetroSimulation.py`.

*   **`MetroAgi()`:**
    *   Constructor: Initializes the metro network with empty station and line dictionaries.
*   **`istasyon_ekle(idx: str, ad: str, hat: str) -> None`:**
    *   Adds a new station to the network.
    *   `idx`: Unique station ID (e.g., "K1").
    *   `ad`: Station name (e.g., "Kızılay").
    *   `hat`: Line name (e.g., "Kırmızı Hat").
*   **`baglanti_ekle(istasyon1_id: str, istasyon2_id: str, sure: int) -> None`:**
    *   Adds a connection between two stations.
    *   `istasyon1_id`: ID of the first station.
    *   `istasyon2_id`: ID of the second station.
    *   `sure`: Travel time (in minutes) between the stations.
*   **`en_az_aktarma_bul(baslangic_id: str, hedef_id: str) -> Optional[List[Istasyon]]`:**
    *   Finds the route with the fewest transfers using BFS.
    *   `baslangic_id`: ID of the starting station.
    *   `hedef_id`: ID of the destination station.
    *   Returns: A list of `Istasyon` objects representing the route, or `None` if no route is found.
*   **`en_hizli_rota_bul(baslangic_id: str, hedef_id: str) -> Optional[Tuple[List[Istasyon], int]]`:**
    *   Finds the fastest route using the A\* algorithm.
    *   `baslangic_id`: ID of the starting station.
    *   `hedef_id`: ID of the destination station.
    *   Returns: A tuple containing a list of `Istasyon` objects representing the route and the total travel time (in minutes), or `None` if no route is found.
*   **`en_kisa_maliyetli_rota_bul(baslangic_id: str, hedef_id: str) -> Optional[Tuple[List[Istasyon], int]]`:**
    *   Finds the shortest route (least cost) using UCS.
    *   `baslangic_id`: ID of the starting station.
    *   `hedef_id`: ID of the destination station.
    *   Returns: A tuple containing a list of `Istasyon` objects representing the route and the total cost (travel time in minutes), or `None` if no route is found.

## Contributing Guidelines

Contributions are welcome! To contribute:

1.  Fork the repository.
2.  Create a new branch for your feature or bug fix.
3.  Implement your changes.
4.  Test your changes thoroughly.
5.  Submit a pull request with a clear description of your changes.

## License Information

License not specified. All rights reserved.

## Contact/Support Information

For questions or support, please contact: akipekmustafa23@gmail.com
