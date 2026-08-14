# Uber Eats Data Schema Design

## Overview

The Uber Eats synthetic dataset consists of seven related datasets.

The schema is designed around Orders as the central transactional table.

---

## Entities

### Customers

Primary Key:

customer_id

Contains customer demographic and membership information.

---

### Restaurants

Primary Key:

restaurant_id

Contains restaurant name, category, rating, and city.

---

### Drivers

Primary Key:

driver_id

Contains driver rating, vehicle type, and experience.

---

### Orders

Primary Key:

order_id

Foreign Keys:

- customer_id → Customers.customer_id
- restaurant_id → Restaurants.restaurant_id

Orders represent customer transactions.

---

### Deliveries

Primary Key:

delivery_id

Foreign Keys:

- order_id → Orders.order_id
- driver_id → Drivers.driver_id

Deliveries contain operational delivery information such as distance,
preparation time, delivery time, traffic, and weather.

---

### Reviews

Primary Key:

review_id

Foreign Keys:

- order_id → Orders.order_id
- customer_id → Customers.customer_id

Reviews contain customer ratings and textual feedback.

---

### Payments

Primary Key:

payment_id

Foreign Key:

- order_id → Orders.order_id

Payments contain payment method, payment amount, and tip amount.

---

## Relationship Diagram

Customers
    |
    | customer_id
    ↓
Orders
    |
    ├── restaurant_id → Restaurants
    |
    ├── order_id → Deliveries
    |
    ├── order_id → Reviews
    |
    └── order_id → Payments

Deliveries
    |
    └── driver_id → Drivers

---

## Design Principles

The schema was designed to:

- Avoid unnecessary duplication
- Maintain referential integrity
- Use unique primary keys
- Use foreign keys to connect related entities
- Support analytical joins
- Support downstream machine-learning workflows