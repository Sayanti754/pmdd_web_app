import streamlit as st

st.set_page_config(page_title="PMDD Detection System", layout="centered")
st.title("🌸 PMDD (Premenstrual Dysphoric Disorder) Detection System")
st.write("This tool is designed to raise awareness and help identify potential PMDD symptoms. Please answer honestly.")

st.header("🔹 Personal Details")
age = st.number_input("Age", min_value=10, max_value=50)
gender = st.radio("Gender", ["Female", "Male", "Other"])
weight = st.number_input("Weight (kg)", min_value=30.0, max_value=150.0)
height_cm = st.number_input("Height (cm)", min_value=100.0, max_value=220.0)
height_m = height_cm / 100 if height_cm else 0
bmi = round(weight / (height_m**2), 2) if height_m else 0
if bmi:
    st.write(f"**Calculated BMI:** {bmi}")

haemoglobin = st.number_input("Haemoglobin (g/dL)", min_value=5.0, max_value=20.0)

st.header("🔹 Hormonal & Menstrual Health")
thyroid = st.radio("Do you have thyroid issues?", ["Yes", "No"])
pcos = st.radio("Have you been diagnosed with PCOS?", ["Yes", "No"])
pcod = st.radio("Have you been diagnosed with PCOD?", ["Yes", "No"])
married = st.radio("Are you married?", ["Yes", "No"])
conceive_trouble = st.radio("Are you having trouble conceiving?", ["Yes", "No"]) if married == "Yes" else "N/A"
menstrual_cycle_days = st.number_input("How many days does your menstruation cycle last?", min_value=1, max_value=50)
irregular_periods = st.radio("Are your periods irregular?", ["Yes", "No"])
trouble_menstruating = st.radio("Do you face trouble menstruating?", ["Yes", "No"])
cramps_level = st.slider("Cramps level during periods", 0, 3)
family_history = st.radio("Any family history of PMDD?", ["Yes", "No"])

st.header("🔹 Lifestyle Factors")
junk_food = st.radio("Do you eat junk food regularly?", ["Yes", "No"])
exercise = st.radio("Do you exercise regularly?", ["Yes", "No"])
physical_activity = st.selectbox("Your physical activity level", ["Low", "Moderate", "High"])

st.header("🔹 Mood Tracking: Before / During / After Menstruation")
st.write("Rate the following symptoms for each phase (0 = None, 3 = Severe)")
mood_data = {}
for symptom in ["Mood Swings", "Sadness / Depression", "Irritability", "Low Energy"]:
    with st.expander(symptom):
        mood_data[symptom] = {
            "Before": st.slider(f"{symptom} (Before Period)", 0, 3, key=symptom + "_before"),
            "During": st.slider(f"{symptom} (During Period)", 0, 3, key=symptom + "_during"),
            "After": st.slider(f"{symptom} (After Period)", 0, 3, key=symptom + "_after")
        }

st.header("🔹 Symptoms Checklist")
before_symptoms = st.multiselect("What do you usually feel *before* your period?",
    ["Mood Swings", "Headache", "Food Cravings", "Anxiety", "Bloating", "Back Pain", "Breast Tenderness"])
during_symptoms = st.multiselect("What do you usually feel *during* your period?",
    ["Pain/Cramps", "Low Energy", "Nausea", "Mood Changes", "Sleepiness"])
after_symptoms = st.multiselect("What do you usually feel *after* your period?",
    ["Relief", "Fatigue", "Irritability", "Low Mood", "Improved Focus"])

st.header("🔹 Medical Consultation")
consulted_doctor = st.radio("Have you consulted a doctor?", ["Yes", "No"])
medication = st.radio("Are you on any medication?", ["Yes", "No"])
medicine_name = st.text_input("If yes, mention your medicines") if medication == "Yes" else "N/A"
trouble_duration = st.text_input("Since when have you been facing these issues? (e.g., 6 months)")
feedback = st.text_area("Any feedback or anything you'd like to share with us? (optional)")

score = (
    mood_data["Mood Swings"]["Before"]
    + mood_data["Sadness / Depression"]["Before"]
    + mood_data["Irritability"]["Before"]
    + mood_data["Low Energy"]["Before"]
)

st.header("🔍 PMDD Risk Assessment")
if score <= 3:
    st.success("✅ You are likely not showing strong signs of PMDD.")
elif 4 <= score <= 6:
    st.warning("⚠️ You may be at risk of PMDD. Consider consulting a doctor soon.")
    st.markdown("[🔗 Female Gynaecologists in Rourkela](https://www.justdial.com/Rourkela/Women-Gynaecologist-Obstetrician-Doctors-in-Rourkela-Sector-7/nct-12102921)")
elif score >= 7:
    st.error("❗ PMDD symptoms detected. Please consult a doctor.")
    st.markdown("[🔗 All Gynaecologists in Rourkela](https://www.justdial.com/Rourkela/Gynaecologist-Obstetrician-Doctors/nct-10551087)")

st.caption("This is not a medical diagnosis. Always consult a doctor for professional guidance.")
