import streamlit as st
import pandas as pd

st.title("📈 Investment Risk Agent")

st.write("Evaluate investment options by volatility and return.")

# Manual Entry
asset = st.text_input("Asset Name")
volatility = st.slider("Volatility (%)", 0, 100, 20)
expected_return = st.slider("Expected Annual Return (%)", -50, 50, 10)

if st.button("Assess Investment"):
    if volatility < 20 and expected_return > 5:
        st.write("✅ Low Risk Investment (Stable growth)")
    elif 20 <= volatility <= 50:
        st.write("⚠️ Medium Risk Investment (Consider portfolio balance)")
    else:
        st.write("❌ High Risk Investment (Speculative / risky)")

# Bulk Upload
st.subheader("Upload Investment Dataset (CSV)")
uploaded_file = st.file_uploader("Upload file", type=["csv"])

if uploaded_file:
    df = pd.read_csv(uploaded_file)

    def assess(row):
        if row["Volatility"] < 20 and row["Return"] > 5:
            return "Low Risk"
        elif 20 <= row["Volatility"] <= 50:
            return "Medium Risk"
        else:
            return "High Risk"

    df["RiskLevel"] = df.apply(assess, axis=1)
    st.dataframe(df)

    csv = df.to_csv(index=False).encode("utf-8")
    st.download_button("Download Investment Risk Report", data=csv, file_name="investment_risk_report.csv")
