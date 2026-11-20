--
-- PostgreSQL database dump
--

\restrict UFHAafuNt3BSu9TNhNhKkmKIgdVwwaqcE4k3ELgoiWIC0f4qutU7VBjjnI1z2cV

-- Dumped from database version 18.6 (Debian 18.6-1.pgdg13+2)
-- Dumped by pg_dump version 18.6 (Debian 18.6-1.pgdg13+2)

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET transaction_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: churn_predictions; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.churn_predictions (
    customer_id character varying(20) NOT NULL,
    actual_churn smallint,
    predicted_churn smallint,
    churn_probability numeric(6,5),
    predicted_at timestamp with time zone DEFAULT now()
);


--
-- Name: customers; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.customers (
    customer_id character varying(20) CONSTRAINT customers_customer_id_not_null1 NOT NULL,
    gender character varying(10),
    senior_citizen smallint,
    partner character varying(3),
    dependents character varying(3),
    tenure integer,
    phone_service character varying(3),
    multiple_lines character varying(30),
    internet_service character varying(30),
    online_security character varying(30),
    online_backup character varying(30),
    device_protection character varying(30),
    tech_support character varying(30),
    streaming_tv character varying(30),
    streaming_movies character varying(30),
    contract character varying(30),
    paperless_billing character varying(3),
    payment_method character varying(50),
    monthly_charges numeric(10,2),
    total_charges numeric(10,2),
    churn character varying(3)
);


--
-- Name: customers_staging; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.customers_staging (
    customer_id text,
    gender text,
    senior_citizen text,
    partner text,
    dependents text,
    tenure text,
    phone_service text,
    multiple_lines text,
    internet_service text,
    online_security text,
    online_backup text,
    device_protection text,
    tech_support text,
    streaming_tv text,
    streaming_movies text,
    contract text,
    paperless_billing text,
    payment_method text,
    monthly_charges text,
    total_charges text,
    churn text
);


--
-- Name: churn_predictions churn_predictions_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.churn_predictions
    ADD CONSTRAINT churn_predictions_pkey PRIMARY KEY (customer_id);


--
-- Name: customers customers_pkey1; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.customers
    ADD CONSTRAINT customers_pkey1 PRIMARY KEY (customer_id);


--
-- Name: churn_predictions churn_predictions_customer_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.churn_predictions
    ADD CONSTRAINT churn_predictions_customer_id_fkey FOREIGN KEY (customer_id) REFERENCES public.customers(customer_id);


--
-- PostgreSQL database dump complete
--

\unrestrict UFHAafuNt3BSu9TNhNhKkmKIgdVwwaqcE4k3ELgoiWIC0f4qutU7VBjjnI1z2cV

