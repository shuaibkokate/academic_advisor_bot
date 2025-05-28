from fastapi import FastAPI, HTTPException, Query
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder

app = FastAPI()

# Load data
student_df = pd.read_csv("student_risk_predictions.csv")
mapping_df = pd.read_csv("advisor_student_mapping.csv")

@app.get("/risk_prediction/")
def get_student_risk(user_id: str, role: str):
    if role not in ["advisor", "chair"]:
        raise HTTPException(status_code=400, detail="Role must be 'advisor' or 'chair'")

    if role == "advisor":
        allowed_students = mapping_df[mapping_df["advisor_id"] == user_id]["student_id"].tolist()
    elif role == "chair":
        allowed_students = mapping_df[mapping_df["program_chair_id"] == user_id]["student_id"].tolist()

    filtered_df = student_df[student_df["student_id"].isin(allowed_students)]
    return filtered_df.to_dict(orient="records")
