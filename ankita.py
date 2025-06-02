import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("Datasets/mutual_funds_india.csv")
df.columns = df.columns.str.replace(" ", "")

# App title
st.title("Mutual Funds Explorer - India")

# Select Category
category_list = df.category.dropna().unique()
category = st.selectbox("Select Fund Category", sorted(category_list))

# Filter by selected category
filtered_by_category = df[df.category == category]

# Select AMC (depends on category)
amc_list = filtered_by_category.AMC_name.dropna().unique()
amc = st.selectbox("Select AMC", sorted(amc_list))

# Filter by selected AMC
filtered_data = filtered_by_category[filtered_by_category.AMC_name == amc]

# Plot bar chart
st.subheader("1-Year Returns of Mutual Funds")
plt.figure(figsize=(12, 6))
sns.barplot(x=filtered_data.MutualFundName, y=filtered_data.return_1yr, palette='ocean')
plt.xticks(rotation=90)
plt.ylabel("1-Year Return (%)")
plt.xlabel("Mutual Fund")
plt.title(f"1-Year Returns for {amc} in {category}")
st.pyplot(plt)
