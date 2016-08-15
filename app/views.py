# -*- coding: utf-8 -*-
from flask import render_template, url_for, send_from_directory
from app import app
import os


@app.route('/')
@app.route('/index')
def index():
    officers = [
        {'name':'Jennifer Chao', 'position':'President', 'email':'jfchao@ucdavis.edu', 'source': 'Jennifer-Chao.png'},
        {'name':'Daniel Kriozere', 'position':'External Vice President', 'email':'djkriozere@ucdavis.edu', 'source': 'Daniel-Kriozere.png'},
        {'name':'Maddi Stadtmueller', 'position':'Internal Vice President', 'email':'mlstadtmueller@ucdavis.edu', 'source': 'Maddi-Stadtmueller.png'},
        {'name':'Randy Xie', 'position':'Treasurer', 'email':'ranxie@ucdavis.edu', 'source': 'Randy-Xie.png'},
        {'name':'Alex Chen', 'position':'Secretary', 'email':'alxchen@ucdavis.edu', 'source': 'Alex-Chen.png'},
        {'name':'Nithya Kumar', 'position':'Student Liaison', 'email':'nkumar@ucdavis.edu', 'source': 'Nithya-Kumar.png'},
        {'name':'Nadia Duenas', 'position':'Presidential Adviser', 'email':'nduenas@ucdavis.edu', 'source': 'Nadia-Duenas.png'},
        {'name':'Tassia El-Sayed', 'position':'Senior Representative', 'email':'trelsayed@ucdavis.edu', 'source': 'Tassia-El-Sayed.png'},
        {'name':'Jacob Saudan', 'position':'Senior Representative', 'email':'jssaudan@ucdavis.edu', 'source': 'Jacob-Saudan.png'},
        {'name':'Grace Chan', 'position':'Senior Representative', 'email':'grchan@ucdavis.edu', 'source': 'Grace-Chan.png'},
        {'name':'Michelle Banh', 'position':'Junior Representative', 'email':'mybanh@ucdavis.edu', 'source': 'Michelle-Banh.png'},
        {'name':'Benjamin Quach', 'position':'Junior Representative', 'email':'bvquach@ucdavis.edu', 'source': 'Benjamin-Quach.png'},
        {'name':'David Maginnis', 'position':'Junior Representative', 'email':'damaginnis@ucdavis.edu', 'source': 'David-Maginnis.png'},
        {'name':'Carlos Alcantara', 'position':'Junior Representative', 'email':'calcantara@ucdavis.edu', 'source': 'Carlos-Alcantara.png'},
        {'name':'Peggy Palsgaard', 'position':'Sophomore Representative', 'email':'pkpalsgaard@ucdavis.edu', 'source': 'Peggy-Palsgaard.png'},
        {'name':'Stanford Atmadja', 'position':'Sophomore Representative', 'email':'ssatmadja@ucdavis.edu', 'source': 'Stanford-Atmadja.png'},
        {'name':'Yepu Xie', 'position':'Sophomore Representative', 'email':'ypxie@ucdavis.edu', 'source': 'Yepu-Xie.png'},
        {'name':'Andrea Kattan', 'position':'Sophomore Representative', 'email':'ajkattan@ucdavis.edu', 'source': 'Andrea-Kattan.png'},
        {'name':'Kevin Tang', 'position':'Freshman Representative', 'email':'ketang@ucdavis.edu', 'source': 'Kevin-Tang.png'},
        {'name':'Amanda Chun', 'position':'Freshman Representative', 'email':'aschun@ucdavis.edu', 'source': 'Amanda-Chun.png'},
        {'name':'Andres Perez', 'position':'Freshman Representative', 'email':'apere@ucdavis.edu', 'source': 'Andres-Perez.png'},
        {'name':'Daron Fong', 'position':'EC Representative', 'email':'dkyfong@ucdavis.edu', 'source': 'Daron-Fong.png'},
        {'name':'Tyson Coffey', 'position':'EC Representative', 'email':'tecoffey@ucdavis.edu', 'source': 'Tyson-Coffey.png'},
        {'name':'Olivia Sullivan', 'position':'EC Representative', 'email':'oksullivan@ucdavis.edu', 'source': 'Olivia-Sullivan.png'},
        {'name':'Carlos Rangel', 'position':'Industry Representative', 'email':'carangel@ucdavis.edu', 'source': 'Carlos-Rangel.png'},
        {'name':'Edgar Hernandez', 'position':'Chem-E-Car Coordinator', 'email':'udahernandez@ucdavis.edu', 'source': 'Edgar-Hernandez.png'},
        {'name':'Andrew Ho', 'position':'Chem-E-Car Coordinator', 'email':'andho@ucdavis.edu', 'source': 'Andrew-Ho.png'},
        {'name':'Nicholas DiPressi', 'position':'Chem-E-Car Coordinator', 'email':'ncdipressi@ucdavis.edu', 'source': 'Nicholas-DiPressi.png'},
        {'name':'Andy Huynh', 'position':'Chem-E-Car Coordinator', 'email':'andhuynh@ucdavis.edu', 'source': 'Andy-Huynh.png'},
        {'name':'Ryan Chen', 'position':'Historian', 'email':'ryfchen@ucdavis.edu', 'source': 'Ryan-Chen.png'},
        {'name':'Aaron Kwong', 'position':'Webmaster/Historian', 'email':'atkwong@ucdavis.edu', 'source': 'Aaron-Kwong.png'}
    ]
    return render_template('index.html', officers=officers)

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

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')