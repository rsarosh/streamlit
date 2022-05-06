import streamlit as st
from auth import *


if __name__ == '__main__':
    st.title("Streamlit Oauth Login")
    st.write(get_login_str(), unsafe_allow_html=True)
        
    if st.button("display user"):  
        display_user()