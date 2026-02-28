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

"""
Task 2: Perform Basic Array Operations 
Using your arrays from Task 1, perform calculations. 
Write code to: 
•	Calculate total revenue (cost * quantity for each order, then sum) 
•	Calculate average order value 
•	Find minimum and maximum costs 
•	Calculate the range of lead times (max - min) 
•	Multiply all costs by a shipping factor (e.g., 1.05 for 5% markup) 
"""
# Total revenue
total_revenue = np.sum(cost * quantity)
print(f"Total revenue: {total_revenue:.2f}")

# Average order value (cost * quantity)
order_value = cost * quantity
average_order_value = np.mean(order_value)
print(f"Average order value: {average_order_value:.2f}")

# Minimum and maximum costs
min_costs = np.min(cost)
max_costs = np.max(cost)
print(f"The minimum cost is {min_costs} while the maximum cost is {max_costs}")

# Range of lead times 
min_lead_time = np.min(lead_time)
max_lead_time = np.max(lead_time)
lead_time_range = max_lead_time - min_lead_time
print(f"The range of lead times is {lead_time_range}")

# Multiply all costs by a shipping factor (0.07)
cost_shipping_factor = cost * 0.07
print(cost_shipping_factor)

"""
Task 3: Calculate Statistical Metrics 
Compute comprehensive statistics on your supply chain metrics. 
Write code to: 
•	For cost array: mean, median (use percentile 50), std deviation, min, max, 25th percentile, 75th percentile 
•	For quantity array: mean, std deviation, min, max 
•	For lead_time array: mean, std deviation, min, max 
•	Identify which products have above-average costs 
•	Identify which orders have below-average lead times 
"""
# Statistical functions for cost array
cost_mean = np.mean(cost)
cost_median = np.median(cost)
cost_std = np.std(cost)
cost_min = np.min(cost)
cost_max = np.max(cost)
cost_25th = np.percentile(cost, 25)
cost_75th = np.percentile(cost, 75)
print(f"Cost mean: {cost_mean}")
print(f"Cost median: {cost_median}")
print(f"Cost std: {cost_std}")
print(f"Cost min: {cost_min}")
print(f"Cost max: {cost_max}")
print(f"Cost 25th percentile: {cost_25th}")
print(f"Cost 75th percentile: {cost_75th}")

# Statistical functions for quantity array
quantity_mean = np.mean(quantity)
quantity_std = np.std(quantity)
quantity_min = np.min(quantity)
quantity_max = np.max(quantity)
print(f"Quantity mean: {quantity_mean}")
print(f"Quantity std: {quantity_std}")
print(f"Minimum quantity: {quantity_min}")
print(f"Maximum quantity: {quantity_max}")

# Statistical functions for lead time array
lead_time_mean = np.mean(lead_time)
lead_time_std = np.std(lead_time)
lead_time_min = np.min(lead_time)
lead_time_max = np.max(lead_time)
print(f"Lead time mean: {lead_time_mean}")
print(f"Lead time std: {lead_time_std}")
print(f"Minimum lead time: {lead_time_min}")
print(f"Maximum lead time: {lead_time_max}")

# Products with above average costs
avg_cost = np.mean(cost)
above_average = np.where(cost > avg_cost)[0]
products_above_avg = df.iloc[above_average]
print(f"Products above average costs: {products_above_avg[['product_category', 'total_cost']]}")

# Orders with below average lead times
lead_time_avg = np.mean(lead_time)
below_avg = np.where(lead_time < lead_time_avg)
orders_below_avg = df.iloc[below_avg]
print(f"Orders below lead time average: {orders_below_avg[['order_id', 'lead_time_days']]}")

"""
Task 4: Compare Supplier Performance Using Arrays 
Extract data for each supplier separately and compare using NumPy. 
Write code to: 
•	Create separate arrays for each supplier's costs 
•	Create separate arrays for each supplier's lead times 
•	Calculate average cost per supplier 
•	Calculate average lead time per supplier 
•	Identify which supplier has the best average delivery time 
•	Identify which supplier has the lowest average cost 
"""
# Extract the unique suppliers from the dataset
suppliers = df['supplier_name'].unique()
print(f"Unique suppliers: {suppliers}")

supplier_names =[]
supplier_avg_costs = []
supplier_avg_lead_times = []

for supplier in suppliers:
    is_supplier = df['supplier_name'] == supplier
    supplier_names.append(supplier)
    supplier_cost = np.array(df[is_supplier]['total_cost'])
    supplier_lead_time = np.array(df[is_supplier]['lead_time_days'])

    supplier_avg_cost = np.mean(supplier_cost)
    supplier_avg_costs.append(supplier_avg_cost)
    supplier_avg_lead_time = np.mean(supplier_lead_time)
    supplier_avg_lead_times.append(supplier_avg_lead_time)
    
    delivery_time = np.array(df['actual_delivery_days'])
    avg_delivery_time = np.mean(delivery_time)
    best_delivery_time = np.argmin(supplier_avg_lead_times)
    lowest_avg_costs = np.argmin(supplier_avg_costs)
