import streamlit as st
import pandas as pd

st.title("🎓 Academic Advisor Risk Dashboard")

# Simulate login
role = st.selectbox("Select Role", ["advisor", "chair"])
user_id = st.text_input("Enter Your User ID")

if user_id:
    df = pd.read_csv("student_risk_predictions.csv")
    mapping_df = pd.read_csv("advisor_student_mapping.csv")

    if role == "advisor":
        allowed = mapping_df[mapping_df["advisor_id"] == user_id]["student_id"].tolist()
    elif role == "chair":
        allowed = mapping_df[mapping_df["program_chair_id"] == user_id]["student_id"].tolist()
    else:
        allowed = []

    st.subheader("📊 Your Assigned Students")
    st.write(df[df["student_id"].isin(allowed)])
