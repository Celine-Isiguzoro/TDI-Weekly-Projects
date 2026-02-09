import csv
with open ("supply_chain_dataset.csv", "r") as file:
    csv_reader = csv.DictReader(file)
    fieldnames = next(csv_reader)
    data = list(csv_reader)

# TASK 1: Organize orders in a list
    print("TASK 1: ORGANIZE ORDERS IN A LIST")
    print("-" * 80)
    # Create a list of all order costs

    order_costs = []
    for row in data:
        cost = float(row["total_cost"]) #Convert to float because csv files are originally strings
        order_costs.append(cost)
    #print("The list of all order costs: ")
    #print(order_costs)


    # Find the total of all orders
    total_no_orders = len(order_costs)
    total_orders = sum(order_costs)
    # print(f"The total number of all orders are {total_no_orders}")
    # print(f"The sum of all orders is {total_orders:.2f}")


    # Find the average order value
    avg_order_value = total_orders / total_no_orders
    #print(f"The average order value is {avg_order_value:.2f}")


    # Sort the list and identify the median value
    sorted_list = sorted(order_costs)
    #print(sorted_list)
    if total_no_orders % 2 == 0:
        # if the median is an even number
        first_mid_no = sorted_list[total_no_orders // 2 -1]
        second_mid_no = sorted_list[total_no_orders // 2]
        median = (first_mid_no + second_mid_no)/ 2
    else: 
        # if the median is an odd number
        median = sorted_list[total_no_orders // 2]
    # print(f"Median Order Value: {median:.2f}")
    # print()


# TASK 2: Map products to suppliers using dictionaries
    print("TASK 2: MAP PRODUCTS TO SUPPLIERS USING DICTIONARIES")
    print("-" * 80)
    # # Create a dictionary of all suppliers and products

    product_supplier = {}
    for row in data:
        product = row["product_category"].strip() # Store the products in the variable while removing extra spaces
        supplier = row["supplier_name"].strip().lower().replace(" ", "") # Store the suppliers in the variable while removing extra spaces and standardizing it 

        if product not in product_supplier:
            product_supplier[product] = []
        product_supplier[product].append(supplier)

    for product, supplier in product_supplier.items():
        print(f"{product}: {supplier}")

    # Look up which supplier provides a specific product 
    supplier_for_specific_product = product_supplier.get("Control Systems", "Not found")
    supplier_for_specific_product2 = product_supplier.get("Motors", "Not found")
    supplier_for_specific_product3 = product_supplier.get("Connectors", "Not found")
    supplier_for_specific_product4 = product_supplier.get("Hydraulics", "Not found")
    supplier_for_specific_product5 = product_supplier.get("Wheels", "Not found")
    print(supplier_for_specific_product)
    print(supplier_for_specific_product2)
    print(supplier_for_specific_product3)
    print(supplier_for_specific_product4)
    print(supplier_for_specific_product5)

    # Count how many unique suppliers you have 
    unique_suppliers = set()
    for supplier_list in product_supplier.values():
        for supplier in supplier_list:
            unique_suppliers.add(supplier)
    print(f"The unique suppliers are {len(unique_suppliers)}")


# TASK 3: Find Unique Values with Sets 
    print("TASK 3: FIND UNIQUE VALUES WITH SETS")
    print("-" * 80)
    # Create sets for all unique suppliers
    unique_suppliers = set()
    for supplier_list in product_supplier.values():
        for supplier in supplier_list:
            unique_suppliers.add(supplier)
    print(f"The unique suppliers are {unique_suppliers}")

    # Create sets for all unique product names 
    unique_products = set(product_supplier.keys())
    print(f"The unique products are: {unique_products}")
   # Create sets for all unique order statuses 
    unique_order_status = set()
    for row in data:
        order_status = row["delivery_status"].strip()
        unique_order_status.add(order_status)
    print(f"The unique order statuses are : {unique_order_status}")
    # Create sets for all supplier_location
    unique_supplier_location = set()
    for row in data:
        supplier_location = row["supplier_location"].strip()
        unique_supplier_location.add(supplier_location)
    print(f"The unique supplier location are : {unique_supplier_location}")
    # Create set for return status
    unique_return_status = set()
    for row in data:
        return_status = row["return_status"].strip()
        unique_return_status.add(return_status)
    print(f"The unique return statuses are : {unique_return_status}")

    # Count how many unique items exist in each category 
    print(f"Number of unique products are {len(unique_products)}")
    print(f"Number of unique suppliers are {len(unique_suppliers)}")
    print(f"Number of unique supplier locations are {len(unique_supplier_location)}")
    print(f"Number of return status are {len(unique_return_status)}")
    print(f"Number of order statuses are {len(unique_order_status)}")

    # Find products that only one supplier provides 
    product_one_supplier = {}
    for product, suppliers in product_supplier.items():
        if len(supplier) == 1:
            product_one_supplier[product] = suppliers[0]
    # print(f"Products with only one supplier: {product_one_supplier}")
        

# TASK 4: Identify single-source products
    print("TASK 4: IDENTIFY SINGLE-SOURCE PRODUCTS")
    print("-" * 80)
    for product, supplier in product_supplier.items():
        # print(f"Product: {product}, Suppliers: {supplier}, Count: {len(supplier)}")
        try:
            if len(suppliers) == 1:
                print("Single-source products")
                print(f"Product {product}: {supplier[0]}")
            else:
                if len(suppliers) > 1:
                    print(f"{product} does not have single source products")
        except Exception as e:
            print("Error")


# Task 5: Build a complex network
    print("TASK 5: BUILD A COMPLEX NETWORK")
    print("-" * 80)
    supplier_network = {}
    
    for row in data:
        supplier = row["supplier_name"].lower().strip().replace(" ", "")
        product = row["product_category"].strip()
        cost = float(row["total_cost"])

        # if they are not in the already created dictionary, create them
        if supplier not in supplier_network:
            supplier_network[supplier] = {}
        if product not in supplier_network[supplier]: # Add the product as a list to the dictionary of suppliers already created
            supplier_network[supplier][product] = []
        # Add cost to it
        supplier_network[supplier][product].append(cost)

    print("Supplier Network Structure")
    for supplier, product in supplier_network.items():
        print(f"{supplier}")
        for product, cost in product.items():
            print(f"{product}: {cost}")

    # Query it 
    query_supplier = "supplierc"
    # for supplier in supplier_network:
    if query_supplier in supplier_network:
        print(f"Products from {query_supplier} are:")
        # for products in supplier_network[query_supplier]:
        print(f"{product}")
    else:
            print(f"{query_supplier} not in dictionary")

    query_supplier2 = "supplierb"
    if query_supplier2 in supplier_network:
        print(f"Products from {query_supplier2} are {product}")

    query_supplier3 = "supplierd"
    if query_supplier3 in supplier_network:
        print(f"Products from {query_supplier3} are {product}")

    # Calculate the total value of products from each supplier 
    for supplier, product_dict in supplier_network.items():
        total = 0
    # for item in product:
    #     print(f"Value: {item}, Type: {type(item)}") # found out therre were strings embedded in my list
    for poduct_name, cost_list in product_dict.items():
        for cost in cost_list:
            total = total + cost
    print(f"{supplier}: ${total:.2f}")


    # Extra Challenges Challenge 1: 
    # Create a list of orders that exceed a certain cost threshold. Then calculate what percentage of total orders this represents
    threshold = 65000
    high_cost_orders = []
    total_order = []
    # Loop through the data
    for row in data:
        cost = float(row["total_cost"])
        total_order.append(cost)
    # Check and append the high order cost in the list already provided
        if cost > threshold:
            high_cost_orders.append(cost)
    # To check the percentage of total orders it represents
    no_high_orders = len(high_cost_orders)
    no_total_orders = len(total_order)
    percentage = (no_high_orders / no_total_orders) * 100
    print(f"The number of total orders is {no_total_orders}")
    print(f"The number of orders that exceeded the threshold is {no_high_orders}")
    print(f"The percentage of the total number of orders that exceeded the threshold is {percentage:.2f}%")


    # Challenge 2: 
    # Using your supplier-to-products dictionary, find which supplier provides the most products. 
    max_supplier = None
    max_count = 0
    for supplier, product_dict in supplier_network.items():
        product_count = len(product_dict)

        if product_count > max_count:
            max_count = product_count
            max_supplier = supplier
    print(f"Supplier with most products: {max_supplier} with the number of {max_count} products")


    # Extra challenge: To find the most expensive product
    costly_product = None
    max_cost = 0

    for product, cost in supplier_network.items():
        # product_cost = max(cost)
        for row in data:
            product = row["product_category"]
            cost = float(row["total_cost"])
        if cost > max_cost:
            costly_product = product
            max_cost = cost
    print(f"The most expensive product is {costly_product} with a cost of ${max_cost:.2f}")


    # Challenge 3: 
    # Create a structure that groups orders by status. Then query it to find all delivered orders and calculate their average value. 
    # Create a dictionary orders and status
    orders_by_status ={}
    for row in data:
        status = row["delivery_status"]
        orders = row["order_id"]
        cost = float(row["total_cost"])

        if status not in orders_by_status:
            orders_by_status[status] = []
        orders_by_status[status].append(cost)

    delivered_orders = orders_by_status.get("Delivered", [])
    print(delivered_orders)
    print(f"The number of delivered orders are {len(delivered_orders)}")

    total_delivered_value = sum(delivered_orders)
    total_delivered_orders = len(delivered_orders)
    average_value = (total_delivered_value / total_delivered_orders) 
    print(f"The average value of delivered orders is {average_value:.2f}")

    # To find number of delayed orders
    delayed_orders = orders_by_status.get("Delayed", [])
    print(f"The number of delayed orders are {len(delayed_orders)}")

    # To find the number of cancelled orders
    cancelled_orders = orders_by_status.get("Cancelled", [])
    print(f"The number of cancelled orders are {len(cancelled_orders)}")

    # To find pending orders
    pending_orders = orders_by_status.get("Pending", [])
    print(f"The number of pending orders are {len(pending_orders)}")