import streamlit as st
import pandas as pd
from ai_processor import process_text_with_ai
st.set_page_config(
    page_title="AI Data Analytics Pipeline",
    layout="wide"
)


st.title("AI Data Analytics Pipeline")
st.write("Upload unstructured text files and generate AI-powered business insights.")

uploaded_files = st.file_uploader("Upload one or more files", type="txt", accept_multiple_files=True)

if uploaded_files:
    if st.button("Analyze Files"):
        results = []
        with (st.spinner("Analyzing Files...")):
            for uploaded_file in uploaded_files:
                text = uploaded_file.read().decode("utf-8")
                result = process_text_with_ai(text)
                result["source_file"] = uploaded_file.name
                results.append(result)
        df = pd.DataFrame(results)
        st.success("Analysis complete")
        st.subheader("Processed Results")
        st.dataframe(df)
        col1, col2, col3 = st.columns(3)
        col1.metric("Total Records", len(df))
        col2.metric("Total Categories", df["category"].nunique())
        col3.metric("Total Issues", df["issue_type"].nunique())

        st.subheader("Category Distribution")
        st.bar_chart(df["category"].value_counts())

        st.subheader("Issue Type Distribution")
        st.bar_chart(df["issue_type"].value_counts())

        st.subheader("Sentiment Distribution")
        st.bar_chart(df["sentiment"].value_counts())

        st.subheader("Executive Summary")

        top_category = df["category"].value_counts().idxmax()
        top_issue = df["issue_type"].value_counts().idxmax()
        top_sentiment = df["sentiment"].value_counts().idxmax()

        st.write(
            f"""
                    {len(df)} records were analyzed. The most common category was **{top_category}**.
                    The most frequent issue type was **{top_issue}**. Overall sentiment was mostly **{top_sentiment}**.
                    """
        )
else:
    st.info("Upload text files to begin analysis.")



