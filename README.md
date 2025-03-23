# Surucusuz-Metro-Simulasyonu-Rota-Optimizasyonu-
# Sürücüsüz Metro Simülasyonu - Rota Optimizasyonu

## Proje Tanıtımı

Bu proje, sürücüsüz bir metro sistemini simüle ederek rota optimizasyonu sağlamaktadır. Belirtilen iki istasyon arasındaki en iyi rotayı belirlemek için farklı algoritmalar kullanılır. Algoritmalar şunlardır:

- **En az aktarmalı rota (BFS):** En az hat değişimini gerektiren rotayı bulur.
- **En hızlı rota (A* Algoritması):** En kısa süreyi hesaplar.
- **En kısa maliyetli rota (Uniform Cost Search - UCS):** En az toplam yolculuk süreli rotayı bulur.

Ayrıca **`networkx`** ve **`matplotlib`** kütüphaneleri kullanılarak metro ağının grafiksel görünümü sağlanır. Kullanıcılar **Tkinter tabanlı GUI** aracılığıyla istasyon seçebilir ve rota optimizasyon kriterlerini belirleyebilir.

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

Sorular ve destek için: **mustafa.akipek@gmail.com**
