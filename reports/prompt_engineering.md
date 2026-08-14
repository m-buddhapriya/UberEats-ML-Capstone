# Prompt Engineering — Day 1

## Objective

Prompt engineering techniques were used to design and generate the Python
synthetic data-generation script for the Uber Eats project.

The techniques used were:

1. P.T.C.F. Prompting
2. Role-Based Prompting
3. Few-Shot Prompting
4. Structured Output Prompting

---

# 1. P.T.C.F. Prompting

## Persona

Act as a Senior Python Data Engineer with experience in synthetic data
generation, relational data modeling, analytics pipelines, and machine
learning datasets.

## Task

Create a Python data-generation script for an Uber Eats Operational &
Customer Intelligence project.

The script should generate realistic synthetic data for Customers,
Restaurants, Drivers, Orders, Deliveries, Reviews, and Payments.

## Context

The datasets will be used for:

- Customer segmentation
- Restaurant segmentation
- Customer review sentiment analysis
- Delivery-time prediction
- Tip prediction
- Demand forecasting
- Business recommendations

The datasets must maintain logical relationships using primary and foreign
keys.

Important relationships include:

- Customers → Orders
- Restaurants → Orders
- Orders → Deliveries
- Drivers → Deliveries
- Orders → Reviews
- Orders → Payments

## Format

Return a complete Python script using Pandas and NumPy.

The script should:

1. Import required libraries
2. Generate each dataset separately
3. Use consistent ID formats
4. Maintain relationships between datasets
5. Generate realistic numerical and categorical values
6. Save datasets as CSV files under data/raw/
7. Print the shape of each generated dataset
8. Use clear comments and sections

---

# 2. Role-Based Prompting

## Prompt

Act as a Senior Data Engineer specializing in synthetic marketplace and
operational datasets.

Design the data-generation pipeline with a focus on:

- Relational integrity
- Primary and foreign keys
- Realistic value ranges
- Reproducibility
- Maintainable Python code
- Pandas DataFrames
- CSV outputs
- Clear code organization

The generated data should be suitable for downstream analytics and
machine-learning tasks.

## Application

The role-based instructions influenced the structure of:

src/generate_data.py

The script separates the generation of each business entity and maintains
relationships between datasets.

---

# 3. Few-Shot Prompting

## Prompt

Use the following examples as the required ID format.

Customer IDs:

C0001
C0002
C0003

Restaurant IDs:

R0001
R0002
R0003

Driver IDs:

D0001
D0002
D0003

Order IDs:

O00001
O00002
O00003

Delivery IDs:

DEL00001
DEL00002
DEL00003

Review IDs:

REV00001
REV00002
REV00003

Payment IDs:

PAY00001
PAY00002
PAY00003

Follow these patterns consistently when generating the datasets.

## Application

The generated Python script uses formatted identifiers such as:

customer_id = C0001
restaurant_id = R0001
driver_id = D0001
order_id = O00001

This ensures consistent and readable identifiers across the project.

---

# 4. Structured Output Prompting

## Prompt

Return the Python solution using the following structure:

1. Import libraries
2. Configuration
3. Customers dataset
4. Restaurants dataset
5. Drivers dataset
6. Orders dataset
7. Deliveries dataset
8. Reviews dataset
9. Payments dataset
10. Save datasets to CSV
11. Print dataset shapes

For every dataset:

- Create a Pandas DataFrame
- Define the required columns
- Maintain relationships with other datasets
- Save the resulting DataFrame under data/raw/

## Application

The structure was followed in:

src/generate_data.py

The script contains separate generation sections for all seven datasets.

---

# Prompt Engineering Outcome

The four prompting techniques were combined to guide the design of the
synthetic data-generation pipeline.

The resulting pipeline generates seven related datasets:

- customers.csv
- restaurants.csv
- drivers.csv
- orders.csv
- deliveries.csv
- reviews.csv
- payments.csv

The datasets were subsequently validated for:

- Missing values
- Duplicate records
- Duplicate primary IDs
- Invalid foreign keys
- Valid relationships between datasets
- Reasonable numerical ranges
- Valid order statuses

---

# Reproducibility

The data-generation process uses a fixed random seed so that the synthetic
dataset can be reproduced consistently.

---

# Data Generation Script

The final generated script is:

src/generate_data.py