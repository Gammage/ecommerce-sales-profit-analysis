import pandas as pd

def main():
    print("Main is working :)")

    df = pd.read_csv("data/ecommerce_sales_data.csv")
    print(df)


    
if __name__ == "__main__":
    main()
