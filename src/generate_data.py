import pandas as pd
import numpy as np

print("Uber Eats data generation started...")

# -----------------------------
# 1. Generate Customers
# -----------------------------

np.random.seed(42)

NUM_CUSTOMERS = 1000

customer_ids = [f"C{i:04d}" for i in range(1, NUM_CUSTOMERS + 1)]

customers = pd.DataFrame({
    "customer_id": customer_ids,
    "age": np.random.randint(18, 65, NUM_CUSTOMERS),
    "gender": np.random.choice(
        ["Male", "Female", "Other"],
        NUM_CUSTOMERS,
        p=[0.48, 0.48, 0.04]
    ),
    "city": np.random.choice(
        ["Bangalore", "Hyderabad", "Mumbai", "Delhi", "Pune", "Chennai"],
        NUM_CUSTOMERS
    ),
    "membership_type": np.random.choice(
        ["Regular", "Gold", "Premium"],
        NUM_CUSTOMERS,
        p=[0.60, 0.25, 0.15]
    )
})

# Save customers dataset
customers.to_csv("data/raw/customers.csv",index=False)
print("Customers dataset created:", customers.shape)

# -----------------------------
# 2. Generate Restaurants
# -----------------------------

NUM_RESTAURANTS = 200

restaurant_ids = [
    f"R{i:04d}" for i in range(1, NUM_RESTAURANTS + 1)
]

restaurant_names = [
    "Spice Kitchen",
    "Pizza Hub",
    "Burger Point",
    "Biryani House",
    "South Indian Corner",
    "Chinese Wok",
    "Cafe Delight",
    "Taco Town",
    "Healthy Bites",
    "The Food Factory"
]

restaurants = pd.DataFrame({
    "restaurant_id": restaurant_ids,
    "restaurant_name": np.random.choice(
        restaurant_names,
        NUM_RESTAURANTS
    ),
    "restaurant_category": np.random.choice(
        [
            "Indian",
            "Chinese",
            "Italian",
            "Fast Food",
            "Cafe",
            "Healthy"
        ],
        NUM_RESTAURANTS
    ),
    "restaurant_rating": np.round(
        np.random.uniform(3.0, 5.0, NUM_RESTAURANTS),
        1
    ),
    "city": np.random.choice(
        [
            "Bangalore",
            "Hyderabad",
            "Mumbai",
            "Delhi",
            "Pune",
            "Chennai"
        ],
        NUM_RESTAURANTS
    )
})

# Save restaurants dataset
restaurants.to_csv("data/raw/restaurants.csv",index=False)
print("Restaurants dataset created:", restaurants.shape)

# -----------------------------
# 3. Generate Drivers
# -----------------------------

NUM_DRIVERS = 300

driver_ids = [
    f"D{i:04d}" for i in range(1, NUM_DRIVERS + 1)
]

drivers = pd.DataFrame({
    "driver_id": driver_ids,

    "driver_rating": np.round(
        np.random.uniform(3.0, 5.0, NUM_DRIVERS),
        1
    ),

    "vehicle_type": np.random.choice(
        ["Bike", "Scooter", "Car"],
        NUM_DRIVERS,
        p=[0.50, 0.35, 0.15]
    ),

    "experience_years": np.round(
        np.random.uniform(0.5, 10, NUM_DRIVERS),
        1
    )
})

# Save drivers dataset
drivers.to_csv("data/raw/drivers.csv",index=False)
print("Drivers dataset created:", drivers.shape)

# -----------------------------
# 4. Generate Orders
# -----------------------------

NUM_ORDERS = 10000

order_ids = [
    f"O{i:05d}" for i in range(1, NUM_ORDERS + 1)
]

# Randomly assign customers and restaurants to orders
order_customer_ids = np.random.choice(
    customers["customer_id"],
    NUM_ORDERS
)

order_restaurant_ids = np.random.choice(
    restaurants["restaurant_id"],
    NUM_ORDERS
)

# Generate order timestamps
start_date = pd.Timestamp("2026-01-01")
end_date = pd.Timestamp("2026-03-31")

order_timestamps = pd.to_datetime(
    np.random.randint(
        start_date.value // 10**9,
        end_date.value // 10**9,
        NUM_ORDERS
    ),
    unit="s"
)

orders = pd.DataFrame({
    "order_id": order_ids,

    "customer_id": order_customer_ids,

    "restaurant_id": order_restaurant_ids,

    "order_timestamp": order_timestamps,

    "order_amount": np.round(
        np.random.uniform(150, 2000, NUM_ORDERS),
        2
    ),

    "number_of_items": np.random.randint(
        1, 9, NUM_ORDERS
    ),

    "order_status": np.random.choice(
        [
            "Delivered",
            "Cancelled",
            "In Progress"
        ],
        NUM_ORDERS,
        p=[0.85, 0.10, 0.05]
    )
})

# Sort by timestamp
orders = orders.sort_values("order_timestamp").reset_index(drop=True)

# Save orders dataset
orders.to_csv("data/raw/orders.csv",index=False)
print("Orders dataset created:", orders.shape)

# -----------------------------
# 5. Generate Deliveries
# -----------------------------

# Only delivered orders should have delivery records
delivered_orders = orders[
    orders["order_status"] == "Delivered"
].copy()

NUM_DELIVERIES = len(delivered_orders)

delivery_ids = [
    f"DEL{i:05d}" for i in range(1, NUM_DELIVERIES + 1)
]

