import streamlit as st
import pandas as pd
import numpy as np
from datetime import datetime
import matplotlib.pyplot as plt
import random

def display_exercise_info(exercise_name, instructions, video_url):
    st.subheader(exercise_name)
    with st.expander(":information_source: Read Instructions"):
        for instruction in instructions:
            st.write(instruction)
    if video_url:
        with st.expander(":video_camera: Watch Video"):
            st.video(video_url)
            st.write(f"Video Source: {video_url}")
    st.divider()

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
    
    if page == "Fitness":
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

        st.subheader("Arm Circles")
        with st.expander(":information_source: Read Instructions"):
            st.write("1. Stand straight with your feet shoulder-width apart.")
            st.write("2. Raise and extend your arms to the sides without bending the elbows.")
            st.write("3. Slowly rotate your arms forward, making small circles of about 1 foot in diameter.")
            st.write("4. Complete a set in one direction and then switch, rotating backward.")
        with st.expander(":video_camera: Watch Video"):
            st.video('https://youtu.be/UVMEnIaY8aU')
            st.write("Video Source: https://youtu.be/UVMEnIaY8aU")
        st.divider()

        st.subheader("Bicep Curls")
        with st.expander(":information_source: Read Instructions"):
            st.write("1. Stand straight with a dumbbell or water bottles in each hand, your feet shoulder-width apart, and hands by your sides.")
            st.write("2. Squeeze the biceps and lift the dumbbells. Keep the elbows close to your body and the upper arms stationary, only the forearms should move.")
            st.write("3. Once the dumbbells are at shoulder level, slowly lower the arms to the starting position.")
            st.write("4. Repeat.")
        with st.expander(":video_camera: Watch Video"):
            st.video('https://youtu.be/TVflFTempWA?t=20')
            st.write("Video Source: https://youtu.be/TVflFTempWA?t=20")
        st.divider()

        st.subheader("Chair Dips")
        with st.expander(":information_source: Read Instructions"):
            st.write("1. Sit on the edge of a bench or chair, hands supporting your weight.")
            st.write("2. Position your feet away from the bench, legs straight and heels on the floor.")
            st.write("3. Lower yourself until your upper arms are parallel to the ground, then push back up.")
            st.write("4. Repeat exercise.")
        with st.expander(":video_camera: Watch Video"):
            st.video('https://youtu.be/HCf97NPYeGY')
            st.write("Video Source: https://youtu.be/HCf97NPYeGY")
        st.divider()

        st.subheader("Isometric Bicep Hold")
        with st.expander(":information_source: Read Instructions"):
            st.write("1. Hold dumbbells in each hand. If you do not have dumbbells, use full water bottles.")
            st.write("2. Keep your elbows close to your torso and your palms facing up. Keeping your upper body stationary, bring the weights to a 90 degrees hold.")
            st.write("3. Hold for a minimum of 5 seconds or other given time.")
        with st.expander(":video_camera: Watch Video"):
            st.video('https://youtu.be/0GYXknAKa8g')
            st.write("Video Source: https://youtu.be/0GYXknAKa8g")
        st.divider()

        st.subheader("Plank Shoulder Taps")
        with st.expander(":information_source: Read Instructions"):
            st.write("1. Start in a plank position, with your wrists under your shoulders and your feet hip-width apart.")
            st.write("2. Touch your left shoulder with your right hand and return to plank position.")
            st.write("3. Touch your right shoulder with your left hand and continue alternating sides until the set is complete.")
        with st.expander(":video_camera: Watch Video"):
            st.video('https://youtu.be/8rgurWd-PB8')
            st.write("Video Source: https://youtu.be/8rgurWd-PB8")
        st.divider()

        st.subheader("Reverse Plank")
        with st.expander(":information_source: Read Instructions"):
            st.write("1. Press into your palms and lift your hips and torso toward the ceiling. Look up to the ceiling during this move.")
            st.write("2. Squeeze your core and pull your belly button back toward your spine.")
            st.write("3. Lower your hips and torso back to the floor, returning to the starting position.")
        with st.expander(":video_camera: Watch Video"):
            st.video('https://youtu.be/v2pPWNSDorE')
            st.write("Video Source: https://youtu.be/v2pPWNSDorE")
        st.divider()
        
        st.subheader("Walking Plank")
        with st.expander(":information_source: Read Instructions"):
            st.write("1. Get into a forearm plank with your shoulders in line with your elbows and forearms parallel to each other on the ground.")
            st.write("2. Pushing the ground with your right hand, straighten your right arm into a high plank, followed by your left arm.") 
            st.write("3. Then, bring your right forearm back to the ground and then your left forearm.")
            st.write("4. Repeat exercise.")
        with st.expander(":video_camera: Watch Video"):
            st.video('https://youtu.be/0EePC0_n6J4')
            st.write("Video Source: https://youtu.be/0EePC0_n6J4")
        st.divider()

        st.subheader("Push-Ups")
        with st.expander(":information_source: Read Instructions"):
            st.write("1. With your legs extended back, place the hands below the shoulders, slightly wider than shoulder-width apart.")
            st.write("2. Start bending your elbows and lower your chest until it’s just above the floor.")
            st.write("3. Push back to the starting position.")
            st.write("4. Repeat exercise.")
        with st.expander(":video_camera: Watch Video"):
            st.video('https://youtu.be/NE96m3TvI2o')
            st.write("Video Source: https://youtu.be/NE96m3TvI2o")
        st.divider()

        st.subheader("Diamond Push-Ups")
        with st.expander(":information_source: Read Instructions"):
            st.write("1. Get into a standard push-up position. Except this time move your hands together so that your thumbs are touching together and your index fingers are touching together, forming a diamond shape in the open area between your hands.")
            st.write("2. Next, lower yourself down to the ground so that your chest almost touches your hands, pause, then push yourself back up.")
            st.write("3. Repeat exercise.")
        with st.expander(":video_camera: Watch Video"):
            st.video('https://youtu.be/XtU2VQVuLYs')
            st.write("Video Source: https://youtu.be/XtU2VQVuLYs")
        st.divider()

        st.subheader("Decline Push-Ups")
        with st.expander(":information_source: Read Instructions"):
            st.write("1. Place a bench or chair horizontally behind you and place both hands on a yoga mat slightly wider than shoulder-width with your feet together on the bench behind you, resting on the balls of your feet.")
            st.write("2. While maintaining a straight back and stabilising through your abdominals, bend your elbows and lower your torso towards the floor until your arms form two 90-degree angles.")
            st.write("3. Push through your chest and extend your arms to lift your body back into starting position.")
            st.write("Repeat exercise.")
        with st.expander(":video_camera: Watch Video"):
            st.video('https://youtu.be/QBlYp-EwHlo')
            st.write("Video Source: https://youtu.be/QBlYp-EwHlo")
        st.divider()

        st.subheader("Incline Push-Ups")
        with st.expander(":information_source: Read Instructions"):
            st.write("1. Place a bench horizontally in front of you and place both hands on the bench slightly further than shoulder-width apart with feet together on the floor behind you, resting on the balls of your feet.")
            st.write("2. While maintaining a neutral spine, bend your elbows and lower your torso towards the bench until your arms form two 90-degree angles.")
            st.write("3. Push through your chest and extend your elbows to lift your body back into the starting position.")
            st.write("4. Repeat exercise.")
        with st.expander(":video_camera: Watch Video"):
            st.video('https://youtu.be/yAbg3_pJKvw')
            st.write("Video Source: https://youtu.be/yAbg3_pJKvw")
        st.divider()

        st.subheader("Plank to Push-Ups")
        with st.expander(":information_source: Read Instructions"):
            st.write("1. Start in a push up position with hands and elbows stacked under your shoulders, with your body in a straight line from shoulders to heels.")
            st.write("2. Transition into a forearm plank by lowering down to rest on your forearms with elbows under the shoulders. Squeeze the abs to maintain a neutral spine.")
            st.write("3. Hold the plank for around 5 seconds, then transition back into push up position while keeping your knees and hips off the floor.")
            st.write("4. Bend at the elbows to lower your chest towards the floor to make a push up, make sure your arms stay close to your sides.")
            st.write("5. Push back into the starting position and repeat exercise.")
        with st.expander(":video_camera: Watch Video"):
            st.video('https://youtu.be/56vUOad6Irs')
            st.write("Video Source: https://youtu.be/56vUOad6Irs")
        st.divider()

        st.subheader("Wall Push-Ups")
        with st.expander(":information_source: Read Instructions"):
            st.write("1. Stand with your feet a few feet away from a wall.")
            st.write("2. Slowly bend your elbows and lower your chest toward the wall.")
            st.write("3. Focus on keeping your body aligned as you pause in this position.")
            st.write("4. Push through your hands and straighten your arms, returning to the starting position.")
            st.write("5. Repeat exercise")
        with st.expander(":video_camera: Watch Video"):
            st.video('https://youtu.be/-KVhapnEtuk')
            st.write("Video Source: https://youtu.be/-KVhapnEtuk")
        st.divider()
    
    elif selected_subcategory == "Back":
        st.subheader("Back Training")
        col1, col2 = st.columns(2)
        with col1:
           st.subheader("Benefits")
           st.write("Back training improves posture, reducing the risk of back pain and injuries. It enhances functional strength for daily activities and sports, promoting overall physical performance. Additionally, a strong back contributes to a balanced physique and better core stability.")
       
        with col2:
           st.subheader("used Muscles")
           st.image("Back-Muscles-jpeg.webp")
           st.write("Image Source: https://samarpanphysioclinic.com/muscles-of-the-back/")
        st.divider()
        
        st.subheader("Bird Dogs")
        with st.expander(":information_source: Read Instructions"):
            st.write("")
        with st.expander(":video_camera: Watch Video"):
            st.video('https://youtu.be/vzU5xrs1gMQ')
            st.write("Video Source: https://youtu.be/vzU5xrs1gMQ")
        st.divider()

        st.subheader("Cat Camel Stretch")
        with st.expander(":information_source: Read Instructions"):
            st.write("")
        with st.expander(":video_camera: Watch Video"):
            st.video('https://youtu.be/c2kKOjpzK14')
            st.write("Video Source: https://youtu.be/c2kKOjpzK14")
        st.divider()

        st.subheader("Cobra Pose")
        with st.expander(":information_source: Read Instructions"):
            st.write("")
        with st.expander(":video_camera: Watch Video"):
            st.video('https://youtu.be/JDcdhTuycOI')
            st.write("Video Source: https://youtu.be/JDcdhTuycOI")
        st.divider()

        st.subheader("Dive Bomber")
        with st.expander(":information_source: Read Instructions"):
            st.write("")
        with st.expander(":video_camera: Watch Video"):
            st.video('https://youtu.be/mvNcSF-nXg4')
            st.write("Video Source: https://youtu.be/mvNcSF-nXg4")
        st.divider()

        st.subheader("Prone T Raises")
        with st.expander(":information_source: Read Instructions"):
            st.write("")
        with st.expander(":video_camera: Watch Video"):
            st.video('https://youtu.be/3GJoiYUYwr0')
            st.write("Video Source: https://youtu.be/3GJoiYUYwr0")
        st.divider()
        
        st.subheader("Prone W Raises")
        with st.expander(":information_source: Read Instructions"):
            st.write("")
        with st.expander(":video_camera: Watch Video"):
            st.video('https://youtu.be/EJpwME9qcEI')
            st.write("Video Source: https://youtu.be/EJpwME9qcEI")
        st.divider()

        st.subheader("Prone Y Raises")
        with st.expander(":information_source: Read Instructions"):
            st.write("")
        with st.expander(":video_camera: Watch Video"):
            st.video('https://youtu.be/w1AWGKubE5U')
            st.write("Video Source: https://youtu.be/w1AWGKubE5U")
        st.divider()
        
        st.subheader("Reverse Snow Angels")
        with st.expander(":information_source: Read Instructions"):
            st.write("")
        with st.expander(":video_camera: Watch Video"):
            st.video('https://youtu.be/8tQUrvafTdg')
            st.write("Video Source: https://youtu.be/8tQUrvafTdg")
        st.divider()

        st.subheader("Seated Forward Folds")
        with st.expander(":information_source: Read Instructions"):
            st.write("")
        with st.expander(":video_camera: Watch Video"):
            st.video('https://youtu.be/xwGv90wpgKU')
            st.write("Video Source: https://youtu.be/xwGv90wpgKU")
        st.divider()

        st.subheader("Supermans")
        with st.expander(":information_source: Read Instructions"):
            st.write("")
        with st.expander(":video_camera: Watch Video"):
            st.video('https://youtu.be/z6PJMT2y8GQ')
            st.write("Video Source: https://youtu.be/z6PJMT2y8GQ")
        st.divider()

        st.subheader("Swimmers")
        with st.expander(":information_source: Read Instructions"):
            st.write("")
        with st.expander(":video_camera: Watch Video"):
            st.video('https://youtu.be/nzzn3YbFp2w')
            st.write("Video Source: https://youtu.be/nzzn3YbFp2w")
        st.divider()
    
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
        
        st.subheader("Boat pose")
        with st.expander(":information_source: Read Instructions"):
            st.write("1. Sit on the floor with your legs extended in front of you. Keep your spine tall and your hands resting on the floor beside your hips for support.")
            st.write("2. As you exhale, lean back slightly and lift your feet off the ground. Your torso and legs should form a V shape.")
            st.write("3. Balance on your glutes while keeping your spine straight. Avoid rounding your back; instead, imagine lengthening through the crown of your head.")
            st.write("4. Extend your arms straight out in front of you, parallel to the floor, with your palms facing each other. Alternatively, you can hold onto the backs of your thighs for additional support, especially if you're a beginner.")
            st.write("5. Take deep breaths in and out as you hold the pose. Aim to maintain steady, even breaths to help you stay focused and relaxed.")
            st.write("6. Hold the pose for as long as you feel comfortable, aiming for 10-30 seconds to start. As you become more experienced, you can gradually increase the duration of your hold.")
            st.write("7. To release the pose, exhale as you lower your feet back to the floor, returning to a seated position with your legs extended.")
            st.write("8. Repeat exercise.")
        with st.expander(":video_camera: Watch Video"):
            st.video('https://youtu.be/VN-6jygZ094')
            st.write("Video Source: https://youtu.be/VN-6jygZ094")
        st.divider()
        
        st.subheader("Crunches")
        with st.expander(":information_source: Read Instructions"):
            st.write("1. Lie down on the floor with your knees bent and your feet planted hip-width apart.")
            st.write("2. Place your hands crossing over your chest OR with your elbows out wide with your hands behind your head, with your fingers grazing your ears.")
            st.write("3. Relax your shoulders and keep your gaze neutral and tuck your chin slightly towards your chest.")
            st.write("4. Inhale, drawing your abdomen in towards your spine. Exhale and lift your head, neck and shoulder blades off the floor, curling inwards.")
            st.write("5. Repeat exercise.")
        with st.expander(":video_camera: Watch Video"):
            st.video('https://youtu.be/nt9jwky07jc')
            st.write("Video Source: https://youtu.be/nt9jwky07jc")

        st.subheader("Variation: Bicycle Crunches")
        with st.expander(":information_source: Read Instructions"):
            st.write("1. Lie down on the floor with your knees bent and your feet planted hip-width apart.")
            st.write("2. Place your hands gently on your head with your elbows out wide, with your fingers grazing your ears.")
            st.write("3. Lift one leg off the ground and straighten it outwards, raising the opposite knee upwards towards your chest.")
            st.write("4. Lift your chest upwards and turn your torso—opposite elbow to opposite knee.")
            st.write("5. Lower back to a neutral position with your knees raised. Switch to the other side—opposite elbow and opposite knee")
            st.write("6. Repeat exercise.")
        with st.expander(":video_camera: Watch Video"):
            st.video('https://youtu.be/cbKIDZ_XyjY')
            st.write("Video Source: https://youtu.be/cbKIDZ_XyjY")
          
        st.subheader("Variation: Reverse Crunches")
        with st.expander(":information_source: Read Instructions"):
            st.write("1. Lie down on the floor with your knees bent and your feet planted hip-width apart.")
            st.write("2. Place your hands on the floor by your side.")
            st.write("3. Inhale, contract your abs towards your spine.")
            st.write("4. Exhale and lift your feet off the floor and raise your knees upwards and inwards towards your chest, keeping your knees at a 90 degree angle. Your hips should tilt inwards to crunch your abs.")
            st.write("5. Repeat exercise.")
        with st.expander(":video_camera: Watch Video"):
            st.video('https://youtu.be/XY8KzdDcMFg')
            st.write("Video Source: https://youtu.be/XY8KzdDcMFg")

        st.subheader("Variation: Standing Oblique Crunches")
        with st.expander(":information_source: Read Instructions"):
            st.write("1. Stand with your knees slightly bent, your feet hip-width apart, and your hands behind your head.")
            st.write("2. Shift your weight to the left leg, crunch to the right side, and bring your right knee up toward your elbow.")
            st.write("3. Lower your right leg and return to the starting position.")
            st.write("4. Switch sides.")
            st.write("5. Repeat exercise")
        with st.expander(":video_camera: Watch Video"):
            st.video('https://youtu.be/j12PC1m6va4')
            st.write("Video Source: https://youtu.be/j12PC1m6va4")
        st.divider()
        
        st.subheader("Flutter Kicks")
        with st.expander(":information_source: Read Instructions"):
            st.write("1. Lay on your back, extending your legs at a 45-degree angle. Your arms should be down at your sides and your legs off the ground.")
            st.write("2. Lift your head, shoulders, and neck slightly off the ground.")
            st.write("3. Start kicking your legs up and down, alternating as you go. Flutter your legs at a pace you can maintain whilst also keeping your core still.")
            st.write("4. Flutter as long as possible.")
        with st.expander(":video_camera: Watch Video"):
            st.video('https://youtu.be/ZB1SwBRVLCc')
            st.write("Video Source: https://youtu.be/ZB1SwBRVLCc")
        st.divider()
        
        st.subheader("Lying Leg Raises")
        with st.expander(":information_source: Read Instructions"):
            st.write("1. Lay supine in a relaxed position with your legs straight and your hands underneath your low back for support.")
            st.write("2. Keep your legs straight and raise them towards your forehead while contracting your abdominals and exhaling.")
            st.write("3. Once your abs are fully contracted and your legs are slightly above parallel, slowly lower your legs back to the starting position.")
            st.write("4. Repeat exercise.")
        with st.expander(":video_camera: Watch Video"):
            st.video('https://youtu.be/Wp4BlxcFTkE')
            st.write("Video Source: https://youtu.be/Wp4BlxcFTkE")
        st.divider()
        
        st.subheader("Mountain Climbers")
        with st.expander(":information_source: Read Instructions"):
            st.write("1. Get into a plank position, making sure to distribute your weight evenly between your hands and your toes.")
            st.write("2. Check your form—your hands should be about shoulder-width apart, back flat, abs engaged, and head in alignment.")
            st.write("3. Pull your right knee into your chest as far as you can.")
            st.write("4. Switch legs, pulling one knee out and bringing the other knee in.")
            st.write("5. Keep your hips down and run your knees in and out as far and as fast as you can. Alternate inhaling and exhaling with each leg change.")
            st.write("6. Repeat as long as possible.")
        with st.expander(":video_camera: Watch Video"):
            st.video('https://youtu.be/kLh-uczlPLg')
            st.write("Video Source: https://youtu.be/kLh-uczlPLg")
        st.divider()
        
        st.subheader("Planks")
        with st.expander(":information_source: Read Instructions"):
            st.write("1. Start in a tabletop position on your hands and knees, then lower down to your forearms with your elbows stacked beneath your shoulders.")
            st.write("2. Step your feet back until your body makes a line from shoulders to heels.")
            st.write("3. Squeeze your core and think about pulling your belly button towards your sternum to engage the abs.")
            st.write("4. Hold the position for as long as possible.")
        with st.expander(":video_camera: Watch Video"):
            st.video('https://youtu.be/q4rDeHYMcIg')
            st.write("Video Source: https://youtu.be/q4rDeHYMcIg")
        st.divider()

        st.subheader("Variation: Side Planks")
        with st.expander(":information_source: Read Instructions"):
            st.write("1. Lie on your side, legs extended and stacked.")
            st.write("2. Place your elbow under your elbow and lift your hips to form a straight line.")
            st.write("3. Hold this position for 30 seconds or longer.")
            st.write("4. Switch sides.")
        with st.expander(":video_camera: Watch Video"):
            st.video('https://youtu.be/0Rl5ZQwmS-o')
            st.write("Video Source: https://youtu.be/0Rl5ZQwmS-o")
        st.divider()
        
        st.subheader("Russian Twists")
        with st.expander(":information_source: Read Instructions"):
            st.write("1. Sit on the floor or mat with your knees bent and feet flat on the ground.")
            st.write("2. Sitting up, angle your upper body 45 degrees backward. Keep your back neutral and your shoulders in their natural position in order to maintain good posture and avoid strain.")
            st.write("3. Gently lift your feet a few inches off the ground, being sure to keep your back neutral and at a 45-degree angle throughout.")
            st.write("4. Rotate your arms to one side of your body, and then rotate them to the opposite side.")
        with st.expander(":video_camera: Watch Video"):
            st.video('https://youtu.be/VfWoNC-NMII')
            st.write("Video Source: https://youtu.be/VfWoNC-NMII")
        st.divider()
        
        st.subheader("Scissor Kicks")
        with st.expander(":information_source: Read Instructions"):
            st.write("1. Lay on your with your hands on your side.")
            st.write("2. Pick your feet up off the ground 6-8 inches.")
            st.write("3. Bring your right foot over your left foot and then alternate your left foot over your right foot.")
            st.write("4. Alternate back and forth so that it looks like a scissor motion.")
        with st.expander(":video_camera: Watch Video"):
            st.video('https://youtu.be/91NZ7XKG1UA')
            st.write("Video Source: https://youtu.be/91NZ7XKG1UA")
        st.divider()
        
        st.subheader("Seated Knee Tucks")
        with st.expander(":information_source: Read Instructions"):
            st.write("Sit down with your hands on the mat, your legs fully extended, and lean back.")
            st.write("Bend your legs and bring your knees toward your chest.")
            st.write("Hold for a second or two and then fully extend your legs without touching the mat.")
            st.write("Repeat exercise.")
        with st.expander(":video_camera: Watch Video"):
            st.video('https://youtu.be/HR_1AqBmVAU')
            st.write("Video Source: https://youtu.be/HR_1AqBmVAU")
        st.divider()
        
        st.subheader("Sit-ups")
        with st.expander(":information_source: Read Instructions"):
            st.write("1. Lie on your back with knees bent and feet flat on the floor and place your hands behind your head or cross them over your chest.")
            st.write("2. Engage your core and lift your upper body towards your knees. Keep your feet flat on the floor and exhale as you sit up.")
            st.write("3. Slowly lower your upper body back to the starting position, inhale as you lower down.")
            st.write("4. Repeat exercise")
        with st.expander(":video_camera: Watch Video"):
            st.video('https://youtu.be/swOyWKk7Oko')
            st.write("Video Source: https://youtu.be/swOyWKk7Oko")
        
        st.subheader("Toe Touches")
        with st.expander(":information_source: Read Instructions"):
            st.write("1. Lie flat on your back with legs extended straight up towards the ceiling. Your arms can be extended alongside your body or reaching towards your toes.")
            st.write("2. Engage your core and lift your upper back off the floor. Reach your hands towards your toes, aiming to touch them.")
            st.write("3. Slowly lower your upper back back down to the floor with control.")
        with st.expander(":video_camera: Watch Video"):
            st.video("https://youtu.be/9iEI95-eZWk")
            st.write("Video Source: https://youtu.be/9iEI95-eZWk")
        st.divider()
        
        st.subheader("V-ups")
        with st.expander(":information_source: Read Instructions"):
            st.write("1. Lie flat on your back with arms extended overhead and legs straight.")
            st.write("2. lift your arms and legs to form a V-shape, trying to touch your hands to your toes. Keep your legs as straight as possible throughout the movement.")
            st.write("3. Lower your arms and legs back to the starting position with control.")
        with st.expander(":video_camera: Watch Video"):
            st.video('https://youtu.be/7UVgs18Y1P4')
            st.write("Video Source: https://youtu.be/7UVgs18Y1P4 ")
        st.divider()
        
        
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

        st.subheader("Bridge")
        with st.expander(":information_source: Read Instructions"):
            st.write("Lie on your back with your knees bent.")
            st.write("Tighten the muscles in your stomach.")
            st.write("Raise your hips off the floor until they line up with your knees and shoulders.")
            st.write("Hold for a chosen amount of time.")
        with st.expander(":video_camera: Watch Video"):
            st.video('https://youtu.be/Xp33YgPZgns')
            st.write("Video source: https://youtu.be/Xp33YgPZgns")
        st.divider()

        st.subheader("Clamshells")
        with st.expander(":information_source: Read Instructions"):
            st.write("1. Lie on your side with your knees slightly bent and with one leg on top of the other.")
            st.write("2. Keep your feet together and lift your top knee until it’s parallel with your hip.")
            st.write("3. Lower your knee back to the initial position.")
            st.write("4. Repeat and then switch sides.")
        with st.expander(":video_camera: Watch Video"):
            st.video('https://youtu.be/39vuP5xozsI')
            st.write("Video source: https://youtu.be/39vuP5xozsI")
        st.divider()

        st.subheader("Donkey Kicks")
        with st.expander(":information_source: Read Instructions"):
            st.write("1. Get down on your hands and knees, with your hands under your shoulders and your knees under your hips.")
            st.write("2. Flex your right foot, lift your right leg up, keeping the knee bent at a 90-degree angle, and squeeze the glutes.")
            st.write("3. Return to the starting position")
            st.write("4. Repeat, and switch legs.")
        with st.expander(":video_camera: Watch Video"):
            st.video('https://youtu.be/SJ1Xuz9D-ZQ')
            st.write("Video source: https://youtu.be/SJ1Xuz9D-ZQ")
        st.divider()

        st.subheader("Fire Hydrants")
        with st.expander(":information_source: Read Instructions"):
            st.write("1. Get down on your hands and knees, with your wrists under your shoulders and your knees hip-width apart.")
            st.write("2. Keeping the knee bent, raise one leg up and out to the side, until it’s level with your hip.")
            st.write("3. Return to the starting position.")
            st.write("4. Repeat, and then switch legs.")
        with st.expander(":video_camera: Watch Video"):
            st.video('https://youtu.be/ofY0RBUtSsw')
            st.write("Video source: https://youtu.be/ofY0RBUtSsw")
        st.divider()

        st.subheader("Hip Thrusts")
        with st.expander(":information_source: Read Instructions"):
            st.write("1. Lie on your back on the floor, with knees bent, feet planted firmly on the floor.")
            st.write("2. Press your heels into the floor, driving your hips upwards. Pause at the top, making sure to squeeze your glutes.") 
            st.write("3. Slowly return to your starting position")
            st.write("4. Repeat for a desired amount.")
        with st.expander(":video_camera: Watch Video"):
            st.video('https://youtu.be/FJNPGhF1R-Y')
            st.write("Video source: https://youtu.be/FJNPGhF1R-Y")
        st.divider()

        st.subheader("Lunges")
        with st.expander(":information_source: Read Instructions"):
            st.write("1. Stand with your feet hip-width apart, keep your back straight, your shoulders back, and your abs tight.")
            st.write("2. Take a step forward and slowly bend both knees, until your back knee is just above the floor.")
            st.write("3. Stand back up and repeat the movement.")
            st.write("4. Alternate legs until the set is complete.")
        with st.expander(":video_camera: Watch Video"):
            st.video('https://youtu.be/tTej-ax9XiA')
            st.write("Video source: https://youtu.be/tTej-ax9XiA")

        st.subheader("Variation: Reverse Lunges")
        with st.expander(":information_source: Read Instructions"):
            st.write("1. Stand with your feet shoulder-width apart. Squeeze your glutes and shoulder blades, keeping your gaze neutral at a point straight ahead of you.")
            st.write("2. Step one leg back and slightly out, landing with your toe first. Work to avoid slamming your knee into the ground and bending your knees to form right angles with both of your legs.")
            st.write("3. Drive off the ground with your front foot and step your rear leg forward into the starting position.")
            st.write("4. Repeat exercise.")
        with st.expander(":video_camera: Watch Video"):
            st.video('https://youtu.be/xrPteyQLGAo')
            st.write("Video source: https://youtu.be/xrPteyQLGAo")

        st.subheader("Variation: Lateral Lunges")
        with st.expander(":information_source: Read Instructions"):
            st.write("1. Stand straight with your feet hip-width apart.")
            st.write("2. Step out to the side and transfer your weight to that leg.")
            st.write("3. Use your lead foot to push you back to the starting position.")
            st.write("4. Repeat and then switch sides.")
        with st.expander(":video_camera: Watch Video"):
            st.video('https://youtu.be/gwWv7aPcD88?t=7')
            st.write("Video source: https://youtu.be/gwWv7aPcD88?t=7")

        st.subheader("Variation: Walking Lunges")
        with st.expander(":information_source: Read Instructions"):
            st.write("1. Stand with your feet hip-width apart, take a step forward with your right foot and then slowly bend both knees until your back knee is just above the floor.")
            st.write("2. Stand back up, take a step forward with your left foot and bend both knees until your back knee is just above the floor.")
            st.write("3. Repeat this forward movement for the entire duration of the set.")
        with st.expander(":video_camera: Watch Video"):
            st.video('https://youtu.be/tQNktxPkSeE')
            st.write("Video source: https://youtu.be/tQNktxPkSeE")
        st.divider()

        st.subheader("Quadruped Leg Raise")
        with st.expander(":information_source: Read Instructions"):
            st.write("1. Start on your hands and knees.")
            st.write("2. Raise leg straight out while tightening your core. Hold the position for 5 seconds.")
            st.write("3. Lower your leg back to the starting position.")
            st.write("4. Repeat the move with the opposite leg.")
        with st.expander(":video_camera: Watch Video"):
            st.video('https://youtu.be/TJbnvoFkLKI')
            st.write("Video source: https://youtu.be/TJbnvoFkLKI")
        st.divider()

        st.subheader("Quadruped Hip Extensions")
        with st.expander(":information_source: Read Instructions"):
            st.write("1. Engage your core and make sure your back is straight and flat from the base of your pelvis to the top of your head.")
            st.write("2. Shift your weight slightly to the right side, keeping your torso stable as you do—your hips and shoulders shouldn't twist or rotate as you shift.")
            st.write("3. Press your left foot up toward the ceiling, keeping your knee bent at a 90-degree angle as you fully extend your left hip.")
            st.write("4. Lower your left knee back toward the floor, slowly and with control. Stop just before it touches down.")
            st.write("5. Repeat exercise, and then change legs.")
        with st.expander(":video_camera: Watch Video"):
            st.video('https://youtu.be/1UwyzWjFx5k')
            st.write("Video source: https://youtu.be/1UwyzWjFx5k")
        st.divider()

        st.subheader("Side Leg Raises")
        with st.expander(":information_source: Read Instructions"):
            st.write("1. Stand up straight with your feet together and your hands on your hips.")
            st.write("2. Slowly lift your right leg straight out to the side.")
            st.write("3. Pause, then slowly lower the leg. Keep your hips even throughout.")
            st.write("4. Repeat exercise and change legs.")
        with st.expander(":video_camera: Watch Video"):
            st.video('https://youtu.be/6b1hu6iSqok')
            st.write("Video source: https://youtu.be/6b1hu6iSqok")
        st.divider()

        st.subheader("Single-Leg Glute Bridges")
        with st.expander(":information_source: Read Instructions"):
            st.write("1. Lie on your back with your arms by your sides, knees bent, and feet flat on the floor.")
            st.write("2. Raise one leg and lift your hips as high as you can.")
            st.write("3. Lower your hips to the initial position.")
            st.write("4. Repeat exercise, and then switch legs.")
        with st.expander(":video_camera: Watch Video"):
            st.video('https://youtu.be/AVAXhy6pl7o')
            st.write("Video source: https://youtu.be/AVAXhy6pl7o")
        st.divider()
        
        st.subheader("Standing Kickbacks")
        with st.expander(":information_source: Read Instructions"):
            st.write("1. Lift one leg off the ground and extend it behind you. Keep your knee straight and squeeze your glutes as you lift your leg.")
            st.write("2. Keep Core Engaged: Throughout the exercise, keep your core tight.")
            st.write("3. Repeat exercise, and then switch legs.")
        with st.expander(":video_camera: Watch Video"):
            st.video('https://youtu.be/pdP0uJXvc44')
            st.write("Video source: https://youtu.be/pdP0uJXvc44")
        st.divider()
        
        st.subheader("Squats")
        with st.expander(":information_source: Read Instructions"):
            st.write("1. Stand with your feet wider than your Hips and feet pointed slightly out.")
            st.write("2. Begin bendin your knees until parallel to the floor with your back as straight as possible.")
            st.write("3. Push back up until you reach standing positions.")
            st.write("4. Repeat.")
        with st.expander(":video_camera: Watch Video"):
            st.video('https://www.youtube.com/watch?v=xqvCmoLULNY')
            st.write("Video Source: https://www.youtube.com/watch?v=xqvCmoLULNY")
        
        st.subheader("Variation: Bulgarian Split Squats")
        with st.expander(":information_source: Read Instructions"):
            st.write("1. Stand with feet hip width apart and approximately 2 shoulder widths in length with shoelaces down on a bench.")
            st.write("2. Drop the trailing knee down until it is slighgtly off the ground maintaining a slight forward torso angle.")
            st.write("3. Reverse the pattern and return to the starting position.")
        with st.expander(":video_camera: Watch Video"):
            st.video('https://youtu.be/vgn7bSXkgkA')
            st.write("Video source: https://youtu.be/vgn7bSXkgkA")
        
        st.subheader("Variation: Plie Squats")
        with st.expander(":information_source: Read Instructions"):
            st.write("1. Stand with your feet in a wide stance, your toes pointing out to the sides.")
            st.write("2. Squat until your thighs are parallel to the floor.")
            st.write("3. Stand up and bring the dumbbells together in front of your chest.")
            st.write("4. Repeat exercise.")
        with st.expander(":video_camera: Watch Video"):
            st.video('https://youtu.be/8ZBXkH6QHRY')
            st.write("Video source: https://youtu.be/8ZBXkH6QHRY")
        
        st.subheader("Variation: Sumo Squats")
        with st.expander(":information_source: Read Instructions"):
            st.write("1. Stand with your feet in a wide stance and with your toes pointing out to the sides.")
            st.write("2. Lower yourself by bending your knees and pressing your hips back. Bend your upper body forwards.")
            st.write("3. Once your thighs are parallel to the floor, come back up and repeat.")
        with st.expander(":video_camera: Watch Video"):
            st.video('https://youtu.be/sqDGkIBYPAk')
            st.write("Video source: https://youtu.be/sqDGkIBYPAk")
        st.divider()
        
        st.subheader("Wall Sit")
        with st.expander(":information_source: Read Instructions"):
            st.write("1. Start in a squat position, with your thighs parallel to the floor and your back against a wall.")
            st.write("2. Hold this position for as long as you can.")
        with st.expander(":video_camera: Watch Video"):
            st.video('https://youtu.be/-cdph8hv0O0')
            st.write("Video source: https://youtu.be/-cdph8hv0O0")

        st.subheader("Variation: Wall Sit with Leg Lifts")
        with st.expander(":information_source: Read Instructions"):
            st.write("1. Start in a squat position, with your thighs parallel to the floor and your back against a wall.")
            st.write("2. Slowly lift one leg and create tension in the other that is grounded.")
            st.write("3. Alternate between legs.")
        with st.expander(":video_camera: Watch Video"):
            st.video('https://youtu.be/E-wrrBgLfeQ')
            st.write("Video source: https://youtu.be/E-wrrBgLfeQ")
        st.divider()
        
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

        st.subheader("Alternating Split Stance Jumps")
        with st.expander(":information_source: Read Instructions"):
            st.write("")
        with st.expander(":video_camera: Watch Video"):
            st.video('https://youtu.be/lPLkTeryw20')
            st.write("Video source: https://youtu.be/lPLkTeryw20")
        st.divider()

        st.subheader("Boxer Shuffle")
        with st.expander(":information_source: Read Instructions"):
            st.write("")
        with st.expander(":video_camera: Watch Video"):
            st.video('https://youtu.be/BmfOURosbdo')
            st.write("Video source: https://youtu.be/BmfOURosbdo")
        st.divider()

        st.subheader("Butt Kicks")
        with st.expander(":information_source: Read Instructions"):
            st.write("")
        with st.expander(":video_camera: Watch Video"):
            st.video('https://youtu.be/-dtvAxibgYQ')
            st.write("Video source: https://youtu.be/-dtvAxibgYQ")
        st.divider()

        st.subheader("Flutter Kicks")
        with st.expander(":information_source: Read Instructions"):
            st.write("")
        with st.expander(":video_camera: Watch Video"):
            st.video('https://youtu.be/ZB1SwBRVLCc')
            st.write("Video source: https://youtu.be/ZB1SwBRVLCc")
        st.divider()

        st.subheader("Half Squat Walk")
        with st.expander(":information_source: Read Instructions"):
            st.write("")
        with st.expander(":video_camera: Watch Video"):
            st.video('https://youtu.be/wqfRvXc7BHY')
            st.write("Video source: https://youtu.be/wqfRvXc7BHY")
        st.divider()

        st.subheader("High Kicks")
        with st.expander(":information_source: Read Instructions"):
            st.write("")
        with st.expander(":video_camera: Watch Video"):
            st.video('https://youtu.be/qzQ5qn6IWmM')
            st.write("Video source: https://youtu.be/qzQ5qn6IWmM")
        st.divider()

        st.subheader("Jumping Jack")
        with st.expander(":information_source: Read Instructions"):
            st.write("")
        with st.expander(":video_camera: Watch Video"):
            st.video('https://youtu.be/PBHUfBzxczU')
            st.write("Video source: https://youtu.be/PBHUfBzxczU")
        st.divider()

        st.subheader("Knee Side Leg Lifts")
        with st.expander(":information_source: Read Instructions"):
            st.write("")
        with st.expander(":video_camera: Watch Video"):
            st.video('https://youtu.be/aOpoqD15TLQ')
            st.write("Video source: https://youtu.be/aOpoqD15TLQ")
        st.divider()

        st.subheader("Lateral Hops")
        with st.expander(":information_source: Read Instructions"):
            st.write("")
        with st.expander(":video_camera: Watch Video"):
            st.video('https://youtu.be/JNMtkCkIYew')
            st.write("Video source: https://youtu.be/JNMtkCkIYew")
        st.divider()

        st.subheader("Lying Leg Circles")
        with st.expander(":information_source: Read Instructions"):
            st.write("")
        with st.expander(":video_camera: Watch Video"):
            st.video('https://youtu.be/_tOo9g-6KcE')
            st.write("Video source: https://youtu.be/_tOo9g-6KcE")
        st.divider()

        st.subheader("Marching Hip Raises")
        with st.expander(":information_source: Read Instructions"):
            st.write("")
        with st.expander(":video_camera: Watch Video"):
            st.video('https://youtu.be/VfUSA0y2JeE')
            st.write("Video source: https://youtu.be/VfUSA0y2JeE")
        st.divider()

        st.subheader("Pulsing Side Lying Leg Raises")
        with st.expander(":information_source: Read Instructions"):
            st.write("")
        with st.expander(":video_camera: Watch Video"):
            st.video('https://youtu.be/Kk2fiskUG98')
            st.write("Video source: https://youtu.be/Kk2fiskUG98")
        st.divider()

        st.subheader("Rainbow Leg Lifts")
        with st.expander(":information_source: Read Instructions"):
            st.write("")
        with st.expander(":video_camera: Watch Video"):
            st.video('https://youtu.be/SGALKLTCCDk')
            st.write("Video source: https://youtu.be/SGALKLTCCDk")
        st.divider()

        st.subheader("Standing Knee Raises")
        with st.expander(":information_source: Read Instructions"):
            st.write("")
        with st.expander(":video_camera: Watch Video"):
            st.video('https://youtu.be/O_8EUJ7i-PI')
            st.write("Video source: https://youtu.be/O_8EUJ7i-PI")
        st.divider()

        st.subheader("Side Lying Leg Lifts")
        with st.expander(":information_source: Read Instructions"):
            st.write("")
        with st.expander(":video_camera: Watch Video"):
            st.video('https://youtu.be/jgh6sGwtTwk')
            st.write("Video source: https://youtu.be/jgh6sGwtTwk")
        st.divider()

        st.subheader("Single Leg V-Ups")
        with st.expander(":information_source: Read Instructions"):
            st.write("")
        with st.expander(":video_camera: Watch Video"):
            st.video('https://youtu.be/RA9nGJVwtJ4')
            st.write("Video source: https://youtu.be/RA9nGJVwtJ4")
        st.divider()

        st.subheader("Walking High Knees")
        with st.expander(":information_source: Read Instructions"):
            st.write("")
        with st.expander(":video_camera: Watch Video"):
            st.video('https://youtu.be/v0C88boWRIg')
            st.write("Video source: https://youtu.be/v0C88boWRIg")
        st.divider()

  
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
            "REverse Snow Angels",
            "Seated Forward Folds",
            "Supermans",
            "Swimmers"
        ]
        
        st.subheader("Randomized Back Workout")

        tab1, tab2, tab3 = st.tabs([":green-background[Beginner]", ":orange-background[Intermediate]", ":red-background[Advanced]"])

        with tab1:
           st.header(":green[Beginner Training]")
           st.header(":green[Beginner Training]")
           st.write("Here are 5 randomized exercises for your back. Do 1-2 sets with each 10 repetitions. Take a break of 60 Seconds in between the exercises.")
           zufällige_übungen_beginner = random.sample(back_fitness_übungen, 5)
           for übung in zufällige_übungen_beginner:
               st.write(übung)
        
        with tab2:
           st.header(":orange[Intermediate Training]")
           st.write("Here are 8 randomized exercises for your arms. Do 3-4 sets with each 10 repetitions. Take a break of 45 Seconds in between the exercises.")
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
            "Plank Shoulder Taps"
            "Reverse Plank"
            "Walking Plank"
            "Push-Ups"
            "Diamond Push-Ups"
            "Decline Push-Ups"
            "Incline Push-Ups"
            "Plank to Push-Ups"
            "Wall Push-Ups"
            "Bird Dogs"
            "Cat Camel Stretch"
            "Cobra Pose"
            "Dive Bombers"
            "Prone T Raises"
            "Prone W Raises"
            "Prone Y Raises"
            "Reverse Snow Angels"
            "Seated Forward Folds"
            "Supermans"
            "Swimmers"
            "Boat pose"
            "Crunches"
            "Bicycle Crunches"
            "Reverse Crunches"
            "Standing Oblique Crunches"
            "Flutter Kicks"
            "Lying Leg Raises"
            "Mountain Climbers"
            "Planks"
            "Side Planks"
            "Russian Twists"
            "Scissor Kicks"
            "Seated Knee Tucks"
            "Sit-ups"
            "Toe Touches"
            "V-ups"

        ]
        st.subheader("Randomized Upper Body Workout")

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

        tab1, tab2, tab3 = st.tabs([":green-background[Beginner]", ":orange-background[Intermediate]", ":red-background[Advanced]"])

        with tab1:
           st.header(":green[Beginner Training]")
        
        with tab2:
           st.header(":orange[Intermediate Training]")
        
        with tab3:
           st.header(":red[Advanced Training]")
            
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
