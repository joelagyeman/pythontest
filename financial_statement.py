print("Welcome to Ahmed's Financial Statement for Capstone!")

totalAmount =  50000
print("His total spending amount is: GHc ", totalAmount)

marketing = (25 /100) * totalAmount
print("Marketing cost is : GHc ", marketing)

operational_expenses = (50 / 100) * totalAmount
print("Operational expense is : GHc ", operational_expenses)

customer_acquisition = (25 / 100) * totalAmount
print("Customer acquisition cost is", customer_acquisition)

totalCustomers = int(customer_acquisition / 5)
print("The total number of customers: ", totalCustomers, "customers")

