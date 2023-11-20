# -*- coding: utf-8 -*-
"""
Created on Fri Nov 10 21:25:09 2023

@author: USER
"""

from flask import Flask,render_template,request,redirect,url_for
import db

from flask_paginate import Pagination,get_page_parameter;

from datetime import datetime


app = Flask(__name__)

@app.route('/')
def index():
    sql = "select title,link_url from news where platform='tvbs' order by id desc limit 9"
    db.cursor.execute(sql)
    
    news = db.cursor.fetchall()
    
    sql = "select title,price,link_url,description,photo_url from goods where platform='yahoo' order by price limit 3"
    db.cursor.execute(sql)
    
    yahoo = db.cursor.fetchall()
    
    sql = "select title,price,link_url,description,photo_url from goods where platform='pchome' order by price limit 3"
    db.cursor.execute(sql)
    
    pchome = db.cursor.fetchall()
    
    
    return render_template('index.html',**locals())



@app.route('/news')
def news():
    
    page = int(request.args.get('page',1))
    
    sql = "select count(*) as c from news"
    
    db.cursor.execute(sql)
    datacount = db.cursor.fetchone()
    count = int(datacount[0])
    
    if page == 1:
        sql = "select platform,title,link_url,photo_url from news limit 36"
    else:
        startp = page - 1
        sql = "select platform,title,link_url,photo_url from news limit {},{}".format(startp*36,36) 
        
    db.cursor.execute(sql)
    
    result = db.cursor.fetchall()
    
    pagination = Pagination(page=page,total=count,per_page=36)
    
    
    
    return render_template('news.html',**locals())
    
    
    
    
@app.route('/goods')    
def goods():
    p= request.args.get('p','')    
    startp = request.args.get('startp','')
    endp = request.args.get('endp','')
    
    
   

    if len(p) == 0 and len(startp) == 0 and len(endp) == 0:
        sql = "select title,price,link_url,description,photo_url from goods order by price"    
    
    elif len(p) > 0 and len(startp) == 0 and len(endp) == 0:
        sql = "select title,price,link_url,description,photo_url from goods where title like '%{}%' ".format(p)
    
    elif len(p) == 0 and len(startp) > 0 and len(endp) > 0:
        sql = "select title,price,link_url,description,photo_url from goods where price between {} and {} ".format(startp,endp)
    else:
        sql = "select title,price,link_url,description,photo_url from goods where price between {} and {} and title like '%{}%' ".format(startp,endp,p)
        
        
    db.cursor.execute(sql)
    
    result = db.cursor.fetchall()
    
    return render_template('product.html',**locals())



@app.route('/product/<string:p>')
def product(p):
    sql = "select title,price,link_url,description,photo_url from goods where title like '%{}%' ".format(p)
    db.cursor.execute(sql)
    
    result = db.cursor.fetchall()
    
    return render_template('product.html',**locals())



@app.route('/contact')
def message():
    return render_template("contact.html")

@app.route("/addcontact",methods=['POST'])
def contact():
    if request.method == 'POST':
        username = request.form.get('name','')
        email = request.form.get('email')
        title = request.form.get('title')
        content = request.form.get('content')
        today = datetime.today()
        c_date = datetime.strftime(today, '%Y-%m-%d')
        
        sql = "insert into contact(subject,name,email,content,create_date) values('{}','{}','{}','{}','{}')".format(title,username,email,content,c_date)
        
        db.cursor.execute(sql)
        db.conn.commit()
        
    return redirect(url_for('message'))    












app.run()