import streamlit as st
import joblib
import pandas as pd
import subprocess
from PIL import Image

# Function to convert user input to binary values
def convert_input_to_binary(user_input):
    return 1 if user_input.lower() == 'yes' else 0


st.title("Dish Recommendation")

# Define the path to the image file
image_path = "C://Users//PARTHIVI//OneDrive//Desktop//PROJECT//mini bomb//dishes.jpg"

# Check if the image file exists
try:
    # Open and display the image
    with Image.open(image_path) as img:
        st.image(img, caption='', use_column_width=True)
except FileNotFoundError:
    st.error("Image file not found. Please check the file path.")

# Ask user for input
st.write("Please enter your choices:")
safed_murgh = convert_input_to_binary(st.radio("Do you prefer Safed Murgh?", options=['Yes', 'No']))
butter_chicken = convert_input_to_binary(st.radio("Do you prefer Butter Chicken?", options=['Yes', 'No']))
chicken_korma = convert_input_to_binary(st.radio("Do you prefer Chicken Korma?", options=['Yes', 'No']))
malai_chicken = convert_input_to_binary(st.radio("Do you prefer Malai Chicken?", options=['Yes', 'No']))
mixed_vegetable_sabzi = convert_input_to_binary(st.radio("Do you prefer Mixed Vegetable Sabzi?", options=['Yes', 'No']))
baingan_bharta = convert_input_to_binary(st.radio("Do you prefer Baingan Bharta?", options=['Yes', 'No']))
aloo_baingan = convert_input_to_binary(st.radio("Do you prefer Aloo Baingan?", options=['Yes', 'No']))
bhindi_masala = convert_input_to_binary(st.radio("Do you prefer Bhindi Masala?", options=['Yes', 'No']))
vegetable_jalfrezi = convert_input_to_binary(st.radio("Do you prefer Vegetable Jalfrezi?", options=['Yes', 'No']))
aloo_gobi_masala = convert_input_to_binary(st.radio("Do you prefer Aloo Gobi Masala?", options=['Yes', 'No']))
sambhar = convert_input_to_binary(st.radio("Do you prefer Sambhar?", options=['Yes', 'No']))
fish_curry = convert_input_to_binary(st.radio("Do you prefer Fish Curry?", options=['Yes', 'No']))
fish_tawa_fry = convert_input_to_binary(st.radio("Do you prefer Fish Tawa Fry?", options=['Yes', 'No']))
goan_fish_curry = convert_input_to_binary(st.radio("Do you prefer Goan Fish Curry?", options=['Yes', 'No']))
fish_tikka = convert_input_to_binary(st.radio("Do you prefer Fish Tikka?", options=['Yes', 'No']))
fish_amritsari = convert_input_to_binary(st.radio("Do you prefer Fish Amritsari?", options=['Yes', 'No']))
chicken_tikka_masala = convert_input_to_binary(st.radio("Do you prefer Chicken Tikka Masala?", options=['Yes', 'No']))
chicken_sukka = convert_input_to_binary(st.radio("Do you prefer Chicken Sukka?", options=['Yes', 'No']))
chicken_masala = convert_input_to_binary(st.radio("Do you prefer Chicken Masala?", options=['Yes', 'No']))
chicken_kolhapuri = convert_input_to_binary(st.radio("Do you prefer Chicken Kolhapuri?", options=['Yes', 'No']))


# Input data
input_data = pd.DataFrame({
    'Safed Murgh': [safed_murgh],
    'Butter Chicken': [butter_chicken],
    'Chicken Korma': [chicken_korma],
    'Malai Chicken': [malai_chicken],
    'Mixed Vegetable Sabzi': [mixed_vegetable_sabzi],
    'Baingan Bharta': [baingan_bharta],
    'Aloo Baingan': [aloo_baingan],
    'Bhindi Masala': [bhindi_masala],
    'Vegetable Jalfrezi': [vegetable_jalfrezi],
    'Aloo Gobi Masala': [aloo_gobi_masala],
    'Sambhar': [sambhar],
    'Fish Curry': [fish_curry],
    'Fish Tawa Fry': [fish_tawa_fry],
    'Goan Fish Curry': [goan_fish_curry],
    'Fish Tikka': [fish_tikka],
    'Fish Amritsari': [fish_amritsari],
    'Chicken Tikka Masala': [chicken_tikka_masala],
    'Chicken Sukka': [chicken_sukka],
    'Chicken Masala': [chicken_masala],
    'Chicken Kolhapuri': [chicken_kolhapuri]
})

# Initialize the button to trigger predictions
if st.button("Next"):
    # Define dish_predictions list within the button click event
    dish_predictions = []
    # Iterate over each target dish
    for dish in ['Chicken Coq au Vin Blanc', 'Ratatouille', 'Fish Meuniere', 'Chicken Provencal']:
        # Load the trained model for the target dish
        model_filename = f"C:\\Users\\PARTHIVI\\OneDrive\\Desktop\\PROJECT\\mini bomb\\{dish}_model.pkl" 
        model = joblib.load(model_filename)

        # Make predictions for the input data
        predictions = model.predict(input_data)
        dish_predictions.append((dish, 'Yes' if predictions[0] == 1 else 'No'))

    # Write predictions to a text file
    with open("predict_dish.txt", "w") as file:
        file.write("Dish Recommendations\n")
        for dish, prediction in dish_predictions:
            file.write(f"{dish}: {prediction}\n")

    # Run the drinks predictor script using subprocess
    subprocess.run(["streamlit", "run", "drink_predictor.py"])