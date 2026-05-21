# %%
import pandas as pd
import numpy

# %%
df = pd.read_csv("data/ecommerce_sales_data.csv")
df["Order Date"] = pd.to_datetime(df["Order Date"])
df.info()

# %%
# best performing categories by sales
import matplotlib.pyplot as plt
df.groupby("Category")["Sales"].sum().sort_values().plot(kind="barh", title="Sales by Category")
plt.xlabel("Total Sales ($ millions)")
plt.savefig("output/best_categories_sales.png", bbox_inches="tight")


# %%
# top 10 products by sales
top = df.groupby("Product Name")["Sales"].sum().sort_values(ascending=True).tail(10)
top.plot(kind="barh", title="Top 10 Products by Sales")
plt.xlabel("Total Sales ($)")
plt.savefig("output/top_products_sales.png", bbox_inches="tight")

# %%
# best performing categories by profit
import matplotlib.pyplot as plt
df.groupby("Category")["Profit"].sum().sort_values().plot(kind="barh", title="Profits by Category")
plt.xlabel("Total profit ($)")
plt.savefig("output/best_categories_profit.png", bbox_inches="tight")

# %%
# top 10 products by profit
top = df.groupby("Product Name")["Profit"].sum().sort_values(ascending=True).tail(10)
top.plot(kind="barh", title="Top 10 Products by Profit")
plt.xlabel("Total Profit ($)")
plt.savefig("output/top_products_profit.png", bbox_inches="tight")


# %%
# monthly sales over time
monthly_sales = df.set_index("Order Date").resample("ME")["Sales"].sum()
monthly_sales.plot(title="Monthly Sales Over Time")
plt.ylabel("Sales ($)")
plt.savefig("output/monthly_sales.png")

# %% 
# best month for profit


# %%
# worst month for profit

# %%
# category margins

# Key findings¶
# Electronics leads in both sales and profit
# December is the strongest month for profit
# February is the weakest month for profit
# products have around 17% margin - Data is most likely fake (from kaggle datasets)

# recommendations
# Focus or increase marketing on Electronics
# Focus on incentives for February (promotions etc)
# you would most definitely investigate the similiar product margins!

# Note
# this analysis breakdown was from an example dataset on kaggle, very clean data. the superficial nature of the product margins would suggest this data was not taken from any real sales data, but it is proof that I can gather insights.