#!/usr/bin/python

import mysql.connector
from datetime import date, datetime, timedelta

cnx = mysql.connector.connect(user='vpalladi', password='vito8a82', database='testRiki')

cursor = cnx.cursor()

query = ("SELECT first_name, last_name, hire_date FROM employees "
           "WHERE hire_date BETWEEN %s AND %s")

myQuery = ("SELECT m.id, m.name FROM operators o " 
           "INNER JOIN machines_operators mo ON mo.operator_id = o.id " 
           "INNER JOIN machines m ON m.id = mo.machine_id "
           "WHERE o.name = %s and o.surname = %s")
cursor.execute(myQuery, ('riccardo', 'di'))
for c in cursor:
    print c
print '########################'

myQuery = ("SELECT m.id, m.name FROM orders ord "
           "INNER JOIN components c ON c.id = ord.component_id "
           "INNER JOIN machines_components mc ON mc.component_id = c.id "
           "INNER JOIN machines m ON m.id = mc.machine_id "
           "WHERE ord.id = 6 ")
cursor.execute( myQuery )
for c in cursor:
    print c

cursor.close()
cnx.close()
