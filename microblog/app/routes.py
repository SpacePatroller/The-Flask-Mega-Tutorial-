#importing the Flask module from _init_.py
from app import app

@app.route('/')
@app.route('/index')
def index():
    return "Hello, World!"

