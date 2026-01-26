import streamlit as st

st.title("E-Rickshaw 24/7 - Barpeta, Assam")
st.write("Welcome to the E-Rickshaw Registration System.")

name = st.text_input("Enter Driver Name:")
phone = st.text_input("Enter Phone Number:")

if st.button("Register"):
    st.success(f"Driver {name} registered successfully!")
