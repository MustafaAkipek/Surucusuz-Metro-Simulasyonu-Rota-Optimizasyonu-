from collections import defaultdict, deque
import heapq
from typing import Dict, List, Set, Tuple, Optional
import tkinter as tk
from tkinter import ttk, messagebox
import metro_station_graph

class Istasyon:
    def __init__(self, idx: str, ad: str, hat: str):
        # İstasyon sınıfının yapıcı metodu. İstasyonun kimlik, ad ve hat bilgilerini alır.
        self.idx = idx  # İstasyonun kimlik numarası
        self.ad = ad    # İstasyonun adı
        self.hat = hat  # İstasyonun ait olduğu hat

        # İstasyonun komşularını ve aralarındaki süreyi tutan liste
        self.komsular: List[Tuple['Istasyon', int]] = []  # (istasyon, süre) tuple'ları lstenin içinde 2 parametreli tuple lar olaracak

    def komsu_ekle(self, istasyon: 'Istasyon', sure: int):
        # İstasyona komşu bir istasyon ekler ve aralarındaki süreyi belirtir
        self.komsular.append((istasyon, sure))

class MetroAgi:
    def __init__(self):
        # MetroAgi sınıfının yapıcı metodu. Metro ağı içindeki istasyonları ve hatları tutar.
        self.istasyonlar: Dict[str, Istasyon] = {}  # İstasyon kimliklerini ve Istasyon nesnelerini tutan sözlük
        self.hatlar: Dict[str, List[Istasyon]] = defaultdict(list)  # Hat adlarını ve bu hatlardaki istasyonları tutan sözlük

    def istasyon_ekle(self, idx: str, ad: str, hat: str) -> None:
        # Yeni bir istasyon ekler. İstasyon zaten mevcut değilse eklenir.
        if id not in self.istasyonlar:
            istasyon = Istasyon(idx, ad, hat)  # Yeni bir Istasyon nesnesi oluşturulur
            self.istasyonlar[idx] = istasyon   # İstasyon, istasyonlar sözlüğüne eklenir
            self.hatlar[hat].append(istasyon)  # İstasyon, ilgili hattın istasyon listesine eklenir

    def baglanti_ekle(self, istasyon1_id: str, istasyon2_id: str, sure: int) -> None:
        # İki istasyon arasında bağlantı ekler ve aralarındaki süreyi belirtir.
        istasyon1 = self.istasyonlar[istasyon1_id]  # İlk istasyon nesnesi
        istasyon2 = self.istasyonlar[istasyon2_id]  # İkinci istasyon nesnesi
        istasyon1.komsu_ekle(istasyon2, sure)  # İlk istasyona, ikinci istasyon komşu olarak eklenir
        istasyon2.komsu_ekle(istasyon1, sure)  # İkinci istasyona, ilk istasyon komşu olarak eklenir
    
    def en_az_aktarma_bul(self, baslangic_id: str, hedef_id: str) -> Optional[List[Istasyon]]:
        """BFS algoritması kullanarak en az aktarmalı rotayı bulur
        
        Bu fonksiyonu tamamlayın:
        1. Başlangıç ve hedef istasyonların varlığını kontrol edin
        2. BFS algoritmasını kullanarak en az aktarmalı rotayı bulun
        3. Rota bulunamazsa None, bulunursa istasyon listesi döndürün
        4. Fonksiyonu tamamladıktan sonra, # TODO ve pass satırlarını kaldırın
        
        İpuçları:
        - collections.deque kullanarak bir kuyruk oluşturun, HINT: kuyruk = deque([(baslangic, [baslangic])])
        - Ziyaret edilen istasyonları takip edin
        - Her adımda komşu istasyonları keşfedin
        """

        # Eğer her 2 istasyon da mevcut ise onları değişkenlere atadık
        if baslangic_id not in self.istasyonlar or hedef_id not in self.istasyonlar:
            return None
        
        baslangic = self.istasyonlar[baslangic_id] 
        hedef = self.istasyonlar[hedef_id]
        ziyaret_edildi = {baslangic}      
        
        queue = deque([(baslangic, [baslangic])])  # (İstasyon, şu ana kadar izlenen rota)
        ziyaret_edildi = set()  # Ziyaret edilenleri takip etmek için bir set oluşturduk(böylece bir daha aynı yeri tekrar ziyaret etmeyeceğiz)

        while queue:
            istasyon, rota = queue.popleft()  # Kuyruğun başındaki istasyonu al
            
            # Hedef istasyona ulaştıysak, rotayı döndür ve bitir
            if istasyon == hedef:
                return rota
            
            # Eğer istasyon daha önce ziyaret edildiyse(atlamamız lazım)
            if istasyon in ziyaret_edildi:
                continue  # Zaten ziyaret edildiyse işlemi atla
            
            ziyaret_edildi.add(istasyon) # İstasyonu ziyaret edildi olarak işaretle(yani set() yapısının içine ekleriz)

            # Komşuları kuyruğa ekle
            for neighbor, _ in istasyon.komsular:  # Sadece istasyonu al, süreyi almasını istemediğimiz için "," den sonra _ kullandık
                if neighbor in ziyaret_edildi:
                    continue  # Ziyaret edildiyse işlemi atla
                
                queue.append((neighbor, rota + [neighbor]))  # Yeni rota ekliyoruz

        # Eğer hedefe ulaşamazsak None döndürülecek
        return None  

    def en_hizli_rota_bul(self, baslangic_id: str, hedef_id: str) -> Optional[Tuple[List[Istasyon], int]]:
        """A* algoritması kullanarak en hızlı rotayı bulur
        
        Bu fonksiyonu tamamlayın:
        1. Başlangıç ve hedef istasyonların varlığını kontrol edin
        2. A* algoritmasını kullanarak en hızlı rotayı bulun
        3. Rota bulunamazsa None, bulunursa (istasyon_listesi, toplam_sure) tuple'ı döndürün
        4. Fonksiyonu tamamladıktan sonra, # TODO ve pass satırlarını kaldırın
        
        İpuçları:
        - heapq modülünü kullanarak bir öncelik kuyruğu oluşturun, HINT: pq = [(0, id(baslangic), baslangic, [baslangic])]
        - Ziyaret edilen istasyonları takip edin
        - Her adımda toplam süreyi hesaplayın
        - En düşük süreye sahip rotayı seçin
        """

        # Eğer her 2 istasyon da mevcut ise onları değişkenlere atadık
        if baslangic_id not in self.istasyonlar or hedef_id not in self.istasyonlar:
            return None

        baslangic = self.istasyonlar[baslangic_id]
        hedef = self.istasyonlar[hedef_id]
        ziyaret_edildi = set() # Ziyaret edilen istasyonları takip etmek için set() oluşturduk

        open_list = [] # Öncelik kuyruğu oluşturduk heapq için

        # id eklememin sebebi iki tane nesne karşılaştıralamaz hatası almak için
        heapq.heappush(open_list, (heuristic[baslangic_id], 0, id(baslangic), baslangic, []))  # (f, g, id, istasyon, yol)
        
        while open_list:
            _, g, _, istasyon, rota = heapq.heappop(open_list)  # Kullanmayacaklarımızı _ ile belirttik

            if istasyon in ziyaret_edildi: # Eğer istasyon ziyaret edildiyse atla
                continue

            rota = rota + [istasyon]  # İstasyon ziyaret edilmemiş ise rotaya ekle

            # Hedefe ulaştıysak rotayı ve toplam süreyi döndürür
            if istasyon == hedef:
                return rota, g

            ziyaret_edildi.add(istasyon)  # Hedefe ulaşmadıysak, ziyaret edildi olarak işaretleriz

            # Komşuları gezeriz ve uygun olanları kuyruğa(queue) ekleriz
            for komsu, sure in istasyon.komsular:
                if komsu not in ziyaret_edildi:
                    g_new = g + sure # g(n)' i güncelledik
                    f_new = g_new + heuristic.get(komsu.idx, 0)  # h(n) ile g(n)' i toplayarak yeni f(n) değerini buluruz
                    heapq.heappush(open_list, (f_new, g_new, id(komsu), komsu, rota))

        # Eğer hedefe ulaşamazsak None döndürürüz
        return None
    
    def en_kisa_maliyetli_rota_bul(self, baslangic_id: str, hedef_id: str):
        """UCS (Uniform Cost Search) ile en düşük maliyetli rotayı buluruz."""
        baslangic = self.istasyonlar[baslangic_id]
        hedef = self.istasyonlar[hedef_id]
    
        # Başlangıç ve hedef istasyonların varlığını kontrol et
        if baslangic_id not in self.istasyonlar or hedef_id not in self.istasyonlar:
            return None

        baslangic = self.istasyonlar[baslangic_id]
        hedef = self.istasyonlar[hedef_id]
        visited = set() # Ziyaret edilen istasyonları takip etmek için 

        queue = []

         # id' nin eklenmesinin sebebi iki nesneyi karşılaştıramazsın hatasını almamak için ekledim
        heapq.heappush(queue, (0, id(baslangic), baslangic, [])) # (Toplam maliyet, id, İstasyon, Rota) 

        while queue:
            maliyet, _, istasyon, rota = heapq.heappop(queue) # kullanmayacağımızı kısımları _ ile belirttik

            if istasyon in visited: # istasyon ziyaret edildiyse atla
                continue

            visited.add(istasyon) # istasyonu ziyaret edilenlere ekledik
            rota = rota + [istasyon] # istasyonu rotamıza dahil ettik

            # Hedefe ulaştıysak rotayı döndür
            if istasyon == hedef:
                return rota, maliyet

            # Komşuları gez ve uygun olanları kuyruğa ekle
            for komsu, sure in istasyon.komsular:
                if komsu not in visited:

                    # id(komsu), her nesneye özel bir sayı döndürür ve heap bunu sıralayabilir. Bu yüzden ekledim ki iki nesne karşılaştırılamaz hatasını almamak için
                    heapq.heappush(queue, (maliyet + sure, id(komsu), komsu, rota)) #  eğer ziyaret edilmemişse heap' e ekleme yap

        return None

