# Sintilatör Data Analizi ile Makine Öğrenimi

## Proje Amaç ve Özet

Bu proje, sintilatör datalarının makine öğrenimi kullanılarak eğitilmesi ve deney sonuçlarının analizini kolaylaştırmayı amaçlamaktadır. 
Sintilatör datalarını taklit etmek için belirli bir fonksiyon kullanılmış ve detektör çıkışının sabit olduğu, ancak `e^-lambda*t` ile bozunan ve üç farklı lambda değerine sahip olduğu durumlar incelenmiştir.

## Kullanım

Proje, sintilatör datalarının karakteristik özelliklerini simüle etmek için bir dizi parametre kullanır:

- `t`: Zaman dizisi (x ekseni)
- `t0`: Rastgele başlangıç ​​zamanı
- `N`: Sinyalin yüksekliği (Amplitude)
- `s_r`: Detektörün sigma değeri
- `s_f`: Üç farklı bozulma için sigma değerleri

Bu parametrelerle, gerçek sintilatör datalarına benzeyen uniform bir gürültü eklenir ve lineer interpolasyon yoluyla belirli noktalar arasında integral hesaplamaları yapılır. 

### Çalıştırma

Proje kodunun çalıştırılması ve sonuçların görüntülenmesi için:

new.py dosyasini calistimanizi oneririm.

Bu, analizin nasıl yapıldığını ve sonuçların nasıl elde edildiğini gösterir.

## Görselleştirme

Analiz sonuçları, `art` klasörü içinde bulunan ve ROOT aracılığıyla verilerin görsel olarak ayrıldığı dosyalarda saklanır.

## Makine Öğrenimi Modelleri

Projede, sintilatör datalarını kullanarak iki farklı makine öğrenimi modeli geliştirilmiştir:

1. **Sınıflandırma:** 
   - `par_25`: Yüklü ve kütleli parçacık
   - `par_50`: Yüksüz ve kütleli parçacık
   - `par_100`: Yüksüz ve kütleli enerji

2. **Regresyon:** 
   - En iyi makine öğrenimi modeli için çalışmalar devam etmektedir.

## İletişim

- Projeyi geliştiren kişi: [GitHub Profiliniz](https://github.com/uugncr)
- E-posta: ugurgencer26@gmail.com