# Assign a driver to each delivery
delivery_driver_ids = np.random.choice(
    drivers["driver_id"],
    NUM_DELIVERIES
)

# Generate delivery distance
delivery_distance = np.round(
    np.random.uniform(1, 20, NUM_DELIVERIES),
    2
)

# Generate preparation time
preparation_time = np.random.randint(
    10, 45, NUM_DELIVERIES
)

# Traffic conditions
traffic_conditions = np.random.choice(
    [
        "Low",
        "Medium",
        "High"
    ],
    NUM_DELIVERIES,
    p=[0.30, 0.45, 0.25]
)

# Weather conditions
weather_conditions = np.random.choice(
    [
        "Clear",
        "Cloudy",
        "Rainy",
        "Stormy"
    ],
    NUM_DELIVERIES,
    p=[0.50, 0.25, 0.20, 0.05]
)

# Base delivery time based on distance
base_delivery_time = (
    15
    + delivery_distance * 3
    + preparation_time
)

# Add traffic impact
traffic_impact = np.select(
    [
        traffic_conditions == "Low",
        traffic_conditions == "Medium",
        traffic_conditions == "High"
    ],
    [
        0,
        10,
        20
    ],
    default=0
)

# Add weather impact
weather_impact = np.select(
    [
        weather_conditions == "Clear",
        weather_conditions == "Cloudy",
        weather_conditions == "Rainy",
        weather_conditions == "Stormy"
    ],
    [
        0,
        3,
        10,
        20
    ],
    default=0
)

# Add random variation
random_variation = np.random.normal(
    0,
    5,
    NUM_DELIVERIES
)

delivery_time = np.maximum(
    base_delivery_time
    + traffic_impact
    + weather_impact
    + random_variation,
    10
)

deliveries = pd.DataFrame({
    "delivery_id": delivery_ids,

    "order_id": delivered_orders["order_id"].values,

    "driver_id": delivery_driver_ids,

    "delivery_distance_km": delivery_distance,

    "preparation_time_minutes": preparation_time,

    "delivery_time_minutes": np.round(
        delivery_time
    ).astype(int),

    "traffic_condition": traffic_conditions,

    "weather": weather_conditions
})

# Save deliveries dataset
deliveries.to_csv("data/raw/deliveries.csv",index=False)
print("Deliveries dataset created:", deliveries.shape)

# -----------------------------
# 6. Generate Reviews
# -----------------------------

# Create reviews only for delivered orders
review_orders = delivered_orders.copy()

NUM_REVIEWS = len(review_orders)

review_ids = [
    f"REV{i:05d}" for i in range(1, NUM_REVIEWS + 1)
]

# Generate ratings
review_ratings = np.random.choice(
    [1, 2, 3, 4, 5],
    NUM_REVIEWS,
    p=[0.05, 0.08, 0.17, 0.35, 0.35]
)

positive_reviews = [
    "Food was amazing and arrived hot.",
    "Excellent food and fast delivery.",
    "Really enjoyed the meal.",
    "Great experience, will order again.",
    "Food was fresh and delicious.",
    "Very good service and tasty food."
]

neutral_reviews = [
    "Food was okay.",
    "Average experience.",
    "The food was decent.",
    "Nothing special but it was fine.",
    "Service was acceptable."
]

negative_reviews = [
    "Food was cold when it arrived.",
    "Delivery was very late.",
    "Food quality was disappointing.",
    "Order arrived late and cold.",
    "Very poor experience.",
    "The food was not fresh."
]

review_texts = []

for rating in review_ratings:

    if rating >= 4:
        review_texts.append(
            np.random.choice(positive_reviews)
        )

    elif rating == 3:
        review_texts.append(
            np.random.choice(neutral_reviews)
        )

    else:
        review_texts.append(
            np.random.choice(negative_reviews)
        )

reviews = pd.DataFrame({
    "review_id": review_ids,

    "order_id": review_orders["order_id"].values,

    "customer_id": review_orders["customer_id"].values,

    "rating": review_ratings,

    "review_text": review_texts
})

# Save reviews dataset
reviews.to_csv("data/raw/reviews.csv",index=False)
print("Reviews dataset created:", reviews.shape)

# -----------------------------
# 7. Generate Payments
# -----------------------------

NUM_PAYMENTS = len(orders)

payment_ids = [
    f"PAY{i:05d}" for i in range(1, NUM_PAYMENTS + 1)
]

payment_methods = np.random.choice(
    [
        "UPI",
        "Credit Card",
        "Debit Card",
        "Cash",
        "Wallet"
    ],
    NUM_PAYMENTS,
    p=[0.40, 0.25, 0.15, 0.10, 0.10]
)

# Generate tips based on order amount
tip_percentage = np.random.choice(
    [
        0,
        0.05,
        0.10,
        0.15,
        0.20
    ],
    NUM_PAYMENTS,
    p=[0.15, 0.25, 0.30, 0.20, 0.10]
)

tip_amount = np.round(orders["order_amount"].values * tip_percentage,2)

payments = pd.DataFrame({
    "payment_id": payment_ids,

    "order_id": orders["order_id"].values,

    "payment_method": payment_methods,

    "payment_amount": orders["order_amount"].values,

    "tip_amount": tip_amount
})

# Save payments dataset
payments.to_csv("data/raw/payments.csv",index=False)
print("Payments dataset created:", payments.shape)