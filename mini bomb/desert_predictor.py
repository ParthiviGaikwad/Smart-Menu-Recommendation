import streamlit as st
import joblib
from PIL import Image
import os
import pandas as pd
import subprocess
# Function to convert user input to binary values
def convert_input_to_binary(user_input):
    return 1 if user_input.lower() == 'yes' else 0

# Initialize the Streamlit app
st.title("Dessert Recommendation")
st.image("dessert.jpg", caption='', use_column_width=True)
# Ask user for input

# Define image paths
image_paths = {
    'Gulab Jamun': "C:\\Users\\PARTHIVI\\OneDrive\\Desktop\\PROJECT\\mini bomb\\Gulab Jamun.jpg",
    'Rasmalai': "C:\\Users\\PARTHIVI\\OneDrive\\Desktop\\PROJECT\\mini bomb\\Rasmalai.jpeg",
    'Phirni': "C:\\Users\\PARTHIVI\\OneDrive\\Desktop\\PROJECT\\mini bomb\\Phirni.jpg",
    'Shrikhand': "C:\\Users\\PARTHIVI\\OneDrive\\Desktop\\PROJECT\\mini bomb\\Shrikhand.jpg",
    'Nankhatai': "C:\\Users\\PARTHIVI\\OneDrive\\Desktop\\PROJECT\\mini bomb\\Nankhatai.jpg"
}

# Define user responses dictionary
user_responses = {}

# Ask user for input for each dessert
for dessert, image_path in image_paths.items():
    st.subheader(f"Do you prefer {dessert}?")
    if os.path.exists(image_path):
        with open(image_path, 'rb') as f:
            image = Image.open(f)
            st.image(image, caption=dessert, use_column_width=True)
    else:
        default_image_path = "C:\\Users\\PARTHIVI\\OneDrive\\Desktop\\PROJECT\\mini bomb\\default.jpg"
        if os.path.exists(default_image_path):
            with open(default_image_path, 'rb') as f:
                default_image = Image.open(f)
                st.image(default_image, caption=dessert, use_column_width=True)
        else:
            st.error("Image not found")

    user_response = st.radio("", options=['Yes', 'No'], key=f"{dessert}_radio")
    user_responses[dessert] = user_response
    st.write("")

# Convert user input to DataFrame
input_data = pd.DataFrame({dessert: 1 if response == "Yes" else 0 for dessert, response in user_responses.items()}, index=[0])

# Load the models
creme_brulee_model = joblib.load("C:\\Users\\PARTHIVI\\OneDrive\\Desktop\\PROJECT\\mini bomb\\Creme Brulee_model.pkl")
profiteroles_model = joblib.load("C:\\Users\\PARTHIVI\\OneDrive\\Desktop\\PROJECT\\mini bomb\\Profiteroles_model.pkl")
ile_flottante_model = joblib.load("C:\\Users\\PARTHIVI\\OneDrive\\Desktop\\PROJECT\\mini bomb\\Ile Flottante_model.pkl")
madeleines_model = joblib.load("C:\\Users\\PARTHIVI\\OneDrive\\Desktop\\PROJECT\\mini bomb\\Madeleines_model.pkl")
# Button to trigger predictions
if st.button("Get Recommendations"):
    # Predictions
    creme_brulee_prediction = creme_brulee_model.predict(input_data)
    profiteroles_prediction = profiteroles_model.predict(input_data)
    ile_flottante_prediction = ile_flottante_model.predict(input_data)
    madeleines_prediction = madeleines_model.predict(input_data)

    # Save predictions to a file
    with open("predict_dessert.txt", "w") as file:
        file.write("Creme Brulee Prediction: {}\n".format("Yes" if creme_brulee_prediction[0] == 1 else "No"))
        file.write("Profiteroles Prediction: {}\n".format("Yes" if profiteroles_prediction[0] == 1 else "No"))
        file.write("Ile Flottante Prediction: {}\n".format("Yes" if ile_flottante_prediction[0] == 1 else "No"))
        file.write("Madeleines Prediction: {}\n".format("Yes" if madeleines_prediction[0] == 1 else "No"))

    # Run the dessert predictor script using subprocess
    subprocess.run(["streamlit", "run", "recom.py"])