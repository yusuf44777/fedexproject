import streamlit as st
import pandas as pd

# Kapsamlı ülke verileri (güncel FedEx ücret yapısına dayalı)
countries_data = {
    "Netherlands": {
        "name": "Hollanda",
        "region": "Avrupa",
        "fees": [
            "KDV: Vergilendirilebilir değer üzerinden %21 (standart oran)",
            "Gümrük vergisi: Tarife sınıflandırmasına göre değişir",
            "Ek Kalem Ücretleri: 6. kalemden itibaren her ek kalem için €8.00",
            "Gümrük Altında Transit: Gönderi başına €45.00",
            "İade Malları: Gönderi başına €42.00",
            "Geçici İthalat: Gönderi başına €42.00",
            "Depolama: Üç iş günü sonrasında paket başına iş günü başına €10.00",
            "Diğer Devlet Kurumları: Gönderi başına €40.00 artı geçiş ücretleri",
            "Özel Hizmet: Saatte €50.00, minimum yarım saatte €40.00",
            "Ön Ödeme: €0.01-€50.00: V&H'ın %30'u (min €5.00), €50.00-€600.00: €15.00, €600.00+: V&H'ın %2.5'i",
            "Kayıt Sonrası Düzeltme: Gönderi başına €90.00",
            "Ödeme Ücreti: €0.01-€50.00: V&H'ın %30'u (min €8.00), €50.00-€600.00: €15.00, €600.00+: V&H'ın %2.5'i",
            "Vergi ve Harç Yönlendirme Ücreti: €18.00 veya V&H'ın %2.5'i hangisi büyükse"
        ]
    },
    "United Kingdom": {
        "name": "Birleşik Krallık",
        "region": "Avrupa",
        "fees": [
            "KDV: %20 (standart oran)",
            "Gümrük vergisi: Tarife sınıflandırmasına göre değişir",
            "Ek Kalem Ücretleri: 6. kalemden itibaren her ek kalem için £5.00",
            "Kargo Gümrük: Gönderi başına £35.00",
            "Geçici İthalat: Gönderi başına £25.00",
            "Depolama: Üç iş günü sonrasında paket başına iş günü başına £10.00",
            "Diğer Devlet Kurumları: Gönderi başına £35.00 artı geçiş ücretleri",
            "Özel Hizmet: Saatte £40.00, minimum yarım saatte £35.00",
            "Kayıt Sonrası Düzeltme: Gönderi başına £75.00",
            "Ödeme Ücreti: £0.01-£50.00: V&H'ın %30'u (min £8.00), £50.00-£600.00: £15.00, £600.00+: V&H'ın %2.5'i"
        ]
    },
    "United States": {
        "name": "Amerika Birleşik Devletleri",
        "region": "Amerika",
        "fees": [
            "Eyalet Satış Vergisi: Eyalete göre değişken",
            "Gümrük vergisi: Tarife sınıflandırmasına göre değişir",
            "Ek Kalem Ücretleri: 4+ kalem için kalem başına $3.50",
            "FWS: Gönderi başına $93.50",
            "ATFE: Gönderi başına $74.00",
            "Transit: Gönderi başına $90.00",
            "Komisyoncu Transfer: Gönderi başına $45.00",
            "Depolama Express: $0.08/kg/gün + $20 (3 gün sonrası)",
            "Depolama Standard: $0.09/kg/gün + $27 (14 gün sonrası)",
            "MPF: $0.3464 per $100 (min $27.75, max $538.40)",
            "HMF: $5.25 per gönderi",
            "FDA: Gönderi başına $27.50",
            "ROD Ücreti: $9.80 + geçerli vergi",
            "Ödeme Ücreti: V&H'ın %2.15'i veya $9.80"
        ]
    },
    "Australia": {
        "name": "Avustralya",
        "region": "Asya Pasifik",
        "fees": [
            "GST: %10 (vergilendirilebilir değer)",
            "Gümrük vergisi: Tarife sınıflandırmasına göre değişir",
            "Vergi ve Harç Değişikliği: AUD $132",
            "Elektronik Kayıt ($1K-$9.9K): AUD $95",
            "Elektronik Kayıt ($10K+): AUD $197",
            "Karantina Belge İşleme: AUD $37",
            "Karantina İnceleme: AUD $99",
            "Karantina Mesai: AUD $120",
            "Avans Ücreti: AUD $20 veya %2.9",
            "ROD Ücreti: %2.9 veya AUD $20",
            "Komisyoncu Transfer: AUD $55/gönderi",
            "Depolama BSO: AUD $38.50/gün (3 gün sonrası)",
            "V&H Yönlendirme: Min AUD $30 veya %2.9"
        ]
    },
    "Canada": {
        "name": "Kanada",
        "region": "Amerika",
        "fees": [
            "GST/HST: İl'e göre %5-15 değişir",
            "Gümrük vergisi: Tarife sınıflandırmasına göre değişir",
            "Express Ek Kalem: CAD $5.30/kalem (3+)",
            "Express Depolama: lb başına günde $0.25 CAD (48 saat sonrası)",
            "Express Kayıt Düzeltme: $75 CAD veya değerin %8'i",
            "Standard Depolama: lb başına günde $0.25 CAD (7 gün sonrası)", 
            "Standard Kayıt Düzeltme: $50 CAD veya değerin %5'i",
            "Diğer Devlet Kurumu: Kayıt başına $16.50 CAD",
            "Güvenlik İşleme: $3-$10 CAD",
            "Mesai Sonrası (Express): $120 CAD",
            "ROD Express: CAD $11.40 + vergi",
            "ROD Standard: CAD $9.90 + vergi",
            "Ödeme Express: V&H'ın %2.95'i veya $11.40 CAD",
            "Ödeme Standard: V&H'ın %2.95'i veya $9.90 CAD"
        ]
    }
}

def create_country_comparison_tables():
    """Ülke ve hizmet karşılaştırma tabloları oluşturur"""
    st.title("FedEx Ülke ve Hizmet Karşılaştırması")
    
    # Sidebar'da sayfalar arası geçiş
    page = st.sidebar.selectbox(
        "Sayfa Seçin:",
        ["Ana Karşılaştırma", "Detaylı Ülke Bilgileri", "Ücret Hesaplama Simülasyonu"]
    )
    
    if page == "Ana Karşılaştırma":
        # Ana karşılaştırma tablosu
        create_main_comparison_table()
        
        # Hizmet türü karşılaştırması
        create_service_comparison_tables()
        
    elif page == "Detaylı Ülke Bilgileri":
        # Detaylı ülke bilgileri
        create_detailed_country_info()
        
    elif page == "Ücret Hesaplama Simülasyonu":
        # Ücret hesaplama simülasyonu
        create_fee_calculator()

