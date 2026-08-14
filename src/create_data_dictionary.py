import pandas as pd
import os


# ---------------------------------
# Create Data Dictionary
# ---------------------------------

data_dictionary = [

    # -----------------------------
    # Customers
    # -----------------------------
    {
        "dataset": "Customers",
        "column": "customer_id",
        "data_type": "String",
        "key_type": "Primary Key",
        "description": "Unique identifier for each customer"
    },
    {
        "dataset": "Customers",
        "column": "age",
        "data_type": "Integer",
        "key_type": "",
        "description": "Age of the customer"
    },
    {
        "dataset": "Customers",
        "column": "gender",
        "data_type": "String",
        "key_type": "",
        "description": "Gender category of the customer"
    },
    {
        "dataset": "Customers",
        "column": "city",
        "data_type": "String",
        "key_type": "",
        "description": "City where the customer is located"
    },
    {
        "dataset": "Customers",
        "column": "membership_type",
        "data_type": "String",
        "key_type": "",
        "description": "Customer membership category"
    },


    # -----------------------------
    # Restaurants
    # -----------------------------
    {
        "dataset": "Restaurants",
        "column": "restaurant_id",
        "data_type": "String",
        "key_type": "Primary Key",
        "description": "Unique identifier for each restaurant"
    },
    {
        "dataset": "Restaurants",
        "column": "restaurant_name",
        "data_type": "String",
        "key_type": "",
        "description": "Name of the restaurant"
    },
    {
        "dataset": "Restaurants",
        "column": "restaurant_category",
        "data_type": "String",
        "key_type": "",
        "description": "Cuisine or restaurant category"
    },
    {
        "dataset": "Restaurants",
        "column": "restaurant_rating",
        "data_type": "Float",
        "key_type": "",
        "description": "Average rating of the restaurant"
    },
    {
        "dataset": "Restaurants",
        "column": "city",
        "data_type": "String",
        "key_type": "",
        "description": "City where the restaurant operates"
    },


    # -----------------------------
    # Drivers
    # -----------------------------
    {
        "dataset": "Drivers",
        "column": "driver_id",
        "data_type": "String",
        "key_type": "Primary Key",
        "description": "Unique identifier for each driver"
    },
    {
        "dataset": "Drivers",
        "column": "driver_rating",
        "data_type": "Float",
        "key_type": "",
        "description": "Rating of the delivery driver"
    },
    {
        "dataset": "Drivers",
        "column": "vehicle_type",
        "data_type": "String",
        "key_type": "",
        "description": "Type of vehicle used by the driver"
    },
    {
        "dataset": "Drivers",
        "column": "experience_years",
        "data_type": "Float",
        "key_type": "",
        "description": "Driver's years of experience"
    },


    # -----------------------------
    # Orders
    # -----------------------------
    {
        "dataset": "Orders",
        "column": "order_id",
        "data_type": "String",
        "key_type": "Primary Key",
        "description": "Unique identifier for each order"
    },
    {
        "dataset": "Orders",
        "column": "customer_id",
        "data_type": "String",
        "key_type": "Foreign Key",
        "description": "Identifier of the customer who placed the order"
    },
    {
        "dataset": "Orders",
        "column": "restaurant_id",
        "data_type": "String",
        "key_type": "Foreign Key",
        "description": "Identifier of the restaurant receiving the order"
    },
    {
        "dataset": "Orders",
        "column": "order_timestamp",
        "data_type": "Datetime",
        "key_type": "",
        "description": "Date and time when the order was placed"
    },
    {
        "dataset": "Orders",
        "column": "order_amount",
        "data_type": "Float",
        "key_type": "",
        "description": "Total monetary value of the order"
    },
    {
        "dataset": "Orders",
        "column": "number_of_items",
        "data_type": "Integer",
        "key_type": "",
        "description": "Number of items included in the order"
    },
    {
        "dataset": "Orders",
        "column": "order_status",
        "data_type": "String",
        "key_type": "",
        "description": "Current status of the order"
    },


    # -----------------------------
    # Deliveries
    # -----------------------------
    {
        "dataset": "Deliveries",
        "column": "delivery_id",
        "data_type": "String",
        "key_type": "Primary Key",
        "description": "Unique identifier for each delivery"
    },
    {
        "dataset": "Deliveries",
        "column": "order_id",
        "data_type": "String",
        "key_type": "Foreign Key",
        "description": "Identifier of the order being delivered"
    },
    {
        "dataset": "Deliveries",
        "column": "driver_id",
        "data_type": "String",
        "key_type": "Foreign Key",
        "description": "Identifier of the driver handling the delivery"
    },
    {
        "dataset": "Deliveries",
        "column": "delivery_distance_km",
        "data_type": "Float",
        "key_type": "",
        "description": "Distance traveled for the delivery in kilometers"
    },
    {
        "dataset": "Deliveries",
        "column": "preparation_time_minutes",
        "data_type": "Integer",
        "key_type": "",
        "description": "Time taken by the restaurant to prepare the order"
    },
    {
        "dataset": "Deliveries",
        "column": "delivery_time_minutes",
        "data_type": "Integer",
        "key_type": "",
        "description": "Total time taken to deliver the order"
    },
    {
        "dataset": "Deliveries",
        "column": "traffic_condition",
        "data_type": "String",
        "key_type": "",
        "description": "Traffic condition during delivery"
    },
    {
        "dataset": "Deliveries",
        "column": "weather",
        "data_type": "String",
        "key_type": "",
        "description": "Weather condition during delivery"
    },


    # -----------------------------
    # Reviews
    # -----------------------------
    {
        "dataset": "Reviews",
        "column": "review_id",
        "data_type": "String",
        "key_type": "Primary Key",
        "description": "Unique identifier for each review"
    },
    {
        "dataset": "Reviews",
        "column": "order_id",
        "data_type": "String",
        "key_type": "Foreign Key",
        "description": "Identifier of the order being reviewed"
    },
    {
        "dataset": "Reviews",
        "column": "customer_id",
        "data_type": "String",
        "key_type": "Foreign Key",
        "description": "Identifier of the customer submitting the review"
    },
    {
        "dataset": "Reviews",
        "column": "rating",
        "data_type": "Integer",
        "key_type": "",
        "description": "Rating given by the customer from 1 to 5"
    },
    {
        "dataset": "Reviews",
        "column": "review_text",
        "data_type": "String",
        "key_type": "",
        "description": "Textual feedback provided by the customer"
    },


    # -----------------------------
    # Payments
    # -----------------------------
    {
        "dataset": "Payments",
        "column": "payment_id",
        "data_type": "String",
        "key_type": "Primary Key",
        "description": "Unique identifier for each payment"
    },
    {
        "dataset": "Payments",
        "column": "order_id",
        "data_type": "String",
        "key_type": "Foreign Key",
        "description": "Identifier of the order associated with the payment"
    },
    {
        "dataset": "Payments",
        "column": "payment_method",
        "data_type": "String",
        "key_type": "",
        "description": "Payment method used for the order"
    },
    {
        "dataset": "Payments",
        "column": "payment_amount",
        "data_type": "Float",
        "key_type": "",
        "description": "Amount paid for the order"
    },
    {
        "dataset": "Payments",
        "column": "tip_amount",
        "data_type": "Float",
        "key_type": "",
        "description": "Tip amount paid by the customer"
    }
]


# Convert to DataFrame
dictionary_df = pd.DataFrame(data_dictionary)


# Create reports folder if it does not exist
os.makedirs("reports", exist_ok=True)


# Save as Excel
dictionary_df.to_excel(
    "reports/data_dictionary.xlsx",
    index=False
)

print("Data dictionary created successfully.")
print("Total columns documented:", len(dictionary_df))