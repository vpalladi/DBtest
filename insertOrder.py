#!/usr/bin/python

import mysql.connector
from datetime import date, datetime, timedelta

cnx = mysql.connector.connect(user='vpalladi', password='vito8a82', database='testRiki')

cursor = cnx.cursor()


add_order = ("INSERT INTO orders "
             "(name, date, deadline, client_id) "
             "VALUES (%s, %s, %s, %s)")

order = ('primo',
         datetime.now(),
         datetime.now().date() + timedelta(days=30),
         1
)

cursor.execute(add_order, order)

cnx.commit()

cursor.close()
cnx.close()
