Supply Chain Data Analysis Project

A Python-based data analysis project that explores supply chain management through comprehensive analysis of orders, suppliers, and product categories.

📋 Project Overview

This project analyzes a supply chain dataset containing 2,999 orders across multiple suppliers and product categories, with a total transaction value exceeding $170 million. 
The analysis focuses on understanding supplier relationships, product costs, order patterns, and delivery metrics.

🎯 Objectives:
- Organize and analyze order data using Python data structures
- Build complex nested dictionaries to represent supplier-product relationships
- Query data to extract meaningful business insights
- Calculate key metrics including averages, totals, and percentages
- Identify patterns in high-value orders and supplier performance

📊 Dataset
File:`supply_chain_dataset.csv`
Key Fields:
- `order_id` - Unique identifier for each order
- `product_category` - Product type (Control Systems, Motors, Hydraulics, etc.)
- `supplier_name` - Supplier identifier
- `total_cost` - Order cost value
- `delivery_status` - Order delivery status
- `order_status` - Current order state

Technologies Used

- Python
- Libraries:
  - `csv` - For reading CSV data
  - Built-in data structures (lists, dictionaries)

📈 Tasks Completed

Task 1: Organize Orders in a List
- Created a list of all order costs
- Calculated total of all orders
- Found the average order value
- Sorted the list and identified the median value

Task 2: Map Products to Suppliers Using Dictionaries
- Built a product-to-supplier mapping dictionary
- Queried specific product suppliers
- Counted unique suppliers in the dataset

Task 3: Track Unique Suppliers
- Identified all unique suppliers
- Analyzed supplier distribution

Task 4: Group Products by Supplier (Reverse Mapping)
- Created supplier-to-products dictionary
- Enabled reverse lookup functionality

Task 5: Build a Complex Network
- Developed nested structure (dictionary of dictionaries)
- Mapped each supplier to their products and associated costs
- Queried supplier-specific product information
- Calculated total value of products from each supplier

🎯 Challenge Solutions

Challenge 1: High-Cost Order Analysis
Objective: Identify orders exceeding a cost threshold and calculate their percentage

Results:
- Threshold set at $50,000
- Orders above threshold: 832
- Total orders: 2,999
- Percentage: 27.74%

 Challenge 2: Supplier Product Diversity
**Objective:** Find which supplier provides the most products

Results:
- Supplier C provides the most diverse product range (3 products)

Challenge 3: Delivery Status Analysis
Objective: Group orders by status and analyze delivered orders

Implementation:
- Created dictionary grouping orders by delivery status
- Queried all delivered orders
- Calculated average value of delivered orders

💡 Key Findings

1. Supplier Performance:
   - Supplier A: $70,837,594.46 (highest transaction volume)
   - Supplier E: $4,760,051.03
   - Supplier C: $23,089,480.95
   - Supplier B: $43,099,100.00
   - Supplier D: $28,449,003.78

2. Product Insights:
   - Most expensive product category: Control Systems ($89,117.66)
   - 27.74% of orders are high-value (>$50,000)

3. Supplier Diversity:
   - Supplier C offers the most product variety

🐛 Key Learning Points

Challenges Faced & Solutions:

1. Data Type Issues:
   - Problem: CSV data imported as strings instead of numbers
   - Solution: Used `float()` conversion for numerical calculations

2. Dictionary Structure Confusion:
   - Problem: Attempted to sum dictionary keys instead of values
   - Solution: Properly iterated through nested dictionaries using `.items()`

3. Type Errors:
   - Problem: Mixed strings and numbers in lists causing sum() failures
   - Solution: Implemented type checking with `isinstance(item, (int, float))`

4. Understanding len():
   - Problem: Tried using `len()` on single numbers
   - Solution: Only use `len()` on containers (lists, dictionaries, strings)

📝 Code Highlights

Building Nested Dictionary Structure
```python
supplier_network = {}

for row in data:
    supplier = row["supplier_name"]
    product = row["product_category"]
    cost = float(row["total_cost"])
    
    if supplier not in supplier_network:
        supplier_network[supplier] = {}
    if product not in supplier_network[supplier]:
        supplier_network[supplier][product] = []
    
    supplier_network[supplier][product].append(cost)
```

Calculating Supplier Totals
```python
for supplier, products_dict in supplier_network.items():
    total = 0
    for product_name, cost_list in products_dict.items():
        for cost in cost_list:
            total = total + cost
    print(f"{supplier}: ${total:.2f}")
```

🎓 Skills Demonstrated

- Data structure design and implementation
- Dictionary manipulation and nested structures
- CSV file handling
- Data aggregation and statistical analysis
- Type checking and error handling
- Code debugging and problem-solving

This project is part of my learning journey in data analysis with Python.

---

*This project was completed as part of Python programming practice, focusing on data structures, file handling, and data analysis techniques.*
