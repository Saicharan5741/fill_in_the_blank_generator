import streamlit as st
import re

if 'step' not in st.session_state:
    st.session_state.step = 1


st.markdown(
    """
    <style>
    .stApp {
        background-color: #f0f0f0;
        font-family: 'Poppins', sans-serif;
    }
    .stTitle {
        color: #3498db;
    }
    .stApp {
        background-image: linear-gradient(135deg, #a8edea 10%, #fed6e3 100%);
       color: black;
    }
        input[data-baseweb="input"] {
        background: linear-gradient(45deg, #3498db, #e74c3c) !important;
        color: black !important;
        border: none !important; 
        border-radius: 8px !important;
        padding: 0.5rem !important; 
    }
    
    select[data-baseweb="select"] {
        background: linear-gradient(45deg, #3498db, #e74c3c) !important;
        color: black !important; 
        border: none !important; 
        border-radius: 8px !important; 
        padding: 0.5rem !important; 
    }
    .footer{
    font-family: 'Poppins', sans-serif;
    color: purple;
    }
    </style>
     
    </style>
    """,
    unsafe_allow_html=True
)

# Page 1
if st.session_state.step == 1:
    st.markdown("<h1 class='stTitle'>Interactive Gaps Adder</h1>", unsafe_allow_html=True)

    text = st.text_area("Enter text:")
    if st.button("Next", key="page1_next_button"):
        words = text.split()
        st.session_state.words = words
        st.session_state.text = text
        st.session_state.step = 2
       

# Page 2
elif st.session_state.step == 2:
    st.markdown("<h1 class='stTitle'>Fill in the Blank Generator </h1>", unsafe_allow_html=True)

    st.subheader("Select a random word from the input:")
    selected_word = st.selectbox("Choose a word:", st.session_state.words)
    if st.button("Submit", key="page2_submit_button"):
        text = st.session_state.text
        result = re.sub(r'\b' + re.escape(selected_word) + r'\b', "___", text)
        st.session_state.result = result
        st.session_state.step = 3

    
    if st.button("Go Back", key="page2_go_back_button"):
        st.session_state.step = 1

# Page 3
elif st.session_state.step == 3:
    st.markdown("<h1 class='stTitle'>Fill in the Blank Generator </h1>", unsafe_allow_html=True)

    st.subheader("The Output:")
    st.write(st.session_state.result)

   
    if st.button("Go Back", key="page3_go_back_button"):
        st.session_state.step = 2
st.markdown("<div class='footer'>Designed by Sai Charan Rapaka</div>", unsafe_allow_html=True) 






