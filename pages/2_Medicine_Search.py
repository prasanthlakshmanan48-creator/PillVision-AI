import streamlit as st

st.title("📖 Medicine Search")

medicine = st.text_input("Enter Medicine Name")

if st.button("Search"):

    st.write("Medicine:", medicine)

    st.info("AI search will be added in Version 2.")
