# %%
import pandas as pd
import numpy

# %%
df = pd.read_csv("data/ecommerce_sales_data.csv")
df["Order Date"] = pd.to_datetime(df["Order Date"])
df.info()

# %%
print(df)

# %%
# First 5 rows
print(df.head())


# %%
# Missing values
print(df.isnull().sum())

# %%
print(df.duplicated().sum())

# %%
print(df.describe())

# %%
print(df.nunique())

# %%
## categories by sales
print(df.groupby("Category")["Sales"].sum().sort_values(ascending=False))

## top 10 products by sales
print(df.groupby(["Product Name", "Category"])["Sales"].sum().sort_values(ascending=False).head(10))

## top 10 products by profit
print(df.groupby(["Product Name", "Category"])["Profit"].sum().sort_values(ascending=False).head(10))

# %%
## categories by profits
print(df.groupby("Category")["Profit"].sum().sort_values(ascending=False))

# %%
## sales by region
print(df.groupby("Region")["Sales"].sum().sort_values(ascending=False))

# %%
## sales/profit by month
print("Monthly Sales:")
print(df.set_index("Order Date").resample("ME")["Sales"].sum())
print("\nMonthly Profit:")
print(df.set_index("Order Date").resample("ME")["Profit"].sum())

## best month for profit
monthly = df.set_index("Order Date").resample("ME")["Profit"].sum()
print("\nBest month for profit:")
print("  Month:", monthly.idxmax())
print("  Profit:", monthly.max())

## worst month for profit
print("Worst month for profit:")
print("  Month:", monthly.idxmin())
print("  Profit:", monthly.min())


## seasonal trends

# this creates a new column month and we label it from order date the month name
df["Month"] = df["Order Date"].dt.month_name()
# sales per month
print("\nSales by month (seasonal):")
print(df.groupby("Month")["Sales"].sum().sort_values(ascending=False))

# %%
## products making losses
## so when profit < 0 (there is no 0 profits)
## df[df["Profit"] < 0].groupby(["Product Name", "Category"])["Profit"].sum().sort_values(ascending=False).head(10)
## products making the least amount of profit
print(df.groupby(["Product Name", "Category"])["Profit"].sum().sort_values(ascending=True).head(10))

# %%
## sales by profit (regional profit)
print(df.groupby("Region")["Profit"].sum().sort_values(ascending=True))

# %%
# defining margin
df["Margin"] = df["Profit"] / df["Sales"]
print("\nTop 10 products by margin:")
print(df.groupby(["Product Name", "Category"])["Margin"].mean().sort_values(ascending=False).head(10))

# %%
# margin by category
print("\nAverage margin by category:")
print(df.groupby("Category")["Margin"].mean().sort_values(ascending=False))

# %%
## charts
import matplotlib.pyplot as plt

fig, axes = plt.subplots(1, 2, figsize=(12, 4))

df.groupby("Category")["Sales"].sum().sort_values().plot(kind="barh", ax=axes[0], title="Sales by Category")
df.groupby("Category")["Profit"].sum().sort_values().plot(kind="barh", ax=axes[1], title="Profit by Category")

plt.tight_layout()
plt.savefig("charts.png")
print("\nChart saved to charts.png")

# %%
## findings & recommendations

# FINDING 1: Electronics generates the highest total sales and profit of all categories.
#            It outperforms Office and Accessories by a wide margin in both metrics.

# FINDING 2: Profit margins are consistent across all categories (~17%),
#            which suggests this dataset is synthetic rather than real sales data.
#            No category performs significantly better or worse than others.

# FINDING 3: [add your finding from seasonal/regional data here]
#            Example: "West region leads in both sales and profit"

# RECOMMENDATION 1: Focus marketing budget on Electronics (highest revenue and profit).

# RECOMMENDATION 2: Investigate product pricing to create margin differentiation
#                   between categories (all at ~17% suggests pricing is formulaic).

# RECOMMENDATION 3: [base this on regional or seasonal data]

# FUTURE INVESTIGATION: Obtain real sales data with customer segments and
# discount information for deeper analysis of profitability drivers.
