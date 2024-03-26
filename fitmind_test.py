import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

st.sidebar.title("Menu")
page = st.sidebar.radio("Choose what you need",["FitMind - Introduction", "Fitness", "Mental Health", "Food & Recipes"])

if page == "FitMind - Introduction":
    st.title("Welcome to FitMind!")
    st.markdown("""
    FitMind is a health app that combines fitness and mental wellbeing to help users lead a balanced and healthy life.
    """)
    st.write("FitMind helps you to achieve your fitness goals and improve your mental well-being at the same time.")

elif page == "Fitness":
    st.title("Fitness")
    st.subheader("Choose your level")
    st.subheader("Beginners")
    st.write("If you're new to exercise or a particular exercise, start with 1 to 2 sets per exercise. Focus on learning proper form and gradually increasing the number of sets as you become more comfortable with the movements.")
    st.subheader("Intermediate")
    st.write("Intermediate: For those who have been exercising regularly and have some experience with the exercises, aim for 3 to 4 sets per exercise. This provides enough volume to challenge your muscles and promote strength and muscle growth.")
    st.subheader("Advanced")
    st.write("Advanced individuals who are looking to increase muscle size or strength may benefit from performing 4 to 5 sets per exercise. Higher volume workouts can help stimulate muscle hypertrophy and strength gains.")
   
    st.divider()
    
    if page == "Fitness":
        st.sidebar.subheader("Workouts")
        
        Workouts = [" ", "Arms", "Abs", "Legs", "Butt"]
        selected_subcategory = st.sidebar.selectbox("Choose a specific area", Workouts)
                
    if selected_subcategory == " ":
        st.subheader(" ")
        st.write(" ")
        
    elif selected_subcategory == "Arms":
        st.subheader("Arms")
        st.write("Content for Cardio category")
    
    elif selected_subcategory == "Abs":
        st.subheader("Abs")
        st.write("Content for Strength Training category")
        
    elif selected_subcategory == "Legs":
        st.subheader("Legs")
        st.write("Content for Flexibility category")
        
    elif selected_subcategory == "Butt":
        st.subheader("Butt")
        st.write("Content for Endurance category")
        st.subheader("Squats")
        st.write("Instructions:")
        st.write(" 1. Stand with your feet wider than your Hips and feet pointed slightly out.")
        st.write(" 2. Begin bendin your knees until parallel to the floor with your back as straight as possible.")
        st.write(" 3. Push back up until you reach standing positions.")
        st.write(" 4. Repeat.")
        st.video('https://youtu.be/xqvCmoLULNY')

        st.subheader("Lunges")
    
        st.subheader("Narrow Squats")
    
        st.subheader("Sumo Squats")
        
    st.sidebar.subheader("Planned Programs")
    second_subcategory = st.sidebar.selectbox("Choose a second subcategory", [" ", "Summerbody", "Get That Booty", "VERY HARD ABS"])
   
    if second_subcategory == " ":
        st.subheader(" ")
        st.write(" ")
    
    elif second_subcategory == "Summerbody":
        st.subheader("Summerbody")
        st.write("Summerbody")
        
    elif second_subcategory == "Get That Booty":
        st.subheader("Get That Booty")
        st.write("Get That Booty")
        
    elif second_subcategory == "VERY HARD ABS":
        st.subheader("ABS ABS ABS")

    st.sidebar.subheader("Fitness Tracker")
    third_subcategory = st.sidebar.selectbox("Choose a third subcategory", ["  ", "Track Fitness"])
    
    if third_subcategory == " ":
        st.write(" ")
        
    elif third_subcategory == "Track Fitness":
        st.title("Fitness Tracker")
        st.subheader("Track your fitness and get recommendations")
        # Input Widgets
        age = st.slider("Age", 18, 100, 25)
        weight = st.number_input("Weight (kg)", min_value=20.0, max_value=500.0, value=70.0, step=0.1)
        height = st.number_input("Height (cm)", min_value=100, max_value=300, value=170, step=1)
        activity_level = st.selectbox("Activity Level", ["Sedentary", "Lightly active", "Moderately active", "Very active", "Extremely active"])

        # Calculate BMI
        bmi = weight / ((height/100) ** 2)
        st.write(f"Your BMI is: {bmi:.2f}")

        # BMI Classification
        bmi_data = pd.DataFrame({
            'Category': ['Underweight', 'Normal weight', 'Overweight', 'Obesity'],
            'BMI Range': ['< 18.5', '18.5 - 24.9', '25.0 - 29.9', '≥ 30.0'],
            'Recommendation': ['Gain weight', 'Maintain normal weight', 'Lose weight', 'Lose weight significantly']
        })
        st.write("BMI Classification:")
        st.dataframe(bmi_data)

        # BMI Chart
        st.bar_chart(bmi_data.set_index('Category')['BMI Range'])

elif page == "Mental Health":
     st.sidebar.subheader("Mental Health Subcategories")
     Mental_Health_Subcategories = [" ", "Stresslevel tracker ", "Mood tracker", "Sleep tracker"]
     selected_subcategory = st.sidebar.selectbox("Choose a tracker", Mental_Health_Subcategories)
  
     if selected_subcategory == " ":
        st.write(" ")

     elif selected_subcategory == "Stresslevel tracker ":
            st.write("Track your Stresslevels")
            stress_level = st.slider("Stress Level", 0, 10, 5)

     elif selected_subcategory == "Mood tracker":
            st.write("Track your mood")
            mood_level = st.slider("Mood Level", 0, 10, 5)

     elif selected_subcategory == "Sleep tracker":
            st.write("track your sleeping hours")
            sleep_hours = st.slider("Hours of Sleep", 0, 24, 8)

elif page == "Food & Recipes":
    st.title("Food & Recipes")

# Footer
st.sidebar.markdown("---")
st.sidebar.subheader("About Us")
st.sidebar.info("This app was developed by Julia and Cherilyn.")

st.sidebar.subheader("Contact")
st.sidebar.text("For questions or suggestions, contact us at:")
st.sidebar.text("fitmindbyjc@gmail.com")
