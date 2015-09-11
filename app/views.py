from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    page = "indexPage"
    user = {'nickname':'NotKevin'}
    choices = [
        { 'quote':'This a quote from Footloose',
            'image':'footloose.jpg' },
        { 'quote':'This is a quote from Tremors',
            'image':'tremors.jpg' },
        { 'quote':'This is a quote from Hollow Man',
            'image':'hollow_man.jpg' }]
    return render_template('index.html',title='Home',user=user,choices=choices,page=page)

@app.route('/cats')
def cats():
    page = "catsPage"
    return render_template('here_is_a_cat.html',title="A cat at 200px by 400px",page=page)

@app.route('/about')
def about():
    page = "aboutPage"
    return render_template("about.html",title="About the Site",page=page)