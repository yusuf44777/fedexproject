import streamlit as st
import pandas as pd

def create_country_comparison_tables():
    """Ülke ve hizmet karşılaştırma tabloları oluşturur"""
    st.title("FedEx Ülke ve Hizmet Karşılaştırması")
    
    # Ana karşılaştırma tablosu
    create_main_comparison_table()
    
    # Hizmet türü karşılaştırması
    create_service_comparison_tables()
    
    # Detaylı ülke bilgileri
    create_detailed_country_info()

def create_main_comparison_table():
    """Ana ülke karşılaştırma tablosu"""
    st.header("Ülkeler Arası Genel Karşılaştırma")
    
    # Ana karşılaştırma verileri
    comparison_data = [
        {
            "Ülke": "Hollanda",
            "Bölge": "Avrupa",
            "KDV/Vergi": "21%",
            "Ücretsiz Kalem": "5",
            "Ek Kalem Ücreti": "€8.00",
            "Depolama (Günlük)": "€10.00",
            "Özel Notlar": "AB üyesi, EORI zorunlu",
            "Para Birimi": "EUR"
        },
        {
            "Ülke": "Birleşik Krallık",
            "Bölge": "Avrupa",
            "KDV/Vergi": "20%",
            "Ücretsiz Kalem": "5",
            "Ek Kalem Ücreti": "£5.00",
            "Depolama (Günlük)": "£10.00",
            "Özel Notlar": "Brexit sonrası, UKCA gerekli",
            "Para Birimi": "GBP"
        },
        {
            "Ülke": "Amerika Birleşik Devletleri",
            "Bölge": "Amerika",
            "KDV/Vergi": "Değişken",
            "Ücretsiz Kalem": "3",
            "Ek Kalem Ücreti": "$3.50",
            "Depolama (Günlük)": "$0.08/kg + $20",
            "Özel Notlar": "De minimis $800",
            "Para Birimi": "USD"
        },
        {
            "Ülke": "Avustralya",
            "Bölge": "Asya Pasifik",
            "KDV/Vergi": "10% GST",
            "Ücretsiz Kalem": "N/A",
            "Ek Kalem Ücreti": "N/A",
            "Depolama (Günlük)": "AUD $38.50",
            "Özel Notlar": "Katı biyogüvenlik",
            "Para Birimi": "AUD"
        },
        {
            "Ülke": "Kanada",
            "Bölge": "Amerika",
            "KDV/Vergi": "5-15% GST/HST",
            "Ücretsiz Kalem": "3",
            "Ek Kalem Ücreti": "CAD $5.30",
            "Depolama (Günlük)": "$0.25/lb",
            "Özel Notlar": "NAFTA/USMCA avantajları",
            "Para Birimi": "CAD"
        }
    ]
    
    df_comparison = pd.DataFrame(comparison_data)
    st.dataframe(df_comparison, use_container_width=True)

def create_service_comparison_tables():
    """Express vs Standard hizmet karşılaştırması"""
    st.header("Express vs Standard Hizmet Karşılaştırması")
    
    # ABD için Express vs Standard
    st.subheader("Amerika Birleşik Devletleri")
    us_comparison = [
        {
            "Hizmet": "Kayıt Kopyası",
            "Express": "$2.10",
            "Standard": "$2.00",
            "Fark": "$0.10"
        },
        {
            "Hizmet": "Canlı Kayıt İşleme",
            "Express": "$27.00",
            "Standard": "$20.00",
            "Fark": "$7.00"
        },
        {
            "Hizmet": "Ek Kayıt Kalemleri",
            "Express": "$3.50 (3+ kalem)",
            "Standard": "$3.50 (3+ kalem)",
            "Fark": "Aynı"
        },
        {
            "Hizmet": "Depolama",
            "Express": "$0.08/kg + $20 (3. gün sonrası)",
            "Standard": "Mevcut değil",
            "Fark": "Sadece Express'te"
        },
        {
            "Hizmet": "Geçici İthalat",
            "Express": "$150",
            "Standard": "Mevcut değil",
            "Fark": "Sadece Express'te"
        }
    ]
    
    df_us = pd.DataFrame(us_comparison)
    st.dataframe(df_us, use_container_width=True)
    
    # Kanada için Express vs Standard
    st.subheader("Kanada")
    canada_comparison = [
        {
            "Hizmet": "Depolama",
            "Express": "$0.25/lb/gün (48 saat sonrası)",
            "Standard": "Mevcut değil",
            "Fark": "Sadece Express'te"
        },
        {
            "Hizmet": "Kayıt Sonrası Düzeltme",
            "Express": "$75 CAD veya değerin %8'i",
            "Standard": "Mevcut değil",
            "Fark": "Sadece Express'te"
        },
        {
            "Hizmet": "Mesai Sonrası Gümrükleme",
            "Express": "FedEx: $120 CAD, Harici: $50 CAD",
            "Standard": "Mevcut değil",
            "Fark": "Sadece Express'te"
        },
        {
            "Hizmet": "Geçici İthalat",
            "Express": "$120 CAD",
            "Standard": "Mevcut değil",
            "Fark": "Sadece Express'te"
        },
        {
            "Hizmet": "Gümrükleme Kayıt Ücreti",
            "Express": "Değer bazlı ($0-$3300+ arası)",
            "Standard": "Değer bazlı yapı",
            "Fark": "Her ikisinde de mevcut"
        }
    ]
    
    df_canada = pd.DataFrame(canada_comparison)
    st.dataframe(df_canada, use_container_width=True)

def create_detailed_country_info():
    """Detaylı ülke bilgi tabloları"""
    st.header("Detaylı Ülke Bilgileri")
    
    # Ülke seçimi
    countries = ["Hollanda", "Birleşik Krallık", "Amerika Birleşik Devletleri", "Avustralya", "Kanada"]
    selected_country = st.selectbox("Ülke Seçin:", countries)
    
    # Ülkeye göre detaylı bilgi göster
    if selected_country == "Hollanda":
        show_netherlands_details()
    elif selected_country == "Birleşik Krallık":
        show_uk_details()
    elif selected_country == "Amerika Birleşik Devletleri":
        show_us_details()
    elif selected_country == "Avustralya":
        show_australia_details()
    elif selected_country == "Kanada":
        show_canada_details()

def show_netherlands_details():
    """Hollanda detaylı bilgileri"""
    st.subheader("Hollanda - Detaylı Bilgiler")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.write("**Ana Ücretler:**")
        nl_fees = [
            {"Hizmet": "KDV", "Ücret": "21% (standart oran)"},
            {"Hizmet": "Gümrük vergisi", "Ücret": "Tarife sınıflandırmasına göre değişir"},
            {"Hizmet": "Ek Kalem Ücretleri (6+)", "Ücret": "€8.00/kalem"},
            {"Hizmet": "Gümrük Altında Transit", "Ücret": "€45.00/gönderi"},
            {"Hizmet": "İade Malları", "Ücret": "€42.00/gönderi"},
            {"Hizmet": "Geçici İthalat", "Ücret": "€42.00/gönderi"},
            {"Hizmet": "Depolama (3 gün sonrası)", "Ücret": "€10.00/gün"},
            {"Hizmet": "Diğer Devlet Kurumları", "Ücret": "€40.00 + geçiş ücretleri"},
            {"Hizmet": "Özel Hizmet", "Ücret": "€50.00/saat (min €40.00)"},
            {"Hizmet": "Ön Ödeme (€0.01-€50.00)", "Ücret": "V&H'ın %30'u (min €5.00)"},
            {"Hizmet": "Ön Ödeme (€50.00-€600.00)", "Ücret": "€15.00"},
            {"Hizmet": "Ön Ödeme (€600.00+)", "Ücret": "V&H'ın %2.5'i"},
            {"Hizmet": "Kayıt Sonrası Düzeltme", "Ücret": "€90.00/gönderi"},
            {"Hizmet": "Ödeme Ücreti (€0.01-€50.00)", "Ücret": "V&H'ın %30'u (min €8.00)"},
            {"Hizmet": "Ödeme Ücreti (€50.00-€600.00)", "Ücret": "€15.00"},
            {"Hizmet": "Ödeme Ücreti (€600.00+)", "Ücret": "V&H'ın %2.5'i"},
            {"Hizmet": "Vergi ve Harç Yönlendirme", "Ücret": "€18.00 veya V&H'ın %2.5'i"}
        ]
        df_nl_fees = pd.DataFrame(nl_fees)
        st.dataframe(df_nl_fees, use_container_width=True, height=600)
    
    with col2:
        st.write("**Gerekli Belgeler:**")
        nl_reqs = [
            "Ticari fatura",
            "EORI numarası",
            "Menşe şahadetnâmesi",
            "CE işaretleme sertifikaları",
            "İthalat lisansları", 
            "MSDS (kimyasallar)",
            "REACH kaydı",
            "Fitosanitasyon sertifikaları",
            "Sağlık sertifikaları",
            "Tarife sınıflandırması"
        ]
        for req in nl_reqs:
            st.write(f"• {req}")

