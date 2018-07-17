#!/usr/bin/python

import mysql.connector
from datetime import date, datetime, timedelta

cnx = mysql.connector.connect(user='vpalladi', password='vito8a82', database='testRiki')

cursor = cnx.cursor()

cursor.execute( 'SET FOREIGN_KEY_CHECKS=0' )

tables=[
    'DROP TABLE IF EXISTS production ',
    'DROP TABLE IF EXISTS machines_operators ',
    'DROP TABLE IF EXISTS machines_components',
    'DROP TABLE IF EXISTS clients            ',
    'DROP TABLE IF EXISTS components         ',
    'DROP TABLE IF EXISTS machines           ',
    'DROP TABLE IF EXISTS operators          ',
    'DROP TABLE IF EXISTS orders             '
]


for table in tables :
    cursor.execute( table )
    
cursor.execute( 'SET FOREIGN_KEY_CHECKS=1' )

cnx.commit()

cursor.close()
cnx.close()