def create_main_comparison_table():
    """Ana ülke karşılaştırma tablosu"""
    st.header("Ülkeler Arası Genel Karşılaştırma")
    
    # Ana karşılaştırma verileri
    comparison_data = [
        {
            "Ülke": "Hollanda",
            "Bölge": "Avrupa",
            "KDV/Vergi": "21% (standart oran)",
            "Ücretsiz Kalem": "5",
            "Ek Kalem Ücreti": "€8.00 (6. kalemden itibaren)",
            "Depolama": "€10.00/gün (3 gün sonrası)",
            "Özel Hizmetler": "Transit €45, Geçici İthalat €42",
            "Düzenleyici": "AB gümrük, EORI zorunlu",
            "Para Birimi": "EUR"
        },
        {
            "Ülke": "Birleşik Krallık",
            "Bölge": "Avrupa",
            "KDV/Vergi": "20% (standart oran)",
            "Ücretsiz Kalem": "5",
            "Ek Kalem Ücreti": "£5.00 (6. kalemden itibaren)",
            "Depolama": "£10.00/gün (3 gün sonrası)",
            "Özel Hizmetler": "Kargo Gümrük £35, Geçici İthalat £25",
            "Düzenleyici": "Brexit sonrası, UKCA gerekli",
            "Para Birimi": "GBP"
        },
        {
            "Ülke": "Amerika Birleşik Devletleri",
            "Bölge": "Amerika",
            "KDV/Vergi": "Eyalet bazlı değişken",
            "Ücretsiz Kalem": "3 (Express/Standard)",
            "Ek Kalem Ücreti": "$3.50 (4. kalemden itibaren)",
            "Depolama": "$0.08/kg/gün + $20 (Express, 3 gün sonrası)",
            "Özel Hizmetler": "FDA $27.50, ATFE $74, Transit $90",
            "Düzenleyici": "CBP, De minimis $800, ISF gerekli",
            "Para Birimi": "USD"
        },
        {
            "Ülke": "Avustralya",
            "Bölge": "Asya Pasifik",
            "KDV/Vergi": "10% GST",
            "Ücretsiz Kalem": "Uygulanmaz",
            "Ek Kalem Ücreti": "Uygulanmaz",
            "Depolama": "AUD $38.50/gün (BSO, 3 gün sonrası)",
            "Özel Hizmetler": "Karantina $37-$120, E-Kayıt $95-$197",
            "Düzenleyici": "ABF, Katı biyogüvenlik, AQIS",
            "Para Birimi": "AUD"
        },
        {
            "Ülke": "Kanada",
            "Bölge": "Amerika",
            "KDV/Vergi": "5-15% GST/HST (il'e göre)",
            "Ücretsiz Kalem": "3 (Express/Standard)",
            "Ek Kalem Ücreti": "CAD $5.30 (4. kalemden itibaren)",
            "Depolama": "$0.25/lb/gün (Express, 48 saat sonrası)",
            "Özel Hizmetler": "Mesai Sonrası $120, Geçici İthalat $120",
            "Düzenleyici": "CBSA, CARM sistemi, NAFTA/USMCA",
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

def create_fee_calculator():
    """Ücret hesaplama simülasyonu"""
    st.header("🧮 FedEx Ücret Hesaplama Simülasyonu")
    st.write("Gerçek gönderi senaryolarınız için detaylı ücret hesaplaması yapın.")
    
    # Ana parametreler
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("📦 Gönderi Bilgileri")
        selected_country = st.selectbox(
            "Hedef Ülke:",
            ["Hollanda", "Birleşik Krallık", "Amerika Birleşik Devletleri", "Avustralya", "Kanada"]
        )
        
        service_type = st.selectbox(
            "Hizmet Türü:",
            ["Express", "Standard"] if selected_country in ["Amerika Birleşik Devletleri", "Kanada"] else ["Express"]
        )
        
        shipment_value = st.number_input(
            "Gönderi Değeri:",
            min_value=0.0,
            max_value=100000.0,
            value=500.0,
            step=50.0,
            help="Gümrük değeri (FOB + Sigorta)"
        )
        
        num_items = st.number_input(
            "Kalem Sayısı:",
            min_value=1,
            max_value=50,
            value=1,
            step=1,
            help="Farklı tarife sınıflandırması gerektiren kalem sayısı"
        )
        
        weight_kg = st.number_input(
            "Ağırlık (kg):",
            min_value=0.1,
            max_value=1000.0,
            value=2.0,
            step=0.1
        )
        
        storage_days = st.number_input(
            "Depolama Günü:",
            min_value=0,
            max_value=30,
            value=0,
            step=1,
            help="Hoşgörü süresinden sonraki depolama günleri"
        )
    
    with col2:
        st.subheader("🛃 Özel Hizmetler")
        
        special_services = {}
        
        if selected_country == "Hollanda":
            special_services["transit"] = st.checkbox("Gümrük Altında Transit (€45)")
            special_services["temporary_import"] = st.checkbox("Geçici İthalat (€42)")
            special_services["return_goods"] = st.checkbox("İade Malları (€42)")
            special_services["other_gov"] = st.checkbox("Diğer Devlet Kurumları (€40)")
            special_services["post_entry"] = st.checkbox("Kayıt Sonrası Düzeltme (€90)")
            
        elif selected_country == "Birleşik Krallık":
            special_services["cargo_clearance"] = st.checkbox("Kargo Gümrükleme (£35)")
            special_services["temporary_import"] = st.checkbox("Geçici İthalat (£25)")
            special_services["return_goods"] = st.checkbox("İade Malları (£21)")
            special_services["other_gov"] = st.checkbox("Diğer Devlet Kurumları (£27)")
            special_services["import_permits"] = st.checkbox("İthalat İzinleri (£40)")
            
        elif selected_country == "Amerika Birleşik Devletleri":
            special_services["fda_clearance"] = st.checkbox("FDA Gümrükleme ($27.50)")
            special_services["fws_clearance"] = st.checkbox("FWS Gümrükleme (Değişken + $22)")
            special_services["atfe_clearance"] = st.checkbox("ATFE Gümrükleme ($74)")
            special_services["govt_records"] = st.checkbox("Devlet Kayıtları ($53)")
            special_services["transit"] = st.checkbox("Gümrük Altında Transit ($90)")
            if service_type == "Express":
                special_services["temporary_import"] = st.checkbox("Geçici İthalat ($150)")
                special_services["broker_transfer"] = st.checkbox("Komisyoncu Belge Transferi ($51)")
            
        elif selected_country == "Avustralya":
            special_services["quarantine_basic"] = st.checkbox("Karantina Belge İşleme (AUD $37)")
            special_services["quarantine_inspection"] = st.checkbox("Karantina İnceleme (AUD $99)")
            special_services["quarantine_weekend"] = st.checkbox("Karantina Hafta Sonu (AUD $120)")
            special_services["broker_transfer"] = st.checkbox("Komisyoncu Belge Transferi (AUD $55)")
            
        elif selected_country == "Kanada":
            special_services["other_gov"] = st.checkbox("Diğer Devlet Kurumu (CAD $16.50)")
            special_services["business_number"] = st.checkbox("İş Kayıt Numarası Başvurusu (CAD $5)")
            special_services["import_permit_single"] = st.checkbox("İthalat İzni - Tek Kalem (CAD $25)")
            special_services["import_permit_multi"] = st.checkbox("İthalat İzni - Çoklu (CAD $10)")
            if service_type == "Express":
                special_services["after_hours_fedex"] = st.checkbox("Mesai Sonrası - FedEx (CAD $120)")
                special_services["after_hours_external"] = st.checkbox("Mesai Sonrası - Harici (CAD $50)")
                special_services["temporary_import"] = st.checkbox("Geçici İthalat (CAD $120)")
                special_services["customs_transit"] = st.checkbox("Gümrük Altında Transfer (CAD $40)")
    
    # Hesapla butonu
    if st.button("💰 Ücretleri Hesapla", type="primary"):
        calculate_fees(selected_country, service_type, shipment_value, num_items, weight_kg, storage_days, special_services)

def calculate_fees(country, service_type, value, items, weight, storage_days, special_services):
    """Ücret hesaplama fonksiyonu"""
    st.subheader("📊 Hesaplanan Ücretler")
    
    total_cost = 0
    fee_breakdown = []
    
    # Para birimi belirleme
    currency_map = {
        "Hollanda": "EUR",
        "Birleşik Krallık": "GBP", 
        "Amerika Birleşik Devletleri": "USD",
        "Avustralya": "AUD",
        "Kanada": "CAD"
    }
    currency = currency_map[country]
    
    # Temel vergiler
    if country == "Hollanda":
        vat = value * 0.21
        fee_breakdown.append({"Kategori": "Temel Vergiler", "Hizmet": "KDV (21%)", "Ücret": f"€{vat:.2f}"})
        total_cost += vat
        
        # Ek kalem ücretleri
        if items > 5:
            extra_items_fee = (items - 5) * 8.0
            fee_breakdown.append({"Kategori": "İşlem Ücretleri", "Hizmet": f"Ek Kalem ({items-5} kalem)", "Ücret": f"€{extra_items_fee:.2f}"})
            total_cost += extra_items_fee
        
        # Depolama
        if storage_days > 3:
            storage_fee = (storage_days - 3) * 10.0
            fee_breakdown.append({"Kategori": "Depolama", "Hizmet": f"Depolama ({storage_days-3} gün)", "Ücret": f"€{storage_fee:.2f}"})
            total_cost += storage_fee
            
    elif country == "Birleşik Krallık":
        vat = value * 0.20
        fee_breakdown.append({"Kategori": "Temel Vergiler", "Hizmet": "KDV (20%)", "Ücret": f"£{vat:.2f}"})
        total_cost += vat
        
        # Ek kalem ücretleri
        if items > 5:
            extra_items_fee = (items - 5) * 5.0
            fee_breakdown.append({"Kategori": "İşlem Ücretleri", "Hizmet": f"Ek Kalem ({items-5} kalem)", "Ücret": f"£{extra_items_fee:.2f}"})
            total_cost += extra_items_fee
        
        # Depolama
        if storage_days > 3:
            storage_fee = (storage_days - 3) * 10.0
            fee_breakdown.append({"Kategori": "Depolama", "Hizmet": f"Depolama ({storage_days-3} gün)", "Ücret": f"£{storage_fee:.2f}"})
            total_cost += storage_fee
            
    elif country == "Amerika Birleşik Devletleri":
        # MPF hesaplama
        mpf = max(27.23, min(528.33, value * 0.003464))
        fee_breakdown.append({"Kategori": "Temel Vergiler", "Hizmet": "MPF (0.3464%)", "Ücret": f"${mpf:.2f}"})
        total_cost += mpf
        
        # Ek kalem ücretleri
        if items > 3:
            extra_items_fee = (items - 3) * 3.5
            fee_breakdown.append({"Kategori": "İşlem Ücretleri", "Hizmet": f"Ek Kalem ({items-3} kalem)", "Ücret": f"${extra_items_fee:.2f}"})
            total_cost += extra_items_fee
        
        # Depolama (sadece Express)
        if service_type == "Express" and storage_days > 3:
            storage_fee = (storage_days - 3) * (weight * 0.08) + 20
            fee_breakdown.append({"Kategori": "Depolama", "Hizmet": f"Depolama ({storage_days-3} gün)", "Ücret": f"${storage_fee:.2f}"})
            total_cost += storage_fee
        
        # Ödeme ücreti
        if value <= 800:
            payment_fee = max(4.50, (mpf * 0.02))
        else:
            payment_fee = max(14.00, (mpf * 0.02))
        fee_breakdown.append({"Kategori": "İşlem Ücretleri", "Hizmet": "Ödeme Ücreti", "Ücret": f"${payment_fee:.2f}"})
        total_cost += payment_fee
        
    elif country == "Avustralya":
        gst = value * 0.10
        fee_breakdown.append({"Kategori": "Temel Vergiler", "Hizmet": "GST (10%)", "Ücret": f"AUD ${gst:.2f}"})
        total_cost += gst
        
        # Elektronik kayıt ücreti
        if 1000 <= value <= 9999:
            e_entry_fee = 95
        elif value >= 10000:
            e_entry_fee = 197
        else:
            e_entry_fee = 0
            
        if e_entry_fee > 0:
            fee_breakdown.append({"Kategori": "İşlem Ücretleri", "Hizmet": "Elektronik Kayıt", "Ücret": f"AUD ${e_entry_fee:.2f}"})
            total_cost += e_entry_fee
        
        # Depolama (BSO)
        if storage_days > 3:
            storage_fee = (storage_days - 3) * 38.50
            fee_breakdown.append({"Kategori": "Depolama", "Hizmet": f"Depolama BSO ({storage_days-3} gün)", "Ücret": f"AUD ${storage_fee:.2f}"})
            total_cost += storage_fee
        
        # ROD ücreti
        rod_fee = max(20, gst * 0.029)
        fee_breakdown.append({"Kategori": "İşlem Ücretleri", "Hizmet": "ROD Ücreti", "Ücret": f"AUD ${rod_fee:.2f}"})
        total_cost += rod_fee
        
    elif country == "Kanada":
        # GST/HST (ortalama %10 kullanılıyor)
        gst = value * 0.10
        fee_breakdown.append({"Kategori": "Temel Vergiler", "Hizmet": "GST/HST (10%)", "Ücret": f"CAD ${gst:.2f}"})
        total_cost += gst
        
        # Ek kalem ücretleri
        if items > 3:
            extra_items_fee = (items - 3) * 5.30
            fee_breakdown.append({"Kategori": "İşlem Ücretleri", "Hizmet": f"Ek Kalem ({items-3} kalem)", "Ücret": f"CAD ${extra_items_fee:.2f}"})
            total_cost += extra_items_fee
        
        # Depolama (sadece Express)
        if service_type == "Express" and storage_days > 2:  # Kanada'da 48 saat = 2 gün
            weight_lb = weight * 2.20462  # kg to lb
            storage_fee = (storage_days - 2) * weight_lb * 0.25
            fee_breakdown.append({"Kategori": "Depolama", "Hizmet": f"Depolama ({storage_days-2} gün)", "Ücret": f"CAD ${storage_fee:.2f}"})
            total_cost += storage_fee
        
        # Gümrükleme kayıt ücreti (Standard için)
        if service_type == "Standard":
            if value <= 40:
                clearance_fee = 0
            elif value <= 60:
                clearance_fee = 17.25
            elif value <= 100:
                clearance_fee = 21.25
            elif value <= 150:
                clearance_fee = 27.50
            elif value <= 200:
                clearance_fee = 32.25
            elif value <= 500:
                clearance_fee = 54.00
            elif value <= 1000:
                clearance_fee = 62.00
            elif value <= 1600:
                clearance_fee = 71.50
            elif value <= 3300:
                clearance_fee = 82.00
            else:
                clearance_fee = 82.00 + ((value - 3300) // 1000) * 7.50
            
            if clearance_fee > 0:
                fee_breakdown.append({"Kategori": "İşlem Ücretleri", "Hizmet": "Gümrükleme Kayıt", "Ücret": f"CAD ${clearance_fee:.2f}"})
                total_cost += clearance_fee
        
        # Ödeme ücreti
        payment_fee = max(11.40, gst * 0.0295)
        fee_breakdown.append({"Kategori": "İşlem Ücretleri", "Hizmet": "Ödeme Ücreti", "Ücret": f"CAD ${payment_fee:.2f}"})
        total_cost += payment_fee
    
    # Özel hizmetler ekleme
    special_fees = add_special_service_fees(country, special_services, fee_breakdown)
    total_cost += special_fees
    
    # Sonuçları göster
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("💵 Ücret Dökümü")
        df_fees = pd.DataFrame(fee_breakdown)
        st.dataframe(df_fees, use_container_width=True, height=400)
        
    with col2:
        st.subheader("📈 Özet")
        st.metric("Toplam Maliyet", f"{currency} {total_cost:.2f}")
        st.metric("Gönderi Değeri", f"{currency} {value:.2f}")
        st.metric("Maliyet Oranı", f"{(total_cost/value)*100:.1f}%")
        
        # Kategori bazında toplam
        st.write("**Kategori Bazında Toplam:**")
        categories = {}
        for fee in fee_breakdown:
            cat = fee["Kategori"]
            amount = float(fee["Ücret"].replace(currency, "").replace("$", "").replace("€", "").replace("£", "").replace("AUD", "").replace("CAD", "").strip())
            categories[cat] = categories.get(cat, 0) + amount
        
        for cat, amount in categories.items():
            st.write(f"• {cat}: {currency} {amount:.2f}")

def add_special_service_fees(country, special_services, fee_breakdown):
    """Özel hizmet ücretlerini ekle"""
    total_special = 0
    
    if country == "Hollanda":
        if special_services.get("transit"):
            fee_breakdown.append({"Kategori": "Özel Hizmetler", "Hizmet": "Gümrük Altında Transit", "Ücret": "€45.00"})
            total_special += 45
        if special_services.get("temporary_import"):
            fee_breakdown.append({"Kategori": "Özel Hizmetler", "Hizmet": "Geçici İthalat", "Ücret": "€42.00"})
            total_special += 42
        if special_services.get("return_goods"):
            fee_breakdown.append({"Kategori": "Özel Hizmetler", "Hizmet": "İade Malları", "Ücret": "€42.00"})
            total_special += 42
        if special_services.get("other_gov"):
            fee_breakdown.append({"Kategori": "Özel Hizmetler", "Hizmet": "Diğer Devlet Kurumları", "Ücret": "€40.00"})
            total_special += 40
        if special_services.get("post_entry"):
            fee_breakdown.append({"Kategori": "Özel Hizmetler", "Hizmet": "Kayıt Sonrası Düzeltme", "Ücret": "€90.00"})
            total_special += 90
    
    elif country == "Birleşik Krallık":
        if special_services.get("cargo_clearance"):
            fee_breakdown.append({"Kategori": "Özel Hizmetler", "Hizmet": "Kargo Gümrükleme", "Ücret": "£35.00"})
            total_special += 35
        if special_services.get("temporary_import"):
            fee_breakdown.append({"Kategori": "Özel Hizmetler", "Hizmet": "Geçici İthalat", "Ücret": "£25.00"})
            total_special += 25
        if special_services.get("return_goods"):
            fee_breakdown.append({"Kategori": "Özel Hizmetler", "Hizmet": "İade Malları", "Ücret": "£21.00"})
            total_special += 21
        if special_services.get("other_gov"):
            fee_breakdown.append({"Kategori": "Özel Hizmetler", "Hizmet": "Diğer Devlet Kurumları", "Ücret": "£27.00"})
            total_special += 27
        if special_services.get("import_permits"):
            fee_breakdown.append({"Kategori": "Özel Hizmetler", "Hizmet": "İthalat İzinleri", "Ücret": "£40.00"})
            total_special += 40
    
    elif country == "Amerika Birleşik Devletleri":
        if special_services.get("fda_clearance"):
            fee_breakdown.append({"Kategori": "Özel Hizmetler", "Hizmet": "FDA Gümrükleme", "Ücret": "$27.50"})
            total_special += 27.50
        if special_services.get("fws_clearance"):
            fee_breakdown.append({"Kategori": "Özel Hizmetler", "Hizmet": "FWS Gümrükleme", "Ücret": "$50.00"})  # Örnek tutar
            total_special += 50
        if special_services.get("atfe_clearance"):
            fee_breakdown.append({"Kategori": "Özel Hizmetler", "Hizmet": "ATFE Gümrükleme", "Ücret": "$74.00"})
            total_special += 74
        if special_services.get("govt_records"):
            fee_breakdown.append({"Kategori": "Özel Hizmetler", "Hizmet": "Devlet Kayıtları", "Ücret": "$53.00"})
            total_special += 53
        if special_services.get("transit"):
            fee_breakdown.append({"Kategori": "Özel Hizmetler", "Hizmet": "Gümrük Altında Transit", "Ücret": "$90.00"})
            total_special += 90
        if special_services.get("temporary_import"):
            fee_breakdown.append({"Kategori": "Özel Hizmetler", "Hizmet": "Geçici İthalat", "Ücret": "$150.00"})
            total_special += 150
        if special_services.get("broker_transfer"):
            fee_breakdown.append({"Kategori": "Özel Hizmetler", "Hizmet": "Komisyoncu Belge Transferi", "Ücret": "$51.00"})
            total_special += 51
    
    elif country == "Avustralya":
        if special_services.get("quarantine_basic"):
            fee_breakdown.append({"Kategori": "Özel Hizmetler", "Hizmet": "Karantina Belge İşleme", "Ücret": "AUD $37.00"})
            total_special += 37
        if special_services.get("quarantine_inspection"):
            fee_breakdown.append({"Kategori": "Özel Hizmetler", "Hizmet": "Karantina İnceleme", "Ücret": "AUD $99.00"})
            total_special += 99
        if special_services.get("quarantine_weekend"):
            fee_breakdown.append({"Kategori": "Özel Hizmetler", "Hizmet": "Karantina Hafta Sonu", "Ücret": "AUD $120.00"})
            total_special += 120
        if special_services.get("broker_transfer"):
            fee_breakdown.append({"Kategori": "Özel Hizmetler", "Hizmet": "Komisyoncu Belge Transferi", "Ücret": "AUD $55.00"})
            total_special += 55
    
    elif country == "Kanada":
        if special_services.get("other_gov"):
            fee_breakdown.append({"Kategori": "Özel Hizmetler", "Hizmet": "Diğer Devlet Kurumu", "Ücret": "CAD $16.50"})
            total_special += 16.50
        if special_services.get("business_number"):
            fee_breakdown.append({"Kategori": "Özel Hizmetler", "Hizmet": "İş Kayıt Numarası", "Ücret": "CAD $5.00"})
            total_special += 5
        if special_services.get("import_permit_single"):
            fee_breakdown.append({"Kategori": "Özel Hizmetler", "Hizmet": "İthalat İzni - Tek", "Ücret": "CAD $25.00"})
            total_special += 25
        if special_services.get("import_permit_multi"):
            fee_breakdown.append({"Kategori": "Özel Hizmetler", "Hizmet": "İthalat İzni - Çoklu", "Ücret": "CAD $10.00"})
            total_special += 10
        if special_services.get("after_hours_fedex"):
            fee_breakdown.append({"Kategori": "Özel Hizmetler", "Hizmet": "Mesai Sonrası - FedEx", "Ücret": "CAD $120.00"})
            total_special += 120
        if special_services.get("after_hours_external"):
            fee_breakdown.append({"Kategori": "Özel Hizmetler", "Hizmet": "Mesai Sonrası - Harici", "Ücret": "CAD $50.00"})
            total_special += 50
        if special_services.get("temporary_import"):
            fee_breakdown.append({"Kategori": "Özel Hizmetler", "Hizmet": "Geçici İthalat", "Ücret": "CAD $120.00"})
            total_special += 120
        if special_services.get("customs_transit"):
            fee_breakdown.append({"Kategori": "Özel Hizmetler", "Hizmet": "Gümrük Altında Transfer", "Ücret": "CAD $40.00"})
            total_special += 40
    
    return total_special

def show_netherlands_details():
    """Hollanda detaylı bilgileri"""
    st.subheader("Hollanda - Detaylı Bilgiler")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.write("**Ana Ücretler:**")
        
        # Detaylı açıklamalarla ücret listesi
        st.write("**🔹 KDV:** 21% (vergilendirilebilir değer üzerinden standart oran)")
        st.write("**🔹 Gümrük vergisi:** Tarife sınıflandırmasına göre değişir")
        
        with st.expander("**🔹 Ek Kalem Ücretleri - €8.00/kalem (6. kalemden itibaren)**"):
            st.write("Gönderi farklı tarife sınıflandırması gerektiren birden fazla emtia, farklı ülkelerden aynı emtialar, birden fazla ticari fatura veya her kalem için ayrı giriş talep edildiğinde uygulanır")
        
        with st.expander("**🔹 Gümrük Altında Transit - €45.00/gönderi**"):
            st.write("Talep üzerine, FedEx gerekli transfer belgelerini hazırlar ve gelen gönderileri varış noktasından kendi kendine gümrükleme veya FedEx dışında bir gümrük müşavirliği kullanımı için belirtilen yere taşır")
        
        with st.expander("**🔹 İade Malları - €42.00/gönderi**"):
            st.write("FedEx, onarım, işleme, test, değerlendirme, ticaret fuarları için geçici olarak ihraç edilen veya değiştirilmeden ihraç ülkesine iade edilen malların iadesini organize eder. İthalatçının gerekli ihracat belgeleriyle vergi/harç muafiyeti talep etmesine olanak sağlar")
        
        with st.expander("**🔹 Geçici İthalat - €42.00/gönderi**"):
            st.write("Gönderilerin belirli bir süre için geçici olarak ithal edilmesi talep edildiğinde, FedEx Gümrük tarafından belirtilen gerekli belgeleri hazırlayarak ve dosyalayarak ithalat sürecini koordine eder")
        
        with st.expander("**🔹 Depolama - €10.00/gün (3 iş günü sonrası)**"):
            st.write("Gönderi yayınlanan süre sınırını aşarak gümrükleme yerinde temizlenmemiş kalırsa FedEx depolama ücreti talep edebilir")
        
        with st.expander("**🔹 Diğer Devlet Kurumları - €40.00 + geçiş ücretleri**"):
            st.write("Devlet kurumu tarafından belge doğrulama veya kimlik kontrolü gerektiğinde uygulanan ücret; yerel konseyler veya ticari ajanslar dahil olmak üzere aynı gönderi için birden fazla kurumdan ücret alınabilir. FedEx tüm harici kurumlardan gelen ücretleri aktarır")
        
        with st.expander("**🔹 Özel Hizmet - €50.00/saat (min €40.00)**"):
            st.write("FedEx özel raporlar oluşturma, paketleri açma/etiketleme gibi ek hizmetler sağlar. Hizmet uygulamasından önce hem FedEx hem de ödeyen saatlik masrafları kabul etmelidir")
        
        with st.expander("**🔹 Ön Ödeme (Doğrudan Ödeme İşlemi)**"):
            st.write("**€0.01-€50.00:** V&H'ın %30'u (min €5.00)")
            st.write("**€50.00-€600.00:** €15.00")
            st.write("**€600.00+:** V&H'ın %2.5'i")
            st.write("Gönderilerin serbest bırakılması ve gümrük ücretlerinin ödenmesi için doğrudan ödeme sürecinin başlatılması ücreti. Kredi riski olan ödeyenler veya çok yüksek değerli gönderiler odaklı hizmet")
        
        with st.expander("**🔹 Kayıt Sonrası Düzeltme - €90.00/gönderi**"):
            st.write("Müşteri talebi üzerine, FedEx daha önce sağlanan bilgilerdeki kaydı düzeltmek için Gümrük'e Kayıt Düzeltmesi sunar. Fazla ödemenin iadesi veya Gümrük'e ek vergi/harç borcu artı FedEx ücreti ile sonuçlanabilir")
        
        with st.expander("**🔹 Ödeme Ücreti**"):
            st.write("**€0.01-€50.00:** V&H'ın %30'u (min €8.00)")
            st.write("**€50.00-€600.00:** €15.00")
            st.write("**€600.00+:** V&H'ın %2.5'i")
            st.write("FedEx, gümrük kurumuna zamanında ödemeyi sağlamak için müşteri adına geçerli vergiler, harçlar ve düzenleyici ücretleri öder. Ödeyen, ödenen toplam tutar artı ek ücret için sorumludur")
        
        with st.expander("**🔹 Vergi ve Harç Yönlendirme - €18.00 veya V&H'ın %2.5'i**"):
            st.write("Gönderici hedef ülke dışında vergi/harç ödemesi için üçüncü taraf faturalandırma seçeneğini seçtiğinde Ödeme Ücreti yerine uygulanır")
    
    with col2:
        st.write("**📋 Gerekli Belgeler:**")
        nl_reqs = [
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
        ]
        for req in nl_reqs:
            st.write(f"• {req}")
        
        st.write("**⚠️ Özel Notlar:**")
        nl_notes = [
            "AB gümrük birliği avantajları - iç gümrük vergileri yok",
            "Ticari ithalatlar için EORI numarası zorunlu", 
            "Ek Kalem Ücretleri 6. kalemden itibaren başlar (5 ücretsiz kalem)",
            "Depolama ücretleri 3 iş günü hoşgörü süresi sonrası uygulanır",
            "İade malları hizmeti uygun belgelerle vergi/harç muafiyeti sağlar",
            "Belirtilen süre için geçici ithalat mevcut",
            "Kredi riski yönetimi için ön ödeme hizmeti mevcut",
            "Kayıt düzeltmeleri için kayıt sonrası ayarlamalar mümkün",
            "Yönlendirme ücreti ile üçüncü taraf faturalandırma seçeneği mevcut"
        ]
        for note in nl_notes:
            st.write(f"• {note}")

def show_uk_details():
    """İngiltere detaylı bilgileri"""
    st.subheader("Birleşik Krallık - Detaylı Bilgiler")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.write("**Ana Ücretler:**")
        
        st.write("**🔹 KDV:** 20% (vergilendirilebilir değer üzerinden standart oran)")
        st.write("**🔹 Gümrük vergisi:** Tarife sınıflandırmasına göre değişir")
        
        with st.expander("**🔹 Ek Kalem Ücretleri - £5.00/kalem (6. kalemden itibaren)**"):
            st.write("Gönderi farklı tarife sınıflandırması gerektiren birden fazla emtia, farklı ülkelerden aynı emtialar, birden fazla ticari fatura veya her kalem için ayrı giriş talep edildiğinde uygulanır")
        
        with st.expander("**🔹 Depolama - £10.00/gün (3 iş günü sonrası)**"):
            st.write("Gönderi yayınlanan süre sınırını aşarak temizlenmemiş kalırsa uygulanır")
        
        with st.expander("**🔹 Kargo Gümrükleme - £35.00/gönderi**"):
            st.write("Kargo ve üçüncü taraf gönderileri için tam uzmanlık kullanan FedEx Gümrük Müşavirliği Hizmetleri")
        
        with st.expander("**🔹 İade Malları - £21.00/gönderi**"):
            st.write("Onarım, işleme, test, değerlendirme, ticaret fuarları için geçici olarak ihraç edilen veya değiştirilmeden vergi/harç muafiyeti talep etmek için iade edilen mallar için")
        
        with st.expander("**🔹 Diğer Devlet Kurumları - £27.00 + geçiş ücretleri**"):
            st.write("Devlet kurumları tarafından belge doğrulama veya kimlik kontrolü gerektiğinde uygulanır")
        
        with st.expander("**🔹 Geçici İthalat - £25.00/gönderi**"):
            st.write("Belirli süre için gerekli gümrük belgeleriyle geçici ithalat sürecinin koordinasyonu")
        
        with st.expander("**🔹 Özel Hizmet - £45.00/saat (min £30.00)**"):
            st.write("Özel raporlar, paketleri açma/etiketleme gibi ek hizmetler (önceden anlaşma gerekir)")
        
        with st.expander("**🔹 Ön Ödeme (Doğrudan Ödeme İşlemi)**"):
            st.write("**£0.01-£42.50:** V&H'ın %30'u (min £4.25)")
            st.write("**£42.50-£510.00:** £12.75")
            st.write("**£510.00+:** V&H'ın %2.5'i")
            st.write("Kredi riski olan müşteriler veya yüksek değerli gönderiler için doğrudan ödeme süreci ücreti")
        
        with st.expander("**🔹 Kayıt Sonrası Düzeltme - £60.00/gönderi**"):
            st.write("Önceki bilgiler için kayıt düzeltme hizmeti, iade veya ek vergi/harç borcu ile sonuçlanabilir")
        
        with st.expander("**🔹 Ödeme Ücreti**"):
            st.write("**£0.01-£42.50:** V&H'ın %30'u (min £6.65)")
            st.write("**£42.50-£510.00:** £12.75")
            st.write("**£510.00+:** V&H'ın %2.5'i")
            st.write("FedEx vergileri, harçları ve düzenleyici ücretleri ödediğinde uygulanır")
        
        with st.expander("**🔹 İthalat İzinleri ve Lisansları - £40.00/gönderi**"):
            st.write("Yerel düzenleyici kurum tarafından gerekli görülen ithalat izni veya lisansının alınması veya yenilenmesi ücreti")
        
        with st.expander("**🔹 Vergi ve Harç Yönlendirme - Min £15.00 veya V&H'ın %2.5'i**"):
            st.write("Hedef ülke dışında vergi/harç ödemesi için üçüncü taraf faturalandırma seçeneği seçildiğinde Ödeme Ücreti yerine uygulanır")
        
        with st.expander("**🔹 Tutma ve Bildirim - £2.50/gönderi**"):
            st.write("Özel gümrük temizleme talimatları için gelen gönderileri durdurma hizmeti (FedEx gümrükleme, kendi kendine gümrükleme veya üçüncü taraf komisyoncu)")
    
    with col2:
        st.write("**📋 Gerekli Belgeler:**")
        uk_reqs = [
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
        ]
        for req in uk_reqs:
            st.write(f"• {req}")
        
        st.write("**⚠️ Brexit Sonrası Özel Notlar:**")
        uk_notes = [
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
        for note in uk_notes:
            st.write(f"• {note}")

def show_us_details():
    """ABD detaylı bilgileri"""
    st.subheader("Amerika Birleşik Devletleri - Detaylı Bilgiler")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.write("**Express Hizmet Ücretleri:**")
        
        st.write("**💵 Temel İşlem Ücretleri:**")
        with st.expander("**🔹 Ek Kayıt Kalemleri - $3.50/kalem (4. kalemden itibaren)**"):
            st.write("Gönderi aşağıdaki durumlarda ek tarife sınıflandırması gerektirebilir: 1) Yayınlanan ücretlerdeki Ücretsiz Kalem sınırının ötesinde bir veya daha fazla tarife sınıflandırması varsa; 2) Aynı emtia birden fazla ülkede üretilmişse; 3) Gümrüğe sunulan birden fazla Ticari Fatura her fatura için ayrı tarife sınıflandırması gerektiriyorsa")
        
        with st.expander("**🔹 Kayıt Kopyası - $2.10/kayıt**"):
            st.write("Talep üzerine, ABD ithalat belgelerinizin ek kopyalarını kompakt disk (CD) veya elektronik veri değişimi (EDI) yoluyla sağlayabiliriz. Önceki ay için derlenen tüm kayıtlarla birlikte ayda bir kez CD veya EDI iletimi alacaksınız.")
        
        with st.expander("**🔹 Depolama - $0.08/kg/gün + $20 taban (3 gün sonrası)**"):
            st.write("Gönderi yayınlanan süre sınırını aşarak gümrükleme yerinde temizlenmemiş kalırsa depolama ücreti talep edebiliriz. Yerel not: Ücretler gümrükleme yerinde üçüncü günden itibaren uygulanır")
        
        st.write("**🏛️ Düzenleyici Kurum Ücretleri:**")
        with st.expander("**🔹 FDA Gümrükleme - $27.50/gönderi**"):
            st.write("Tıbbi cihazlar, ilaçlar, bilgisayar monitörleri, lazer CD çalarlar, kozmetikler, gözlükler, gıda ve gıda ürünleri veya diğer kontrollü ürünler gibi belirli ticari malların girişi için gerektiği gibi bilgi dosyalayacağız ve onay alacağız")
        
        with st.expander("**🔹 ATFE Gümrükleme - $74.00/gönderi**"):
            st.write("ABD Alkol, Tütün, Ateşli Silahlar ve Patlayıcılar Bürosu (ATFE) tarafından düzenlenen emtiaların girişi için gerektiği gibi ek işlem sağlayacağız, İç Gelir Servisi Vergi Değerlendirmesi ve gönderinin tüm gerekli ATFE lisans ve izinlerine sahip olduğundan emin olmak için denetim dahil.")
        
        with st.expander("**🔹 FWS Gümrükleme - Gerçek ücret + $22 idari**"):
            st.write("Canlı hayvanları ve/veya hayvanlardan yaratılan ürünleri içeren emtiaların girişi için gerektiği gibi Balık ve Yaban Hayatı USFWS Form 3-177 (edec) dosyalayacağız ve Balık ve Yaban Hayatı Servisi'ne (FWS) belgeler ve izinler sunacağız")
        
        st.write("**🚚 Özel Hizmetler:**")
        with st.expander("**🔹 Geçici İthalat - $150.00/gönderi**"):
            st.write("Gönderilerin belirli bir süre için geçici olarak ithal edilmesini talep ettiğinizde, Gümrük tarafından belirtilen gerekli belgeleri tavsiye ederek, hazırlayarak ve dosyalayarak ithalat sürecini koordine edeceğiz. Yerel Not: Geçici İthalat hizmeti yeni müşteriler için mevcut değildir")
        
        with st.expander("**🔹 Gümrük Altında Transit - $90.00/gönderi**"):
            st.write("Talep üzerine, kendi kendine temizliyorsanız veya gelen gönderinizi temizlemek için FedEx dışında bir Aracılık şirketi kullanıyorsanız, gerekli transfer belgelerini hazırlayacağız ve gelen gönderinizi varış noktasından belirttiğiniz yere taşıyacağız")
        
        with st.expander("**🔹 Komisyoncu Belge Transferi - $51.00/gönderi**"):
            st.write("Komisyoncu Belge Transferi, kendi gümrük temizleme departmanınızı kullanarak kendi kendine temizleme veya gelen gönderinizi temizlemek için FedEx dışında bir Aracılık şirketi kullanma esnekliği sağlarken, tüm evrakları size veya seçtiğiniz komisyoncuya sağlıyoruz")
        
        # Ödeme ücretleri tablosu
        st.write("**💳 Ödeme Ücretleri:**")
        payment_fees = [
            {"Değer Aralığı": "≤$800", "Ödeme Ücreti": "$4.50 veya V&H'ın %2'si", "Yönlendirme": "$8.50 veya V&H'ın %2'si"},
            {"Değer Aralığı": ">$800", "Ödeme Ücreti": "$14.00 veya V&H'ın %2'si", "Yönlendirme": "$27.00 veya V&H'ın %2'si"}
        ]
        df_payment = pd.DataFrame(payment_fees)
        st.dataframe(df_payment, use_container_width=True)
    
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
        
        st.write("**🔹 GST:** 10% (vergilendirilebilir değer)")
        st.write("**🔹 Gümrük vergisi:** Tarife sınıflandırmasına göre değişir")
        
        with st.expander("**🔹 Vergi ve Harç Değişikliği - AUD $132**"):
            st.write("Müşteri vergi ve harç tutarını itiraz ettiğinde uygulanır")
        
        with st.expander("**🔹 Elektronik Kayıt Ücreti (Resmi Kayıt)**"):
            st.write("**$1,000-$9,999 değeri için:** AUD $95")
            st.write("**$10,000+ değer için:** AUD $197")
            st.write("Resmi gümrük kayıt işlemleri için elektronik veri işleme ücreti")
        
        with st.expander("**🔹 Bitki, Hayvan ve Gıda Karantinası**"):
            st.write("**Belge İşleme:** AUD $37")
            st.write("**Belge İşleme ve İnceleme:** AUD $99") 
            st.write("**Hafta Sonu/Mesai Değerlendirme İşleme:** AUD $120")
            st.write("Avustralya'nın katı biyogüvenlik yasaları kapsamında karantina işlemleri")
        
        with st.expander("**🔹 Avans Ücreti - AUD $20 veya %2.9**"):
            st.write("AUD $20 veya vergi, harç, Kayıt Ücreti ve diğer düzenleyici ücretlerin %2.9'u hangisi büyükse. FedEx hesabıyla düzenleyici ücretleri ödeme yapan müşteriler için uygulanır")
        
        with st.expander("**🔹 ROD Ücreti - %2.9 veya AUD $20**"):
            st.write("Vergi harcının %2.9'u veya gönderi başına AUD $20, hangisi yüksekse. FedEx hesap numarası olmayan müşteriler için uygulanır")
        
        with st.expander("**🔹 Komisyoncu Belge Transferi - AUD $55/gönderi**"):
            st.write("Kendi gümrük temizleme sürecinizi yönetmek istediğinizde tüm gerekli belgelerin size veya seçtiğiniz komisyoncuya transferi")
        
        with st.expander("**🔹 Depolama - AUD $38.50/gün (BSO - 3 gün sonrası)**"):
            st.write("Broker Hizmet Seçeneği (BSO) gönderileri için 3 günlük hoşgörü süresi sonrasında günlük depolama ücreti")
        
        with st.expander("**🔹 Vergi ve Harç Yönlendirme - Min AUD $30 veya %2.9**"):
            st.write("Minimum AUD $30 veya V&H'ın %2.9'u. Üçüncü taraf faturalandırma seçeneği seçildiğinde uygulanır")
    
    with col2:
        st.write("**🦘 Biyogüvenlik Gereklilikleri:**")
        au_bio = [
            "Tüm ahşap ambalajlar ISPM-15 uyumlu olmalı",
            "Gıda ürünleri detaylı bileşen listesi gerektirir",
            "Karantina beyanı zorunlu",
            "AQIS (Avustralya Karantina ve Denetim Servisi) katılımı gerekli",
            "Bitki ürünleri için fitosanitasyon sertifikaları",
            "Hayvan ürünleri için sağlık sertifikaları",
            "Katı kontrol prosedürleri uygulanır"
        ]
        for bio in au_bio:
            st.write(f"• {bio}")
        
        st.write("**📋 Gerekli Belgeler:**")
        au_reqs = [
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
        ]
        for req in au_reqs:
            st.write(f"• {req}")
        
        st.write("**⚠️ Özel Notlar:**")
        au_notes = [
            "Avustralya dünyanın en katı biyogüvenlik yasalarından bazılarına sahip",
            "Yüksek değer eşiği: Kombine FOB ve sigorta > AUD 1,000 $",
            "ROD Ücreti FedEx hesap numarası olmayan müşteriler için uygulanır",
            "FedEx hesabıyla düzenleyici ücretleri ödeme yapan müşteriler için Avans Ücreti",
            "Depolama ücretleri yalnızca BSO (Broker Hizmet Seçeneği) gönderileri için uygulanır",
            "Karantina ücretleri yenilebilir ürünler, hayvan ürünleri, sanat eserleri, yapay aroma ve kereste için yerel otoriteler tarafından belirlenir",
            "Tedavi amaçlı ürünler TGA onayı gerektirir",
            "Elektronik ürünler ACMA uyumluluğu gerektirebilir"
        ]
        for note in au_notes:
            st.write(f"• {note}")

def show_canada_details():
    """Kanada detaylı bilgileri"""
    st.subheader("Kanada - Detaylı Bilgiler")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.write("**🇨🇦 Express Hizmet Ücretleri:**")
        
        st.write("**🔹 GST/HST:** İl'e göre %5-15 değişir")
        st.write("**🔹 Gümrük vergisi:** Tarife sınıflandırmasına göre değişir")
        
        with st.expander("**🔹 Ek Kalem (3+) - CAD $5.30/kalem**"):
            st.write("3 veya daha fazla kalemden oluşan gönderilerde her bir ek kalem için uygulanır")
        
        with st.expander("**🔹 Depolama (48 saat sonrası) - lb başına günde $0.25 CAD**"):
            st.write("48 saatlik hoşgörü süresi sonrasında pound başına günlük depolama ücreti")
        
        with st.expander("**🔹 Kayıt Sonrası Düzeltme - $75 CAD veya değerin %8'i**"):
            st.write("$75 CAD veya değerin %8'i, hangisi yüksekse. Gümrük beyanından sonra yapılan düzeltmeler için")
        
        with st.expander("**🔹 Diğer Devlet Kurumu - Kayıt başına $16.50 CAD**"):
            st.write("Sağlık Kanada, CFIA gibi diğer devlet kurumları için gerekli kayıt işlemleri")
        
        with st.expander("**🔹 Hesap Güvenlik İşleme**"):
            st.write("**Serbest Bırakma:** $3 CAD")
            st.write("**Onaylama:** $7 CAD")
            st.write("**Her ikisi de:** $10 CAD")
            st.write("C-TPAT, CSA gibi güvenlik programları için işlem ücretleri")
        
        with st.expander("**🔹 Mesai Sonrası İşlem Ücretleri**"):
            st.write("**FedEx Mesai Sonrası:** $120 CAD")
            st.write("**Harici Mesai Sonrası:** $50 CAD")
            st.write("Normal çalışma saatleri dışında yapılan işlemler için")
        
        with st.expander("**🔹 İş Kayıt Numarası Başvurusu - Kayıt başına $5 CAD**"):
            st.write("İş kayıt numarası olmayan müşteriler için geçici numara başvuru ücreti")
        
        with st.expander("**🔹 Faks Ücreti**"):
            st.write("**Yerel:** $3 CAD")
            st.write("**Şehirlerarası:** $4 CAD")
            st.write("Belge gönderimi için faks hizmet ücretleri")
        
        with st.expander("**🔹 İthalat İzni**"):
            st.write("**Tek Kullanım:** $25 CAD + CBSA ücretleri")
            st.write("**Çoklu Kullanım:** $10 CAD + CBSA ücretleri")
            st.write("Kontrollü mallar için gerekli ithalat izin belgesi işlemleri")
        
        with st.expander("**🔹 Düşük Değerli Gönderi İşlemleri**"):
            st.write("**Belge İşleme:** $4 CAD")
            st.write("**Kayıt Düzeltme:** $25 CAD")
            st.write("**Kayıt İstisnası:** $4 CAD")
            st.write("$20 CAD altındaki gönderi değerleri için özel işlem ücretleri")
        
        with st.expander("**🔹 Geçici İthalat - Kayıt başına $120 CAD**"):
            st.write("Geçici olarak Kanada'ya getirilen mallar için (fuarlar, sergi, onarım vb.)")
        
        with st.expander("**🔹 Gümrük Altında Transfer - Kayıt başına $40 CAD**"):
            st.write("Malların gümrük kontrolü altında başka bir yere transferi")
        
        with st.expander("**🔹 ROD Ücreti - CAD $11.40 + Geçerli Vergi**"):
            st.write("FedEx hesap numarası olmayan müşteriler için düzenleyici ücretler")
        
        with st.expander("**🔹 Ödeme Ücreti - V&H'ın %2.95'i veya $11.40 CAD**"):
            st.write("V&H'ın %2.95'i veya $11.40 CAD, hangisi yüksekse. Ücret ödeme hizmet komisyonu")
    
    with col2:
        st.write("**🇨🇦 Standard Hizmet Ücretleri:**")
        
        st.write("**🔹 GST/HST:** İl'e göre %5-15 değişir")
        st.write("**🔹 Gümrük vergisi:** Tarife sınıflandırmasına göre değişir")
        
        with st.expander("**🔹 Depolama (7 gün sonrası) - lb başına günde $0.25 CAD**"):
            st.write("7 günlük hoşgörü süresi sonrasında pound başına günlük depolama ücreti")
        
        with st.expander("**🔹 Kayıt Sonrası Düzeltme - $50 CAD veya değerin %5'i**"):
            st.write("$50 CAD veya değerin %5'i, hangisi yüksekse. Standard hizmet için düzeltme ücreti")
        
        with st.expander("**🔹 Diğer Devlet Kurumu - Kayıt başına $16.50 CAD**"):
            st.write("Standard hizmet için diğer devlet kurumu kayıt işlemleri")
        
        with st.expander("**🔹 İş Kayıt Numarası Başvurusu - Kayıt başına $5 CAD**"):
            st.write("Standard hizmet müşterileri için iş kayıt numarası başvuru ücreti")
        
        with st.expander("**🔹 Düşük Değerli Gönderi Belge - $4 CAD**"):
            st.write("$20 CAD altındaki gönderiler için belge işleme ücreti")
        
        with st.expander("**🔹 Geçici İthalat - Kayıt başına $120 CAD**"):
            st.write("Standard hizmet için geçici ithalat işlem ücreti")
        
        with st.expander("**🔹 Gümrük Altında Transfer - Kayıt başına $40 CAD**"):
            st.write("Standard hizmet için gümrük altında transfer ücreti")
        
        with st.expander("**🔹 ROD Ücreti - CAD $9.90 + Geçerli Vergi**"):
            st.write("Standard hizmet için düzenleyici ücretler (Express'den düşük)")
        
        with st.expander("**🔹 Ödeme Ücreti - V&H'ın %2.95'i veya $9.90 CAD**"):
            st.write("V&H'ın %2.95'i veya $9.90 CAD, hangisi yüksekse. Standard hizmet ödeme komisyonu")
        
        st.write("**📋 Gerekli Belgeler:**")
        ca_reqs = [
            "Detaylı ticari fatura (İngilizce veya Fransızca)",
            "Gerekiyorsa ithalat izni",
            "Kontrollü mallar için özel lisanslar",
            "CFIA sertifikaları (gıda, bitki, hayvan ürünleri)",
            "Sağlık Kanada onayı (ilaç, tıbbi cihaz)",
            "Çevre Kanada izni (kimyasallar)",
            "Menşe şahadetnâmesi (NAFTA, CETA vb.)",
            "Ticari ithalatlar için İş Numarası",
            "MSDS (kimyasallar için)",
            "ATA Carnet (geçici ithalat)"
        ]
        for req in ca_reqs:
            st.write(f"• {req}")
        
        st.write("**⚠️ Özel Notlar:**")
        ca_notes = [
            "Express hizmet ücretleri Standard'dan genellikle yüksek",
            "48 saat (Express) vs 7 gün (Standard) hoşgörü süresi",
            "GST/HST oranları il'e göre değişir (%5-15 arası)",
            "Düşük değer eşiği: $20 CAD",
            "CBSA (Kanada Sınır Hizmetleri Ajansı) ek ücretler uygulayabilir",
            "ROD ücretleri hizmet tipine göre farklılık gösterir",
            "Ödeme ücreti komisyonu her iki hizmette de %2.95",
            "Mesai sonrası ücretler sadece Express hizmette",
            "Güvenlik programı ücretleri Express'e özel"
        ]
        for note in ca_notes:
            st.write(f"• {note}")

# Ana uygulama
if __name__ == "__main__":
    create_country_comparison_tables()



'''
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

'''