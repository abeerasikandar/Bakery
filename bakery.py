import streamlit as st
import os

# Function to load images
def load_image(image_path, default_path):
    if os.path.exists(image_path):
        return image_path
    else:
        return default_path

# Set title
st.title("Alex Bakes")

# Load and display the logo
logo_path = load_image("lady_baker_logo.jpg", "default_logo.jpg")
st.image(logo_path, width=150)

# Menu items with prices and images
menu = {
    "Balgarian Chocolate Cake": {"price": 1500, "image": load_image("chocolate_cake.jpg", "default_cake.jpg")},
    "Red Velvet Cake": {"price": 1600, "image": load_image("red_velvet.jpg", "default_cake.jpg")},
    "Coconut Truffle Cake": {"price": 1700, "image": load_image("coconut_truffle.jpg", "default_cake.jpg")},
    "Lemon Tart": {"price": 800, "image": load_image("lemon_tart.jpg", "default_tart.jpg")},
    "Apple Pie": {"price": 900, "image": load_image("apple_pie.jpg", "default_pie.jpg")},
    "Banana Pie": {"price": 950, "image": load_image("banana_pie.jpg", "default_pie.jpg")},
    "Roasted Almonds Cake": {"price": 1400, "image": load_image("roasted_almonds.jpg", "default_cake.jpg")},
    "Salted Caramel Pie": {"price": 1100, "image": load_image("salted_caramel.jpg", "default_pie.jpg")},
    "Muffins": {"price": 500, "image": load_image("muffins.jpg", "default_muffins.jpg")},
    "Cupcakes": {"price": 600, "image": load_image("cupcakes.jpg", "default_cupcakes.jpg")},
}

# Cart
cart = []

# Display menu items
for item, details in menu.items():
    col1, col2, col3 = st.columns([1, 2, 1])
    
    with col1:
        st.image(details["image"], use_column_width=True)
    
    with col2:
        st.subheader(item)
        st.write(f"Price: PKR {details['price']}")
        if st.button(f"Add {item} to Cart"):
            cart.append(item)
            st.success(f"{item} added to cart!")
    
    with col3:
        st.write("")  # For spacing

# Checkout section
st.subheader("Your Cart")
if cart:
    for item in cart:
        st.write(item)
    st.write("Total: PKR", sum(menu[item]["price"] for item in cart))
    if st.button("Checkout"):
        st.success("Thank you for your order! A complimentary cupcake will be included.")
else:
    st.write("Your cart is empty.")

# Display complimentary cupcake
st.write("Note: A complimentary cupcake will be included with every order!")
