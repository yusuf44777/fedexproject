# FedEx Ülke Karşılaştırma Uygulaması

Bu uygulama, FedEx gümrük ücretlerini ve gereksinimleri farklı ülkeler için karşılaştırmanıza olanak sağlar.

## Özellikler

- 🌍 **5 Ülke Karşılaştırması**: Hollanda, İngiltere, ABD, Avustralya, Kanada
- 💰 **Detaylı Ücret Yapısı**: Her ülke için kapsamlı FedEx ücret bilgileri
- 📊 **İnteraktif Tablolar**: Pandas DataFrames ile görselleştirme
- 🚚 **Hizmet Türü Karşılaştırması**: Express vs Standard servis farkları
- 📋 **Gümrük Gereksinimleri**: Her ülke için özel düzenleyici gereksinimler

## Desteklenen Ülkeler

### 🇳🇱 Hollanda
- 13 kapsamlı ücret kategorisi
- AB gümrük düzenlemeleri
- KDV ve gümrük vergisi detayları

### 🇬🇧 İngiltere  
- 19 detaylı ücret listesi
- Brexit sonrası güncel düzenlemeler
- UKCA işaretleme gereksinimleri

### 🇺🇸 Amerika Birleşik Devletleri
- **Express**: 17 ücret kategorisi
- **Standard**: 12 ücret kategorisi + karşılaştırma
- CBP düzenlemeleri ve ACE sistemi

### 🇦🇺 Avustralya
- 13 ücret kategorisi
- Biyogüvenlik gereksinimleri
- GST ve karantina ücretleri

### 🇨🇦 Kanada
- **Express**: 19 kapsamlı ücret
- **Standard**: 7 ücret + değer bazlı yapı
- CBSA düzenlemeleri ve CARM sistemi

## Kurulum

### Gereksinimler
- Python 3.8+
- Streamlit
- Pandas
- Numpy

### Adımlar

1. **Repoyu klonlayın:**
   ```bash
   git clone <repo-url>
   cd fedexproject
   ```

2. **Gerekli paketleri yükleyin:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Uygulamayı çalıştırın:**
   ```bash
   streamlit run app.py
   ```

4. **Tarayıcınızda açın:**
   ```
   http://localhost:8501
   ```

## Kullanım

1. 🏠 **Ana Sayfa**: Ülke karşılaştırma tablolarını görüntüleyin
2. 🔍 **Ülke Seçimi**: Sidebar'dan detaylı bilgi almak istediğiniz ülkeyi seçin
3. 📊 **Ücret Analizi**: Her ülkenin ücret yapısını detaylı olarak inceleyin
4. 📋 **Gereksinimler**: Gümrük belgeleri ve düzenleyici gereksinimleri kontrol edin

## Ücret Kategorileri

- **Temel Vergiler**: KDV/GST, Gümrük vergisi
- **İşlem Ücretleri**: Ek kalem, depolama, kayıt düzeltme
- **Devlet Kurumu Ücretleri**: FDA, USDA, AQIS vb.
- **Özel Hizmetler**: Geçici ithalat, mesai sonrası, transfer
- **Ödeme Ücretleri**: ROD, avans, yönlendirme

## Teknik Detaylar

- **Framework**: Streamlit
- **Veri İşleme**: Pandas DataFrames
- **Görselleştirme**: Streamlit native components
- **Veri Kaynağı**: FedEx resmi ücret tarifeleri

## Katkıda Bulunma

1. Fork edin
2. Feature branch oluşturun (`git checkout -b feature/yeni-ozellik`)
3. Değişikliklerinizi commit edin (`git commit -am 'Yeni özellik ekle'`)
4. Branch'inizi push edin (`git push origin feature/yeni-ozellik`)
5. Pull Request oluşturun

## Lisans

Bu proje MIT lisansı altında lisanslanmıştır.

## İletişim

Sorularınız için issue açabilir veya doğrudan iletişime geçebilirsiniz.

---

⚡ **Streamlit ile geliştirilmiştir** | 🚚 **FedEx ücret karşılaştırması** | 🌍 **5 ülke desteği**
