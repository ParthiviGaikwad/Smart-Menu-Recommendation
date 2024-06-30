import os
import pandas as pd
import streamlit as st
from sklearn.naive_bayes import BernoulliNB
from PIL import Image
import subprocess

# Load the dataset
data = pd.read_excel("C:\\Users\\PARTHIVI\\OneDrive\\Desktop\\PROJECT\\mini bomb\\cleaned_drinks.xlsx")

# Define drinks list
drinks = ['Nimbu Pani', 'Rooh Afza', 'Pudina Nimbu Pani', 'Watermelon Mint Cooler', 'Cherry Lime Sharbat']

# Initialize an empty dictionary to store user input
user_input = {}

# Initialize the Streamlit app
st.title("Drink Recommendation")
# Add image to the app
st.image('drinks.jpeg', caption='', use_column_width=True)

for drink in drinks:
    st.subheader(f"Do you prefer {drink}?")
    image_paths = {
        'Nimbu Pani': "C:\\Users\\PARTHIVI\\OneDrive\\Desktop\\PROJECT\\mini bomb\\Nimbu Pani.jpg",
        'Rooh Afza': "C:\\Users\\PARTHIVI\\OneDrive\\Desktop\\PROJECT\\mini bomb\\Rooh Afza.jpg",
        'Pudina Nimbu Pani': "C:\\Users\\PARTHIVI\\OneDrive\\Desktop\\PROJECT\\mini bomb\\Pudina Nimbu Pani.jpg",
        'Watermelon Mint Cooler': "C:\\Users\\PARTHIVI\\OneDrive\\Desktop\\PROJECT\\mini bomb\\Watermelon Mint Cooler.jpg",
        'Cherry Lime Sharbat': "C:\\Users\\PARTHIVI\\OneDrive\\Desktop\\PROJECT\\mini bomb\\Cherry Lime Sharbat.jpg"
    }
    default_image_path = "C:\\Users\\PARTHIVI\\OneDrive\\Desktop\\PROJECT\\mini bomb\\default.jpg"
    image_path = image_paths.get(drink, default_image_path)
    if os.path.exists(image_path):
        with open(image_path, 'rb') as f:
            image = Image.open(f)
            st.image(image, caption=drink, use_column_width=True)
    else:
        st.error(f"Image not found for {drink}")
    user_response = st.radio("", options=['Yes', 'No'], key=f"{drink}_radio")
    user_input[drink] = 1 if user_response == "Yes" else 0

# Convert user input to DataFrame
input_data = pd.DataFrame(user_input, index=[0])

# Define features (inputs)
features = data[['Nimbu Pani', 'Rooh Afza', 'Pudina Nimbu Pani', 'Watermelon Mint Cooler', 'Cherry Lime Sharbat']]

# Initialize the Naive Bayes classifier
model = BernoulliNB()

# Initialize a list to store predictions
predictions = []

# Button to trigger recommendation
if st.button("Next"):
    # Iterate over each target drink
    for drink in ['Citronnade', 'Eau de Rose', 'Limonade', 'Melon Mint Cooler', 'Cherry Citrus Splash']:
        # Define target variable (output)
        target = data[drink]

        # Fit the classifier with the entire dataset
        model.fit(features, target)

        # Make prediction for the input data
        prediction = model.predict(input_data)[0]

        # Convert prediction to "Yes" or "No"
        prediction_label = "Yes" if prediction == 1 else "No"

        # Store the prediction
        predictions.append((drink, prediction_label))

    # Write predictions to a text file
    with open("predict_drink.txt", "w") as file:
        for drink, prediction_label in predictions:
            file.write(f"{drink}: {prediction_label}\n")

    # Run the dessert predictor script using subprocess
    subprocess.run(["streamlit", "run", "desert_predictor.py"])