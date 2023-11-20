# -*- coding: utf-8 -*-
"""
Created on Fri Nov 10 20:07:12 2023

@author: USER
"""

import db

search = input('請輸入新聞關鍵字：')

sql = "select platform,title,link_url from news where title like '%{}%'".format(search)


db.cursor.execute(sql)

result = db.cursor.fetchall()

for  item in result:
    print(item[0])    
    print(item[1])
    print(item[2])
    print()



