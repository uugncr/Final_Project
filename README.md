## ⚠️ Uyarı / Warning

### Türkçe

> Bu projeyi geliştirirken kendi dosya dizinime göre çalıştım. Şimdi bunun ne kadar büyük bir hata olduğunu fark etmiş bulunuyorum.  
> 
> Eğer elinizde organik bir sintilatör datası varsa, `new.py` dosyasını kullanarak verileri görselleştirebilir, maksimum tepe (peak) değerine göre yüzde (%) ve zaman (t) değerlerini analiz edebilirsiniz.  
> 
> `time_range.py` ile sentetik veriler üretebilir, `creator.py` ile yüz binlerce veri oluşturabilirsiniz.  
> 
> `Model` klasörlerinde bu sentetik verilerle eğitilmiş modelleri, `test_model` klasörlerinde ise bu modellerin farklı sentetik verilerle doğrulanmış hâllerini bulabilirsiniz.  
> 
> `art` klasöründe ise, eğer bilgisayarınızda CERN tarafından geliştirilen ROOT programı yüklüyse, verileri görselleştirebilirsiniz.  
> 
> Bu repoya ilerleyen süreçte deneysel veriler ve deney düzeneği de eklenecektir. Amaç, sentetik verilerle eğitilen modellerin deneysel verilerle doğruluğunu test etmektir.  
> 
> Başta bu hatayı yaptığım için özür dilerim.

---

### English

> While working on this project, I structured it according to my own file directory. Now, I realize how big of a mistake that was.  
> 
> If you have any real (organic) scintillator data, you can visualize it using `new.py` and analyze the percentage (%) and time (t) values based on the maximum peak.  
> 
> You can generate synthetic data using `time_range.py` and produce hundreds of thousands of data points with `creator.py`.  
> 
> In the `Model` folders, you will find models trained with synthetic data. In the `test_model` folders, these models have been validated using different sets of synthetic data.  
> 
> In the `art` folder, if you have ROOT (developed by CERN) installed on your system, you can visualize the data.  
> 
> Experimental data and setup will be added to this repository in the future. The goal is to test how accurately the models trained with synthetic data perform on real experimental data.  
> 
> I apologize for the mistake I made at the beginning.

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

## Gerekli Kütüphanelerin Yüklenmesi

Projeyi çalıştırmadan önce gerekli Python kütüphanelerini yüklemek için aşağıdaki adımları izleyin:

1. Python ortamınızı oluşturun ve etkinleştirin (isteğe bağlı).
2. Gerekli kütüphaneleri yüklemek için şu komutu çalıştırın:
   ```bash
   pip install -r requirements.txt

## Çalıştırma

Proje kodunu çalıştırmak ve sonuçları görüntülemek için aşağıdaki adımları izleyin:

1. `new.py` dosyasını çalıştırın:
   ```bash
   python new.py
   ```

Bu, analizin nasıl yapıldığını ve sonuçların nasıl elde edildiğini gösterir.

## Görselleştirme

Analiz sonuçları, `art` klasörü içinde bulunan ve ROOT aracılığıyla verilerin görsel olarak ayrıldığı dosyalarda saklanır.

## Yeni Görselleştirme Araçları

Projeye iki yeni Python dosyası eklenmiştir:

1. **`art_total.py`**:
   - Bu dosya, kullanılan yöntemin genel ayrım gücünü görselleştirir.
   - Tüm veriler bir arada analiz edilerek sonuçlar görsel olarak sunulur.

   Çalıştırmak için:
   ```bash
   python art_total.py
   ```

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
