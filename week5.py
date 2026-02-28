"""
Task 1: Convert Cleaned Data to NumPy Arrays 
Load your cleaned supply chain dataset. Extract numerical columns (costs, quantities, lead times) into NumPy arrays. 
Write code to: 
•	Load the cleaned CSV file 
•	Extract all cost values into a NumPy array 
•	Extract all quantity values into a NumPy array 
•	Extract all lead_time values into a NumPy array 
•	Verify the arrays were created correctly (print shape, dtype, first few values) 
"""
import csv
import numpy as np 
import pandas as pd

# Load the cleaned csv file
df = pd.read_csv('supply_chain_dataset.csv')

# Cost values into a NumPy array
cost = np.array(df['total_cost'])

# Quantity values into a NumPy array
quantity = np.array(df['quantity'])

# Lead time values into a NumPy array
lead_time = np.array(df['lead_time_days'])

# Verify the arrays
print(f"The shape of the cost array is {cost.shape} with the type {cost.dtype} with a display of a few values: {cost[0:5]}")
print(f"The shape of the quantity array is {quantity.shape} with the type {quantity.dtype} with a display of a few values: {quantity[4:9]}")
print(f"The shape of the lead time array is {lead_time.shape} with the type {lead_time.dtype} with a display of a few values: {lead_time[0:5]}")

