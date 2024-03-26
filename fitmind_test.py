import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

st.sidebar.title("Menu")
page = st.sidebar.radio("Choose what you need",["FitMind - Introduction", "Fitness", "Mental Health", "Food & Recipes"])

if page == "FitMind - Introduction":
    st.title("FitMind")
    st.markdown("""
    FitMind ist eine ganzheitliche Gesundheits-App, die Fitness und mentales Wohlbefinden kombiniert, um Benutzern zu helfen, ein ausgewogenes und gesundes Leben zu führen.
    """)
    st.subheader("Willkommen bei FitMind!")
    st.write("FitMind unterstützt dich dabei, deine Fitnessziele zu erreichen und gleichzeitig dein mentales Wohlbefinden zu verbessern.")

elif page == "Fitness":
    st.title("Fitness")
    
    st.subheader("Beginners")
    st.write("If you're new to exercise or a particular exercise, start with 1 to 2 sets per exercise. Focus on learning proper form and gradually increasing the number of sets as you become more comfortable with the movements.")
    st.subheader("Intermediate")
    st.write("Intermediate: For those who have been exercising regularly and have some experience with the exercises, aim for 3 to 4 sets per exercise. This provides enough volume to challenge your muscles and promote strength and muscle growth.")
    st.subheader("Advanced")
    st.write("Advanced individuals who are looking to increase muscle size or strength may benefit from performing 4 to 5 sets per exercise. Higher volume workouts can help stimulate muscle hypertrophy and strength gains.")
   
    st.title("Workouts")
    st.subheader("Choose your Workouts")

    st.subheader("Lunges")

    st.subheader("Squats")
    st.write("Stand with your feet wider than your Hips and feet pointed slightly out.")
    st.write("Begin bendin your knees until parallel to the floor with your back as straight as possible.")
    st.write("Push back up until you reach standing positions.")
    st.write("Repeat.")
    st.video('https://youtu.be/xqvCmoLULNY')

    st.write("Narrow Squats")

    st.subheader("Sumo Squats")

    # Fitness Tracker
    st.title("Fitness Tracker")
    st.subheader("Tracke deine Fitness und erhalte Empfehlungen")
    # Input Widgets
    age = st.slider("Alter", 18, 100, 25)
    weight = st.number_input("Gewicht (kg)", min_value=20.0, max_value=500.0, value=70.0, step=0.1)
    height = st.number_input("Größe (cm)", min_value=100, max_value=300, value=170, step=1)
    activity_level = st.selectbox("Aktivitätslevel", ["Sedentär", "Leicht aktiv", "Mäßig aktiv", "Sehr aktiv", "Extrem aktiv"])

    # Calculate BMI
    bmi = weight / ((height/100) ** 2)
    st.write(f"Ihr BMI beträgt: {bmi:.2f}")

    # BMI Classification
    bmi_data = pd.DataFrame({
        'Kategorie': ['Untergewicht', 'Normalgewicht', 'Übergewicht', 'Adipositas'],
        'BMI-Bereich': ['< 18.5', '18.5 - 24.9', '25.0 - 29.9', '≥ 30.0'],
        'Empfehlung': ['Zunehmen', 'Normalgewicht halten', 'Abnehmen', 'Stark abnehmen']
    })
    st.write("BMI-Klassifikation:")
    st.dataframe(bmi_data)

    # BMI Chart
    st.bar_chart(bmi_data.set_index('Kategorie')['BMI-Bereich'])

elif page == "Mental Health":
    st.title("Mental Health")
    st.write("Hier finden Sie Informationen über unser Team und unsere Mission.")
    st.subheader("Überprüfe deine Stimmung und Stresslevel")

    # Mood and Stress Level Input Widgets
    mood = st.slider("Stimmung", 0, 10, 5)
    stress_level = st.slider("Stresslevel", 0, 10, 5)

    # Mood and Stress Level Chart
    mood_data = pd.DataFrame({
        'Datum': pd.date_range(start='2024-01-01', periods=30),
        'Stimmung': np.random.randint(0, 11, size=30),
        'Stresslevel': np.random.randint(0, 11, size=30)
    })
    st.write("Verlauf der Stimmung und des Stresslevels:")
    st.line_chart(mood_data.set_index('Datum'))

elif page == "Food & Recipes":
    st.title("Food & Recipes")

# Footer
st.sidebar.markdown("---")
st.sidebar.subheader("Über uns")
st.sidebar.info("Diese App wurde von Julia und Cherilyn entwickelt.")

st.sidebar.subheader("Kontakt")
st.sidebar.text("Bei Fragen oder Anregungen kontaktieren Sie uns unter:")
st.sidebar.text("fitmind@example.com")
