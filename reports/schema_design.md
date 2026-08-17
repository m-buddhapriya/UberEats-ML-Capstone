# Day 1 — Data Schema Design

## 1. Objective

The Uber Eats synthetic dataset was designed as a relational data model.

The objective of the schema is to connect customers, restaurants, drivers,
orders, deliveries, reviews, and payments so that the datasets can be joined
for analytics and machine learning.

---

# 2. Datasets

The project contains seven datasets:

1. Customers
2. Restaurants
3. Drivers
4. Orders
5. Deliveries
6. Reviews
7. Payments

---

# 3. Primary Keys

Each dataset has a unique identifier.

| Dataset | Primary Key |
|---|---|
| Customers | `customer_id` |
| Restaurants | `restaurant_id` |
| Drivers | `driver_id` |
| Orders | `order_id` |
| Deliveries | `delivery_id` |
| Reviews | `review_id` |
| Payments | `payment_id` |

Primary keys uniquely identify each record within a dataset.

---

# 4. Foreign Keys

Foreign keys are used to connect related datasets.

| Dataset | Foreign Key | References |
|---|---|---|
| Orders | `customer_id` | Customers.`customer_id` |
| Orders | `restaurant_id` | Restaurants.`restaurant_id` |
| Deliveries | `order_id` | Orders.`order_id` |
| Deliveries | `driver_id` | Drivers.`driver_id` |
| Reviews | `order_id` | Orders.`order_id` |
| Reviews | `customer_id` | Customers.`customer_id` |
| Payments | `order_id` | Orders.`order_id` |

---

# 5. Dataset-Level Schema

## Customers

| Column | Data Type | Key | Description |
|---|---|---|---|
| `customer_id` | String | PK | Unique customer identifier |
| `age` | Integer | | Customer age |
| `gender` | String | | Customer gender category |
| `city` | String | | Customer city |
| `membership_type` | String | | Customer membership category |

---

## Restaurants

| Column | Data Type | Key | Description |
|---|---|---|---|
| `restaurant_id` | String | PK | Unique restaurant identifier |
| `restaurant_name` | String | | Restaurant name |
| `restaurant_category` | String | | Restaurant/cuisine category |
| `restaurant_rating` | Float | | Restaurant rating |
| `city` | String | | Restaurant city |

---

## Drivers

| Column | Data Type | Key | Description |
|---|---|---|---|
| `driver_id` | String | PK | Unique driver identifier |
| `driver_rating` | Float | | Driver rating |
| `vehicle_type` | String | | Vehicle used for delivery |
| `experience_years` | Float | | Driver experience in years |

---

## Orders

| Column | Data Type | Key | Description |
|---|---|---|---|
| `order_id` | String | PK | Unique order identifier |
| `customer_id` | String | FK | Customer who placed the order |
| `restaurant_id` | String | FK | Restaurant receiving the order |
| `order_timestamp` | Datetime | | Date and time of order |
| `order_amount` | Float | | Monetary value of order |
| `number_of_items` | Integer | | Number of items in order |
| `order_status` | String | | Current order status |

---

## Deliveries

| Column | Data Type | Key | Description |
|---|---|---|---|
| `delivery_id` | String | PK | Unique delivery identifier |
| `order_id` | String | FK | Order being delivered |
| `driver_id` | String | FK | Driver handling the delivery |
| `delivery_distance_km` | Float | | Delivery distance in kilometres |
| `preparation_time_minutes` | Integer | | Restaurant preparation time |
| `delivery_time_minutes` | Integer | | Total delivery time |
| `traffic_condition` | String | | Traffic condition |
| `weather` | String | | Weather condition |

---

## Reviews

| Column | Data Type | Key | Description |
|---|---|---|---|
| `review_id` | String | PK | Unique review identifier |
| `order_id` | String | FK | Order associated with review |
| `customer_id` | String | FK | Customer submitting review |
| `rating` | Integer | | Customer rating from 1 to 5 |
| `review_text` | String | | Customer textual feedback |

---

## Payments

| Column | Data Type | Key | Description |
|---|---|---|---|
| `payment_id` | String | PK | Unique payment identifier |
| `order_id` | String | FK | Order associated with payment |
| `payment_method` | String | | Payment method |
| `payment_amount` | Float | | Amount paid |
| `tip_amount` | Float | | Tip paid by customer |

---

# 6. Relationship Model

The overall relationship structure is:

```text
                         ┌─────────────────┐
                         │    Customers    │
                         │   customer_id   │
                         └────────┬────────┘
                                  │
                                  │ customer_id
                                  │
                                  ▼
                         ┌─────────────────┐
                         │     Orders      │
                         │    order_id     │
                         │   customer_id   │
                         │  restaurant_id  │
                         └──────┬───┬──────┘
                                │   │
                 restaurant_id  │   │ order_id
                                │   │
                                ▼   ├───────────────┐
                     ┌──────────────┐               │
                     │ Restaurants  │               │
                     │restaurant_id │               │
                     └──────────────┘               │
                                                    │
                      ┌─────────────────────────────┼──────────────┐
                      │                             │              │
                      ▼                             ▼              ▼
              ┌───────────────┐            ┌──────────────┐ ┌──────────────┐
              │  Deliveries   │            │   Reviews    │ │   Payments   │
              │ delivery_id   │            │  review_id   │ │  payment_id  │
              │   order_id    │            │   order_id   │ │   order_id   │
              │   driver_id   │            │ customer_id  │ │              │
              └───────┬───────┘            └──────────────┘ └──────────────┘
                      │
                      │ driver_id
                      ▼
               ┌──────────────┐
               │   Drivers    │
               │  driver_id   │
               └──────────────┘