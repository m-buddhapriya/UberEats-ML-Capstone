# Day 1 — Prompt Engineering

## 1. Objective

Prompt engineering was used to design and generate the Python script for
creating the synthetic Uber Eats datasets.

The objective was to generate realistic, structured, and relational data
that can later be used for:

- Customer segmentation
- Restaurant segmentation
- Customer sentiment analysis
- Delivery-time prediction
- Tip prediction
- Demand forecasting
- Business recommendations

The following prompting techniques were used:

1. P.T.C.F. Prompting
2. Role-Based Prompting
3. Few-Shot Prompting
4. Structured Output Prompting

---

# 2. P.T.C.F. Prompting

P.T.C.F. was used to clearly define the requirements before generating the
Python data-generation script.

## P — Persona

The model was assigned the following role:

> Act as a Senior Python Data Engineer specializing in synthetic data
> generation, data modeling, and analytics pipelines.

This establishes the expected technical perspective for the solution.

---

## T — Task

The task was defined as:

> Create a Python script that generates realistic synthetic Uber Eats
> operational and customer data.

The script needed to generate seven datasets:

- Customers
- Restaurants
- Drivers
- Orders
- Deliveries
- Reviews
- Payments

---

## C — Context

The following project context was provided:

The generated data will be used for customer segmentation, restaurant
segmentation, NLP sentiment analysis, delivery-time prediction, tip
prediction, demand forecasting, and business analysis.

The datasets must maintain realistic relationships using primary keys and
foreign keys.

Required relationships include:

- Orders → Customers
- Orders → Restaurants
- Deliveries → Orders
- Deliveries → Drivers
- Reviews → Orders
- Reviews → Customers
- Payments → Orders

---

## F — Format

The required output format was defined as:

1. Import required libraries
2. Configure random seed
3. Generate Customers
4. Generate Restaurants
5. Generate Drivers
6. Generate Orders
7. Generate Deliveries
8. Generate Reviews
9. Generate Payments
10. Save each dataset as CSV
11. Print dataset shapes

The generated CSV files should be stored under:

```text
data/raw/