def show_uk_details():
    """İngiltere detaylı bilgileri"""
    st.subheader("Birleşik Krallık - Detaylı Bilgiler")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.write("**Ana Ücretler:**")
        uk_fees = [
            {"Hizmet": "KDV", "Ücret": "20% (standart oran)"},
            {"Hizmet": "Gümrük vergisi", "Ücret": "Tarife sınıflandırmasına göre değişir"},
            {"Hizmet": "Ek Kalem Ücretleri (5+)", "Ücret": "£5.00/kalem"},
            {"Hizmet": "Depolama (3 gün sonrası)", "Ücret": "£10.00/gün"},
            {"Hizmet": "Kargo Gümrükleme", "Ücret": "£35.00/gönderi"},
            {"Hizmet": "İade Malları", "Ücret": "£21.00/gönderi"},
            {"Hizmet": "Diğer Devlet Kurumları", "Ücret": "£27.00 + geçiş ücretleri"},
            {"Hizmet": "Geçici İthalat", "Ücret": "£25.00/gönderi"},
            {"Hizmet": "Özel Hizmet", "Ücret": "£45.00/saat (min £30.00)"},
            {"Hizmet": "Ön Ödeme (£0.01-£42.50)", "Ücret": "V&H'ın %30'u (min £4.25)"},
            {"Hizmet": "Ön Ödeme (£42.50-£510.00)", "Ücret": "£12.75"},
            {"Hizmet": "Ön Ödeme (£510.00+)", "Ücret": "V&H'ın %2.5'i"},
            {"Hizmet": "Kayıt Sonrası Düzeltme", "Ücret": "£60.00/gönderi"},
            {"Hizmet": "Ödeme Ücreti (£0.01-£42.50)", "Ücret": "V&H'ın %30'u (min £6.65)"},
            {"Hizmet": "Ödeme Ücreti (£42.50-£510.00)", "Ücret": "£12.75"},
            {"Hizmet": "Ödeme Ücreti (£510.00+)", "Ücret": "V&H'ın %2.5'i"},
            {"Hizmet": "İthalat İzinleri ve Lisansları", "Ücret": "£40.00/gönderi"},
            {"Hizmet": "Vergi ve Harç Yönlendirme", "Ücret": "Min £15.00 veya V&H'ın %2.5'i"},
            {"Hizmet": "Tutma ve Bildirim", "Ücret": "£2.50/gönderi"}
        ]
        df_uk_fees = pd.DataFrame(uk_fees)
        st.dataframe(df_uk_fees, use_container_width=True, height=600)
    
    with col2:
        st.write("**Brexit Sonrası Özel Notlar:**")
        uk_notes = [
            "UKCA işaretleme gerekli",
            "AB'den ayrı gümrük prosedürleri",
            "EORI numarası zorunlu",
            "Kuzey İrlanda Protokolü",
            "CHIEF sistemi → CDS geçiş",
            "REACH UK kaydı gerekli"
        ]
        for note in uk_notes:
            st.write(f"• {note}")

def show_us_details():
    """ABD detaylı bilgileri"""
    st.subheader("Amerika Birleşik Devletleri - Detaylı Bilgiler")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.write("**Express Hizmet Ücretleri:**")
        us_express = [
            {"Hizmet": "Ek Kayıt Kalemleri (3+)", "Ücret": "$3.50/kalem"},
            {"Hizmet": "Kayıt Kopyası", "Ücret": "$2.10/kayıt"},
            {"Hizmet": "Devlet Kayıtları", "Ücret": "$53.00/gönderi"},
            {"Hizmet": "Canlı Kayıt İşleme", "Ücret": "$27.00/gönderi"},
            {"Hizmet": "Özel Aracılık İşleme", "Ücret": "Talep üzerine fiyatlandırma"},
            {"Hizmet": "Depolama (3 gün sonrası)", "Ücret": "$0.08/kg/gün + $20 taban"},
            {"Hizmet": "ATFE Gümrükleme", "Ücret": "$74.00/gönderi"},
            {"Hizmet": "FWS Gümrükleme", "Ücret": "Gerçek ücret + $22 idari"},
            {"Hizmet": "FDA Gümrükleme", "Ücret": "$27.50/gönderi"},
            {"Hizmet": "FDA Ön Bildirim", "Ücret": "$13.50/gönderi"},
            {"Hizmet": "Komisyoncu Belge Transferi", "Ücret": "$51.00/gönderi"},
            {"Hizmet": "Gümrük Altında Transit", "Ücret": "$90.00/gönderi"},
            {"Hizmet": "Ödeme Ücreti (≤$800)", "Ücret": "$4.50 veya V&H'ın %2'si"},
            {"Hizmet": "Ödeme Ücreti (>$800)", "Ücret": "$14.00 veya V&H'ın %2'si"},
            {"Hizmet": "Geçici İthalat", "Ücret": "$150.00/gönderi"},
            {"Hizmet": "V&H Yönlendirme (≤$800)", "Ücret": "$8.50 veya V&H'ın %2'si"},
            {"Hizmet": "V&H Yönlendirme (>$800)", "Ücret": "$27.00 veya V&H'ın %2'si"}
        ]
        df_us_express = pd.DataFrame(us_express)
        st.dataframe(df_us_express, use_container_width=True, height=600)
    
    with col2:
        st.write("**Standard Hizmet Ücretleri:**")
        us_standard = [
            {"Hizmet": "Ek Kayıt Kalemleri (3+)", "Ücret": "$3.50/kalem"},
            {"Hizmet": "FWS Gümrükleme", "Ücret": "Gerçek ücret + $22 idari"},
            {"Hizmet": "FDA Gümrükleme", "Ücret": "$27.50/gönderi"},
            {"Hizmet": "Diğer Devlet Kurumu", "Ücret": "Değişken"},
            {"Hizmet": "Ödeme Ücreti (≤$800)", "Ücret": "$4.50 veya V&H'ın %2'si"},
            {"Hizmet": "Ödeme Ücreti (>$800)", "Ücret": "$14.00 veya V&H'ın %2'si"},
            {"Hizmet": "Gümrükleme Kayıt Ücreti", "Ücret": "Değer bazlı ($0-$2000+)"},
            {"Hizmet": "Canlı Kayıt İşleme", "Ücret": "$20.00/gönderi"},
            {"Hizmet": "Özel Aracılık İşleme", "Ücret": "Talep üzerine fiyatlandırma"},
            {"Hizmet": "Kayıt Kopyası", "Ücret": "$2.00/kayıt"},
            {"Hizmet": "V&H Yönlendirme (≤$800)", "Ücret": "$8.50 veya V&H'ın %2'si"},
            {"Hizmet": "V&H Yönlendirme (>$800)", "Ücret": "$27.00 veya V&H'ın %2'si"}
        ]
        df_us_standard = pd.DataFrame(us_standard)
        st.dataframe(df_us_standard, use_container_width=True, height=400)
        
        st.write("**Standard vs Express Farkları:**")
        differences = [
            "Kayıt Kopyası: $2.00 (Express: $2.10)",
            "Canlı Kayıt İşleme: $20.00 (Express: $27.00)",
            "Geçici İthalat mevcut değil",
            "Depolama hizmeti mevcut değil",
            "Devlet Kayıtları mevcut değil",
            "FDA Ön Bildirim mevcut değil",
            "Komisyoncu Belge Transferi mevcut değil",
            "Gümrük Altında Transit mevcut değil",
            "Kanada'dan 5 ücretsiz kalem (Express: 3)"
        ]
        for diff in differences:
            st.write(f"• {diff}")

def show_australia_details():
    """Avustralya detaylı bilgileri"""
    st.subheader("Avustralya - Detaylı Bilgiler")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.write("**Ana Ücretler:**")
        au_fees = [
            {"Hizmet": "GST", "Ücret": "10% (vergilendirilebilir değer)"},
            {"Hizmet": "Gümrük vergisi", "Ücret": "Tarife sınıflandırmasına göre değişir"},
            {"Hizmet": "Vergi ve Harç Değişikliği", "Ücret": "AUD $132"},
            {"Hizmet": "Elektronik Kayıt ($1K-$9.9K)", "Ücret": "AUD $95"},
            {"Hizmet": "Elektronik Kayıt ($10K+)", "Ücret": "AUD $197"},
            {"Hizmet": "Karantina Belge İşleme", "Ücret": "AUD $37"},
            {"Hizmet": "Karantina Belge İşleme ve İnceleme", "Ücret": "AUD $99"},
            {"Hizmet": "Karantina Hafta Sonu/Mesai", "Ücret": "AUD $120"},
            {"Hizmet": "Avans Ücreti", "Ücret": "AUD $20 veya %2.9"},
            {"Hizmet": "ROD Ücreti", "Ücret": "%2.9 veya AUD $20"},
            {"Hizmet": "Komisyoncu Belge Transferi", "Ücret": "AUD $55/gönderi"},
            {"Hizmet": "Depolama (BSO - 3 gün sonrası)", "Ücret": "AUD $38.50/gün"},
            {"Hizmet": "Vergi ve Harç Yönlendirme", "Ücret": "Min AUD $30 veya %2.9"}
        ]
        df_au_fees = pd.DataFrame(au_fees)
        st.dataframe(df_au_fees, use_container_width=True, height=450)
    
    with col2:
        st.write("**Biyogüvenlik Gereklilikleri:**")
        au_bio = [
            "Tüm ahşap ISPM-15 uyumlu",
            "Gıda ürünleri detaylı bileşen listesi",
            "Karantina beyanı zorunlu",
            "AQIS katılımı gerekli",
            "Bitki ürünleri için sertifika",
            "Hayvan ürünleri için sağlık sertifikası",
            "Katı kontrol prosedürleri"
        ]
        for bio in au_bio:
            st.write(f"• {bio}")

