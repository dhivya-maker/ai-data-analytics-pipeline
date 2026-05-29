import streamlit as st
import pandas as pd

st.title("AI Data Analytics Pipeline")

st.header("Processed Analytics Results")

df = pd.read_csv("output/csv_results.csv")

st.dataframe(df)

st.header("Issue Type Distribution")

issue_counts = df["issue_type"].value_counts()

st.bar_chart(issue_counts)

st.header("Category Distribution")

category_counts = df["category"].value_counts()

st.bar_chart(category_counts)