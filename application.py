import os
from flask import Flask
from flask import render_template



app = Flask(__name__)

@app.route('/')
@app.route('/index')
def homepage():
    return render_template('homepage.html')


@app.route('/profile')
def profile():
    return render_template('profile.html')

@app.route('/bios')
def bios():
    return render_template('bios.html')

@app.route('/partners')
def partners():
    return render_template('partners.html')
	
@app.route('/slideshow')
def slideshow():
    return render_template('slideshow.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/ecotable')
def products():
    return render_template('ecotable.html')

@app.route('/projects')
def projects():
    return render_template('projects.html')
	
@app.route('/projects_copy')
def projects_copy():
    return render_template('projects_copy.html')

@app.route('/learn')
def learn():
    return render_template('learn.html')

@app.route('/store')
def store():
    return render_template('store.html')

@app.route('/blog')
def blog():
    return render_template('blog.html')

@app.route('/events')
def events():
    return render_template('events.html')

@app.route('/sustainability')
def sustainability():
    return render_template('sustainability.html')

@app.route('/angolaslide')
def angolaslide():
    return render_template('angolaslide.html')

@app.route('/phillyearthslide')
def phillyearthslide():
    return render_template('phillyearthslide.html')

@app.route('/weaverswayslide')
def weaverswayslide():
    return render_template('weaverswayslide.html')

@app.route('/classes')
def classes():
    return render_template('classes.html')

@app.route('/press')
def press():
    return render_template('press.html')
