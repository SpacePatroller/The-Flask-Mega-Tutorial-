
from flask import render_template
#importing the Flask module from _init_.py
from app import app

@app.route('/')

@app.route('/home')
def home():
    return render_template('base.html')
    
@app.route('/index')
def index():
    user = {'username': 'Emanshu'}
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        }
    ]
    return render_template('index.html',user=user, posts=posts)