def show_canada_details():
    """Kanada detaylı bilgileri"""
    st.subheader("Kanada - Detaylı Bilgiler")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.write("**Express Hizmet Ücretleri:**")
        ca_express = [
            {"Hizmet": "GST/HST", "Ücret": "İl'e göre %5-15 değişir"},
            {"Hizmet": "Gümrük vergisi", "Ücret": "Tarife sınıflandırmasına göre değişir"},
            {"Hizmet": "Ek Kalem (3+)", "Ücret": "CAD $5.30/kalem"},
            {"Hizmet": "Depolama (48 saat sonrası)", "Ücret": "lb başına günde $0.25 CAD"},
            {"Hizmet": "Kayıt Sonrası Düzeltme", "Ücret": "$75 CAD veya değerin %8'i"},
            {"Hizmet": "Diğer Devlet Kurumu", "Ücret": "Kayıt başına $16.50 CAD"},
            {"Hizmet": "Hesap Güvenlik İşleme", "Ücret": "Serbest Bırakma: $3, Onaylama: $7, İkisi: $10 CAD"},
            {"Hizmet": "Mesai Sonrası (FedEx)", "Ücret": "$120 CAD"},
            {"Hizmet": "Mesai Sonrası (Harici)", "Ücret": "$50 CAD"},
            {"Hizmet": "İş Kayıt Numarası Başvurusu", "Ücret": "Kayıt başına $5 CAD"},
            {"Hizmet": "Faks Ücreti", "Ücret": "Yerel: $3, Şehirlerarası: $4 CAD"},
            {"Hizmet": "İthalat İzni", "Ücret": "Tek: $25 + CBSA, Çoklu: $10 + CBSA"},
            {"Hizmet": "Düşük Değerli Gönderi Belge", "Ücret": "$4 CAD"},
            {"Hizmet": "Kurye Düşük Değerli Kayıt Düzeltme", "Ücret": "Kayıt başına $25 CAD"},
            {"Hizmet": "Düşük Değerli Gönderi Kayıt İstisnası", "Ücret": "$4 CAD"},
            {"Hizmet": "Geçici İthalat", "Ücret": "Kayıt başına $120 CAD"},
            {"Hizmet": "Gümrük Altında Transfer", "Ücret": "Kayıt başına $40 CAD"},
            {"Hizmet": "ROD Ücreti", "Ücret": "CAD $11.40 + Geçerli Vergi"},
            {"Hizmet": "Ödeme Ücreti", "Ücret": "V&H'ın %2.95'i veya $11.40 CAD"}
        ]
        df_ca_express = pd.DataFrame(ca_express)
        st.dataframe(df_ca_express, use_container_width=True, height=650)
    
    with col2:
        st.write("**Standard Hizmet Ücretleri:**")
        ca_standard = [
            {"Hizmet": "GST/HST", "Ücret": "İl'e göre %5-15 değişir"},
            {"Hizmet": "Gümrük vergisi", "Ücret": "Tarife sınıflandırmasına göre değişir"},
            {"Hizmet": "Ek Kalem (3+)", "Ücret": "CAD $5.30/kalem"},
            {"Hizmet": "Diğer Devlet Kurumu", "Ücret": "Kayıt başına $16.50 CAD"},
            {"Hizmet": "Faks Ücreti", "Ücret": "Yerel: $3, Şehirlerarası: $4 CAD"},
            {"Hizmet": "Ödeme Ücreti", "Ücret": "V&H'ın %2.95'i veya $11.40 CAD"},
            {"Hizmet": "Gümrükleme Kayıt Ücreti", "Ücret": "Değer bazlı ($0-$3300+)"}
        ]
        df_ca_standard = pd.DataFrame(ca_standard)
        st.dataframe(df_ca_standard, use_container_width=True, height=250)
        
        st.write("**Değer Bazlı Gümrükleme Kayıt Ücretleri:**")
        ca_clearance_fees = [
            {"Değer Aralığı (CAD)", "Ücret"},
            {"$0-$40", "$0.00"},
            {"$40.01-$60", "$17.25"},
            {"$60.01-$100", "$21.25"},
            {"$100.01-$150", "$27.50"},
            {"$150.01-$200", "$32.25"},
            {"$200.01-$500", "$54.00"},
            {"$500.01-$1000", "$62.00"},
            {"$1000.01-$1600", "$71.50"},
            {"$1600.01-$3300", "$82.00"},
            {"$3300.01+", "$82 + her ek $1000 için $7.50"}
        ]
        df_ca_clearance = pd.DataFrame(ca_clearance_fees)
        st.dataframe(df_ca_clearance, use_container_width=True, height=350)

# Ana fonksiyon
if __name__ == "__main__":
    create_country_comparison_tables()

