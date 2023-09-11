import streamlit as st 
import requests
from flask import Flask, render_template, request, redirect, url_for
import random
import re

app = Flask(__name__)

@app.route('/')
def page1():
    return render_template('index.html')

@app.route('/page2', methods=['POST'])
def page2():
    text = request.form['text']
    words = text.split()
    return render_template('page2.html', words=words, text=text)

@app.route('/page3', methods=['POST'])
def page3():
    selected_word = request.form['selected_word']
    text = request.form['text']
    result = re.sub(r'\b' + re.escape(selected_word) + r'\b', "___", text)
    return render_template('page3.html', result=result)
def main():
    st.title('Streamlit Frontend for Flask API')
    response = requests.get('http://localhost:5000/api/data')
    data = response.json()
    st.write(f"Data from Flask API: {data['data']}")



if __name__ == '__main__':
    app.run(debug=True)








