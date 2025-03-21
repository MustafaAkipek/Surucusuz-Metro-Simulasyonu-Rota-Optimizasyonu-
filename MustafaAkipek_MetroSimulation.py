from collections import defaultdict, deque
import heapq
from typing import Dict, List, Set, Tuple, Optional

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

    def __str__(self):
        return self.ad

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
            
            ziyaret_edildi.add(istasyon)  # İstasyonu ziyaret edildi olarak işaretle

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
        # TODO: Bu fonksiyonu tamamlayın
        pass
        if baslangic_id not in self.istasyonlar or hedef_id not in self.istasyonlar:
            return None

        baslangic = self.istasyonlar[baslangic_id]
        hedef = self.istasyonlar[hedef_id]
        ziyaret_edildi = set()

        open_list = []
        heapq.heappush(open_list, (heuristic[baslangic_id], 0, id(baslangic), baslangic, []))  # (f, g, id, istasyon, yol)
        
        ziyaret_edildi = set()  # Ziyaret edilen istasyonları takip et

        while open_list:
            _, g, _, istasyon, rota = heapq.heappop(open_list)  # Kuyruğun başındaki düğümü alarak başlarız

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
                    g_new = g + sure
                    f_new = g_new + heuristic.get(komsu.idx, 0)  # Heuristic değerini ile gerçek değeri toplayarak yeni f(n) değerini buluruz
                    heapq.heappush(open_list, (f_new, g_new, id(komsu), komsu, rota))

        # Eğer hedefe ulaşamazsak None döndürürüz
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
    
    # Senaryo 2: Batıkent'ten Keçiören'e
    print("\n2. Batıkent'ten Keçiören'e:")
    rota = metro.en_az_aktarma_bul("T1", "T4")
    if rota:
        print("En az aktarmalı rota:", " -> ".join(i.ad for i in rota))
    
    sonuc = metro.en_hizli_rota_bul("T1", "T4")
    if sonuc:
        rota, sure = sonuc
        print(f"En hızlı rota ({sure} dakika):", " -> ".join(i.ad for i in rota))
    
    # Senaryo 3: Keçiören'den AŞTİ'ye
    print("\n3. Keçiören'den AŞTİ'ye:")
    rota = metro.en_az_aktarma_bul("T4", "M1")
    if rota:
        print("En az aktarmalı rota:", " -> ".join(i.ad for i in rota))
    
    sonuc = metro.en_hizli_rota_bul("T4", "M1")
    if sonuc:
        rota, sure = sonuc
        print(f"En hızlı rota ({sure} dakika):", " -> ".join(i.ad for i in rota)) 