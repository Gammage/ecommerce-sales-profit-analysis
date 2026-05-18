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

# %%
## categories by profits
df.groupby("Category")["Profit"].sum().sort_values(ascending=False)








