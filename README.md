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