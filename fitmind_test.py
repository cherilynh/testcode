import streamlit as st
import pandas as pd
import numpy as np
from datetime import datetime
import matplotlib.pyplot as plt
import random
import json
import os
import hashlib
from github_contents import GithubContents
import streamlit_authenticator as stauth
import api_calls 

# Pfad zur Datei, in der Benutzerdaten gespeichert werden
USER_DATA_FILE = 'user_data.json'

# Funktion zum Laden von Benutzerdaten
def load_user_data():
    if os.path.exists(USER_DATA_FILE):
        with open(USER_DATA_FILE, 'r') as file:
            return json.load(file)
    return {}

# Funktion zum Speichern von Benutzerdaten
def save_user_data(user_data):
    with open(USER_DATA_FILE, 'w') as file:
        json.dump(user_data, file)

# Funktion zum Hashen von Passwörtern
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

# Funktion zum Überprüfen der Anmeldedaten
def authenticate(username, password):
    user_data = load_user_data()
    if username in user_data and user_data[username] == hash_password(password):
        return True
    return False

# Funktion zur Registrierung eines neuen Benutzers
def register_user(username, password):
    user_data = load_user_data()
    if username in user_data:
        return False
    user_data[username] = hash_password(password)
    save_user_data(user_data)
    return True

# Funktion zur Anzeige der Login-Seite
def show_login_page():
    st.subheader("Login")
    username = st.text_input("Benutzername", key="login_username")
    password = st.text_input("Passwort", type='password', key="login_password")
    if st.button("Login", key="login_button"):
        if authenticate(username, password):
            st.success("Erfolgreich eingeloggt!")
            st.session_state['logged_in'] = True
            st.session_state['username'] = username
        else:
            st.error("Falscher Benutzername oder Passwort.")
    if st.button("Zur Registrierungsseite", key="go_to_register"):
        st.session_state['show_registration'] = True

# Funktion zur Anzeige der Registrierungsseite
def show_registration_page():
    st.subheader("Registrieren")
    new_username = st.text_input("Neuer Benutzername", key="register_username")
    new_password = st.text_input("Neues Passwort", type='password', key="register_password")
    confirm_password = st.text_input("Passwort bestätigen", type='password', key="confirm_password")
    if st.button("Registrieren", key="register_button"):
        if new_password != confirm_password:
            st.error("Passwörter stimmen nicht überein.")
        elif register_user(new_username, new_password):
            st.success("Erfolgreich registriert!")
            st.session_state['logged_in'] = True
            st.session_state['username'] = new_username
        else:
            st.error("Benutzername bereits vergeben.")
    if st.button("Zurück zum Login", key="go_to_login"):
        st.session_state['show_registration'] = False


def main():
    st.title("Login und Registrierung")

    # Auswahlbox für Login oder Registrierung
    choice = st.sidebar.selectbox("Wählen Sie eine Option", ["Login", "Registrieren"])

    # Initialisierungsstatus für Login
    login_status = False

    # Login-Formular
    if choice == "Login":
        st.subheader("Login")
        username = st.text_input("Benutzername")
        password = st.text_input("Passwort", type='password')
        if st.button("Login"):
            if authenticate(username, password):
                st.success("Erfolgreich eingeloggt!")
                st.session_state['logged_in'] = True
                st.session_state['username'] = username
            else:
                st.error("Falscher Benutzername oder Passwort.")

    # Registrierungs-Formular
    elif choice == "Registrieren":
        st.subheader("Registrieren")
        new_username = st.text_input("Neuer Benutzername")
        new_password = st.text_input("Neues Passwort", type='password')
        confirm_password = st.text_input("Passwort bestätigen", type='password')
        if st.button("Registrieren"):
            if new_password != confirm_password:
                st.error("Passwörter stimmen nicht überein.")
            elif register_user(new_username, new_password):
                st.success("Erfolgreich registriert!")
                st.session_state['logged_in'] = True
                st.session_state['username'] = new_username
            else:
                st.error("Benutzername bereits vergeben.")

    # Prüfen, ob der Benutzer eingeloggt ist
    if st.session_state.get('logged_in'):
        st.subheader(f"Willkommen, {st.session_state['username']}!")
        # Hier kannst du den Hauptinhalt der App anzeigen
        st.write("Hier ist der Hauptinhalt der Anwendung.")
    else:
        st.warning("Bitte melden Sie sich an oder registrieren Sie sich, um fortzufahren.")

# Pfad zur JSON-Datei
file_path = 'exercises.json'

