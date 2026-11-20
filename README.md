# Customer Churn Prediction System

## Proje Hakkında
Bu proje, PostgreSQL ve Python kullanarak telekomünikasyon müşterilerinin abonelikten ayrılma durumunu tahmin etmek amacıyla geliştirilmiştir.

## Kullanılan Teknolojiler
- PostgreSQL
- Docker Desktop
- Python
- Pandas
- Scikit-learn
- Psycopg
- Logistic Regression

## Veri Seti
Telco Customer Churn — 7.043 müşteri, 21 sütun.

Kaynak: https://www.kaggle.com/datasets/blastchar/telco-customer-churn

## Model Performansı
- Accuracy: %81,05
- Precision: %67,66
- Recall: %54,81
- F1-Score: %60,56

## Sistem
Müşteri verileri PostgreSQL'den SQL sorgularıyla alınır. Python'da makine öğrenmesi modeli eğitilir ve test edilir. Model tahminleri tekrar PostgreSQL'deki `churn_predictions` tablosuna kaydedilir.

## Kurulum ve Çalıştırma

**Gereksinimler:** Docker Desktop, PostgreSQL 18, Python 3.14 ve Git.

1. Projeyi GitHub üzerinden bilgisayarınıza indirin.
2. Docker Desktop üzerinde PostgreSQL container'ını başlatın.
3. `churn_prediction_db` isimli veritabanını oluşturun.
4. `schema.sql` dosyasını çalıştırarak tabloları oluşturun.
5. Kaggle'dan Telco Customer Churn veri setini indirin.
6. CSV dosyasını Docker container'ındaki `/tmp/telco.csv` konumuna kopyalayın.
7. `veri_aktar.sql` dosyasını çalıştırarak müşteri verilerini yükleyin.
8. PostgreSQL'de `churn_app` kullanıcısını oluşturup gerekli okuma ve tahmin yazma izinlerini verin.
9. Python sanal ortamını oluşturun ve `requirements.txt` dosyasındaki kütüphaneleri kurun.
10. `python veri_cek.py` komutuyla modeli çalıştırın.

**Not:** PostgreSQL bağlantı şifresi program çalışırken kullanıcıdan alınır. Şifreler GitHub'a yüklenmez.