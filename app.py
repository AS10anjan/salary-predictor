# import streamlit as st
# from joblib import load
# model = load("linear_model.pkl")
# Age = int(input("Enter age: "))
# Gender = int(input("Enter gender: "))
# Education_Level = int(input("Enter eduaction level: "))
# Job_Title = int(input("Enter job title: "))
# years = int(input("Enter years of experience: "))

# result = model.predict([[Age,Gender,Education_Level,Job_Title,years]])
# print("Predicted Salary:", result[0])

# import streamlit as st
# from joblib import load

# model = load("linear_model.pkl")

# st.title("Employee Salary Prediction App")

# # Age
# Age = st.number_input("Age", min_value=18, max_value=65)

# # Gender (Dropdown)
# gender_option = st.selectbox("Gender", ["Male", "Female"])
# Gender = 1 if gender_option == "Male" else 0

# # Education (Dropdown)
# education_option = st.selectbox("Education Level", ["Bachelor's", "Master's", "PhD"])

# # Convert to numbers (IMPORTANT)
# education_map = {
#     "Bachelor's": 0,
#     "Master's": 1,
#     "PhD": 2
# }
# Education_Level = education_map[education_option]

# # Job Title (Dropdown example)
# job_option = st.selectbox("Job Title", ["Engineer", "Manager", "Analyst"])

# job_map = {
#     "Engineer": 0,
#     "Manager": 1,
#     "Analyst": 2
# }
# Job_Title = job_map[job_option]

# # Experience
# years = st.number_input("Years of Experience", min_value=0)

# # Prediction
# if st.button("Predict Salary"):
#     result = model.predict([[Age, Gender, Education_Level, Job_Title, years]])
#     st.success(f"Predicted Salary: {result[0]}")

# Age1 = scaler.transform([[49]])
# Age = Age1[0][0]
# Gender = 0
# Education_Level = 2
# Job_Title = 22
# Years_of_Experience1 = scaler.transform([[15]])
# Years_of_Experience = Years_of_Experience1[0][0]

import streamlit as st
from joblib import load

model = load("linear_model.pkl")

st.title("Salary Prediction App")

Age = st.number_input("Enter age")
Gender = st.number_input("Enter gender (0/1)")
Education_Level = st.number_input("Enter education level")
Job_Title = st.number_input("Enter job title")
years = st.number_input("Enter years of experience")

if st.button("Predict"):
    result = model.predict([[Age, Gender, Education_Level, Job_Title, years]])
    st.success(f"Predicted Salary: {result[0]}")