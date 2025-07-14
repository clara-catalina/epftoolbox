# -*- coding: utf-8 -*-
"""
Created on Mon Jul 14 12:34:38 2025

@author: draga
"""

import pandas as pd
import matplotlib.pyplot as plt

# Load the CSV
df = pd.read_csv("DNN_forecast_nl2_datPJM_YT2_SFH1_CW4_1.csv", index_col=0, parse_dates=True)
og_data = pd.read_csv("../datasets/DE.csv", index_col = 0, parse_dates = True)

# Reshape to long format (stack days and hours into a single time series)
df_long = df.stack()

# Convert the multi-index to a proper datetime index
df_long.index = [
    pd.Timestamp(f"{day} {hour.replace('h','')}:00:00")
    for day, hour in df_long.index
]

# Sort by datetime just in case
df_long = df_long.sort_index()

# Extract just the Price column of the og dataset
price_series = og_data["Price"]

# This will match only the timestamps that exist in both csvs
aligned_price = price_series.reindex(df_long.index)

# Plot
plt.figure(figsize=(14, 6))
df_long.plot(label="Predicted Prices")
aligned_price.plot(label="Original Prices")
plt.xlabel("Datetime")
plt.ylabel("Price")
plt.title("Predicted DE prices")
plt.grid(True)
plt.tight_layout()
plt.show()
