
import psycopg
from getpass import getpass

# PostgreSQL bağlantısı
sifre = getpass("PostgreSQL sifrenizi girin: ")

with psycopg.connect(
    host="127.0.0.1",
    port=5432,
    dbname="churn_prediction_db",
    user="churn_app",
    password=sifre
) as baglanti:

    print("PostgreSQL baglantisi basarili!")

    # SQL sorgusunu çalıştır
    with baglanti.cursor() as imlec:
        imlec.execute("SELECT COUNT(*) FROM customers;")

        sonuc = imlec.fetchone()

        print("Toplam musteri sayisi:", sonuc[0])
