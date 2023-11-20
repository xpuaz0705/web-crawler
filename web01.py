# -*- coding: utf-8 -*-
"""
Created on Fri Nov 10 21:25:09 2023

@author: USER
"""

from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '首頁'

@app.route('/news')
def lccgood():
    return '新聞'


app.run()