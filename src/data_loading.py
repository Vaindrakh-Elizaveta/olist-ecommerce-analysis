from pathlib import Path
import pandas as pd

def load_processed_data(data_path):
    data_path = Path(data_path)

    tables = {
        "orders": pd.read_csv(data_path / "orders.csv", parse_dates=["order_purchase_timestamp",
                                                                     "order_approved_at",
                                                                     "order_delivered_carrier_date",
                                                                     "order_delivered_customer_date",
                                                                     "order_estimated_delivery_date"]),
        "customers": pd.read_csv(data_path / "customers.csv"),
        "geolocation": pd.read_csv(data_path / "geolocation.csv"),
        "order_items": pd.read_csv(data_path / "order_items.csv", parse_dates=["shipping_limit_date"]),
        "order_payments": pd.read_csv(data_path / "order_payments.csv"),
        "order_reviews": pd.read_csv(data_path / "order_reviews.csv", parse_dates=["review_creation_date", 
                                                                                   "review_answer_timestamp"]),
        "products": pd.read_csv(data_path / "products.csv"),
        "sellers": pd.read_csv(data_path / "sellers.csv"),
        "product_category_name_translation": pd.read_csv(data_path / "product_category_name_translation.csv")
    }

    return tables

