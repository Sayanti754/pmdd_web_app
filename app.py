import streamlit as st

def get_recommendation(diagnosis, consulted, gender):
    link_all = "https://www.justdial.com/Rourkela/Gynaecologist-Obstetrician-Doctors/nct-10551087"
    link_female = "https://www.justdial.com/Rourkela/Women-Gynaecologist-Obstetrician-Doctors-in-Rourkela-Sector-7/nct-12102921"

    if diagnosis == "PMDD":
        message = (
            "⚠️ You are showing signs of Premenstrual Dysphoric Disorder (PMDD).\n"
            "🩺 Please follow your doctor's prescription carefully.\n"
            "💊 Continue medications and maintain proper lifestyle habits.\n"
        )
        if consulted == "no":
            message += "‼️ It is highly advised to consult a gynecologist immediately.\n"
        message += "\n👩‍⚕️ Recommended Doctors:\n"
        if gender == "female":
            message += f"🔗 Female Doctors Only: {link_female}\n"
        message += f"🔗 All Doctors: {link_all}"
        return message

    elif diagnosis == "At Risk":
        message = (
            "⚠️ You may be at risk of developing PMDD.\n"
            "🧘‍♀️ Suggested actions:\n"
            "- Maintain a balanced diet\n"
            "- Regular sleep and physical activity\n"
            "- Manage stress and track menstrual health\n"
            "- Avoid caffeine and alcohol during PMS\n"
        )
        if consulted == "no":
            message += "\n‼️ Please consult a gynecologist for early evaluation.\n"
        message += "\n👩‍⚕️ Doctors to consult:\n"
        if gender == "female":
            message += f"🔗 Female Doctors Only: {link_female}\n"
        message += f"🔗 All Doctors: {link_all}"
        return message

    else:
        return (
            "✅ You currently show no signs of PMDD.\n"
            "🎉 Keep up the good habits! Stay healthy and emotionally strong.\n"
            "🏃‍♀️ Exercise, eat well, get regular sleep and track your menstrual health.\n"
            "💪 You're doing great — continue your wellness journey!\n"
            "\n👩‍⚕️ If needed, consult a doctor anytime:\n"
            f"🔗 Female Doctors Only: {link_female}\n"
            f"🔗 All Doctors: {link_all}"
        )

st.set_page_config(page_title="PMDD Detection", layout="centered")
st.title("💮 PMDD Detection & Support System 💮")

st.markdown("Please fill in the following details to assess your symptoms:")

# SECTION 1: Personal Info
gender = st.radio("Gender:", ["female", "male"])
age = st.number_input("Your age:", 10, 60)
first_period_age = st.number_input("Age at first period:", 8, 25)
weight = st.number_input("Your weight (in kg):", 30.0, 150.0)
hemoglobin = st.number_input("Haemoglobin level (g/dL):", 5.0, 20.0)

# New Hormonal Questions
thyroid = st.radio("Do you have thyroid issues?", ["yes", "no"])
pcos = st.radio("Have you been diagnosed with PCOS?", ["yes", "no"])
pcod = st.radio("Have you been diagnosed with PCOD?", ["yes", "no"])

# SECTION 2: Menstrual Info
married = st.radio("Are you married?", ["yes", "no"])
if married == "yes":
    conceive_problem = st.radio("Are you having trouble conceiving?", ["yes", "no"])

family_history = st.radio("Any family history of PMDD?", ["yes", "no"])
period_cycle = st.number_input("How many days does your menstruation cycle last?", 2, 10)
trouble_menstruation = st.radio("Do you face trouble menstruating?", ["yes", "no"])
irregular_periods = st.radio("Are your periods irregular?", ["yes", "no"])
cramps = st.slider("Cramps level during periods (0–3):", 0, 3)

# New Lifestyle Questions
junk_food = st.radio("Do you eat junk food regularly?", ["yes", "no"])
exercise = st.radio("Do you exercise regularly?", ["yes", "no"])
physical_activity = st.selectbox("How would you rate your physical activity?", ["Low", "Moderate", "High"])

# SECTION 3: Medical History and Symptoms
consulted = st.radio("Have you consulted a doctor?", ["yes", "no"])
takes_med = st.radio("Are you on any medication?", ["yes", "no"])
if takes_med == "yes":
    med_names = st.text_input("Mention your medicines:")

duration_symptoms = st.text_input("Since when have you been facing these troubles? (e.g., 6 months)")

mood_swings = st.slider("Mood Swings severity (0–3):", 0, 3)
anxiety = st.slider("Anxiety/Depression severity (0–3):", 0, 3)
irritability = st.slider("Irritability level (0–3):", 0, 3)
sleep_issues = st.slider("Sleep issues severity (0–3):", 0, 3)
fatigue = st.slider("Fatigue severity (0–3):", 0, 3)

# Submit and Diagnosis
if st.button("Submit"):
    total_score = mood_swings + anxiety + irritability + sleep_issues + fatigue

    if total_score <= 3:
        diagnosis = "No PMDD"
    elif 4 <= total_score <= 6:
        diagnosis = "At Risk"
    else:
        diagnosis = "PMDD"

    st.markdown("## 📝 Assessment Summary")
    st.write(f"Age: {age}")
    st.write(f"Weight: {weight} kg")
    st.write(f"First Period Age: {first_period_age}")
    st.write(f"Haemoglobin: {hemoglobin} g/dL")
    st.write(f"Thyroid Issues: {thyroid}")
    st.write(f"PCOS: {pcos}")
    st.write(f"PCOD: {pcod}")
    st.write(f"Cycle Duration: {period_cycle} days")
    st.write(f"Symptoms Duration: {duration_symptoms}")
    st.write(f"Symptom Score: {total_score} / 15")
    st.write(f"Junk Food: {junk_food}")
    st.write(f"Exercise: {exercise}")
    st.write(f"Physical Activity: {physical_activity}")

    st.success(f"🩺 Diagnosis: {diagnosis}")
    st.markdown("## 💡 Recommendation")
    st.info(get_recommendation(diagnosis, consulted, gender))
