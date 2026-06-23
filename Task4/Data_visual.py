

import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
df = pd.read_excel(r"C:\Users\ahtas\Downloads\Dataset for Data Analytics.xlsx")

# Product count nikalna
product_counts = df['Product'].value_counts()
order_count =df['OrderStatus'].value_counts()
Referral_Source =df['ReferralSource'].value_counts()
iteam_cart = df ['ItemsInCart']
total_price = df['TotalPrice'].value_counts()

print(order_count)
print(product_counts)
print(Referral_Source)
print(iteam_cart)
print(total_price)

# Bar chart product 
plt.figure(figsize=(4,3))
product_counts.plot(kind='bar')

# Labels aur title
plt.xlabel('Product')
plt.ylabel('Number of Orders')
plt.title('Product Sales Distribution')

# Rotation for readability
plt.xticks(rotation=45)

plt.show()
  
# chart of order status
plt.figure(figsize=(4,3))
order_count.plot(kind='pie', autopct='%1.1f%%')
starting_angle = 90
# Labels aur title
plt.title('Order Status Distribution')
plt.show()
# bar chart of Referral Source
plt.figure(figsize=(4,3))   
Referral_Source.plot(kind='bar',color='orange', edgecolor='black')
plt.xlabel('Referral Source')
plt.ylabel('Number of Orders')
plt.title('Referral Source Distribution')
plt.xticks(rotation=45)
plt.show()
#cart of item in  cart 
plt.figure(figsize=(4,3))
iteam_cart.plot(kind='hist', bins=10, edgecolor='black')
plt.xlabel('Items in Cart')
plt.ylabel('Frequency')
plt.title('Items in Cart Distribution')
plt.show()
# cart of total prrice chart 
plt.figure(figsize=(4,3))
total_price.plot(kind='hist', bins=10, color ='green', edgecolor='black')
#title and labels
plt.xlabel('TotalPrice')
plt.ylabel('Frequency')
plt.title('Total Price Distribution')


plt.show()

