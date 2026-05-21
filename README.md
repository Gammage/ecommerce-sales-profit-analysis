# ecommerce-sales-profit-analysis

## Overview
This project uses a beginner-friendly dataset from Kaggle.

I followed the "EDA" workflow, which consists of the following:
- Check structure (`df.info()`)
- Summary stats (`df.describe()`)
- Find missing values
- Group and compare data
- Visualise trends

I already had an inclination that it was a fake dataset — all profits were up and the margins for profit/sales were basically 17% across the board.

## Key findings

### The data 
- Around February, monthly sales drop. This is realistic given the post-Christmas period, which aligns with my experience working in insurance marketing and my own trading hobby.
- Electronics leads in sales and profits across all categories. This is also realistic, in my assumptions.

### The tooling
This was my first project analysing data with Pandas. To make the data presentable, I relied heavily on AI for styling, which introduced me to `FuncFormatter`, enabling me to label the x-axis.

AI was heavily used in the tooling, specifically Molten.nvim and using a persistent kernel on NixOS. More of that can be read in my [blog article](https://gammagelabs.com/blog/molten-nvim-for-data-analysis/).

### Project reflections
You can read the full blog post here [COMING SOON], but the trade-off I'm currently facing is using Jupyter Lab's GUI over making Molten.nvim work in Neovim. It will take significant time to debug Molten, as my keymaps are conflicting with the visual buffer.

Overall this was a massive jump in using Pandas syntax. My concern is not learning proper function definitions when running individual cells in Python — I don't want to develop bad habits.
