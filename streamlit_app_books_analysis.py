
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Title
st.title("📚 Bestselling Books Analysis")

# Load dataset
@st.cache_data
def load_data():
    df = pd.read_csv(r"C:\Users\dawit\BestsellingBooks\bestsellers with categories.csv")
    return df

df = load_data()

# Dropdown to filter by Genre
genre_filter = st.selectbox("Select Genre", ["All"] + sorted(df["Genre"].unique()))

if genre_filter != "All":
    df = df[df["Genre"] == genre_filter]

# Show data preview
if st.checkbox("Show Raw Data"):
    st.dataframe(df)

# Log transform Reviews column
df["Log Reviews"] = df["Reviews"].apply(lambda x: np.log1p(x))

# Display rating distribution
st.subheader("User Rating Distribution")
fig, ax = plt.subplots()
sns.histplot(df["User Rating"], kde=True, ax=ax, color="skyblue")
st.pyplot(fig)

# Correlation heatmap
st.subheader("Feature Correlation")
fig2, ax2 = plt.subplots()
sns.heatmap(df[["User Rating", "Reviews", "Price", "Log Reviews"]].corr(), annot=True, cmap="coolwarm", ax=ax2)
st.pyplot(fig2)

# Yearly book count
st.subheader("Books Published per Year")
yearly = df["Year"].value_counts().sort_index()
st.bar_chart(yearly)

# Price vs Reviews
st.subheader("Price vs Reviews")
fig3, ax3 = plt.subplots()
sns.scatterplot(data=df, x="Price", y="Reviews", hue="Genre", ax=ax3)
st.pyplot(fig3)

# Author count
st.subheader("Top 10 Authors by Book Count")
top_authors = df["Author"].value_counts().head(10)
st.bar_chart(top_authors)
