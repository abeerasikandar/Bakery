import streamlit as st
from PIL import Image
import requests
from io import BytesIO

# Set title
st.title("🍰 Alex Bakes 🍰")

# Menu items with prices and icons
menu = {
    "Balgarian Chocolate Cake": {"price": 1500, "icon": "🍫"},
    "Red Velvet Cake": {"price": 1600, "icon": "🍰"},
    "Coconut Truffle Cake": {"price": 1700, "icon": "🥥"},
    "Lemon Tart": {"price": 800, "icon": "🍋"},
    "Apple Pie": {"price": 900, "icon": "🍏"},
    "Banana Pie": {"price": 950, "icon": "🍌"},
    "Roasted Almonds Cake": {"price": 1400, "icon": "🌰"},
    "Salted Caramel Pie": {"price": 1100, "icon": "🧂"},
    "Muffins": {"price": 500, "icon": "🧁"},
    "Cupcakes": {"price": 600, "icon": "🧁"},
}

# Cart
cart = []

# Display menu items in a grid layout
st.subheader("🎉 Menu 🎉")
cols = st.columns(3)  # Create three columns for the layout

for index, (item, details) in enumerate(menu.items()):
    with cols[index % 3]:  # Cycle through columns
        st.markdown(f"### {details['icon']} {item}")
        st.write(f"**Price:** PKR {details['price']}")
        if st.button(f"Add {item} to Cart"):
            cart.append(item)
            st.success(f"{item} added to cart!")

# Checkout section
st.subheader("🛒 Your Cart")
if cart:
    for item in cart:
        st.write(item)
    total_price = sum(details["price"] for item in cart for details in [menu[item]])
    st.write("**Total:** PKR", total_price)
    if st.button("Checkout"):
        st.success("🎊 Thank you for your order! A complimentary cupcake will be included. 🎊")
else:
    st.write("Your cart is empty.")

# Display complimentary cupcake note
st.write("🧁 **Note:** A complimentary cupcake will be included with every order!")
