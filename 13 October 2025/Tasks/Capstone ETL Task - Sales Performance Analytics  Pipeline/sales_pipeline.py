import pandas as pd
from datetime import datetime
#1. extracting
products=pd.read_csv("products.csv")
customers=pd.read_csv("customers.csv")
orders=pd.read_csv("orders.csv")


    print(f"Pipeline completed at {datetime.now()}")
    print("Output saved to ")


if __name__ == "__main__":
    run_pipeline()