def show_exercises_by_category(file_path, category):
    # Öffnen und Lesen der JSON-Datei
    with open(file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)

    # Filtern der Übungen basierend auf der Kategorie
    exercises = data['exercises'].get(category, [])

    # Überprüfen, ob Übungen gefunden wurden
    if not exercises:
        st.write(f"No exercises found in the '{category}' category.")
        return
    
    # Anzeigen der gefilterten Übungen
    for exercise in exercises:
        st.subheader(exercise['name'])
        with st.expander(":information_source: Read Instructions"):
            instructions = exercise['instructions']
            if isinstance(instructions, list):
                for instruction in instructions:
                    st.write(instruction)
            else:
                st.write(instructions)
                
        if exercise['video']:
            with st.expander(":video_camera: Watch Video"):
                st.video(exercise['video'])
                st.write(f"Video Source: {exercise['video']}")
        st.divider()

def show_main_page():
    st.sidebar.header("Menu")
    page = st.sidebar.radio("Choose what you need",["FitMind - Introduction", "Fitness", "Mental Health"])

    if page == "FitMind - Introduction":
        st.title("Welcome to FitMind!")
        st.markdown("""
        FitMind is a health app that combines fitness and mental wellbeing to help users lead a balanced and healthy life.
        """)
        st.write("FitMind helps you to achieve your fitness goals and improve your mental well-being at the same time.")

    elif page == "Fitness":
        st.title("Fitness")
        st.subheader("Choose your level")
        st.subheader(":green[Beginners]")
        st.write(":green-background[If you're new to exercise or a particular exercise, start with 1 to 2 sets with 10 repetitions per exercise. Focus on learning proper form and gradually increasing the number of sets as you become more comfortable with the movements.]")
        st.subheader(":orange[Intermediate]")
        st.write(":orange-background[Intermediate: For those who have been exercising regularly and have some experience with the exercises, aim for 3 to 4 sets with 10 repetitions per exercise. This provides enough volume to challenge your muscles and promote strength and muscle growth.]")
        st.subheader(":red[Advanced]")
        st.write(":red-background[Advanced individuals who are looking to increase muscle size or strength may benefit from performing 4 to 5 sets with 10 repetitions per exercise. Higher volume workouts can help stimulate muscle hypertrophy and strength gains.]")
    
        st.divider()

        st.subheader("Gear Requirements")
        st.write("This app was designed so that people who are new to sports can start their workouts without any gym equipment. Of course, people who want a more intensive workout can use their dumbbells, resistance bands and other equipment for their workouts")

        st.divider()
        
        st.sidebar.subheader("Workouts")
            
        Workouts = [" ", "Arms", "Back", "Core", "Glutes", "Legs"]
        selected_subcategory = st.sidebar.selectbox("Choose a specific area", Workouts)
                    
        if selected_subcategory == " ":
            st.subheader(" ")
            st.write(" ")
            
        elif selected_subcategory == "Arms":
            st.subheader("Arm Training")
            col1, col2 = st.columns(2)
            with col1:
                st.subheader("Benefits")
                st.write("Arm training increases muscle strength, improves functional performance in daily tasks, and enhances athletic performance. Additionally, it improves aesthetics by toning muscles and helps prevent injuries by supporting joints, tendons, and ligaments.")
        
            with col2:
                st.subheader("used Muscles")
                st.image("arm-muscle.jpeg")
                st.write("Image Source: https://media.geeksforgeeks.org/wp-content/uploads/20240328112244/Diagram-of-arm-muscle.png")
                st.divider()
            
            category = 'Arms'
            show_exercises_by_category(file_path, category)      
        
        elif selected_subcategory == "Back":
            st.subheader("Back Training")
            col1, col2 = st.columns(2)
            with col1:
                st.subheader("Benefits")
                st.write("Back training improves posture, reducing the risk of back pain and injuries. It enhances functional strength for daily activities and sports, promoting overall physical performance. Additionally, a strong back contributes to a balanced physique and better core stability.")
        
            with col2:
                st.subheader("used Muscles")
                st.image("Rückenmuskulatur.jpeg")
                st.write("Image Source: https://samarpanphysioclinic.com/muscles-of-the-back/")
                st.divider()
            
            category = 'Back'
            show_exercises_by_category(file_path, category)
        
        elif selected_subcategory == "Core":
            st.subheader("Core Training")
            col1, col2 = st.columns(2)
            with col1:
                st.subheader("Benefits")
                st.write("Core training offers benefits like including improved stability, better posture, relief from back pain, increased power, improved breathing efficiency and appearance with a stronger, more defined midsection.")
        
            with col2:
                st.subheader("used Muscles")
                st.image("Muscles-wall.jpeg")
                st.write("Image source: https://cdn.britannica.com/13/125813-050-BB16AC7C/Muscles-wall.jpg")
                st.divider()
            
            category = 'Core'
            show_exercises_by_category(file_path, category)
            
            
        elif selected_subcategory == "Glutes":
            st.subheader("Glute Training")
            col1, col2 = st.columns(2)
            with col1:
                st.subheader("Benefits")
                st.write("Glute exercises, are beneficial for several reason: they strenghten the glutes, improve posture and enhance athletic performances. They also enhance and shape your body to your liking.")
            
            with col2:
                st.subheader("Used Muscles")
                st.image("glutes_muscles_480x480.jpeg")
                st.write("Image source: https://asitisnutrition.com/blogs/health/7-exercises-to-achieve-strong-butt-improve-your-posture")
                st.divider()

            category = 'Glutes'
            show_exercises_by_category(file_path, category)
            
        elif selected_subcategory == "Legs":
            st.subheader("Leg Training")
            col1, col2 = st.columns(2)
            with col1:
                st.subheader("Benefits")
                st.write("leg exercises offer benefits like increased muscle strength, better Bone Health, improved cardiovascular health and reduce the risk of chronic diseases")
                
            with col2:
                st.subheader("used Muscles")
                st.image("beinmuskeln.jpg")
                st.write("Image source: https://www.muskelpower.de/beinmuskeln/")
                st.divider()

            category = 'Legs'
            show_exercises_by_category(file_path, category)

    
        st.sidebar.subheader("Randomized workout")
        second_subcategory = st.sidebar.selectbox("Choose a randomized workout", ["  ", "Arms", "Back", "Core", "Glutes", "Legs", "Lower Body", "Upper Body", "Full Body"])
        
        if second_subcategory == " ":
            st.subheader(" ")
            st.write(" ")

        
        elif second_subcategory == "Arms":
            arms_fitness_übungen = [
                "Arm Circles",
                "Bicep Curls",
                "Chair Dips",
                "Isometric Bicep Hold",
                "Plank Shoulder Taps",
                "Reverse Plank",
                "Walking Plank",
                "Push-Ups",
                "Diamond Push-Ups",
                "Decline Push-Ups",
                "Incline Push-Ups",
                "Plank to Push-Ups",
                "Wall Push-Ups"
            ]

            st.subheader("Randomized Arm Workout")

            tab1, tab2, tab3 = st.tabs([":green-background[Beginner]", ":orange-background[Intermediate]", ":red-background[Advanced]"])

            with tab1:
                st.header(":green[Beginner Training]")
                st.write("Here are 5 randomized exercises for your arms. Do 1-2 sets with each 10 repetitions. Take a break of 60 Seconds in between the exercises.")
                zufällige_übungen_beginner = random.sample(arms_fitness_übungen, 5)
                for übung in zufällige_übungen_beginner:
                    st.write(übung)
                
            with tab2:
                st.header(":orange[Intermediate Training]")
                st.write("Here are 8 randomized exercises for your arms. Do 3-4 sets with each 10 repetitions. Take a break of 45 Seconds in between the exercises.")
                zufällige_übungen_intermediate = random.sample(arms_fitness_übungen, 8)
                for übung in zufällige_übungen_intermediate:
                    st.write(übung)
            
            with tab3:
                st.header(":red[Advanced Training]")
                st.write("Here are 11 randomized exercises for your arms. Do 4-5 sets with each 10 repetitions. Take a break of 30 Seconds in between the exercises.")
                zufällige_übungen_advanced = random.sample(arms_fitness_übungen, 11)
                for übung in zufällige_übungen_advanced:
                    st.write(übung)
                

        elif second_subcategory == "Back":

            back_fitness_übungen = [
                "Bird Dogs",
                "Cat Camel Stretch",
                "Cobra Pose",
                "Dive Bomber",
                "Prone T Raises",
                "Prone W Raises",
                "Prone Y Raises",
                "Reverse Snow Angels",
                "Seated Forward Folds",
                "Supermans",
                "Swimmers"
            ]
            
            st.subheader("Randomized Back Workout")

            tab1, tab2, tab3 = st.tabs([":green-background[Beginner]", ":orange-background[Intermediate]", ":red-background[Advanced]"])

            with tab1:
                st.header(":green[Beginner Training]")
                st.write("Here are 5 randomized exercises for your back. Do 1-2 sets with each 10 repetitions. Take a break of 60 Seconds in between the exercises.")
                zufällige_übungen_beginner = random.sample(back_fitness_übungen, 5)
                for übung in zufällige_übungen_beginner:
                    st.write(übung)
            
            with tab2:
                st.header(":orange[Intermediate Training]")
                st.write("Here are 8 randomized exercises for your back. Do 3-4 sets with each 10 repetitions. Take a break of 45 Seconds in between the exercises.")
                zufällige_übungen_intermediate = random.sample(back_fitness_übungen, 8)
                for übung in zufällige_übungen_intermediate:
                    st.write(übung)
                
            with tab3:
                st.header(":red[Advanced Training]")
                st.write("Here are 11 randomized exercises for your back. Do 4-5 sets with each 10 repetitions. Take a break of 30 Seconds in between the exercises.")
                zufällige_übungen_advanced = random.sample(back_fitness_übungen, 11)
                for übung in zufällige_übungen_advanced:
                    st.write(übung)
            
        elif second_subcategory == "Core":
            core_fitness_übungen = [
                "Bicycle Crunches",
                "Boat pose",
                "Crunches",
                "Flutter Kicks",
                "Lying Leg Raises",
                "Mountain Climbers",
                "Plank for 30 Seconds",
                "Reverse Crunches",
                "Russian Twists",
                "Scissor Kicks",
                "Seated Knee Tucks",
                "Side Planks",
                "Sit-ups",
                "Standing Oblique Crunches",
                "Toe Touches",
                "V-ups"
            ]
            
            st.subheader("Randomized Core Workout")

            tab1, tab2, tab3 = st.tabs([":green-background[Beginner]", ":orange-background[Intermediate]", ":red-background[Advanced]"])

            with tab1:
                st.header(":green[Beginner Training]")
                st.write("Here are 5 randomized exercises for your core. Do 1-2 sets with each 10 repetitions. Take a break of 60 Seconds in between the exercises.")
                zufällige_übungen_beginner = random.sample(core_fitness_übungen, 5)
                for übung in zufällige_übungen_beginner:
                    st.write(übung)

            with tab2:
                st.header(":orange[Intermediate Training]")
                st.write("Here are 8 randomized exercises for your core. Do 3-4 sets with each 10 repetitions. Take a break of 45 Seconds in between the exercises.")
                zufällige_übungen_intermediate = random.sample(core_fitness_übungen, 8)
                for übung in zufällige_übungen_intermediate:
                    st.write(übung)
            
            with tab3:
                st.header(":red[Advanced Training]")
                st.write("Here are 11 randomized exercises for your core. Do 4-5 sets with each 10 repetitions. Take a break of 30 Seconds in between the exercises.")
                zufällige_übungen_advanced = random.sample(core_fitness_übungen, 11)
                for übung in zufällige_übungen_advanced:
                    st.write(übung)

        elif second_subcategory == "Glutes":
            glutes_fitness_übungen = [
                "Bridge for 30 seconds",
                "Clamshells",
                "Donkey Kicks",
                "Fire Hydrants",
                "Hip Thrusts",
                "Lunges",
                "Reverse Lunges",
                "Lateral Lunges",
                "Walking Lunges",
                "Quadruped Leg Raises",
                "Quadruped Hip Extensions",
                "Side Leg Raises",
                "Single-Leg Glute Bridges",
                "Standard Squats",
                "Bulgarian Split Squats",
                "Sumo Squats",
                "Plie Squats",
                "Standing Kickbacks",
                "Wall Sit",
                "Wall Sit With Leg Lifts"
            ]

            st.subheader("Randomized Glutes Workout")

            tab1, tab2, tab3 = st.tabs([":green-background[Beginner]", ":orange-background[Intermediate]", ":red-background[Advanced]"])

            with tab1:
                st.header(":green[Beginner Training]")
                st.write("Here are 5 randomized exercises for your glutes. Do 1-2 sets with each 10 repetitions. Take a break of 60 Seconds in between the exercises.")
                zufällige_übungen_beginner = random.sample(glutes_fitness_übungen, 5)
                for übung in zufällige_übungen_beginner:
                    st.write(übung)
            with tab2:
                st.header(":orange[Intermediate Training]")
                st.write("Here are 8 randomized exercises for your glutes. Do 3-4 sets with each 10 repetitions. Take a break of 45 Seconds in between the exercises.")
                zufällige_übungen_intermediate = random.sample(glutes_fitness_übungen, 8)
                for übung in zufällige_übungen_intermediate:
                    st.write(übung)

            with tab3:
                st.header(":red[Advanced Training]")
                st.write("Here are 11 randomized exercises for your glutes. Do 4-5 sets with each 10 repetitions. Take a break of 30 Seconds in between the exercises.")
                zufällige_übungen_advanced = random.sample(glutes_fitness_übungen, 11)
                for übung in zufällige_übungen_advanced:
                    st.write(übung)


        elif second_subcategory == "Legs":
            st.subheader("Randomized Leg Workout")
            legs_fitness_übungen = [
                "Butt Kicks",
                "Flutter Kicks",
                "Half Squat walk",
                "High Kicks",
                "30 Jumping Jacks",
                "Knee Side Leg Lifts",
                "Lateral Hops",
                "Lying Leg Circles",
                "Marching Hip Raises",
                "Pulsing Side Lying Leg Raises",
                "Rainbow Leg Lifts",
                "Side Knee Raises",
                "Side Lying Bottom Leg Lifts",
                "Side Lying Leg Lifts",
                "Single Leg V-Ups",
                "Walking High Knees",
            ]
                    
            tab1, tab2, tab3 = st.tabs([":green-background[Beginner]", ":orange-background[Intermediate]", ":red-background[Advanced]"])

            with tab1:
                st.header(":green[Beginner Training]")
                st.write("Here are 5 randomized exercises for your legs. Do 1-2 sets with each 10 repetitions. Take a break of 60 Seconds in between the exercises.")
                zufällige_übungen_beginner = random.sample(legs_fitness_übungen, 5)
                for übung in zufällige_übungen_beginner:
                    st.write(übung)
            
            with tab2:
                st.header(":orange[Intermediate Training]")
                st.write("Here are 8 randomized exercises for your legs. Do 3-4 sets with each 10 repetitions. Take a break of 45 Seconds in between the exercises.")
                zufällige_übungen_intermediate = random.sample(legs_fitness_übungen, 8)
                for übung in zufällige_übungen_intermediate:
                    st.write(übung)
                    
            with tab3:
                st.header(":red[Advanced Training]")
                st.write("Here are 11 randomized exercises for your legs. Do 4-5 sets with each 10 repetitions. Take a break of 30 Seconds in between the exercises.")
                zufällige_übungen_advanced = random.sample(legs_fitness_übungen, 11)
                for übung in zufällige_übungen_advanced:
                    st.write(übung)

        elif second_subcategory == "Lower Body":
            st.subheader("Randomized Lower Body Workout")
            st.write("This randomized lower body workout contains exercises for your legs and glutes.")
            Lower_Body_fitness_übungen = [
                "Alternating Stance Jumps",
                "Boxer Shuffle",
                "Butt Kicks",
                "Flutter Kicks",
                "Half Squat walk",
                "High Kicks",
                "30 Jumping Jacks",
                "Knee Side Leg Lifts",
                "Lateral Hops",
                "Lying Leg Circles",
                "Marching Hip Raises",
                "Pulsing Side Lying Leg Raises",
                "Rainbow Leg Lifts",
                "Side And Cross Crunches",
                "Side Knee Raises",
                "Side Lying Bottom Leg Lifts",
                "Side Lying Leg Raises",
                "Single Leg V-Ups",
                "Straight Leg Circles",
                "Walking High Knees",
                "Bridge for 30 seconds",
                "Clamshells",
                "Donkey Kicks",
                "Donkey Kicks",
                "Fire Hydrants",
                "Glute Bridges",
                "Hip Thrusts",
                "Forward Lunges",
                "Reverse Lunges",
                "Lateral Lunges",
                "Walking Lunges",
                "Quadruped Leg Lifts",
                "Quadruped Hip Extensions",
                "Side Leg Raises",
                "Single-Leg Glute Bridges",
                "Standard Squats",
                "Bulgarian Split Squats",
                "Sumo Squats",
                "Plie Squats",
                "Standing Leg Abduction",
                "Standing Kickbacks",
                "Wall Sit"
            ]

            tab1, tab2, tab3 = st.tabs([":green-background[Beginner]", ":orange-background[Intermediate]", ":red-background[Advanced]"])

            with tab1:
                st.header(":green[Beginner Training]")
                st.write("Here are 5 randomized exercises for your lower body. Do 1-2 sets with each 10 repetitions. Take a break of 60 Seconds in between the exercises.")
                zufällige_übungen_beginner = random.sample(Lower_Body_fitness_übungen, 5)
                for übung in zufällige_übungen_beginner:
                    st.write(übung)
            
            with tab2:
                st.header(":orange[Intermediate Training]")
                st.write("Here are 8 randomized exercises for your lower body. Do 3-4 sets with each 10 repetitions. Take a break of 45 Seconds in between the exercises.")
                zufällige_übungen_beginner = random.sample(Lower_Body_fitness_übungen, 8)
                for übung in zufällige_übungen_beginner:
                    st.write(übung)
            
            with tab3:
                st.header(":red[Advanced Training]")
                st.write("Here are 11 randomized exercises for your lower body. Do 5-6 sets with each 10 repetitions. Take a break of 30 Seconds in between the exercises.")
                zufällige_übungen_beginner = random.sample(Lower_Body_fitness_übungen, 11)
                for übung in zufällige_übungen_beginner:
                    st.write(übung)
                    
        elif second_subcategory == "Upper Body":
            Upper_Body_fitness_übungen = [
                "Arm Circles",
                "Bicep Curls",
                "Chair Dips",
                "Isometric Dips",
                "Plank Shoulder Taps",
                "Reverse Plank",
                "Walking Plank",
                "Push-Ups",
                "Diamond Push-Ups",
                "Decline Push-Ups",
                "Incline Push-Ups",
                "Plank to Push-Ups",
                "Wall Push-Ups",
                "Bird Dogs",
                "Cat Camel Stretch",
                "Cobra Pose",
                "Dive Bombers",
                "Prone T Raises",
                "Prone W Raises",
                "Prone Y Raises",
                "Reverse Snow Angels",
                "Seated Forward Folds",
                "Supermans",
                "Swimmers",
                "Boat pose",
                "Crunches",
                "Bicycle Crunches",
                "Reverse Crunches",
                "Standing Oblique Crunches",
                "Flutter Kicks",
                "Lying Leg Raises",
                "Mountain Climbers",
                "Planks",
                "Side Planks",
                "Russian Twists",
                "Scissor Kicks",
                "Seated Knee Tucks",
                "Sit-ups",
                "Toe Touches",
                "V-ups"

            ]
            st.subheader("Randomized Upper Body Workout")
            st.write("This randomized lower body workout contains exercises for your arms, back and core.")


            tab1, tab2, tab3 = st.tabs([":green-background[Beginner]", ":orange-background[Intermediate]", ":red-background[Advanced]"])

            with tab1:
                st.header(":green[Beginner Training]")
                st.write("Here are 5 randomized exercises for your upper body. Do 1-2 sets with each 10 repetitions. Take a break of 60 Seconds in between the exercises.")
                zufällige_übungen_beginner = random.sample(Upper_Body_fitness_übungen, 5)
                for übung in zufällige_übungen_beginner:
                    st.write(übung)        
            with tab2:
                st.header(":orange[Intermediate Training]")
                st.write("Here are 8 randomized exercises for your upper body. Do 3-4 sets with each 10 repetitions. Take a break of 45 Seconds in between the exercises.")
                zufällige_übungen_beginner = random.sample(Upper_Body_fitness_übungen, 8)
                for übung in zufällige_übungen_beginner:
                    st.write(übung)
            
            with tab3:
                st.header(":red[Advanced Training]")
                st.write("Here are 11 randomized exercises for your upper body. Do 5-6 sets with each 10 repetitions. Take a break of 30 Seconds in between the exercises.")
                zufällige_übungen_beginner = random.sample(Upper_Body_fitness_übungen, 11)
                for übung in zufällige_übungen_beginner:
                    st.write(übung)

        elif second_subcategory == "Full Body":
            st.subheader("Randomized Full Body Workout")
            st.write("This randomized lower body workout contains exercises for your arms, back, core, glutes and legs.")
            Full_Body_fitness_übungen = [
                "Arm Circles",
                "Bicep Curls",
                "Chair Dips",
                "Isometric Dips",
                "Plank Shoulder Taps",
                "Reverse Plank",
                "Walking Plank",
                "Push-Ups",
                "Diamond Push-Ups",
                "Decline Push-Ups",
                "Incline Push-Ups",
                "Plank to Push-Ups",
                "Wall Push-Ups",
                "Bird Dogs",
                "Cat Camel Stretch",
                "Cobra Pose",
                "Dive Bombers",
                "Prone T Raises",
                "Prone W Raises",
                "Prone Y Raises",
                "Reverse Snow Angels",
                "Seated Forward Folds",
                "Supermans",
                "Swimmers",
                "Boat pose",
                "Crunches",
                "Bicycle Crunches",
                "Reverse Crunches",
                "Standing Oblique Crunches",
                "Flutter Kicks",
                "Lying Leg Raises",
                "Mountain Climbers",
                "Planks",
                "Side Planks",
                "Russian Twists",
                "Scissor Kicks",
                "Seated Knee Tucks",
                "Sit-ups",
                "Toe Touches",
                "V-ups",
                "Bridge",
                "Bulgarian Split Squats",
                "Clamshells",
                "Donkey Kicks",
                "Fire Hydrants",
                "Hip Thrusts",
                "Lateral Lunges",
                "Lunges",
                "Plie Squats",
                "Quadruped Hip Extensions",
                "Quadruped Leg Raise",
                "Reverse Lunges",
                "Side Leg Raises",
                "Single-Leg Glute Bridges",
                "Squats",
                "Standing Kickbacks",
                "Sumo Squats",
                "Walking Lunges",
                "Wall Sit",
                "Wall Sit with Leg Lifts"
                "Butt Kicks",
                "Flutter Kicks",
                "Half Squat Walk",
                "High Kicks",
                "Jumping Jack",
                "Knee Side Leg Lifts",
                "Lateral Hops",
                "Lying Leg Circles",
                "Marching Hip Raises",
                "Pulsing Side Lying Leg Raises",
                "Rainbow Leg Lifts",
                "Standing Knee Raises",
                "Side Lying Leg Lifts",
                "Single Leg V-Ups",
                "Walking High Knees"


            ]

            tab1, tab2, tab3 = st.tabs([":green-background[Beginner]", ":orange-background[Intermediate]", ":red-background[Advanced]"])

            with tab1:
                st.header(":green[Beginner Training]")
                st.write("Here are 5 randomized exercises for your whole body. Do 1-2 sets with each 10 repetitions. Take a break of 60 Seconds in between the exercises.")
                zufällige_übungen_beginner = random.sample(Full_Body_fitness_übungen, 5)
                for übung in zufällige_übungen_beginner:
                    st.write(übung)         
            with tab2:
                st.header(":orange[Intermediate Training]")
                st.write("Here are 8 randomized exercises for your whole body. Do 3-4 sets with each 10 repetitions. Take a break of 45 Seconds in between the exercises.")
                zufällige_übungen_beginner = random.sample(Full_Body_fitness_übungen, 8)
                for übung in zufällige_übungen_beginner:
                    st.write(übung)        
            with tab3:
                st.header(":red[Advanced Training]")
                st.write("Here are 11 randomized exercises for your whole body. Do 5-6 sets with each 10 repetitions. Take a break of 30 Seconds in between the exercises.")
                zufällige_übungen_beginner = random.sample(Full_Body_fitness_übungen, 11)
                for übung in zufällige_übungen_beginner:
                    st.write(übung)   

        st.sidebar.subheader("Fitness Tracker")
        third_subcategory = st.sidebar.selectbox("Choose a Fitness Tracker", ["  ", "water intake", "BMI-Calculator"])
        
        if third_subcategory == " ":
            st.write(" ")
            
        elif third_subcategory == "water intake":
            st.subheader(":blue[Track your water intake] :droplet:")
            st.write("Track your water intake. A glass has about 250ml of water in it. Aim to drink around 2.5 liters of water per day.")
            if "water_intake" not in st.session_state:
                st.session_state.water_intake = 0
            
            # Display the water emoji
            water_emoji = "💧"
            st.write("if you drank a glass of water, press the button below! :droplet:")
            
            # Add a button to increment the water intake counter when clicked
            if st.button(":blue[Drink a glass of water] :droplet:"):
                st.session_state.water_intake += 1
                st.write("You drank a glass of water! :droplet:")
                st.write("Total glasses of water drank today:", st.session_state.water_intake)

                
        elif third_subcategory == "BMI-Calculator":
            st.subheader("BMI-Calculator")
            st.write("Calculate your Body Mass Index here")

            # Input Widgets
            age = st.slider("Alter", 18, 100, 25)
            weight = st.number_input("Gewicht (kg)", min_value=20.0, max_value=500.0, value=70.0, step=0.1)
            height = st.number_input("Größe (cm)", min_value=100, max_value=300, value=170, step=1)
            activity_level = st.selectbox("Aktivitätslevel", ["nicht aktiv", "Leicht aktiv", "Mäßig aktiv", "Sehr aktiv", "Extrem aktiv"])
        
            # Data elements
            bmi = weight / ((height/100) ** 2)
            st.write(f"Ihr BMI beträgt: {bmi:.2f}")
        
            # Chart elements
            data = pd.DataFrame({
                'Kategorie': ['Untergewicht', 'Normalgewicht', 'Übergewicht', 'Adipositas'],
                'BMI-Bereich': ['< 18.5', '18.5 - 24.9', '25.0 - 29.9', '≥ 30.0'],
                'Empfehlung': ['Zunehmen', 'Normalgewicht halten', 'Abnehmen', 'Stark abnehmen']
            })
            st.write("BMI-Klassifikation:")
            st.dataframe(data)



    elif page == "Mental Health":
        st.sidebar.subheader("Mental Health Subcategories")
        Mental_Health_Subcategories = [" ", "Stress & Mood Tracker", "Sleep tracker", "Supplements"]
        selected_subcategory = st.sidebar.selectbox("Choose a tracker", Mental_Health_Subcategories)
    
        if selected_subcategory == " ":
            st.write(" ")
        
        elif selected_subcategory == "Stress & Mood Tracker":
            st.subheader("Track your stress ")
            st.write('Enter your stress level for each day.')
            # Text elements
            st.write("How is your mood today?")
            mood = st.slider("Stimmung", 0, 10, 5)
            # Input Widgets

            st.write("How stressed have you been today")
            stress_level = st.slider("Stresslevel", 0, 10, 5)
        
            # Chart elements
            mood_data = pd.DataFrame({
                'Datum': pd.date_range(start='2024-05-01', periods=10),
                'Stimmung': np.random.randint(0, 11, size=10),
                'Stresslevel': np.random.randint(0, 11, size=10)
            })
            st.write("Verlauf der Stimmung und des Stresslevels:")
            st.line_chart(mood_data.set_index('Datum'))
        
        elif selected_subcategory == "Sleep tracker":
            st.subheader("Track your sleep")
            st.write("Enter your sleep duration and quality for each day.")

            # Input Widgets
            sleep_quality = st.slider("Sleep Quality (0-10)", 0, 10, 5)
            sleep_duration = st.slider("Sleep Duration (Hours)", 0, 24, 8)

            # Save Button
            if st.button("Save"):
            # Hier kannst du den Code zum Speichern der Daten implementieren
                st.write("Sleep data saved successfully!")
            
            # Chart elements
            sleep_data = pd.DataFrame({
                'Date': pd.date_range(start='2024-05-01', periods=10),
                'Sleep Quality': np.random.randint(0, 11, size=10),
                'Sleep Duration': np.random.randint(0, 24, size=10)
            })

            st.write("Sleep Quality and Duration Trends:")
            st.line_chart(sleep_data.set_index('Date'))

        elif selected_subcategory == "Supplements":
            st.title("Supplements to support your mental health")
            st.subheader("Sleeplessness")
            st.write("Herbal preparations with valerian root and hop cones can support and regulate sleep. These medicinal plants, whose effects complement each other, help to calm the mind and improve sleep disorders. Valerian increases the urge to sleep and shortens the time it takes to fall asleep, similar to the body's own messenger substance adenosine. Hops regulate the cycle of sleep and wakefulness, similar to the hormone melatonin.")
            col1, col2 = st.columns(2)
            with col1:
                st.subheader("Zeller Schlaf Forte")
                st.write("Adults and adolescents from 12 years of age take 1 tablet per day, about 30min to 1h before planned bedtime")
        
            with col2:
                st.image("Zeller-Schlaf-Forte.png")
                st.write("Image Source: https://zellerag.ch/media/cnrnvuav/zell_zeller_schlaf_forte_30filmtabl_de.png?anchor=bottomcenter&mode=max&format=png&width=940&lazyload=true&lazyloadPixelated=true&height=705&preferFocalPoint=false&useCropDimensions=false&maxwidth=3200&maxheight=3200&c.focalPoint=0.5%2C0.5&c.finalmode=crop&c.zoom=false")
            st.divider()

            st.subheader("Nervousness")
            st.write("In cases of anxiety and inner restlessness, herbal medicine made from lavender oil supports the neuronal stimulus filter and helps to reduce nervousness.")
            col1, col2 = st.columns(2)
            
            with col1:
                st.subheader("Lasea")
                st.write("Lasea is taken once a day, preferably in the evening with a meal and a glass of still water. Lasea is for adults aged 18 and over and is available over the counter in pharmacies and drugstores.")
        
            with col2:
                st.image("Lasea.jpeg")
                st.write("https://www.lasea.ch/sites/g/files/oawcqg281/files/styles/landscape_extra_large/public/2023-02/lasea-lavendelol_0.jpg.webp?itok=NfKPykot")
            st.divider()
            
            st.subheader("Poor Concentration, Fatigue and Exhaustion")
            st.write("Vitango contains the standardized rose root extract WS 1375 of the highest quality. It is a herbal remedy used to relieve mental and physical symptoms of stress and overwork, such as irritability, tension, tiredness and fatigue. The dual action normalizes the release of stress hormones (adrenaline and cortisol) and at the same time increases the body's energy levels")
            col1, col2 = st.columns(2)
            with col1:
                st.subheader("Vitango")
                st.write("Adults over the age of 18 take 2 tablets a day, one before breakfast and one before lunch. The tablet should be taken with a glass of water.")
        
            with col2:
                st.image("vitango.jpeg")
                st.write("https://www.schwabepharma.ch/sites/g/files/oawcqg1436/files/styles/landscape_full/public/2022-04/vitango-stress-muedigkeit-packshot-deutsch.jpg.webp?itok=tIReNZPR")
            st.divider()
            
            st.subheader("Depressed Moods")
            st.write("Hyperiforce is a fresh plant preparation made from the fresh shoot tips of flowering St. John's wort (Hypericum perforatum). Hyperiforce is used for depressed mood, lack of drive, imbalance, mood instability and states of tension")
            col1, col2 = st.columns(2)
            with col1:
                st.subheader("A. Vogel Hyperiforce")
                st.write("The preparation should be taken for at least 14 days until it takes effect. At the start of treatment, take 1 tablet 3 times a day with meals and a little liquid. After 2 weeks, take 1 tablet twice a day. A treatment period of 4-6 weeks is recommended.")
        
            with col2:
                st.image("Hyperiforce.png")
                st.write("https://www.avogel-company.ch/img/client/av3-packshots-deutsch/2020_Hyperiforce_120T_CH_d.png?m=1608019976")
            st.divider()
            
    # Footer
    st.sidebar.markdown("---")
    st.sidebar.subheader("About us")
    st.sidebar.info("This app was developed by Julia and Cherilyn.")

    st.sidebar.subheader("Contact")
    st.sidebar.text("For questions or suggestions, contact us at")
    st.sidebar.text("fitmindbyjc@gmail.com")

def main():
    st.title("Willkommen zur Streamlit App")

    # Initialisierungsstatus für Login
    if 'logged_in' not in st.session_state:
        st.session_state['logged_in'] = False

    # Login-Seite anzeigen, wenn der Benutzer nicht eingeloggt ist
    if not st.session_state['logged_in']:
        show_login_page()
    else:
        show_main_page()

if __name__ == '__main__':
    main()

