import streamlit as st

# Logo and app title
st.image("lady_baker_logo.jpg", width=150)  # Add your bakery logo here
st.title("Alex Bakes 🍰")
st.subheader("Delicious Baked Goods, Delivered Fresh to Your Door")

# Bakery menu with prices and images
menu = {
    "Balgarian Chocolate Cake": {"price": 1500, "image": "chocolate_cake.jpg"},
    "Red Velvet Cake": {"price": 1800, "image": "red_velvet.jpg"},
    "Coconut Truffle Cake": {"price": 1600, "image": "coconut_truffle.jpg"},
    "Lemon Tart": {"price": 500, "image": "lemon_tart.jpg"},
    "Apple Pie": {"price": 600, "image": "apple_pie.jpg"},
    "Banana Pie": {"price": 550, "image": "banana_pie.jpg"},
    "Roasted Almonds Cake": {"price": 1700, "image": "roasted_almonds.jpg"},
    "Salted Caramel Pie": {"price": 700, "image": "salted_caramel.jpg"},
    "Muffins (Mixed Flavors)": {"price": 300, "image": "muffins.jpg"},
    "Cupcakes (Mixed Flavors)": {"price": 250, "image": "cupcakes.jpg"}
}

# Shopping cart
cart = []

# Display the menu with prices and images
st.subheader("Menu")
for item, details in menu.items():
    col1, col2 = st.columns([1, 2])
    with col1:
        st.image(details["image"], width=120)  # Add the image for the menu item
    with col2:
        st.write(f"**{item}** - Rs {details['price']}")
        if st.button(f"Add {item} to cart", key=item):
            cart.append((item, details["price"]))
            st.success(f"{item} added to cart!")

# Show cart items and total
st.subheader("Your Cart")
if cart:
    total = 0
    for item, price in cart:
        st.write(f"{item}: Rs {price}")
        total += price
    st.write(f"**Total (without shipping): Rs {total}**")

    # Ask for the customer's location
    location = st.text_input("Enter your city for shipping", "")

    # Add free shipping for Islamabad
    shipping = 0 if location.lower() == "islamabad" else 200
    st.write(f"**Shipping Cost: Rs {shipping}**")
    st.write("Note: Free shipping is available only for Islamabad.")
    
    # Add a complimentary cupcake
    st.write("**Complimentary Cupcake added! 🍰**")

    # Final total
    final_total = total + shipping
    st.write(f"**Final Total: Rs {final_total}**")

    # Checkout button
    if st.button("Checkout"):
        st.success(f"Order confirmed! Your total is Rs {final_total}. Thank you for shopping at Alex Bakes!")
else:
    st.write("Your cart is empty. Add some items to start!")

# Footer
st.write("---")
st.write("Made with ❤️ by Alex Bakes. Freshly baked for you!")
