#!/usr/bin/python

import mysql.connector
from datetime import date, datetime, timedelta

cnx = mysql.connector.connect(user='vpalladi', password='vito8a82', database='testRiki')

cursor = cnx.cursor()

id_to_remove = 11

delete_order = ("DELETE FROM orders WHERE id LIKE '%s'") %(id_to_remove)

cursor.execute(delete_order)

cnx.commit()

cursor.close()
cnx.close()
