import streamlit as st
from PIL import Image

# HTML formatting examples
st.write("<h1>We recommend you our ~</h1>", unsafe_allow_html=True)

# Dictionary mapping dish names to their respective image paths
dish_image_mapping = {
    "Chicken Coq au Vin Blanc": "C:\\Users\\PARTHIVI\\PARTHIVI\\OneDrive\\Desktop\\PROJECT\\mini bomb\\Chicken Coq au Vin Blanc.jpg",
    "Ratatouille": "C:\\Users\\PARTHIVI\\OneDrive\\Desktop\\PROJECT\\mini bomb\\Ratatouille.jpg",
    "Fish Meuniere": "C:\\Users\\PARTHIVI\\OneDrive\\Desktop\\PROJECT\\mini bomb\\Fish Meunière.jpg",
    "Chicken Provencal": "C:\\Users\\PARTHIVI\\OneDrive\\Desktop\\PROJECT\\mini bomb\\Chicken Provencal.jpg",
}

# Function to display recommended items with images
def display_recommended_items(recommended_items, image_mapping, description_mapping, header_size="small"):
    if header_size == "small":
        st.markdown("<h3>Main Course Dish</h3>", unsafe_allow_html=True)
    elif header_size == "medium":
        st.markdown("<h2>Main Course Dish</h2>", unsafe_allow_html=True)
    elif header_size == "large":
        st.markdown("<h1>Main Course Dish</h1>", unsafe_allow_html=True)
    for item in recommended_items:
        st.markdown(f"**{item}**:")
        image_path = image_mapping.get(item, "C:\\Users\\PARTHIVI\\OneDrive\\Desktop\\PROJECT\\mini bomb\\default.jpg")
        with open(image_path, "rb") as img_file:
            img = Image.open(img_file)
            st.image(img, caption=description_mapping.get(item, ""), use_column_width=True)

# List of recommended dishes
recommended_dishes = ["Chicken Coq au Vin Blanc", "Ratatouille", "Fish Meuniere", "Chicken Provencal"]

# Dictionary mapping dish names to their respective descriptions
dish_description_mapping = {
    "Chicken Coq au Vin Blanc": "A variation of the classic Coq au Vin, this dish features chicken cooked in white wine with mushrooms, onions, and herbs.",
    "Ratatouille": "A vegetable medley dish featuring eggplant, zucchini, bell peppers, tomatoes, onions, and aromatic herbs.",
    "Fish Meuniere": "Fish Meunière is a classic French preparation where fish is dredged in flour, pan-fried, and served with a brown butter and lemon sauce.",
    "Chicken Provencal": "Chicken Provencal typically consists of chicken pieces cooked with tomatoes, olives, garlic, onions, herbs, and white wine.",
}

# Display recommended dishes with images and descriptions
display_recommended_items(recommended_dishes, dish_image_mapping, dish_description_mapping, header_size="small")


# Read predictions for drinks from predict_drinks.txt
predictions_drinks = {}
with open("C:\\Users\\PARTHIVI\\OneDrive\\Desktop\\PROJECT\\mini bomb\\predict_drink.txt", "r") as file:
    for line in file:
        parts = line.strip().split(": ")
        prediction_value = 1 if parts[1] == 'Yes' else 0
        predictions_drinks[parts[0]] = prediction_value

# Dictionary mapping drink names to their respective image paths
drink_image_mapping = {
    "Citronnade": "C:\\Users\\PARTHIVI\\OneDrive\\Desktop\\PROJECT\\mini bomb\\Citronnade.jpg",
    "Eau de Rose": "C:\\Users\\PARTHIVI\\OneDrive\\Desktop\\PROJECT\\mini bomb\\Eau de Rose.jpg",
    "Limonade": "C:\\Users\\PARTHIVI\\OneDrive\\Desktop\\PROJECT\\mini bomb\\Mint Lemonade.jpg",
    "Melon Mint Cooler": "C:\\Users\\PARTHIVI\\OneDrive\\Desktop\\PROJECT\\mini bomb\\Melon Mint Cooler.jpg",
    "Cherry Citrus Splash": "C:\\Users\\PARTHIVI\\OneDrive\\Desktop\\PROJECT\\mini bomb\\Cherry Citrus Splash.jpg"
}

