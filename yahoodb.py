# -*- coding: utf-8 -*-
"""
Created on Wed Nov  8 20:14:13 2023

@author: USER
"""

import requests

from bs4 import BeautifulSoup
import json
import db


url =  'https://tw.buy.yahoo.com/search/product'

header = {
    'User-Agent':
'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'

    }
    
    
param = {}

p = input('請輸入查詢的商品：')

param['p'] = p


data = requests.get(url,params=param,headers=header).text


soup = BeautifulSoup(data,'html.parser')


ul = soup.find(id='isoredux-data').get('data-state')

goods = json.loads(ul)

searchgoods = goods['search']['ecsearch']['hits']

for item in searchgoods:
    info = item['ec_description']
    
    if item['pres_data'].get('pictureurl') != None:
    
        photo = item['pres_data']['pictureurl']
        
        
        
        if len(item['ec_promotional_item']) == 0:
        
            price = item['pres_data']['creditprice']
        else:
            price = item['ec_promotional_item'][0]['promo_price']
        
        
        
        
        link = item['pres_data']['producturl']
        title = item['pres_data']['productname_disp']
        
        
        sql = "select * from goods where platform='Yahoo' and title='{}'".format(title)
        
        db.cursor.execute(sql)
        
        if db.cursor.rowcount == 0:
            
            sql= "insert into goods(title,price,photo_url,link_url,description,platform) values('{}','{}','{}','{}','{}','Yahoo')".format(title,price,photo,link,info)
            db.cursor.execute(sql)
            db.conn.commit()
        
        
db.conn.close()


                     




