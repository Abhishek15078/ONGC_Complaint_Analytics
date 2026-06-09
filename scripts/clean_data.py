import pandas as pd

df = pd.read_excel(
    "data/raw/Complaint_Analysis_Dashboard_Dataset_v3.xlsx"
)
df["Priority"] = (
    df["Priority"]
    .str.strip()
    .str.capitalize()
)
df["Resolution_Time_Hours"].isnull().sum()
df["Is_Resolved"] = (
    df["Resolution_Time_Hours"]
    .notna()
)
df["Resolution_Time_Hours"] = (
    df["Resolution_Time_Hours"]
    .fillna(0)
)
df["Description"] = (
    df["Description"]
    .str.encode("ascii","ignore")
    .str.decode("ascii")
)
def speed_bucket(hours):

    if hours == 0:
        return "Unresolved"

    elif hours <= 24:
        return "Fast"

    elif hours <= 72:
        return "Medium"

    else:
        return "Slow"
df["Resolution_Speed"] = df["Resolution_Time_Hours"].apply(speed_bucket)


df["SLA_Status"] = df.apply(
    lambda row:
    "Within SLA"
    if row["Resolution_Time_Hours"] <= 72
    else "Breached",
    axis=1
)    
df["Month"] = df["Arising_Date"].dt.month_name()

df["Year"] = df["Arising_Date"].dt.year

df["Quarter"] = df["Arising_Date"].dt.quarter

df["Weekday"] = df["Arising_Date"].dt.day_name()

priority_map = {
    "Low":1,
    "Medium":2,
    "High":3,
    "Critical":4
}

df["Priority_Score"] = (
    df["Priority"]
    .map(priority_map)
)
df["Description_Length"] = (
    df["Description"]
    .astype(str)
    .apply(len)
)
df["Word_Count"] = (
    df["Description"]
    .astype(str)
    .apply(lambda x: len(x.split()))
)
df.to_excel(
    "data/cleaned/cleaned_complaints.xlsx",
    index=False
)
df.to_csv(
    "data/cleaned/cleaned_complaints.csv",
    index=False
)