#!/usr/bin/python

import mysql.connector
from mysql.connector import errorcode
from datetime import date, datetime, timedelta

cnx = mysql.connector.connect(user='vpalladi', password='vito8a82', database='testRiki')

cursor = cnx.cursor()

## map of tables
TABLES = {}

### primary tables
TABLES['clients'] = ( # add init date and end date
    "CREATE TABLE `clients` ("
    "  `id` INT NOT NULL AUTO_INCREMENT,"
    "  `name` VARCHAR(100) NOT NULL,"
    "  `address` VARCHAR(100) NOT NULL,"
    "  PRIMARY KEY (`id`)"
    ")")

TABLES['components'] = ( # add init date and end date
    "CREATE TABLE `components` ("
    "  `id` INT NOT NULL AUTO_INCREMENT,"
    "  `name` VARCHAR(100) NOT NULL,"
    "  `description` VARCHAR(100),"
    "  `manufacturer` VARCHAR(100),"
    "  PRIMARY KEY (`id`)"
    ")")


TABLES['machines'] = ( # add init date and end date
    "CREATE TABLE `machines` ("
    "  `id` INT NOT NULL AUTO_INCREMENT,"
    "  `name` VARCHAR(100),"
    "  `model` VARCHAR(100) NOT NULL,"
    "  `description` VARCHAR(100),"
    "  PRIMARY KEY (`id`)"
    ")")

TABLES['operators'] = ( # add init date and end date
    "CREATE TABLE `operators` ("
    "  `id` INT NOT NULL AUTO_INCREMENT,"
    "  `name` VARCHAR(100) NOT NULL,"
    "  `surname` VARCHAR(100) NOT NULL,"
    "  `role` VARCHAR(100),"
    "  PRIMARY KEY (`id`)"
    ")")

### create the tables ###
for name, ddl in TABLES.iteritems():
    try:
        print "Creating table \"",name,"\":"
        print " >>>",
        cursor.execute(ddl)
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
            print "Already exists."
        else:
            print err.msg
    else:
        print "Created."

TABLES={}

###### FOREIGN KEYS ######
TABLES['orders'] = (
    "CREATE TABLE `orders` ("
    "  `id` INT NOT NULL AUTO_INCREMENT,"
    "  `date` DATETIME NOT NULL,"
    "  `client_id` INT NOT NULL,"
    "  `component_id` INT NOT NULL,"
    "  `quantity` INT NOT NULL,"
    "  PRIMARY KEY (`id`),"
    "  FOREIGN KEY (client_id) REFERENCES clients(id),"
    "  FOREIGN KEY (component_id) REFERENCES components(id)"
    ")")

TABLES['machines_components'] = (
    "CREATE TABLE `machines_components` ("
    "  `machine_id` INT NOT NULL,"
    "  `component_id` INT NOT NULL,"
    "  FOREIGN KEY (`machine_id`) REFERENCES machines(`id`),"
    "  FOREIGN KEY (`component_id`) REFERENCES components(`id`),"
    "  PRIMARY KEY (`machine_id`, `component_id`)"
    ")")

TABLES['machines_operators'] = (
    "CREATE TABLE `machines_operators` ("
    "  `machine_id` INT NOT NULL,"
    "  `operator_id` INT NOT NULL,"
    "  PRIMARY KEY (`machine_id`, `operator_id`),"
    "  FOREIGN KEY (machine_id) REFERENCES machines(id),"
    "  FOREIGN KEY (operator_id) REFERENCES operators(id)"
    ")")

### create the tables ###
for name, ddl in TABLES.iteritems():
    try:
        print "Creating table \"",name,"\":"
        print " >>>",
        cursor.execute(ddl)
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
            print "Already exists."
        else:
            print err.msg
    else:
        print "Created."

TABLES={}
TABLES['production'] = (
    "CREATE TABLE `production` ("
    "  `order_id` INT NOT NULL,"
    "  `quantity` INT NOT NULL,"
    "  `date` DATETIME NOT NULL,"
    "  FOREIGN KEY (order_id) REFERENCES orders(id)"
    ")")

### create the tables ###
for name, ddl in TABLES.iteritems():
    try:
        print "Creating table \"",name,"\":"
        print " >>>",
        cursor.execute(ddl)
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
            print "Already exists."
        else:
            print err.msg
    else:
        print "Created."
        
        
cursor.close()
cnx.close()
