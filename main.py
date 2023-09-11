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

if __name__ == '__main__':
    app.run(debug=True)