# Dictionary mapping drink names to their respective descriptions
drink_description_mapping = {
    "Citronnade": "Citronnade is a French beverage that translates to 'lemonade' in English. It is a refreshing and citrusy drink made primarily from lemons, sugar, and water.",
    "Eau de Rose": "Eau de Rose (Rose Water) is a French drink made by infusing rose petals in water, capturing the essence of fresh roses in a refreshing and aromatic beverage. This floral-infused water is known for its delicate and fragrant taste, often enjoyed chilled as a light and elegant drink.",
    "Limonade": "Limonade typically involves combining lemonade with fresh mint leaves, creating a drink that is both citrusy and minty, offering a refreshing and aromatic experience.",
    "Melon Mint Cooler": "Melon Mint Cooler is a tasty and refreshing drink made with sweet melon and fresh mint. It's a perfect balance of fruity and minty flavors, great for cooling down on a hot day. With fresh melon, mint leaves, ice, and a touch of lime, it's a delicious and hydrating beverage for any occasion.",
    "Cherry Citrus Splash": "Cherry Citrus Splash is a fruity and refreshing beverage that combines the sweet and tart flavors of cherries with the bright citrusy notes of lemon, lime, or orange. This drink typically includes cherry juice or fresh cherries, along with citrus juice, sparkling water, and perhaps a sweetener like sugar or honey."
}

# Function to display recommended drinks with images and descriptions
def display_recommended_drinks(recommended_drinks, image_mapping, description_mapping, header_size="small"):
    if header_size == "small":
        st.markdown("<h3>Drinks</h3>", unsafe_allow_html=True)
    elif header_size == "medium":
        st.markdown("<h2>Drinks</h2>", unsafe_allow_html=True)
    elif header_size == "large":
        st.markdown("<h1>Drinks</h1>", unsafe_allow_html=True)
    for drink, prediction in recommended_drinks.items():
        if prediction == 1:
            st.markdown(f"**{drink}**")
            image_path = image_mapping.get(drink, "C:\\Users\\PARTHIVI\\OneDrive\\Desktop\\PROJECT\\mini bomb\\default.jpg")
            with open(image_path, "rb") as img_file:
                img = Image.open(img_file)
                st.image(img, caption=description_mapping.get(drink, ""), use_column_width=True)

# Display recommended drinks with images and descriptions
display_recommended_drinks(predictions_drinks, drink_image_mapping, drink_description_mapping, header_size="small")


# Read predictions for desserts from predict_dessert.txt
predictions_desserts = {}
with open("predict_dessert.txt", "r") as file:
    for line in file:
        parts = line.strip().split(": ")
        predictions_desserts[parts[0]] = parts[1]

# Dictionary mapping dessert names to their respective image paths
dessert_image_mapping = {
    "Creme Brulee Prediction": "C:\\Users\\PARTHIVI\\OneDrive\\Desktop\\PROJECT\\mini bomb\\Crème Brûlée.jpg",
    "Profiteroles Prediction": "C:\\Users\\PARTHIVI\\OneDrive\\Desktop\\PROJECT\\mini bomb\\Profiteroles.jpg",
    "Ile Flottante Prediction": "C:\\Users\\PARTHIVI\\OneDrive\\Desktop\\PROJECT\\mini bomb\\Île Flottante.jpg",
    "Madeleines Prediction": "C:\\Users\\PARTHIVI\\OneDrive\\Desktop\\PROJECT\\mini bomb\\Madeleines.jpg",
}

# Dictionary mapping dessert names to their respective descriptions
dessert_description_mapping = {
    "Creme Brulee Prediction": "Creme Brulee is a classic French dessert consisting of a rich custard base topped with a contrasting layer of hard caramel. It's made by baking a custard until it's set, then sprinkling sugar on top and caramelizing it under a broiler or with a torch.",
    "Profiteroles Prediction": "Profiteroles are small, round pastries made from choux dough that are typically filled with whipped cream, pastry cream, or ice cream. They're often served with chocolate sauce or caramel drizzle.",
    "Ile Flottante Prediction": "Ile Flottante, or 'Floating Island,' is a traditional French dessert featuring a delicate meringue floating on a pool of vanilla custard. The meringue is made from whipped egg whites and sugar, and the custard is flavored with vanilla bean.",
    "Madeleines Prediction": "Madeleines are small sponge cakes with a distinctive shell-like shape. They're typically flavored with lemon zest and baked in special molds, resulting in a light and fluffy texture with crispy edges."
}

# Function to display recommended desserts with descriptions and images
def display_recommended_desserts(recommended_desserts, image_mapping, description_mapping):
    st.markdown("<h3>Desserts</h3>", unsafe_allow_html=True)
    for dessert, prediction in recommended_desserts.items():
        if prediction == "Yes":
            dessert_name = dessert.replace(" Prediction", "").strip()
            st.markdown(f"**{dessert_name}**:")
            image_path = image_mapping.get(dessert, "C:\\Users\\PARTHIVI\\OneDrive\\Desktop\\PROJECT\\mini bomb\\default.jpeg")
            with open(image_path, "rb") as img_file:
                img = Image.open(img_file)
                st.image(img, caption=dessert_name, use_column_width=True)
                st.markdown(description_mapping.get(dessert, ""), unsafe_allow_html=True)

# Display recommended desserts with descriptions and images
display_recommended_desserts(predictions_desserts, dessert_image_mapping, dessert_description_mapping)
