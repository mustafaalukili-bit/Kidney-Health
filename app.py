import streamlit as st

st.markdown("""
    <style>
    /* إخفاء القائمة العلوية وشريط التذييل */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    /* جعل الخلفية بيضاء نقية */
    .stApp {background-color: #f8f9fa;}
    </style>
""", unsafe_allow_html=True)
