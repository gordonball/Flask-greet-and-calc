from flask import Flask
app = Flask(__name__)



@app.get('/welcome')
def say_welcome():
    """ Returns 'welcome' """
    html = "<html><body><h1>'welcome'</h1><body></html"
    return html



@app.get('/welcome/home')
def say_welcome_home():
    """ Returns 'welcome home' """
    html = "<html><body><h1>'welcome home'</h1><body></html"
    return html



@app.get('/welcome/back')
def say_welcome_back():
    """ Returns 'welcome back' """
    html = "<html><body><h1>'welcome back'</h1><body></html"
    return html