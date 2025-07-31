@echo off
echo 🚚 FedEx Ülke Karşılaştırma Uygulaması Başlatılıyor...
echo.

echo 📦 Gereksinimler kontrol ediliyor...
pip install -r requirements.txt

echo.
echo 🌐 Streamlit uygulaması başlatılıyor...
echo 📱 Tarayıcınızda http://localhost:8501 adresinde açılacak
echo.
echo ⏹️  Durdurmak için Ctrl+C kullanın
echo.

streamlit run app.py
pause
