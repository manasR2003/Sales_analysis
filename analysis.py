import pandas as pd
import matplotlib.pyplot as plt

# Load data
data = pd.read_csv('Data.csv')

# Convert Date column to datetime
data['Date'] = pd.to_datetime(data['Date'])

# Create Revenue column
data['Revenue'] = data['Units_Sold'] * data['Unit_Price']

# Print full dataset
print(data.to_string())

# ==========================
# Business Calculations
# ==========================

total_unit_sale = data['Units_Sold'].sum()
total_revenue = data['Revenue'].sum()
average_order = data['Revenue'].mean()
maximum_unit_sale = data['Units_Sold'].max()

maximum_sale_product_name = data.loc[
    data['Units_Sold'] == maximum_unit_sale,
    'Product'
]

# ==========================
# Print Results
# ==========================

print("\n========== SALES SUMMARY ==========")
print("Total Unit Sale :", total_unit_sale)
print("Total Revenue :", total_revenue)
print("Average Order Value :", round(average_order))
print("Maximum Unit Sale :", maximum_unit_sale)
print("Maximum Sale Product Name :",maximum_sale_product_name.to_string(index=False))
print("===================================")


plt.plot(data['Date'],data['Units_Sold'],'o:r',mec='blue',ms=15)
plt.xlabel('Date')
plt.ylabel('Units Sold')
plt.title('Growth')
plt.show()