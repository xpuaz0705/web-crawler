# -*- coding: utf-8 -*-
"""
Created on Fri Nov 10 21:12:24 2023

@author: USER
"""

import db

startp = int(input('請輸入初始價格：'))
endp = int(input('請輸入終止價格：'))

p = input('請輸入商品：')

if p == '':
    sql = "select title,price,link_url,description from goods where price between {} and {} ".format(startp,endp)
else:
    sql = "select title,price,link_url,description from goods where price between {} and {} and title like '%{}%' ".format(startp,endp,p)
    
    
db.cursor.execute(sql)

result = db.cursor.fetchall()

for  item in result:
    print(item[0])    
    print(item[1])
    print(item[2])
    print(item[3])
    print()    
    