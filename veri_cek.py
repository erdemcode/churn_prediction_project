
import psycopg
import pandas as pd
from getpass import getpass

# PostgreSQL sifresini al
sifre = getpass("PostgreSQL sifrenizi girin: ")

# Veritabanina baglan
with psycopg.connect(
    host="127.0.0.1",
    port=5432,
    dbname="churn_prediction_db",
    user="churn_app",
    password=sifre
) as baglanti:

    with baglanti.cursor() as imlec:

        # Musteri verilerini PostgreSQL'den cek
        imlec.execute("SELECT * FROM customers;")

        veriler = imlec.fetchall()

        sutunlar = [
            sutun.name for sutun in imlec.description
        ]

# Verileri DataFrame'e donustur
df = pd.DataFrame(veriler, columns=sutunlar)

print("\nVeri boyutu:")
print(df.shape)

print("\nIlk 5 musteri:")
print(df.head())

print("\nEksik toplam odeme sayisi:")
print(df["total_charges"].isna().sum())

# Sayisal sutunlari donustur
df["monthly_charges"] = pd.to_numeric(
    df["monthly_charges"], errors="coerce"
)

df["total_charges"] = pd.to_numeric(
    df["total_charges"], errors="coerce"
)

# Hedef degiskeni 0 ve 1 olarak kodla
df["churn"] = df["churn"].map({
    "No": 0,
    "Yes": 1
})

print("\nDonusturulen ilk 5 kayit:")
print(df[["monthly_charges", "total_charges", "churn"]].head())

print("\nHedef degisken dagilimi:")
print(df["churn"].value_counts())

print("\nEksik toplam odeme:")
print(df["total_charges"].isna().sum())

from sklearn.model_selection import train_test_split

# Ozellikler ve hedef degisken
X = df.drop(columns=["customer_id", "churn"])
y = df["churn"]

# Veriyi egitim ve test olarak ayir
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42,
    stratify=y
)

print("\nEgitim veri sayisi:", len(X_train))
print("Test veri sayisi:", len(X_test))

print("\nEgitim hedef dagilimi:")
print(y_train.value_counts())

print("\nTest hedef dagilimi:")
print(y_test.value_counts())

from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score

# Sayisal ve kategorik sutunlar
sayisal = X_train.select_dtypes(include="number").columns
kategorik = X_train.select_dtypes(exclude="number").columns

# Veri hazirlama
hazirlik = ColumnTransformer([
    ("sayisal", Pipeline([
        ("eksik", SimpleImputer(strategy="median")),
        ("olcekle", StandardScaler())
    ]), sayisal),

    ("kategorik", Pipeline([
        ("eksik", SimpleImputer(strategy="most_frequent")),
        ("kodla", OneHotEncoder(handle_unknown="ignore"))
    ]), kategorik)
])

# Model olusturma
model = Pipeline([
    ("hazirlik", hazirlik),
    ("siniflandir", LogisticRegression(max_iter=1000))
])

# Modeli egit
model.fit(X_train, y_train)

# Test verileriyle tahmin yap
tahminler = model.predict(X_test)

# Performans sonuclari
print("\nMODEL PERFORMANSI")
print("Accuracy:", round(accuracy_score(y_test, tahminler), 4))
print("Precision:", round(precision_score(y_test, tahminler), 4))
print("Recall:", round(recall_score(y_test, tahminler), 4))
print("F1-Score:", round(f1_score(y_test, tahminler), 4))

# Musterilerin ayrilma olasiliklarini hesapla
olasiliklar = model.predict_proba(X_test)[:, 1]

# Veritabanina kaydedilecek sonuclari hazirla
kayitlar = []

for indeks, tahmin, olasilik in zip(
    X_test.index, tahminler, olasiliklar
):
    kayitlar.append((
        df.loc[indeks, "customer_id"],
        int(y_test.loc[indeks]),
        int(tahmin),
        round(float(olasilik), 5)
    ))

# Tahminleri PostgreSQL'e kaydet
with psycopg.connect(
    host="127.0.0.1",
    port=5432,
    dbname="churn_prediction_db",
    user="churn_app",
    password=sifre
) as baglanti:

    with baglanti.cursor() as imlec:
        imlec.executemany("""
            INSERT INTO churn_predictions
            (customer_id, actual_churn,
             predicted_churn, churn_probability)
            VALUES (%s, %s, %s, %s)
            ON CONFLICT (customer_id)
            DO UPDATE SET
                actual_churn = EXCLUDED.actual_churn,
                predicted_churn = EXCLUDED.predicted_churn,
                churn_probability = EXCLUDED.churn_probability,
                predicted_at = NOW();
        """, kayitlar)

print("\nPostgreSQL'e kaydedilen tahmin:", len(kayitlar))

