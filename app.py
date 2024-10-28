import streamlit as st
from src.healthllama.healthllama import get_response

# Streamlit app design
st.set_page_config(page_title="Medical Chatbot", page_icon="💬")

# Title of the app
st.title("Medical Chatbot 💬")
st.subheader("Ask your medical-related questions here!")

# Description
st.write("This chatbot uses LLaMA2 to answer your medical questions. Please note that the information provided is for general guidance, and you should always consult a healthcare provider for serious concerns.")

# User input field for medical query
user_input = st.text_area("Enter your query :", placeholder="Describe your symptoms or ask about a medical condition...")

# Button to submit query
if st.button("Get Response"):
    # If input is provided
    if user_input.strip():
        # Display a loading spinner while generating the response
        with st.spinner("Generating response..."):
            # Call the LLaMA2 model function to get the response
            response = get_response(user_input)
            
            # Display the response in the UI
            st.success("Here’s what I found:")
            st.write(response)
    else:
        # Error message if no input is provided
        st.error("Please enter a query to get a response.")

# Disclaimer at the bottom
st.write("**Disclaimer**: The information provided by this chatbot is for general informational purposes only. Always consult a healthcare provider for an accurate diagnosis and professional advice.")
