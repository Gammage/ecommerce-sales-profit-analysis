# %%
import pandas as pd
import numpy
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker

# %%
df = pd.read_csv("data/ecommerce_sales_data.csv")
df["Order Date"] = pd.to_datetime(df["Order Date"])
df.info()

# %%
# best performing categories by sales
ax = df.groupby("Category")["Sales"].sum().sort_values().plot(kind="barh", title="Sales by Category")
ax.set_facecolor("none")
ax.tick_params(colors="#c0f0e0")
_ = [spine.set_color("#33666b") for spine in ax.spines.values()]
ax.title.set_color("#c0f0e0")
ax.xaxis.label.set_color("#c0f0e0")
ax.yaxis.label.set_color("#c0f0e0")
plt.xlabel("Total Sales ($ millions)")
ax.xaxis.set_major_formatter(mticker.FuncFormatter(lambda x, p: f'{x:,.0f}'))
plt.savefig("output/best_categories_sales.png", bbox_inches="tight", facecolor="#00343d")
plt.close()


# %%
# top 10 products by sales
top = df.groupby("Product Name")["Sales"].sum().sort_values(ascending=True).tail(10)
ax = top.plot(kind="barh", title="Top 10 Products by Sales")
ax.set_facecolor("none")
ax.tick_params(colors="#c0f0e0")
_ = [spine.set_color("#33666b") for spine in ax.spines.values()]
ax.title.set_color("#c0f0e0")
ax.xaxis.label.set_color("#c0f0e0")
ax.yaxis.label.set_color("#c0f0e0")
plt.xlabel("Total Sales ($)")
ax.xaxis.set_major_formatter(mticker.FuncFormatter(lambda x, p: f'{x:,.0f}'))
plt.savefig("output/top_products_sales.png", bbox_inches="tight", facecolor="#00343d")
plt.close()


# %%
# best performing categories by profit
ax = df.groupby("Category")["Profit"].sum().sort_values().plot(kind="barh", title="Profits by Category")
ax.set_facecolor("none")
ax.tick_params(colors="#c0f0e0")
_ = [spine.set_color("#33666b") for spine in ax.spines.values()]
ax.title.set_color("#c0f0e0")
ax.xaxis.label.set_color("#c0f0e0")
ax.yaxis.label.set_color("#c0f0e0")
plt.xlabel("Total profit ($)")
ticks = ax.get_xticks()
ax.set_xticks(ticks)
ax.set_xticklabels([f'{x:,.0f}' for x in ticks])
plt.savefig("output/best_categories_profit.png", bbox_inches="tight", facecolor="#00343d")
plt.close()


# %%
# top 10 products by profit
top = df.groupby("Product Name")["Profit"].sum().sort_values(ascending=True).tail(10)
ax = top.plot(kind="barh", title="Top 10 Products by Profit")
ax.set_facecolor("none")
ax.tick_params(colors="#c0f0e0")
_ = [spine.set_color("#33666b") for spine in ax.spines.values()]
ax.title.set_color("#c0f0e0")
ax.xaxis.label.set_color("#c0f0e0")
ax.yaxis.label.set_color("#c0f0e0")
plt.xlabel("Total Profit ($)")
ax.xaxis.set_major_locator(plt.MaxNLocator(5))
ticks = ax.get_xticks()
ax.set_xticks(ticks)
ax.set_xticklabels([f'{x:,.0f}' for x in ticks])
plt.savefig("output/top_products_profit.png", bbox_inches="tight", facecolor="#00343d")
plt.close()


# %%
# monthly sales over time
monthly_sales = df.set_index("Order Date").resample("ME")["Sales"].sum()
plt.figure()
ax = monthly_sales.plot(kind="line", title="Monthly Sales Over Time")
ax.set_facecolor("none")
ax.tick_params(colors="#c0f0e0")
_ = [spine.set_color("#33666b") for spine in ax.spines.values()]
ax.title.set_color("#c0f0e0")
ax.xaxis.label.set_color("#c0f0e0")
ax.yaxis.label.set_color("#c0f0e0")
plt.ylabel("Sales ($)")
ax.yaxis.set_major_formatter(mticker.FuncFormatter(lambda x, p: f'{x:,.0f}'))
plt.savefig("output/monthly_sales.png", bbox_inches="tight", facecolor="#00343d")

