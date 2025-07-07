# -*- coding: utf-8 -*-
"""
Created on Mon Jul  7 14:18:31 2025

@author: draga
"""

import pandas as pd
import matplotlib.pyplot as plt

"Plotting Forecasts: "
# Load the data
pred_BE = pd.read_csv("Forecasts_BE_DNN_LEAR_ensembles.csv", parse_dates=['Time'])

print(pred_BE.head())
print(pred_BE.columns)

# Plot
plt.figure(figsize=(10, 6))
plt.plot(pred_BE['Time'], pred_BE['Real price'], color = 'aquamarine', label = 'Real Price')
plt.plot(pred_BE['Time'], pred_BE['DNN Ensemble'], color = 'purple', alpha = 0.5, label = 'DNN Ensemble')

# Formating the plot
plt.legend()
plt.title('Belgium Price Forecasting')
plt.xlabel('Time')
plt.ylabel('Price [euro/MWh]')
plt.show()