# Heuristic değerleri aktarma olan duraklar da 2 diğer duraklarda 0 olacak şekilde belirledim
heuristic = {
    "K1": 2,  # Kızılay
    "K2": 0,
    "K3": 2,  # Demetevler
    "K4": 0,
    "M1": 0,
    "M2": 2,  # Kızılay (Mavi Hat)
    "M3": 0,
    "M4": 2,  # Gar
    "T1": 0,
    "T2": 2,  # Demetevler (Turuncu Hat)
    "T3": 2,  # Gar (Turuncu Hat)
    "T4": 0
}  

# Örnek Kullanım
if __name__ == "__main__":
    metro = MetroAgi()
    
    # İstasyonlar ekleme
    # Kırmızı Hat
    metro.istasyon_ekle("K1", "Kızılay", "Kırmızı Hat")
    metro.istasyon_ekle("K2", "Ulus", "Kırmızı Hat")
    metro.istasyon_ekle("K3", "Demetevler", "Kırmızı Hat")
    metro.istasyon_ekle("K4", "OSB", "Kırmızı Hat")
    
    # Mavi Hat
    metro.istasyon_ekle("M1", "AŞTİ", "Mavi Hat")
    metro.istasyon_ekle("M2", "Kızılay", "Mavi Hat")  # Aktarma noktası
    metro.istasyon_ekle("M3", "Sıhhiye", "Mavi Hat")
    metro.istasyon_ekle("M4", "Gar", "Mavi Hat")
    
    # Turuncu Hat
    metro.istasyon_ekle("T1", "Batıkent", "Turuncu Hat")
    metro.istasyon_ekle("T2", "Demetevler", "Turuncu Hat")  # Aktarma noktası
    metro.istasyon_ekle("T3", "Gar", "Turuncu Hat")  # Aktarma noktası
    metro.istasyon_ekle("T4", "Keçiören", "Turuncu Hat")
    
    # Bağlantılar ekleme
    # Kırmızı Hat bağlantıları
    metro.baglanti_ekle("K1", "K2", 4)  # Kızılay -> Ulus
    metro.baglanti_ekle("K2", "K3", 6)  # Ulus -> Demetevler
    metro.baglanti_ekle("K3", "K4", 8)  # Demetevler -> OSB
    
    # Mavi Hat bağlantıları
    metro.baglanti_ekle("M1", "M2", 5)  # AŞTİ -> Kızılay
    metro.baglanti_ekle("M2", "M3", 3)  # Kızılay -> Sıhhiye
    metro.baglanti_ekle("M3", "M4", 4)  # Sıhhiye -> Gar
    
    # Turuncu Hat bağlantıları
    metro.baglanti_ekle("T1", "T2", 7)  # Batıkent -> Demetevler
    metro.baglanti_ekle("T2", "T3", 9)  # Demetevler -> Gar
    metro.baglanti_ekle("T3", "T4", 5)  # Gar -> Keçiören
    
    # Hat aktarma bağlantıları (aynı istasyon farklı hatlar)
    metro.baglanti_ekle("K1", "M2", 2)  # Kızılay aktarma
    metro.baglanti_ekle("K3", "T2", 3)  # Demetevler aktarma
    metro.baglanti_ekle("M4", "T3", 2)  # Gar aktarma
    
    # Test senaryoları
    print("\n=== Test Senaryoları ===")
    
    # Senaryo 1: AŞTİ'den OSB'ye
    print("\n1. AŞTİ'den OSB'ye:")
    rota = metro.en_az_aktarma_bul("M1", "K4")
    if rota:
        print("En az aktarmalı rota:", " -> ".join(i.ad for i in rota))
    
    sonuc = metro.en_hizli_rota_bul("M1", "K4")
    if sonuc:
        rota, sure = sonuc
        print(f"En hızlı rota ({sure} dakika):", " -> ".join(i.ad for i in rota))

    ucs_sonuc = metro.en_kisa_maliyetli_rota_bul("M1", "K4")
    if ucs_sonuc:
        rota, maliyet = ucs_sonuc
        print(f"En düşük maliyetli rota ({maliyet} dakika):", " -> ".join(i.ad for i in rota))
    
    # Senaryo 2: Batıkent'ten Keçiören'e
    print("\n2. Batıkent'ten Keçiören'e:")
    rota = metro.en_az_aktarma_bul("T1", "T4")
    if rota:
        print("En az aktarmalı rota:", " -> ".join(i.ad for i in rota))
    
    sonuc = metro.en_hizli_rota_bul("T1", "T4")
    if sonuc:
        rota, sure = sonuc
        print(f"En hızlı rota ({sure} dakika):", " -> ".join(i.ad for i in rota))

    ucs_sonuc = metro.en_kisa_maliyetli_rota_bul("T1", "T4")
    if ucs_sonuc:
        rota, maliyet = ucs_sonuc
        print(f"En düşük maliyetli rota ({maliyet} dakika):", " -> ".join(i.ad for i in rota))
    
    # Senaryo 3: Keçiören'den AŞTİ'ye
    print("\n3. Keçiören'den AŞTİ'ye:")
    rota = metro.en_az_aktarma_bul("T4", "M1")
    if rota:
        print("En az aktarmalı rota:", " -> ".join(i.ad for i in rota))
    
    sonuc = metro.en_hizli_rota_bul("T4", "M1")
    if sonuc:
        rota, sure = sonuc
        print(f"En hızlı rota ({sure} dakika):", " -> ".join(i.ad for i in rota)) 

    ucs_sonuc = metro.en_kisa_maliyetli_rota_bul("T4", "M1")
    if ucs_sonuc:
        rota, maliyet = ucs_sonuc
        print(f"En düşük maliyetli rota ({maliyet} dakika):", " -> ".join(i.ad for i in rota))


