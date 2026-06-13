import pandas as pd
# Load the dataset
df = pd. read_excel('Dataset for Data Analytics.xlsx')

print(df.head())
print("info")
print(df.info())
print("describe")
print(df.describe())

df ["Product"].value_counts().head(1)
df ["OrderStatus"].value_counts().head(1)
df ["PaymentMethod"].value_counts().head(1)
df ["ReferralSource"].value_counts().head(1)
print("Most popular product:", df["Product"].value_counts().idxmax())
print("Most common order status:", df["OrderStatus"].value_counts().idxmax())
print("Most common payment method:", df["PaymentMethod"].value_counts().idxmax())
print("Most common referral source:", df["ReferralSource"].value_counts().idxmax())

