import streamlit as st
import re

# Page 1
st.title("Fill in the Blank Generator")
text = st.text_area("Enter text:")
if st.button("Next"):
    words = text.split()
    st.session_state['words'] = words
    st.session_state['text'] = text
    st.session_state['step'] = 2

# Page 2
if st.session_state.get('step') == 2:
    st.subheader("Select a random word from the input:")
    selected_word = st.selectbox("Choose a word:", st.session_state['words'])
    if st.button("Submit"):
        text = st.session_state['text']
        result = re.sub(r'\b' + re.escape(selected_word) + r'\b', "___", text)
        st.session_state['result'] = result
        st.session_state['step'] = 3

# Page 3
if st.session_state.get('step') == 3:
    st.subheader("The random clicked word is replaced with:")
    st.write(st.session_state['result'])

# You can add a "Go Back" button if needed
if st.button("Go Back"):
    st.session_state['step'] -= 1







