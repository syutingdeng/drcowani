"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import render_template,request
from anime import app
from anime.main import newani
from flask import jsonify
from google.oauth2 import id_token
from google.auth.transport import requests
import sqlite3

mail=" "
@app.route('/')
@app.route('/home')
def home():
    """Renders the home page."""
    return render_template(
        'index.html',
        title='Home Page',
        year=datetime.now().year,
    )
@app.route('/new')
def new():
    return jsonify(result0=newani(0,0),img0=newani(0,1),href0=newani(0,2),
                              result1=newani(1,0),img1=newani(1,1),href1=newani(1,2),
                              result2=newani(2,0),img2=newani(2,1),href2=newani(2,2),
                              result3=newani(3,0),img3=newani(3,1),href3=newani(3,2))


@app.route('/myanime')
def myanime():
    """Renders the contact page."""
    try:
        db=sqlite3.connect("./anime/anime.sqlite3")
        c = db.cursor()
        c.execute("select * from ani where mail=?",[mail])
        ret = c.fetchall()
        print(ret[0])
        db.commit()
        db.close()
        return render_template(
            'myani.html',
            title='近期瀏覽',
        
        )
    except:
        return ("login error")

@app.route('/google_sign_in', methods=['POST'])
def google_sign_in():
    mail = str(request.json['email'])
    print("郵件"+mail)
    return "ok"


#db=sqlite3.connect("./anime/anime.sqlite3")
#c = db.cursor()
#c.execute("select * from ani where mail=?",(mail))
#db.commit()
#db.close()