# Kapsamlı ülke verileri (güncel FedEx ücret yapısına dayalı)
countries_data = {
                "Netherlands": {
                    "name": "Hollanda",
                    "region": "Avrupa",
                    "content": [
                        "AB gümrük düzenlemeleri uygulanır",
                        "Ticari ithalatlar için EORI numarası gereklidir",
                        "Gümrük Birliği Kodu (UCC) uyumluluğu",
                        "Düzenli ithalatlar için KDV kaydı gerekli olabilir",
                        "Uygulanabilir ürünler için CE işaretleme gereklilikleri",
                        "Kimyasallar için REACH mevzuatı uyumluluğu",
                        "Hollanda gümrük otoritesi (Douane) gözetimi"
                    ],
                    "fees": [
                        "KDV: Vergilendirilebilir değer üzerinden %21 (standart oran)",
                        "Gümrük vergisi: Tarife sınıflandırmasına göre değişir",
                        "Ek Kalem Ücretleri: 6. kalemden itibaren her ek kalem için €8.00 - Gönderi farklı tarife sınıflandırması gerektiren birden fazla emtia, farklı ülkelerden aynı emtialar, birden fazla ticari fatura veya her kalem için ayrı giriş talep edildiğinde uygulanır",
                        "Gümrük Altında Transit: Gönderi başına €45.00 - Talep üzerine, FedEx gerekli transfer belgelerini hazırlar ve gelen gönderileri varış noktasından kendi kendine gümrükleme veya FedEx dışında bir gümrük müşavirliği kullanımı için belirtilen yere taşır",
                        "İade Malları: Gönderi başına €42.00 - FedEx, onarım, işleme, test, değerlendirme, ticaret fuarları için geçici olarak ihraç edilen veya değiştirilmeden ihraç ülkesine iade edilen malların iadesini organize eder. İthalatçının gerekli ihracat belgeleriyle vergi/harç muafiyeti talep etmesine olanak sağlar",
                        "Geçici İthalat: Gönderi başına €42.00 - Gönderilerin belirli bir süre için geçici olarak ithal edilmesi talep edildiğinde, FedEx Gümrük tarafından belirtilen gerekli belgeleri hazırlayarak ve dosyalayarak ithalat sürecini koordine eder",
                        "Depolama: Üç iş günü sonrasında paket başına iş günü başına €10.00 - Gönderi yayınlanan süre sınırını aşarak gümrükleme yerinde temizlenmemiş kalırsa FedEx depolama ücreti talep edebilir",
                        "Diğer Devlet Kurumları: Gönderi başına €40.00 artı geçiş ücretleri - Devlet kurumu tarafından belge doğrulama veya kimlik kontrolü gerektiğinde uygulanan ücret; yerel konseyler veya ticari ajanslar dahil olmak üzere aynı gönderi için birden fazla kurumdan ücret alınabilir. FedEx tüm harici kurumlardan gelen ücretleri aktarır",
                        "Özel Hizmet: Saatte €50.00, minimum yarım saatte €40.00 - FedEx özel raporlar oluşturma, paketleri açma/etiketleme gibi ek hizmetler sağlar. Hizmet uygulamasından önce hem FedEx hem de ödeyen saatlik masrafları kabul etmelidir",
                        "Ön Ödeme (Doğrudan Ödeme İşlemi): €0.01-€50.00: Vergi/Harç'ın %30'u (min €5.00), €50.00-€600.00: €15.00, €600.00+: Vergi/Harç'ın %2.5'i - Gönderilerin serbest bırakılması ve gümrük ücretlerinin ödenmesi için doğrudan ödeme sürecinin başlatılması ücreti. Kredi riski olan ödeyenler veya çok yüksek değerli gönderiler odaklı hizmet",
                        "Kayıt Sonrası Düzeltme: Gönderi başına €90.00 - Müşteri talebi üzerine, FedEx daha önce sağlanan bilgilerdeki kaydı düzeltmek için Gümrük'e Kayıt Düzeltmesi sunar. Fazla ödemenin iadesi veya Gümrük'e ek vergi/harç borcu artı FedEx ücreti ile sonuçlanabilir",
                        "Ödeme Ücreti: €0.01-€50.00: Vergi/Harç'ın %30'u (min €8.00), €50.00-€600.00: €15.00, €600.00+: Vergi/Harç'ın %2.5'i - FedEx, gümrük kurumuna zamanında ödemeyi sağlamak için müşteri adına geçerli vergiler, harçlar ve düzenleyici ücretleri öder. Ödeyen, ödenen toplam tutar artı ek ücret için sorumludur",
                        "Vergi ve Harç Yönlendirme Ücreti: €18.00 veya V&H'ın %2.5'i hangisi büyükse - Gönderici hedef ülke dışında vergi/harç ödemesi için üçüncü taraf faturalandırma seçeneğini seçtiğinde Ödeme Ücreti yerine uygulanır"
                    ],
                    "requirements": [
                        "Detaylı emtia açıklaması içeren ticari fatura",
                        "AB'ye ticari ithalatlar için EORI numarası",
                        "Tercihli gümrük vergisi oranları için menşe şahadetnâmesi (EUR.1, ATR)",
                        "Uygulanabilir yerlerde uygunluk sertifikaları (CE işaretlemesi)",
                        "Kısıtlı mallar için ithalat lisansları",
                        "Kimyasallar için Malzeme Güvenlik Bilgi Formu (MSDS)",
                        "Kimyasal maddeler için REACH kaydı",
                        "Bitki ürünleri için fitosanitasyon sertifikaları",
                        "Hayvan ürünleri için sağlık sertifikaları",
                        "Uygun tarife sınıflandırması (Kombine Nomenclature)"
                    ],
                    "special_notes": [
                        "AB gümrük birliği avantajları - iç gümrük vergileri yok",
                        "Ticari ithalatlar için EORI numarası zorunlu",
                        "Ek Kalem Ücretleri 6. kalemden itibaren başlar (5 ücretsiz kalem)",
                        "Depolama ücretleri 3 iş günü hoşgörü süresi sonrası uygulanır",
                        "İade malları hizmeti uygun belgelerle vergi/harç muafiyeti sağlar",
                        "Belirtilen süre için geçici ithalat mevcut",
                        "Kredi riski yönetimi için ön ödeme hizmeti mevcut",
                        "Kayıt düzeltmeleri için kayıt sonrası ayarlamalar mümkün",
                        "Yönlendirme ücreti ile üçüncü taraf faturalandırma seçeneği mevcut",
                        "Özelleştirilmiş hizmetler saatlik oranlar için önceden anlaşma gerektirir",
                        "Diğer devlet kurumu ücretleri geçiş ücretlerini içerir"
                    ]
                },
                "United Kingdom": {
                    "name": "Birleşik Krallık",
                    "region": "Avrupa",
                    "content": [
                        "Brexit sonrası gümrük düzenlemeleri uygulanır",
                        "Uygulanabilir ürünler için UKCA işaretleme gereklilikleri",
                        "İngiltere gümrük otoritesi (HMRC) gözetimi",
                        "Kuzey İrlanda Protokolü değerlendirmeleri",
                        "GB-NI ticaret düzenlemeleri",
                        "CHIEF sistemi (CDS - Gümrük Beyan Servisine geçiş)",
                        "Ticari ithalatlar için EORI numarası gerekli"
                    ],
                    "fees": [
                        "KDV: Vergilendirilebilir değer üzerinden %20 (standart oran)",
                        "Gümrük vergisi: Tarife sınıflandırmasına göre değişir",
                        "Ek Kalem Ücretleri: 5 kalemde fazlaysa kalem başına £5.00 - Gönderi farklı tarife sınıflandırması gerektiren birden fazla emtia, farklı ülkelerden aynı emtialar, birden fazla ticari fatura veya her kalem için ayrı giriş talep edildiğinde uygulanır",
                        "Depolama: Üç iş günü sonrasında paket başına iş günü başına £10.00 - Gönderi yayınlanan süre sınırını aşarak temizlenmemiş kalırsa uygulanır",
                        "Kargo Gümrükleme: Gönderi başına £35.00 - Kargo ve üçüncü taraf gönderileri için tam uzmanlık kullanan FedEx Gümrük Müşavirliği Hizmetleri",
                        "İade Malları: Gönderi başına £21.00 - Onarım, işleme, test, değerlendirme, ticaret fuarları için geçici olarak ihraç edilen veya değiştirilmeden vergi/harç muafiyeti talep etmek için iade edilen mallar için",
                        "Diğer Devlet Kurumları: Gönderi başına £27.00 artı geçiş ücretleri - Devlet kurumları tarafından belge doğrulama veya kimlik kontrolü gerektiğinde uygulanır",
                        "Geçici İthalat: Gönderi başına £25.00 - Belirli süre için gerekli gümrük belgeleriyle geçici ithalat sürecinin koordinasyonu",
                        "Özel Hizmet: Saatte £45.00, minimum yarım saatte £30.00 - Özel raporlar, paketleri açma/etiketleme gibi ek hizmetler (önceden anlaşma gerekir)",
                        "Ön Ödeme (Doğrudan Ödeme İşlemi): £0.01-£42.50: Vergi/Harç'ın %30'u (min £4.25), £42.50-£510.00: £12.75, £510.00+: Vergi/Harç'ın %2.5'i - Kredi riski olan müşteriler veya yüksek değerli gönderiler için doğrudan ödeme süreci ücreti",
                        "Kayıt Sonrası Düzeltme: Gönderi başına £60.00 - Önceki bilgiler için kayıt düzeltme hizmeti, iade veya ek vergi/harç borcu ile sonuçlanabilir",
                        "Ödeme Ücreti: £0.01-£42.50: Vergi/Harç'ın %30'u (min £6.65), £42.50-£510.00: £12.75, £510.00+: Vergi/Harç'ın %2.5'i - FedEx vergileri, harçları ve düzenleyici ücretleri ödediğinde uygulanır",
                        "İthalat İzinleri ve Lisansları: Gönderi başına £40.00 - Yerel düzenleyici kurum tarafından gerekli görülen ithalat izni veya lisansının alınması veya yenilenmesi ücreti",
                        "Vergi ve Harç Yönlendirme Ücreti: Minimum £15.00 veya V&H'ın %2.5'i - Hedef ülke dışında vergi/harç ödemesi için üçüncü taraf faturalandırma seçeneği seçildiğinde Ödeme Ücreti yerine uygulanır",
                        "Tutma ve Bildirim: Gönderi başına £2.50 - Özel gümrük temizleme talimatları için gelen gönderileri durdurma hizmeti (FedEx gümrükleme, kendi kendine gümrükleme veya üçüncü taraf komisyoncu)"
                    ],
                    "requirements": [
                        "Detaylı emtia açıklaması içeren ticari fatura",
                        "İngiltere'ye ticari ithalatlar için EORI numarası",
                        "Tercihli gümrük vergisi oranları için menşe şahadetnâmesi",
                        "Uygulanabilir yerlerde UKCA işaretleme sertifikaları (Brexit sonrası)",
                        "Kısıtlı mallar için ithalat lisansları",
                        "Kimyasallar için Malzeme Güvenlik Bilgi Formu (MSDS)",
                        "Kimyasal maddeler için REACH UK kaydı",
                        "Bitki ürünleri için fitosanitasyon sertifikaları",
                        "Hayvan ürünleri için sağlık sertifikaları",
                        "Uygun tarife sınıflandırması (İngiltere Ticaret Tarifesi)",
                        "Uygulanabilir yerlerde Kuzey İrlanda Protokolü uyumluluğu"
                    ],
                    "special_notes": [
                        "Brexit sonrası düzenlemeler - AB gümrük prosedürlerinden ayrı",
                        "Ticari ithalatlar için EORI numarası zorunlu",
                        "Ek Kalem Ücretleri 6. kalemden itibaren başlar (5 ücretsiz kalem)",
                        "Depolama ücretleri 3 iş günü hoşgörü süresi sonrası uygulanır",
                        "Üçüncü taraf gönderileri için kargo temizleme hizmeti mevcut",
                        "İade malları hizmeti uygun belgelerle vergi/harç muafiyeti sağlar",
                        "Belirtilen süre için geçici ithalat mevcut",
                        "Kredi riski yönetimi için ön ödeme hizmeti mevcut",
                        "Kayıt düzeltmeleri için kayıt sonrası ayarlamalar mümkün",
                        "İthalat izinleri ve lisansları hizmeti mevcut",
                        "Yönlendirme ücreti ile üçüncü taraf faturalandırma seçeneği mevcut",
                        "Gümrük temizleme talimat yönetimi için Tutma ve Bildirim hizmeti",
                        "Kuzey İrlanda Protokol kapsamında özel düzenlemelere sahip",
                        "Birçok ürün için UKCA işaretlemesi gerekli (CE işaretlemesinin yerini alır)",
                        "CHIEF sistemi Gümrük Beyan Servisi (CDS) ile değiştiriliyor"
                    ]
                },
                "United States": {
                    "name": "Amerika Birleşik Devletleri",
                    "region": "Amerika",
                    "content": [
                        "CBP (ABD Gümrük ve Sınır Koruma) düzenlemeleri uygulanır",
                        "ACE (Otomatik Ticari Ortam) sistemi kullanılır",
                        "Okyanus gönderileri için ISF (İthalatçı Güvenlik Dosyalaması) gerekli",
                        "Çoklu düzenleyici kurum katılımı (FDA, USDA, FWS, ATFE, vb.)",
                        "MPF (Mal İşleme Ücreti) ve HMF (Liman Bakım Ücreti) uygulanabilir",
                        "De minimis eşiği: Gümrük vergisinden muaf tedavi için 800 $",
                        "Bölüm 321 düşük değerli gönderi prosedürleri"
                    ],
                    "fees": [
                        "Gümrük vergisi tarife sınıflandırması ve ticaret anlaşmalarına göre değişir",
                        "MPF (Mal İşleme Ücreti): Gümrük değerinin %0.3464'ü (min 27.23 $, maks 528.33 $)",
                        "HMF (Liman Bakım Ücreti): Okyanus gönderileri için %0.125"
                    ],
                    "express_fees": [
                        "Ek Kayıt Kalemleri: Üç (3) kalemden fazlası için kalem başına $3.50 - Gönderi aşağıdaki durumlarda ek tarife sınıflandırması gerektirebilir: 1) Yayınlanan ücretlerdeki Ücretsiz Kalem sınırının ötesinde bir veya daha fazla tarife sınıflandırması varsa; 2) Aynı emtia birden fazla ülkede üretilmişse; 3) Gümrüğe sunulan birden fazla Ticari Fatura her fatura için ayrı tarife sınıflandırması gerektiriyorsa; 4) Gönderi içindeki her kalem için ayrı kayıt girişi talep ediyorsanız",
                        "Kayıt Kopyası: Kayıt başına $2.10 - Talep üzerine, ABD ithalat belgelerinizin ek kopyalarını kompakt disk (CD) veya elektronik veri değişimi (EDI) yoluyla sağlayabiliriz. Önceki ay için derlenen tüm kayıtlarla birlikte ayda bir kez CD veya EDI iletimi alacaksınız. Bu hizmeti kullanmak için: 1) Kayıt belgelerini elektronik olarak tutmak için gümrük kurumunuz tarafından onaylanmış olmanız ve 2) Özel Aracılık İşleme programı aracılığıyla sunulan Kayıt İmportörü hizmetine kaydolmanız gerekir. Daha fazla bilgi için Hesap Yöneticinizle iletişime geçin. Not: CD seçeneği yeni müşteriler için mevcut değildir",
                        "Devlet Kayıtları: Gönderi başına $53 - Devlet Askeri Sözleşmeleri uyarınca malların girişi için gerektiği gibi özel giriş prosedürlerini kolaylaştıracağız ve/veya sertifika alacağız, böylece ithalatçı Vergisiz muameleden yararlanabilir",
                        "Canlı Kayıt İşleme: Gönderi başına $27 - İthalat için ihracat lisansı (vize) zorunlu olduğunda, gümrük tarafından gerekli görüldüğü şekilde canlı kayıtları işleyeceğiz",
                        "Özel Aracılık İşleme (Eski adıyla Özelleştirilmiş İşleme Hesapları): Talep üzerine fiyatlandırma - Özel Aracılık İşleme, özel uyumluluk ihtiyaçları olan müşteriler için tasarlanmış, geniş bir özel işlem hizmetleri yelpazesi sunan bir programdır. Program, gönderinizin gümrük temizleme yolculuğunda daha fazla kontrol ve görünürlük için kendi Kayıt İmportörünüz olmaya olanak tanır. Diğer temel avantajlar arasında özel destek, benzersiz iş ihtiyaçlarınıza göre uyarlanmış standart işletim prosedürü (SOP) ve My Global Trade Data aracılığıyla ithalat kayıtlarınıza görünürlük ve müşteri raporlama aracı diğer hizmet seçenekleri arasında yer alır. Daha fazla bilgi için Hesap Yöneticinizle iletişime geçin",
                        "Depolama: İş Günü başına kg başına $0.08 artı $20 taban ücret - Gönderi yayınlanan süre sınırını aşarak gümrükleme yerinde temizlenmemiş kalırsa depolama ücreti talep edebiliriz. Yerel not: Ücretler gümrükleme yerinde üçüncü günden itibaren uygulanır",
                        "ABD Alkol, Tütün, Ateşli Silahlar ve Patlayıcılar Bürosu (ATFE) Gümrükleme: Gönderi başına $74 - ABD Alkol, Tütün, Ateşli Silahlar ve Patlayıcılar Bürosu (ATFE) tarafından düzenlenen emtiaların girişi için gerektiği gibi ek işlem sağlayacağız, İç Gelir Servisi Vergi Değerlendirmesi ve gönderinin tüm gerekli ATFE lisans ve izinlerine sahip olduğundan emin olmak için denetim dahil. Lütfen bazı ATFE düzenlemeli ürünlerin FedEx nakliyesi için onaylanmadığını unutmayın. Ayrıntılar için FedEx uluslararası Şartlar ve Koşullar'a bakın",
                        "ABD Balık ve Yaban Hayatı Servisi (FWS) Gümrükleme: FWS tarafından değerlendirilen gerçek ücretler, artı ek $22 FedEx idari ücreti - Canlı hayvanları ve/veya hayvanlardan yaratılan ürünleri içeren emtiaların girişi için gerektiği gibi Balık ve Yaban Hayatı USFWS Form 3-177 (edec) dosyalayacağız ve Balık ve Yaban Hayatı Servisi'ne (FWS) belgeler ve izinler sunacağız",
                        "ABD Gıda ve İlaç İdaresi (FDA) Gümrükleme: Gönderi başına $27.50 - Tıbbi cihazlar, ilaçlar, bilgisayar monitörleri, lazer CD çalarlar, kozmetikler, gözlükler, gıda ve gıda ürünleri veya diğer kontrollü ürünler gibi belirli ticari malların girişi için gerektiği gibi bilgi dosyalayacağız ve onay alacağız",
                        "Gıda ve İlaç Ürünleri için Önceden Bildirim: Gönderi başına $13.50 - Ülkeye ithal edilen veya ülke içinden geçen gıda ve ilaç ürünleri için ABD Gıda ve İlaç İdaresi'ne önceden bildirim gerektiren gönderiler için ek işlem sağlayacağız. İthalat gönderileri için, Önceden Bildirim ücreti mevcut ülke Gıda ve İlaç İdaresi Gümrükleme ücretine ek olarak düzenlenen gıda ve ilaç ürünleri için uygulanır",
                        "Komisyoncu Belge Transferi: Gönderi başına $51.00 - Komisyoncu Belge Transferi, kendi gümrük temizleme departmanınızı kullanarak kendi kendine temizleme veya gelen gönderinizi temizlemek için FedEx dışında bir Aracılık şirketi kullanma esnekliği sağlarken, tüm evrakları size veya seçtiğiniz komisyoncuya sağlıyoruz",
                        "Gümrük Altında Transit: Gönderi başına $90 - Talep üzerine, kendi kendine temizliyorsanız veya gelen gönderinizi temizlemek için FedEx dışında bir Aracılık şirketi kullanıyorsanız, gerekli transfer belgelerini hazırlayacağız ve gelen gönderinizi varış noktasından belirttiğiniz yere taşıyacağız",
                        "Ödeme Ücreti: Gümrük Değeri $800'e eşit veya daha azsa Ücret $4.50 veya Vergi, Harç ve Mal İşleme Ücreti masraflarının %2'si hangisi büyükse. Gümrük Değeri $800'den fazlaysa Ücret $14 veya Vergi, Harç ve Mal İşleme Ücreti masraflarının %2'si hangisi büyükse - Gümrük kurumuna zamanında ödemeyi sağlamak için sizin adınıza geçerli vergileri, harçları ve diğer düzenleyici ücretleri ödeyebiliriz. Ödeyen, ödenen toplam tutardan artı ücretlerde yayınlanan ek ücretten sorumludur",
                        "Geçici İthalat: $150 - Gönderilerin belirli bir süre için geçici olarak ithal edilmesini talep ettiğinizde, Gümrük tarafından belirtilen gerekli belgeleri tavsiye ederek, hazırlayarak ve dosyalayarak ithalat sürecini koordine edeceğiz. Yerel Not: Geçici İthalat hizmeti yeni müşteriler için mevcut değildir",
                        "Vergi ve Harç Yönlendirme Ücreti: Gümrük Değeri $800'e eşit veya daha azsa Ücret $8.5 veya Vergi, Harç ve Mal İşleme Ücreti masraflarının %2'si hangisi büyükse, Gümrük Değeri $800'den fazlaysa Ücret $27 veya Vergi, Harç ve Mal İşleme Ücreti masraflarının %2'si hangisi büyükse - Gönderici vergi ve harçların hedef ülke dışında ödenmesi için üçüncü taraf faturalandırma seçeneğini seçerse Ödeme Ücreti yerine Vergi ve Harç Yönlendirme Ücreti uygulanacaktır"
                    ],
                    "standard_fees": [
                        "Ek Kayıt Kalemleri: Üç (3) kalemden fazlası için kalem başına $3.50 - Gönderi aşağıdaki durumlarda ek tarife sınıflandırması gerektirebilir: 1) Yayınlanan ücretlerdeki Ücretsiz Kalem sınırının ötesinde bir veya daha fazla tarife sınıflandırması varsa; 2) Aynı emtia birden fazla ülkede üretilmişse; 3) Gümrüğe sunulan birden fazla Ticari Fatura her fatura için ayrı tarife sınıflandırması gerektiriyorsa; 4) Gönderi içindeki her kalem için ayrı kayıt girişi talep ediyorsanız",
                        "Balık ve Yaban Hayatı Servisi (FWS) Gümrükleme: FWS tarafından değerlendirilen gerçek ücretler, artı ek $22 FedEx idari ücreti - Canlı hayvanları ve/veya hayvanlardan yaratılan ürünleri içeren emtiaların girişi için gerektiği gibi Balık ve Yaban Hayatı USFWS Form 3-177 (edec) dosyalayacağız ve Balık ve Yaban Hayatı Servisi'ne (FWS) belgeler ve izinler sunacağız",
                        "Gıda ve İlaç İdaresi Gümrükleme: Gönderi başına $27.50 - Tıbbi cihazlar, ilaçlar, bilgisayar monitörleri, lazer CD çalarlar, kozmetikler, gözlükler, gıda ve gıda ürünleri veya diğer kontrollü ürünler gibi belirli ticari malların girişi için gerektiği gibi bilgi dosyalayacağız ve onay alacağız",
                        "Diğer Devlet Kurumu: Değişken - Bir devlet kurumu tarafından belgelerin doğrulanması veya kimlik kontrolü yapılması gerektiğinde ücret veya ücretler uygulanır; ancak yerel konseyler veya ticari ajanslar gibi aynı gönderi için birden fazla kurumdan da ücret alınabilir. FedEx tüm harici kurumlardan alınan ücretleri aktaracaktır",
                        "Ödeme Ücreti: Gümrük Değeri $800'e eşit veya daha azsa Ücret $4.50 veya Vergi, Harç ve Mal İşleme Ücreti masraflarının %2'si hangisi büyükse. Gümrük Değeri $800'den fazlaysa Ücret $14 veya Vergi, Harç ve Mal İşleme Ücreti masraflarının %2'si hangisi büyükse - Gümrük kurumuna zamanında ödemeyi sağlamak için sizin adınıza geçerli vergileri, harçları ve diğer düzenleyici ücretleri ödeyebiliriz. Ödeyen, ödenen toplam tutardan artı ücretlerde yayınlanan ek ücretten sorumludur",
                        "Gümrükleme Kayıt Ücreti: Kanada'dan ABD'ye Vergi Değeri - $0-$800: $0.00, $800.01-$1250: $28.75, $1250.01-$2000: $40.50, $2000.01+: Her ek $1,000 için $40.50 artı $1.95. Ek Kayıt Kalemleri: 5 kalemden fazlası için kalem başına $3.50 - FedEx, Gümrük Kurumları aracılığıyla gönderilerin gümrüklenmesi ve serbest bırakılması için Gümrük Kaydı ve destekleyici belgelerin hazırlanması ve dosyalanması için bir ücret talep eder",
                        "Canlı Kayıt İşleme: $20 USD - İthalat için ihracat lisansı (vize) zorunlu olduğunda, gümrük tarafından gerekli görüldüğü şekilde canlı kayıtları işleyeceğiz",
                        "Özel Aracılık İşleme (Eski adıyla CPA): Talep üzerine fiyatlandırma - Özel Aracılık İşleme, özel uyumluluk ihtiyaçları olan müşteriler için tasarlanmış, geniş bir özel işlem hizmetleri yelpazesi sunan bir programdır. Program, gönderinizin gümrük temizleme yolculuğunda daha fazla kontrol ve görünürlük için kendi Kayıt İmportörünüz olmaya olanak tanır. Diğer temel avantajlar arasında özel destek, benzersiz iş ihtiyaçlarınıza göre uyarlanmış standart işletim prosedürü (SOP) ve My Global Trade Data aracılığıyla ithalat kayıtlarınıza görünürlük ve müşteri raporlama aracı diğer hizmet seçenekleri arasında yer alır. Daha fazla bilgi için Hesap Yöneticinizle iletişime geçin",
                        "Kayıt Kopyası: Kayıt başına $2.00 - Talep üzerine, ABD ithalat belgelerinizin ek kopyalarını kompakt disk (CD) veya elektronik veri değişimi (EDI) yoluyla sağlayabiliriz. Önceki ay için derlenen tüm kayıtlarla birlikte ayda bir kez CD veya EDI iletimi alacaksınız. Bu hizmeti kullanmak için: 1) Kayıt belgelerini elektronik olarak tutmak için gümrük kurumunuz tarafından onaylanmış olmanız ve 2) Özel Aracılık İşleme programı aracılığıyla sunulan Kayıt İmportörü hizmetine kaydolmanız gerekir. Daha fazla bilgi için Hesap Yöneticinizle iletişime geçin. Not: CD seçeneği yeni müşteriler için mevcut değildir",
                        "Vergi ve Harç Yönlendirme Ücreti: Gümrük Değeri $800'e eşit veya daha azsa Ücret $8.5 veya Vergi, Harç ve Mal İşleme Ücreti masraflarının %2'si hangisi büyükse, Gümrük Değeri $800'den fazlaysa Ücret $27 veya Vergi, Harç ve Mal İşleme Ücreti masraflarının %2'si hangisi büyükse - Gönderici vergi ve harçların hedef ülke dışında ödenmesi için üçüncü taraf faturalandırma seçeneğini seçerse Ödeme Ücreti yerine Vergi ve Harç Yönlendirme Ücreti uygulanacaktır"
                    ],
                    "requirements": [
                        "Detaylı emtia açıklaması içeren ticari fatura",
                        "Okyanus gönderileri için ISF (İthalatçı Güvenlik Dosyalaması) - yüklemeden 24 saat önce dosyalanır",
                        "Kayıt İthalatçısı kaydı ve EIN (İşveren Kimlik Numarası)",
                        "Giriş/Anında Teslimat belgeleri (CBP Form 3461)",
                        "10 iş günü içinde Giriş Özeti (CBP Form 7501)",
                        "Gümrük komisyoncusu temsili için Vekâletname",
                        "Gıda, ilaç ve tıbbi cihaz tesisleri için FDA kaydı",
                        "Tarım ürünleri için USDA izinleri",
                        "Yaban hayatı ve yaban hayatı ürünleri için FWS izinleri",
                        "Alkol, tütün, ateşli silahlar ve patlayıcılar için ATFE lisansları",
                        "HTSUS (Harmonize Tarife Çizelgesi) altında uygun tarife sınıflandırması",
                        "Tercihli gümrük vergi oranları için menşe şahadetnâmesi (NAFTA/USMCA)"
                    ],
                    "special_notes": [
                        "De minimis eşiği: 800 $ - bu değerin altındaki gönderiler gümrük vergisinden muaf",
                        "Bölüm 321 düşük değerli gönderiler için hızlandırılmış işleme izin verir",
                        "ACE (Otomatik Ticari Ortam) birincil gümrük sistemidir",
                        "Çoklu düzenleyici kurumlar ayrı temizlemeler ve ücretler gerektirebilir",
                        "Özel Aracılık İşleme müşterilerin kendi Kayıt İthalatçıları olmalarına olanak tanır",
                        "Express Hizmet: Depolama ücretleri temizleme yerinde üçüncü iş gününde başlar",
                        "Express Hizmet: Kayıt kopyaları CD (mevcut müşteriler) veya EDI iletimi yoluyla mevcut (2.10 $)",
                        "Standard Hizmet: Sabit ücretler yerine değer bazlı Temizleme Giriş Ücreti yapısı kullanır",
                        "Standard Hizmet: Kayıt başına 2.00 $ karşılığında kayıt kopyaları mevcut",
                        "Standard Hizmet: Kanada'dan ABD'ye gönderiler 3 yerine 5 ücretsiz satır alır",
                        "Askeri sözleşme gönderileri için devlet girişleri mevcut (yalnızca Express)",
                        "Canlı kayıt işleme: Express 27.00 $, Standard 20.00 $",
                        "Geçici ithalat hizmeti yeni müşteriler için mevcut değil (yalnızca Express)",
                        "FDA temizlemesine ek olarak gıda ve ilaç ürünleri için Ön Bildirim gerekli (yalnızca Express)",
                        "Farklı yerde temizlenen gönderiler için gümrük altında transit mevcut (yalnızca Express)",
                        "Gümrük değeri eşiklerine dayalı ödeme ve yönlendirme ücretleri (her iki hizmet)",
                        "ATFE düzenlemeli ürünler FedEx nakliyesi için onaylanmayabilir",
                        "FWS temizlemesi gerçek devlet ücretleri artı FedEx idari ücreti içerir",
                        "Standard Hizmet rutin gönderiler için daha uygun maliyetli işleme sunar",
                        "Express Hizmet karmaşık temizlemeler için kapsamlı yan hizmetler sağlar"
                    ]
                },
                "Australia": {
                "name": "Avustralya",
                "region": "Asya Pasifik", 
                "content": [
                    "ABF (Avustralya Sınır Kuvvetleri) düzenlemeleri uygulanır",
                    "Biyogüvenlik gereklilikleri son derece katıdır",
                    "AQIS (Avustralya Karantina ve Denetim Servisi) katılımı",
                    "Gümrük Kanunu 1901 ve düzenlemeler",
                    "Elektronik Entegre Kargo Sistemi (ICS) kullanılır",
                    "Yüksek değer eşiği: FOB + Sigorta > AUD 1,000 $",
                    "BSO (Broker Hizmet Seçeneği) gönderilerinin özel depolama kuralları vardır"
                ],
                "fees": [
                    "GST: Vergilendirilebilir değer üzerinden %10",
                    "Gümrük vergisi: Tarife sınıflandırmasına göre değişir",
                    "Vergi ve Harç Değişikliği: AUD $132 - Müşteri vergi ve harç tutarını itiraz ettiğinde uygulanır",
                    "Elektronik Kayıt Ücreti (Resmi Kayıt): $1,000-$9,999 değeri için AUD $95, $10,000+ değer için AUD $197",
                    "Bitki, Hayvan ve Gıda Karantinası: Belge İşleme AUD $37, Belge İşleme ve İnceleme AUD $99, Hafta Sonu/Mesai Değerlendirme İşleme AUD $120",
                    "Avans Ücreti: AUD $20 veya vergi, harç, Kayıt Ücreti ve diğer düzenleyici ücretlerin %2.9'u hangisi büyükse",
                    "ROD Ücreti (Vergi Harç İşleme Ücreti): Vergi harcının %2.9'u veya gönderi başına AUD $20, hangisi yüksekse",
                    "Komisyoncu Belge Transferi: Gönderi başına AUD $55",
                    "Depolama: 3. günden itibaren günde AUD $38.50 (yalnızca BSO gönderileri)",
                    "Vergi ve Harç Yönlendirme Ücreti: Minimum AUD $30 veya V&H'ın %2.9'u - Üçüncü taraf faturalandırma seçeneği seçildiğinde uygulanır"
                ],
                "requirements": [
                    "Detaylı açıklama içeren ticari fatura",
                    "Gerekiyorsa ithalat izni (AQIS, TGA, ACMA vb.)",
                    "Tüm gönderiler için karantina beyanı",
                    "Kimyasallar için Malzeme Güvenlik Bilgi Formu (MSDS)", 
                    "Tercihli gümrük vergi oranları için menşe şahadetnâmesi",
                    "Biyogüvenlik beyanı zorunlu",
                    "Ticari ithalatlar için Avustralya İş Numarası (ABN)",
                    "Gümrük deposu lisansı gümrük altı depolama için",
                    "Kontrollü mallar için özel izinler",
                    "AUD 1,000 $ üzerindeki gönderiler için resmi giriş gerekli (FOB + Sigorta)"
                ],
                "special_notes": [
                    "Avustralya dünyanın en katı biyogüvenlik yasalarından bazılarına sahip",
                    "Tüm ahşap ambalajlar ISPM-15 uyumlu olmalı", 
                    "Gıda ürünleri detaylı bileşen listesi gerektirir",
                    "Tedavi amaçlı ürünler TGA onayı gerektirir",
                    "Elektronik ürünler ACMA uyumluluğu gerektirebilir",
                    "Yüksek değer eşiği: Kombine FOB ve sigorta > AUD 1,000 $",
                    "ROD Ücreti FedEx hesap numarası olmayan müşteriler için uygulanır",
                    "FedEx hesabıyla düzenleyici ücretleri ödeme yapan müşteriler için Avans Ücreti",
                    "Depolama ücretleri yalnızca BSO (Broker Hizmet Seçeneği) gönderileri için uygulanır",
                    "Karantina ücretleri yenilebilir ürünler, hayvan ürünleri, sanat eserleri, yapay aroma ve kereste için yerel otoriteler tarafından belirlenir"
                ]
            },
            "Canada": {
                "name": "Kanada",
                "region": "Amerika",
                "content": [
                    "CBSA (Kanada Sınır Hizmetleri Ajansı) prosedürleri uygulanır",
                    "CARM (Gümrük Otomatik Serbest Bırakma Yönetimi) sistem uygulaması",
                    "Gümrük Kanunu ve Tarife düzenlemeleri",
                    "NAFTA/USMCA ticaret avantajları mevcut",
                    "Gıda ürünleri için Kanada Gıda Denetim Ajansı (CFIA) katılımı",
                    "Doğrudan CBSA faturalandırma ilişkisi için Hesap Güvenlik Numarası sistemi",
                    "Otomatik serbest bırakma vs resmi temizleme için düşük değer eşiği CAD 3,300 $"
                ],
                "express_fees": [
                    "GST/HST: İl'e göre %5-15 değişir",
                    "Gümrük vergisi: Tarife sınıflandırmasına göre değişir",
                    "Ek Kalem Ücretleri: 3 kalemden fazlaysa kalem başına CAD $5.30 - Gönderi aşağıdaki durumlarda ek tarife sınıflandırması gerektirebilir: 1) Yayınlanan ücretlerdeki Ücretsiz Kalem sınırının ötesinde bir veya daha fazla tarife sınıflandırması varsa; 2) Aynı emtia birden fazla ülkede üretilmişse; 3) Gümrüğe sunulan birden fazla Ticari Fatura her fatura için ayrı tarife sınıflandırması gerektiriyorsa; 4) Gönderi içindeki her kalem için ayrı kayıt girişi talep ediyorsanız. Yerel Not: FedEx birden fazla tarife sınıflandırması içeren gönderilerin gümrüklenmesini sağlayabilir, ancak Ek Kalem Ücreti uygulanır",
                    "Depolama: İlk 48 saat sonrasında lb başına günde $0.25 CAD - Gönderi ücretlerde yayınlanan süre sınırını aşarak FedEx bağlı tesisinde temizlenmemiş kalırsa depolama ücreti talep edebiliriz",
                    "Kayıt Sonrası Düzeltme: $75 CAD veya talep değerinin %8'i, hangisi büyükse - Talebiniz üzerine, FedEx daha önce sağladığınız bilgilerdeki kaydı düzeltmek için Gümrük'e Kayıt Düzeltmesi sunacaktır. Bu, Vergi/Harç fazla ödemesinin iadesi veya FedEx ücretinin yanı sıra Gümrük'e ek Vergi/Harç borcu ile sonuçlanabilir. Yerel Not: Kayıt belgelerinizdeki hatayı düzeltmek için Gümrük ile düzeltme veya ayarlama işlemi yaptığımızda ücret uygulanır. Bu ücret gönüllü kayıt değişiklikleri için de geçerlidir",
                    "Diğer Devlet Kurumu: Kayıt başına $16.50 CAD - Bir devlet kurumu tarafından belgelerin doğrulanması veya kimlik kontrolü yapılması gerektiğinde ücret veya ücretler uygulanır; ancak yerel konseyler veya ticari ajanslar gibi aynı gönderi için birden fazla kurumdan da ücret alınabilir. FedEx tüm harici kurumlardan alınan ücretleri aktaracaktır. Yerel Not: FedEx ilgili Düzenleyici Kuruma gerekli bilgileri (kağıt veya elektronik) dosyalamak için gerekli aracılık işlemini sağlayacaktır. FedEx bu iş için size sabit işlem ücreti faturalayacaktır",
                    "Hesap Güvenlik İşleme: Serbest Bırakma: $3 CAD, Onaylama: $7 CAD, Serbest Bırakma ve Onaylama: $10 CAD - Kanada Sınır Hizmetleri Ajansı'ndan (CBSA) hesap güvenlik numarası alarak, vergiler ve harçlar için CBSA ile doğrudan faturalandırma ve ödeme ilişkisi kurabilirsiniz. Bu aynı zamanda CBSA'nın doğrudan kayıt ithalatçısına vergi ve harçları listeleyen K84 Özetini göndermesini sağlar. FedEx gümrük serbest bırakma işlemini gerçekleştirirse ve ithalatçı onay için harici komisyoncu kullanırsa, yüksek değerli gönderiler ($3,300 CAD veya daha fazla değerli) için ücret $3 CAD'dir. FedEx yalnızca onaylamayı gerçekleştirirse, tüm gönderiler için ücret $7 CAD'dir. FedEx hem serbest bırakma hem de onaylamayı gerçekleştirirse, ücret $10 CAD'dir",
                    "Mesai Sonrası Gümrükleme: FedEx $120 CAD; Harici Komisyoncu $50 CAD - Talebiniz üzerine, normal iş saatleri dışında gümrük temizleme sağlayacağız. Cumartesi dahil olmak üzere normal iş saatleri dışında veya harici komisyoncu gümrüklemeyi kolaylaştırmak için bizden gümrük belgelerini talep ettiğinde gönderi başına ücret uygulanacaktır",
                    "İş Kayıt Numarası Başvurusu: Kayıt başına $5 CAD - Kanada'ya ithalat yapmak için iş kayıt numarası gereklidir. Eğer yoksa, FedEx talep edilirse sizin adınıza CBSA'ya başvuru dosyalayabilir",
                    "Faks Ücreti: Yerel: Arama başına $3 CAD; Şehirlerarası: Arama başına $4 CAD - FedEx dışında bir taraf gümrük temizleme gerçekleştirirken, aşağıdakilerden biri geçerliyse kayıt belgelerini faks yoluyla ileteceğiz: Kendi iç aracılık departmanınız gümrük temizleme gerçekleştiriyorsa. Harici komisyoncu kullanıyorsanız ve komisyoncunun Kanada'da tek merkezi konumu varsa. Hesap güvenlik numaranızı kullanıyor ve kendi kendine gümrükleme-onaylama yapıyorsanız. Fakslanacak sayfa sayısına bakılmaksızın yerel arama başına $3 CAD ve şehirlerarası arama başına $4 CAD ücreti uygulanır",
                    "İthalat İzni: Tek kalem: $25.00 CAD artı CBSA ücretleri; Birden Fazla Kalem: $10 CAD artı CBSA ücretleri - Birçok ülkede belirli mal veya ürünleri yerel ticarete ithal etmek için İthalat İzinleri gerekli olabilir. İzin için ve/veya İthalat İzni almak için İzin başvurusunu hazırlama ve dosyalama maliyeti için ücret değerlendirilir",
                    "Düşük Değerli Gönderi Belge İstisnası: $4 CAD - FedEx sizin adınıza gümrükten düşük değerli gönderi (3,300 CAD'den daha az değerli gönderi) temizlerse, talep üzerine vergi ve harç faturalandırması sırasında tüm temizleme belgelerinin kopyalarını size sağlayacağız",
                    "Kurye Düşük Değerli Gönderi Kayıt Düzeltmesi: Kayıt başına $25 CAD - Sizin adınıza kurye düşük değerli gönderi (3,300 CAD'den daha az değerli) için kayıt belgelerinizdeki hatayı düzelttiğimizde ücret uygulanır. Hata nakliye tarihini takip eden ayın 20'sinde veya öncesinde rapor edilmelidir; aksi takdirde kayıt sonrası düzeltme gereklidir",
                    "Düşük Değerli Gönderi Kayıt İstisnası: $4 CAD - CBSA düzenlemeleri uyarınca, 3,300 CAD'den daha az değerli gönderiler otomatik olarak gümrükten serbest bırakılır. Ancak teslimat öncesinde resmi gümrük serbest bırakma talep edebilirsiniz",
                    "Geçici İthalat: Kayıt başına $120 CAD - Gönderilerin belirli bir süre için geçici olarak ithal edilmesini talep ettiğinizde, FedEx Gümrük tarafından belirtilen gerekli belgeleri tavsiye ederek, hazırlayarak ve dosyalayarak ithalat sürecini koordine edebilir",
                    "Gümrük Altında Transfer: Kayıt başına $40 CAD - Talebiniz üzerine FedEx gelen gönderileri varış noktasından gümrük temizleme için başka bir yere taşımak için gerekli belgeleri hazırlayabilir. Malların temizleme öncesinde iki konum arasında hareket etmesine izin verecek Gümrük onayını alacağız. FedEx belge hazırlama için ücret talep edecektir. Gönderi alıcısı herhangi bir ek nakliye ücretinden sorumlu olacaktır",
                    "ROD Ücreti: CAD $11.40 + Geçerli Vergi - FedEx hesap numarası olmayan müşteriler için gönderilerin serbest bırakılması ve Gümrük ücretlerinin ödenmesi için doğrudan ödeme sürecini işletmek için FedEx'in talep edeceği ücret. Yerel Not: Bu ücret aynı zamanda kötü ödeme geçmişi olan müşterilerden de talep edilir",
                    "Ödeme Ücreti: Avans verilen toplam vergi ve harcın %2.95'i veya $11.40 CAD, hangisi büyükse - Gümrük kurumuna zamanında ödemeyi sağlamak için sizin adınıza geçerli vergileri, harçları ve diğer düzenleyici ücretleri ödeyebiliriz. Ödeyen, ödenen toplam tutardan artı ücretlerde yayınlanan ek ücretten sorumludur"
                ],
                "standard_fees": [
                    "GST/HST: İl'e göre %5-15 değişir",
                    "Gümrük vergisi: Tarife sınıflandırmasına göre değişir",
                    "Ek Kalem Ücretleri: 3 kalemden fazlaysa kalem başına CAD $5.30 - Gönderi aşağıdaki durumlarda ek tarife sınıflandırması gerektirebilir: 1) Yayınlanan ücretlerdeki Ücretsiz Kalem sınırının ötesinde bir veya daha fazla tarife sınıflandırması varsa; 2) Aynı emtia birden fazla ülkede üretilmişse; 3) Gümrüğe sunulan birden fazla Ticari Fatura her fatura için ayrı tarife sınıflandırması gerektiriyorsa; 4) Gönderi içindeki her kalem için ayrı kayıt girişi talep ediyorsanız. Yerel Not: FedEx birden fazla tarife sınıflandırması içeren gönderilerin gümrüklenmesini sağlayabilir, ancak Ek Kalem Ücreti uygulanır",
                    "Diğer Devlet Kurumu: Kayıt başına $16.50 CAD - Bir devlet kurumu tarafından belgelerin doğrulanması veya kimlik kontrolü yapılması gerektiğinde ücret veya ücretler uygulanır; ancak yerel konseyler veya ticari ajanslar gibi aynı gönderi için birden fazla kurumdan da ücret alınabilir. FedEx tüm harici kurumlardan alınan ücretleri aktaracaktır. Yerel Not: FedEx ilgili Düzenleyici Kuruma gerekli bilgileri (kağıt veya elektronik) dosyalamak için gerekli aracılık işlemini sağlayacaktır. FedEx bu iş için size sabit işlem ücreti faturalayacaktır",
                    "Faks Ücreti: Yerel: Arama başına $3 CAD; Şehirlerarası: Arama başına $4 CAD - FedEx dışında bir taraf gümrük temizleme gerçekleştirirken, aşağıdakilerden biri geçerliyse kayıt belgelerini faks yoluyla ileteceğiz: Kendi iç aracılık departmanınız gümrük temizleme gerçekleştiriyorsa. Harici komisyoncu kullanıyorsanız ve komisyoncunun Kanada'da tek merkezi konumu varsa. Hesap güvenlik numaranızı kullanıyor ve kendi kendine gümrükleme-onaylama yapıyorsanız. Fakslanacak sayfa sayısına bakılmaksızın yerel arama başına $3 ve şehirlerarası arama başına $4 ücreti uygulanır",
                    "Ödeme Ücreti: Avans verilen toplam vergi ve harcın %2.95'i veya $11.40 CAD, hangisi büyükse - Gümrük kurumuna zamanında ödemeyi sağlamak için sizin adınıza geçerli vergileri, harçları ve diğer düzenleyici ücretleri ödeyebiliriz. Ödeyen, ödenen toplam tutardan artı ücretlerde yayınlanan ek ücretten sorumludur",
                    "Gümrükleme Kayıt Ücreti: Vergi Değeri (CAD) - $0-$40: $0.00, $40.01-$60: $17.25, $60.01-$100: $21.25, $100.01-$150: $27.50, $150.01-$200: $32.25, $200.01-$500: $54.00, $500.01-$1000: $62.00, $1000.01-$1600: $71.50, $1600.01-$3300: $82.00, $3300.01+: Her ek $1000 için $82 artı $7.50 - Gümrük Kurumları aracılığıyla gönderilerin gümrüklenmesi ve serbest bırakılması için Gümrük Kaydı ve destekleyici belgelerin hazırlanması ve dosyalanması için Hazırlık Ücreti"
                ],
                "requirements": [
                    "Detaylı emtia açıklaması içeren ticari fatura",
                    "Tercihli oranlar için NAFTA/USMCA menşe şahadetnâmesi",
                    "Gerekiyorsa ithalat izni (Health Canada, CFIA, vb.)",
                    "Ticari ithalatlar için İş Numarası (BN) - tüm ithalatlar için gerekli",
                    "Kayıtlı ithalatçı kaydı",
                    "Tehlikeli mallar için Malzeme Güvenlik Bilgi Formu",
                    "Ahşap ambalaj ISPM-15 uyumlu olmalı",
                    "Gıda ürünleri CFIA uyumluluğu gerektirir",
                    "Doğrudan CBSA faturalandırması için Hesap Güvenlik Numarası (isteğe bağlı ama faydalı)",
                    "Gönderideki tüm kalemler için uygun tarife sınıflandırması"
                ],
                "special_notes": [
                    "Düşük değer eşiği: Kurye gönderileri için CAD 3,300 $ - bunun altında otomatik serbest bırakma, üstünde resmi temizleme gerekli",
                    "Hesap Güvenlik Numarası doğrudan CBSA faturalandırma ve K84 Özet makbuzu sağlar",
                    "CARM sistemi gümrük süreçlerini modernleştiriyor",
                    "3 ücretsiz kalem ötesinde çoklu tarife sınıflandırmaları Ek Kalem Ücretlerini tetikler",
                    "FedEx gümrük altı tesisinde 48 saat sonrası depolama ücretleri uygulanır (yalnızca Express)",
                    "Kayıt düzeltmeleri kayıt sonrası ayarlama ücretlerinden kaçınmak için nakliye tarihini takip eden ayın 20'sine kadar raporlanmalı",
                    "Mesai sonrası temizleme mevcut ancak ek ücretler doğurur (yalnızca Express)",
                    "ROD Ücreti FedEx hesabı olmayan veya kötü ödeme geçmişi olan müşteriler için uygulanır",
                    "Zamanında gümrük ödemesini sağlamak için ödeme hizmetleri mevcut",
                    "Özel durumlar için geçici ithalat ve gümrük altında transfer hizmetleri mevcut (yalnızca Express)",
                    "Standard Hizmet sabit aracılık ücretleri yerine değer bazlı Temizleme Giriş Ücreti yapısı kullanır",
                    "Express Hizmet depolama, kayıt sonrası ayarlamalar ve mesai sonrası temizleme gibi daha kapsamlı yan hizmetler içerir"
                ]
            }
        }
