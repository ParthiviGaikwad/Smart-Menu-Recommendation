import pandas as pd
import streamlit as st
from sklearn.naive_bayes import BernoulliNB

# Load the dataset
data = pd.read_excel("data\cleaned_drinks.xlsx")

# Define drinks list
drinks = ['Nimbu Pani', 'Rooh Afza', 'Pudina Nimbu Pani', 'Watermelon Mint Cooler', 'Cherry Lime Sharbat']

# Initialize an empty dictionary to store user input
user_input = {}

# Initialize the Streamlit app
st.title("Drink Recommendation")


# Add image to the app
st.image('data/drinks.jpeg', caption='drinks', use_column_width=True)


# Ask user for input for each drink
for drink in drinks:
    user_response = st.radio(f"Do you prefer {drink}?", options=['Yes', 'No'])
    user_input[drink] = 1 if user_response == "Yes" else 0

# Convert user input to DataFrame
input_data = pd.DataFrame(user_input, index=[0])

# Define features (inputs)
features = data[['Nimbu Pani', 'Rooh Afza', 'Pudina Nimbu Pani', 'Watermelon Mint Cooler', 'Cherry Lime Sharbat']]

# Initialize the Naive Bayes classifier
model = BernoulliNB()

# Button to trigger recommendation
if st.button("Get Recommendation"):
    # Iterate over each target drink
    for drink in ['Citronnade', 'Eau de Rose', 'Limonade', 'Melon Mint Cooler', 'Cherry Citrus Splash']:
        # Define target variable (output)
        target = data[drink]

        # Fit the classifier with the entire dataset
        model.fit(features, target)

        # Make prediction for the input data
        prediction = model.predict(input_data)[0]

        # Display the recommendation to the user
        st.write(f"Prediction for {drink}: {prediction}")
