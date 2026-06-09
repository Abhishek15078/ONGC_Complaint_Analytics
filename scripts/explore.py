import pandas as pd

df = pd.read_excel(
    "data/raw/Complaint_Analysis_Dashboard_Dataset_v3.xlsx"
)

print("\n===== Shape =====")
print(df.shape)

print("\n===== Missing Values =====")
print(df.isnull().sum())

print("\n===== Priority Distribution =====")
print(df["Priority"].value_counts())

print("\n===== Category Distribution =====")
print(df["Category"].value_counts())

print("\n===== Department Distribution =====")
print(df["Department"].value_counts())