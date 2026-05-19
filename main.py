# %%
import pandas as pd
import numpy
import matplotlib.pyplot as plt

# %%
df = pd.read_csv("data/ecommerce_sales_data.csv")
df["Order Date"] = pd.to_datetime(df["Order Date"])
df.info()

# %%
print(df)

# %%
# First 5 rows
df.head()


# %%
# Missing values
df.isnull().sum()

# %%
df.duplicated().sum()

# %%
df.describe()

# %%
df.nunique()

# %%
## categories by sales
df.groupby("Category")["Sales"].sum().sort_values(ascending=False)

## top 10 sales
df.groupby(["Product Name", "Category"])["Sales"].sum().sort_values(ascending=False).head(10)

## top 10 products for profit
df.groupby(["Product Name", "Category"])["Profit"].sum().sort_values(ascending=False).head(10)

# %%
## categories by profits
df.groupby("Category")["Profit"].sum().sort_values(ascending=False)

# %%
## sales by region
df.groupby("Region")["Sales"].sum().sort_values(ascending=False)

# %%
## sales/profit by month
df.set_index("Order Date").resample("M")["Sales"].sum()
df.set_index("Order Date").resample("M")["Profit"].sum()

## best month for profit
monthly = df.set_index("Order Date").resample("M")["Profit"].sum()
monthly.idxmax() # name/label of that numbers row
monthly.max() # the number

## worst month for profit
monthly.idxmin()
monthly.min()


## seasonal trends

# this creates a new column month and we label it from order date the month name
df["Month"] = df["Order Date"].dt.month_name()
# sales per month
df.groupby("Month")["Sales"].sum().sort_values(ascending=False)

# %%
## products making losses
## so when profit < 0 (there is no 0 profits)
## df[df["Profit"] < 0].groupby(["Product Name", "Category"])["Profit"].sum().sort_values(ascending=False).head(10)
## products making the least amount of profit
df.groupby(["Product Name", "Category"])["Profit"].sum().sort_values(ascending=True).head(10)

# %%
## sales by profit (regional profit)
df.groupby("Region")["Profit"].sum().sort_values(ascending=True)

# %%
# defining margin
df["Margin"] = df["Profit"] / df["Sales"]
df.groupby(["Product Name", "Category"])["Margin"].mean().sort_values(ascending=False).head(10)











