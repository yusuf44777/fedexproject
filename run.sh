#!/bin/bash

# FedEx Karşılaştırma Uygulaması Başlatıcı

echo "🚚 FedEx Ülke Karşılaştırma Uygulaması Başlatılıyor..."
echo ""

# Gerekli paketlerin yüklü olup olmadığını kontrol et
echo "📦 Gereksinimler kontrol ediliyor..."
pip install -r requirements.txt

echo ""
echo "🌐 Streamlit uygulaması başlatılıyor..."
echo "📱 Tarayıcınızda http://localhost:8501 adresinde açılacak"
echo ""
echo "⏹️  Durdurmak için Ctrl+C kullanın"
echo ""

# Streamlit uygulamasını başlat
streamlit run app.py
