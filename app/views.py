from flask import render_template, url_for
from app import app


@app.route('/')
@app.route('/index')
def index():
	return render_template('index.html')

@app.route('/about')
def about():
	return render_template('about.html')

@app.route('/board')
def board():
	return render_template('board.html')

@app.route('/chem-e-car')
def chem_e_car():
	return render_template('chem_e_car.html')

@app.route('/mentorship-family')
def mentorship_family():
	return render_template('mentorship_family.html')

@app.route('/sponsors')
def sponsors():
	return render_template('sponsors.html')