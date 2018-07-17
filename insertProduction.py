#!/usr/bin/python

import mysql.connector
from datetime import date, datetime, timedelta


def exec_cmd(cnx, cursor, cmd, opt):
    cursor.execute(cmd, opt)
    cnx.commit()


def add_batch(cnx, cursor, order_id, date, quantity ):
    cmd = ("INSERT INTO production "
           "(order_id, date, quantity)"
           "VALUES (%s, %s, %s)")
    
    opt = (order_id, date, quantity)

    exec_cmd(cnx, cursor, cmd, opt)

### connetc to DB
cnx = mysql.connector.connect(user='vpalladi', password='vito8a82', database='testRiki')

### get the cursor
cursor = cnx.cursor()

add_batch(cnx, cursor, 1, datetime.now(), 100 )
add_batch(cnx, cursor, 2, datetime.now(), 100 )
add_batch(cnx, cursor, 3, datetime.now(), 10  )
add_batch(cnx, cursor, 4, datetime.now(), 100 ) 

add_batch(cnx, cursor, 1, datetime.now(), 101 )
add_batch(cnx, cursor, 2, datetime.now(), 101 )
add_batch(cnx, cursor, 3, datetime.now(), 101 )
add_batch(cnx, cursor, 4, datetime.now(), 101 )

cursor.close()
cnx.close()




