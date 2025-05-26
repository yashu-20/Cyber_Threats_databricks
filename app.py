import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="Cyber Threats Dashboard", layout="wide")

# Title
st.title("Cyber Threat Detection Dashboard")
st.markdown("**Built using Databricks + Streamlit**")

# Load dataset
df = pd.read_csv("Global_Cybersecurity_Threats_2015-2024.csv")



# Show raw data
with st.expander("View Raw Dataset"):
    st.dataframe(df.head())

# Summary stats
st.subheader("Data Summary")
st.write(df.describe())

# Top attack types
st.subheader("Attack Types Distribution")
st.bar_chart(df['Attack Type'].value_counts())

# Target industries
st.subheader("Target Industries Distribution")
industry_counts = df['Target Industry'].value_counts()
st.bar_chart(industry_counts)

# Visual results
st.subheader("Model Performance")
st.markdown("""
- **Model Used**: Gradient Boosted Trees
- **Target Variable**: Long Resolution Time
- **AUC ROC**: 0.478
- **Accuracy**: 0.474
- **F1 Score**: 0.474
- **Precision**: 0.474
- **Recall**: 0.474

These results were based on features like:
`Year`, `Country`, `Attack Type`, `Target Industry`, `Financial Loss`, and `Affected Users`
""")

st.sidebar.header("Filter Data")

selected_year = st.sidebar.selectbox("Select Year", sorted(df["Year"].dropna().unique()))
filtered_df = df[df["Year"] == selected_year]

st.subheader(f"Filtered Data for Year {selected_year}")
st.dataframe(filtered_df.head())


st.subheader("Top 5 Attack Types")
top_attacks = df["Attack Type"].value_counts().head(5)
st.bar_chart(top_attacks)

# GitHub link
st.markdown("[View full project on GitHub](https://github.com/yashu-20/Cyber_Threats_databricks)")