# 📌 İstasyon isimlerini ve kodlarını eşleştirdiğim sözlük
istasyon_kodlari = {
    "Kızılay(K1-Kırmızı Hat)" : "K1",
    "Ulus(K2-Kırmızı Hat)": "K2",
    "Demetevler(K3-Kırmızı Hat)": "K3",
    "OSB(K4-Kırmızı Hat)": "K4",
    "AŞTİ(M1-Mavi Hat)": "M1",
    "Kızılay(M2-Mavi Hat)": "M2",
    "Sıhhiye(M3-Mavi Hat)": "M3",
    "Gar(M4-Mavi Hat)": "M4",
    "Batıkent(T1-Turuncu Hat)": "T1",
    "Demetevler(T2-Turuncu Hat)": "T2",
    "Gar(T3-Turuncu Hat)": "T3",
    "Keçiören(T4-Turuncu Hat)": "T4"
}

# Tkinter ana pencereyi oluştur
root = tk.Tk()
root.title("Sürücüsüz Metro Simülasyonu")
root.geometry("400x300")

# 📌 İstasyonları Göster Butonu(Graph' ın görsel halini açar)
def istasyonlari_goster():
    metro_station_graph.show_graph(metro_station_graph.G)  # metro_station_graph.py içindeki fonksiyon çağrılır

