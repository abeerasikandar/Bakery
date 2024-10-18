import streamlit as st

# Set title
st.title("Alex Bakes")

# Menu items with prices
menu = {
    "Balgarian Chocolate Cake": 1500,
    "Red Velvet Cake": 1600,
    "Coconut Truffle Cake": 1700,
    "Lemon Tart": 800,
    "Apple Pie": 900,
    "Banana Pie": 950,
    "Roasted Almonds Cake": 1400,
    "Salted Caramel Pie": 1100,
    "Muffins": 500,
    "Cupcakes": 600,
}

# Cart
cart = []

# Display menu items
st.subheader("Menu")
for item, price in menu.items():
    col1, col2, col3 = st.columns([1, 2, 1])
    
    with col1:
        st.write("")  # Placeholder for image
    
    with col2:
        st.subheader(item)
        st.write(f"Price: PKR {price}")
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
    total_price = sum(menu[item] for item in cart)
    st.write("Total: PKR", total_price)
    if st.button("Checkout"):
        st.success("Thank you for your order! A complimentary cupcake will be included.")
else:
    st.write("Your cart is empty.")

# Display complimentary cupcake note
st.write("Note: A complimentary cupcake will be included with every order!")
