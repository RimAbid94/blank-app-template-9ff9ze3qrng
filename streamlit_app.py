import streamlit as st
import panel as pn

st.title("🎈 My new app")

# Create a Panel widget
cylinders = pn.widgets.IntSlider(name='Cylinders', start=4, end=8, step=2)

# Display the widget using Streamlit's HTML capabilities
st.write("Select number of cylinders:")
st.write(cylinders)

# Serve the Panel widget using its own server
if st.button("Run Panel server"):
    pn.serve(cylinders)