btn_goster = tk.Button(root, text="İstasyonları Göster", command=istasyonlari_goster)
btn_goster.pack(pady=5)

# 📌 Başlangıç İstasyonu Seçimi
tk.Label(root, text="Başlangıç İstasyonu:").pack()
baslangic_var = tk.StringVar()
baslangic_cb = ttk.Combobox(root, textvariable=baslangic_var, values=list(istasyon_kodlari.keys()))
baslangic_cb.pack()

# 📌 İniş İstasyonu Seçimi
tk.Label(root, text="Varış İstasyonu:").pack()
varis_var = tk.StringVar()
varis_cb = ttk.Combobox(root, textvariable=varis_var, values=list(istasyon_kodlari.keys()))
varis_cb.pack()

# 📌 Rota Tipi Seçimi
tk.Label(root, text="Rota Tipi:").pack()
rota_tipi_var = tk.StringVar()
rota_tipi_cb = ttk.Combobox(root, textvariable=rota_tipi_var, values=["En Az Aktarmalı", "En Hızlı", "En Kısa Maliyetli"])
rota_tipi_cb.pack()

# 📌 Rotayı Göster Butonu
def rotayi_goster():
    secilen_baslangic = baslangic_var.get()
    secilen_varis = varis_var.get()
    rota_tipi = rota_tipi_var.get()

    if not secilen_baslangic or not secilen_varis or not rota_tipi:
        messagebox.showerror("Hata", "Lütfen tüm seçimleri yapın!")
        return

    # 📌 Seçilen istasyon adlarını, istasyon kodlarına dönüştür
    baslangic_kodu = istasyon_kodlari.get(secilen_baslangic)
    varis_kodu = istasyon_kodlari.get(secilen_varis)

    if not baslangic_kodu or not varis_kodu:
        messagebox.showerror("Hata", "Geçersiz istasyon seçildi!")
        return

    # Kullanıcının seçimine göre istenilen algoritmayı çalıştırır
    if rota_tipi == "En Az Aktarmalı":
        sonuc = metro.en_az_aktarma_bul(baslangic_kodu, varis_kodu)
    elif rota_tipi == "En Hızlı":
        sonuc = metro.en_hizli_rota_bul(baslangic_kodu, varis_kodu)
    elif rota_tipi == "En Kısa Maliyetli":
        sonuc = metro.en_kisa_maliyetli_rota_bul(baslangic_kodu, varis_kodu)
    else:
        messagebox.showerror("Hata", "Geçersiz rota tipi seçildi!")
        return

    # Sonucu göster
    if sonuc:
        if isinstance(sonuc, tuple):  # A* ve UCS için bu bloğa girecek (rota, süre)
            rota, sure = sonuc
            mesaj = f"Rota: {' -> '.join(ist.ad for ist in rota)}\nSüre: {sure} dakika"
        else:  # BFS için (sadece rota listesi döner)
            mesaj = f"Rota: {' -> '.join(ist.ad for ist in sonuc)}"

        messagebox.showinfo("Rota Sonucu", mesaj)
    else:
        messagebox.showerror("Hata", "Rota bulunamadı!")

btn_rota = tk.Button(root, text="Rotayı Göster", command=rotayi_goster)
btn_rota.pack(pady=10)

root.mainloop()