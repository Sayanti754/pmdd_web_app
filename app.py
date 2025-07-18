import streamlit as st
import random

st.set_page_config(page_title="PMDD Detection System", layout="centered")
st.title("🌸 PMDD (Premenstrual Dysphoric Disorder) Detection System")
st.write("This tool is designed to raise awareness and help identify potential PMDD symptoms. Please answer honestly.")
st.markdown("🛡️ _Your identity is safe. You may leave your name blank if you'd like to stay anonymous. We're here to support, not to judge._")

with st.form("pmdd_form"):
    st.header("🔹 Personal Details")
    name = st.text_input("Full Name (optional)")
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

    st.header("🔹 Additional Symptoms")
    digestive_issues = st.radio("Do you face digestive issues?", ["Yes", "No"])
    hair_fall = st.radio("Do you experience hair fall?", ["Yes", "No"])
    skin_problems = st.radio("Do you face skin problems (acne, rashes, etc.)?", ["Yes", "No"])

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

    st.header("🔹 Emotional Expression")
    real_feelings = st.text_area("How do you really feel during your menstrual cycle? (Physically or emotionally)")

    st.header("🔹 Medical Consultation")
    consulted_doctor = st.radio("Have you consulted a doctor?", ["Yes", "No"])
    medication = st.radio("Are you on any medication?", ["Yes", "No"])
    medicine_name = st.text_input("If yes, mention your medicines") if medication == "Yes" else "N/A"
    trouble_duration = st.text_input("Since when have you been facing these issues? (e.g., 6 months)")
    feedback = st.text_area("Any feedback or anything you'd like to share with us? (optional)")

    submitted = st.form_submit_button("Submit")

if submitted:
    total_score = sum([
        mood_data["Mood Swings"]["Before"], mood_data["Mood Swings"]["During"], mood_data["Mood Swings"]["After"],
        mood_data["Sadness / Depression"]["Before"], mood_data["Sadness / Depression"]["During"], mood_data["Sadness / Depression"]["After"],
        mood_data["Irritability"]["Before"], mood_data["Irritability"]["During"], mood_data["Irritability"]["After"],
        mood_data["Low Energy"]["Before"], mood_data["Low Energy"]["During"], mood_data["Low Energy"]["After"]
    ])

    st.header("🔍 PMDD Risk Assessment")

    if bmi > 25:
        st.warning("⚠️ Your BMI indicates you may be overweight. Try to keep your weight in check with regular exercise and a balanced diet.")

    if haemoglobin < 12.0:
        st.warning("🩸 Your haemoglobin is low. This may lead to fatigue, weakness, and can worsen PMDD symptoms.")
        st.markdown("**Suggestions to improve haemoglobin:**")
        st.markdown("- Eat iron-rich foods like spinach, dates, lentils, tofu, eggs, and red meat")
        st.markdown("- Include vitamin C (like lemon, oranges) for better iron absorption")
        st.markdown("- Avoid tea/coffee right after meals")
        st.markdown("- Consult a doctor about iron supplements if levels remain low")
    elif haemoglobin > 15.5:
        st.info("ℹ️ Your haemoglobin is slightly higher than the normal range. It's usually not a concern, but if you're experiencing symptoms, consider consulting a healthcare provider.")
    else:
        st.success("✅ Your haemoglobin level is within the healthy range.")

    if total_score <= 3:
        st.success("✅ You seem to have no strong signs of PMDD.")
        st.info("💖 Keep nurturing your mind and body. Your mental well-being matters.")

    elif 4 <= total_score <= 6:
        st.warning("⚠️ You may be at risk of PMDD.")
        st.markdown("🔗 [👩‍⚕️ Female Gynaecologists in Rourkela](https://www.justdial.com/Rourkela/Women-Gynaecologist-Obstetrician-Doctors-in-Rourkela-Sector-7/nct-12102921)")
        st.markdown("🔗 [🏥 All Gynaecologists in Rourkela](https://www.justdial.com/Rourkela/Gynaecologist-Obstetrician-Doctors/nct-10551087)")
        st.markdown("🤍 Try preventive measures:")
        st.markdown("- Eat more whole foods and greens")
        st.markdown("- Regular light workouts (walk, dance, yoga)")
        st.markdown("- Track symptoms and talk to a doctor early")

    elif total_score > 6:
        st.error("❗ Your responses indicate strong signs of PMDD.")
        st.markdown("🔗 [👩‍⚕️ Female Gynaecologists in Rourkela](https://www.justdial.com/Rourkela/Women-Gynaecologist-Obstetrician-Doctors-in-Rourkela-Sector-7/nct-12102921)")
        st.markdown("🔗 [🏥 All Gynaecologists in Rourkela](https://www.justdial.com/Rourkela/Gynaecologist-Obstetrician-Doctors/nct-10551087)")
        st.markdown("💊 Please consult a doctor and strictly follow medication.")
        st.markdown("🧘‍♀️ What can help:")
        st.markdown("- Take prescribed medicines on time")
        st.markdown("- Avoid sugar, junk, caffeine")
        st.markdown("- Practice yoga, meditation or journaling")
        st.markdown("- Seek emotional support from friends or therapists")

    encouraging_quotes = [
        "You are stronger than you think 🌷",
        "Every emotion you feel is valid. Be kind to yourself 💛",
        "Healing is not linear — take it one step at a time 💫",
        "Your health matters. Your voice matters. You matter 🩷"
    ]
    st.markdown(f"💬 **Reminder:** _{random.choice(encouraging_quotes)}_")

    st.caption("This tool is for awareness only. Always consult a qualified doctor for diagnosis and treatment.")
    st.success("Thank you for using the PMDD Detection System. Your responses have been recorded.")