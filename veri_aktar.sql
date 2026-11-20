BEGIN;

TRUNCATE TABLE customers_staging;

COPY customers_staging
FROM '/tmp/telco.csv'
WITH (FORMAT csv, HEADER true);

INSERT INTO customers
SELECT
    customer_id,
    gender,
    senior_citizen::SMALLINT,
    partner,
    dependents,
    tenure::INTEGER,
    phone_service,
    multiple_lines,
    internet_service,
    online_security,
    online_backup,
    device_protection,
    tech_support,
    streaming_tv,
    streaming_movies,
    contract,
    paperless_billing,
    payment_method,
    monthly_charges::NUMERIC(10,2),
    NULLIF(TRIM(total_charges), '')::NUMERIC(10,2),
    churn
FROM customers_staging
ON CONFLICT (customer_id) DO NOTHING;

COMMIT;