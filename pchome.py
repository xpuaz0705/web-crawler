# -*- coding: utf-8 -*-
"""
Created on Mon Oct 30 20:34:54 2023

@author: USER
"""

import requests
import json
import db



header = {
    'User-Agent':
'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'
    }

url = "https://ecshweb.pchome.com.tw/search/v4.3/all/results"

for i in range(1,5):

    param = {
        'q': '登機箱',
    'page': i,
    'sort': 'rnk/dc'
        }
    
    
    
    data = requests.get(url,headers=header,params=param).text
    
    pchome = json.loads(data)
    
    goods =  pchome['Prods']
    
    
    for item in goods:
        
        link = "https://24h.pchome.com.tw/prod/" + item['Id']
        
        title = item['Name']
        photo = "https://cs-b.ecimg.tw" + item['PicB']
        price = item['Price']
        info = item['Describe']
        
        
        
        sql = "select * from goods where platform='Pchome' and title='{}'".format(title)
        
        db.cursor.execute(sql)
        
        if db.cursor.rowcount == 0:
            
            sql= "insert into goods(title,price,photo_url,link_url,description,platform) values('{}','{}','{}','{}','{}','Pchome')".format(title,price,photo,link,info)
            db.cursor.execute(sql)
            db.conn.commit()
        
        
db.conn.close()        
        
        
        

    
    
    

