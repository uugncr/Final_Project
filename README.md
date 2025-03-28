# Sentetik Veri Üreterek AI Modeli Geliştirmek 
# Deneysel Veri Toplama ve Modelin Doğruluğunu Test Edilecektir

## Proje Amacı ve Özeti

Bu proje, sintilatör verilerinin makine öğrenimi teknikleriyle analiz edilmesini ve deney sonuçlarının daha kolay bir şekilde değerlendirilmesini amaçlamaktadır. Sintilatör verilerini simüle etmek için belirli bir matematiksel model kullanılmıştır. Bu modelde, dedektör çıkışı sabit olup, `e^-lambda*t` formülü ile bozunan ve üç farklı lambda değerine sahip durumlar incelenmiştir.

## Kullanım

Proje, sintilatör verilerinin karakteristik özelliklerini simüle etmek için aşağıdaki parametreleri kullanır:

- **`t`**: Zaman dizisi (x ekseni)
- **`t0`**: Rastgele başlangıç zamanı
- **`N`**: Sinyalin yüksekliği (Amplitude)
- **`s_r`**: Dedektörün sigma değeri
- **`s_f`**: Üç farklı bozulma için sigma değerleri

Bu parametreler kullanılarak, gerçek sintilatör verilerine benzeyen bir yapı oluşturulur. Simülasyon sırasında uniform bir gürültü eklenir ve belirli noktalar arasında integral hesaplamaları yapılır.

## Çalıştırma

Proje kodunu çalıştırmak ve sonuçları görüntülemek için aşağıdaki adımları izleyin:

1. `new.py` dosyasını çalıştırın:
   ```bash
   python new.py
   ```

Bu, analizin nasıl yapıldığını ve sonuçların nasıl elde edildiğini gösterir.

## Görselleştirme

Analiz sonuçları, `art` klasörü içinde bulunan ve ROOT aracılığıyla verilerin görsel olarak ayrıldığı dosyalarda saklanır.

## Makine Öğrenimi Modelleri

Projede, sintilatör verilerini kullanarak iki farklı makine öğrenimi modeli geliştirilmiştir:

1. **Sınıflandırma:** 
   - `par_25`: Yüklü ve kütleli parçacık
   - `par_50`: Yüksüz ve kütleli parçacık
   - `par_100`: Yüksüz ve kütlesiz enerji

2. **Regresyon:** 
   - En iyi makine öğrenimi modeli için çalışmalar devam etmektedir.

## İletişim

- Projeyi geliştiren kişi: [GitHub Profiliniz](https://github.com/uugncr)
- E-posta: ugurgencer26@gmail.com