print()
print(f"Supplier with the best delivery time: {supplier_names[best_delivery_time]}({supplier_avg_lead_times[best_delivery_time]:.2f}days)")
print(f"Supplier with the lowest average cost: {supplier_names[lowest_avg_costs]} ({supplier_avg_costs[lowest_avg_costs]:.2f})")

# print(f"Supplier with the best average delivery time: {supplier_delivery_time[['supplier_name', 'actual_delivery_days']]}")
# print(f"Supplier with the lowest average cost: {min_avg_cost[['supplier_name', 'total_cost']]}")

"""
Task 5: Detect Outliers Using Statistical Thresholds Use NumPy's statistical functions to identify unusual orders. 
Write code to: 
•	Calculate mean and standard deviation for cost 
•	Find all orders where cost is more than 2 standard deviations above the mean (high outliers) 
•   Find all orders where cost is more than 2 standard deviations below the mean (low outliers) 
•	Do the same for lead_time 
•	Print which orders are statistical outliers and whether they seem legitimate or problematic 
"""
# Mean and Standard deviation for cost
cost_mean1 = np.mean(cost)
cost_std1 = np.std(cost)

# Orders where cost is more than 2 std above and below the mean
high_outliers = cost > (cost_mean1 + 2 * cost_std)
low_outliers = cost < (cost_mean1 - 2 * cost_std)

high_orders_outliers = df[high_outliers][['order_id', 'total_cost']]
low_orders_outliers = df[low_outliers][['order_id', 'total_cost']]

# Outliers in lead time
lead_time_mean1 = np.mean(lead_time)
lead_time_std1 = np.std(lead_time)

high_lead_time_outliers = lead_time > (lead_time_mean1 + 2 * lead_time_std)
low_lead_time_outliers = lead_time < (lead_time_mean1 - 2 * lead_time_std)

high_lead_time_orders = df[high_lead_time_outliers][['order_id', 'lead_time_days']]
low_lead_time_orders = df[low_lead_time_outliers][['order_id', 'lead_time_days']]

print(f"High orders outliers: {len(high_orders_outliers)}")
print(f"High lead time outliers: {len(high_lead_time_outliers)}")


"""
Extra Challenges Challenge 1: 
Create a "profit score" array by calculating (cost * quantity * profit_margin).
Use broadcasting to apply a different profit margin (0.20, 0.25, 0.30) and see how total profit changes. 
"""
# Broadcasting
profit_margins = np.array([0.20, 0.25, 0.30])
profit_score = (cost * quantity)[:, np.newaxis] * profit_margins
total_profits = np.sum(profit_score, axis=0)

print(f"Total profit at 20% margin: {total_profits[0]:.2f}")
print(f"Total profit at 25% margin: {total_profits[1]:.2f}")
print(f"Total profit at 30% margin: {total_profits[2]:.2f}")

"""Challenge 2: 
Use NumPy to find correlations. 
Extract two variables (e.g., quantity and cost, or lead_time and on_time_delivery). 
Calculate the correlation between them. What does the result tell you about your supply chain? 
"""
# Finding correlation between quantity and cost
quan_cost_corr = np.corrcoef(quantity, cost)[0, 1]
print(f"Correlation between quantity and cost is: {quan_cost_corr:.2f}")

# Finding correlation between lead time and on time delays
on_time = np.where(df['on_time'] == 'Yes', 1, 0)
lead_time_on_time_corr = np.corrcoef(lead_time, on_time)[0,1]
print(f"Correlation between lead time and on time:{lead_time_on_time_corr:.2f}")

"""
Challenge 3: 
Create a distribution analysis. 
Divide costs into bins (e.g., under $1000, $1000-$5000, $5000+). 
Count how many orders fall into each bin. What does this tell you about your order distribution? 
"""
# Distribution analysis using the if statement
cost_under_1000 = []
cost_5000 = []
cost_above_5000 = []

for cost_value in cost:
    if cost_value < 1000:
        cost_under_1000.append(cost_value)
    elif cost_value >= 1000 and cost_value < 5000:
        cost_5000.append(cost_value)
    else:
        cost_above_5000.append(cost_value)

print(f"Orders under 1000 are {len(cost_under_1000)}")
print(f"Orders between 1000 and 5000 are {len(cost_5000)}")
print(f"Orders more 5000 are {len(cost_above_5000)}")
print()

# Distribution analysis using histogram
cost_bins = [0, 1000, 5000, np.inf]
counts = np.histogram(cost, bins=cost_bins)
print(f"Orders under 1000: {counts[0][0]}")
print(f"Orders between 1000 and 5000 are {counts[0][1]}")
print(f"Orders more 5000 are {counts[0][2]}")