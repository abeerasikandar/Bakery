import streamlit as st

# Custom CSS to style the app
st.markdown(
    """
    <style>
    .title {
        color: #FF69B4;  /* Pink color for the title */
        font-size: 50px;
        text-align: center;
    }
    .menu-item {
        background-color: #F0E68C;  /* Light yellow for menu items */
        border: 2px solid #FFD700;   /* Gold border */
        border-radius: 10px;
        padding: 10px;
        margin: 10px;
    }
    .cart {
        background-color: #E6E6FA;  /* Lavender for cart */
        border: 2px solid #9370DB;   /* Medium purple border */
        border-radius: 10px;
        padding: 10px;
        margin: 10px;
    }
    .button {
        background-color: #FF7F50;  /* Coral color for buttons */
        color: white;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Set title
st.markdown("<h1 class='title'>🍰 Alex Bakes 🍰</h1>", unsafe_allow_html=True)

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
        st.markdown(
            f"<div class='menu-item'>"
            f"<h3>{details['icon']} {item}</h3>"
            f"<p><strong>Price:</strong> PKR {details['price']}</p>"
        , unsafe_allow_html=True)
        
        if st.button(f"Add {item} to Cart", key=item, help=f"Add {item} to your cart"):
            cart.append(item)
            st.success(f"{item} added to cart!", icon="✅")
        st.markdown("</div>", unsafe_allow_html=True)

# Checkout section
st.subheader("🛒 Your Cart")
with st.container():
    if cart:
        st.markdown("<div class='cart'>", unsafe_allow_html=True)
        for item in cart:
            st.write(item)
        total_price = sum(details["price"] for item in cart for details in [menu[item]])
        st.write("**Total:** PKR", total_price)
        
        if st.button("Checkout"):
            st.success("🎊 Thank you for your order! A complimentary cupcake will be included. 🎊", icon="🎉")
        st.markdown("</div>", unsafe_allow_html=True)
    else:
        st.write("Your cart is empty.")

# Display complimentary cupcake note
st.write("🧁 **Note:** A complimentary cupcake will be included with every order!")
