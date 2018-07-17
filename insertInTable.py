#!/usr/bin/python

import mysql.connector
from datetime import date, datetime, timedelta


def exec_cmd(cnx, cursor, cmd, opt):
    cursor.execute(cmd, opt)
    cnx.commit()

def add_client(cnx, cursor, name, address):
    cmd = ("INSERT INTO clients "
           "(name, address)"
           "VALUES (%s, %s)")
    
    opt = (name, address)

    exec_cmd(cnx, cursor, cmd, opt)

def add_component(cnx, cursor, name, description ):
    cmd = ("INSERT INTO components "
           "(name, description)"
           "VALUES (%s, %s)")
    
    opt = (name, description)

    exec_cmd(cnx, cursor, cmd, opt)  
    
def add_machine(cnx, cursor, name, model, description):
    cmd = ("INSERT INTO machines "
           "(name, model, description)"
           "VALUES (%s, %s, %s)")
    
    opt = (name, model, description)

    exec_cmd(cnx, cursor, cmd, opt)

    
def add_operator(cnx, cursor, name, surname, role ):
    cmd = ("INSERT INTO operators "
           "(name, surname, role)"
           "VALUES (%s, %s, %s)")
    
    opt = (name, surname, role)

    exec_cmd(cnx, cursor, cmd, opt)


def add_order(cnx, cursor, date, client_id, component_id, quantity ):
    cmd = ("INSERT INTO orders "
           "(date, client_id, component_id, quantity)"
           "VALUES (%s, %s, %s, %s)")
    
    opt = (date, client_id, component_id, quantity)

    exec_cmd(cnx, cursor, cmd, opt)

###########################
### many to many tables ###

def add_machines_components(cnx, cursor, machine_id, component_id ):
    cmd = ("INSERT INTO machines_components"
           "(machine_id, component_id)"
           "VALUES (%s, %s)")
    
    opt = (machine_id, component_id)

    exec_cmd(cnx, cursor, cmd, opt)

def add_machines_operators(cnx, cursor, machine_id, operator_id ):
    cmd = ("INSERT INTO machines_operators"
           "(machine_id, operator_id)"
           "VALUES (%s, %s)")
    
    opt = (machine_id, operator_id)

    exec_cmd(cnx, cursor, cmd, opt)

### end many to many    ###
###########################

### connetc to DB
cnx = mysql.connector.connect(user='vpalladi', password='vito8a82', database='testRiki')

### get the cursor
cursor = cnx.cursor()

add_client(cnx, cursor, 'Riccardo', 'via hai rotto n 18')
add_client(cnx, cursor, 'Vito', 'magnifico n 8')

add_machine(cnx, cursor, 'prima_macchina', 'meccatronic', 'ti fa le pippe') # n 1
add_machine(cnx, cursor, 'seconda_macchina', 'meccatronic', 'ti fa le seghe')
add_machine(cnx, cursor, 'terza_macchina', 'segatronic', 'ti prende a calci in culo') # n 3

add_operator(cnx, cursor, 'riccardo', 'fuffolo', 'pippaiolo') # n1
add_operator(cnx, cursor, 'vito', 'palla', 'ricottaro')
add_operator(cnx, cursor, 'riccardo', 'di', 'pippaiolo')
add_operator(cnx, cursor, 'vito', 'palladi', 'ricottaro')
add_operator(cnx, cursor, 'riccardo', 'di maria', 'pippaiolo')
add_operator(cnx, cursor, 'vito', 'palladino', 'ricottaro') # n6

add_component(cnx, cursor, 'dildo', 'ti serve per fare il zozzone') # n1
add_component(cnx, cursor, 'condom', 'meglio usarlo')
add_component(cnx, cursor, 'occhialini', 'comprali buoni una sola volta, e non perderli...')
add_component(cnx, cursor, 'ciabatte', 'come condom') # n 4

# M2M machine-operator #
add_machines_operators(cnx, cursor, 1, 1 )
add_machines_operators(cnx, cursor, 1, 2 )
add_machines_operators(cnx, cursor, 1, 3 )
add_machines_operators(cnx, cursor, 1, 4 )
add_machines_operators(cnx, cursor, 1, 5 )
add_machines_operators(cnx, cursor, 1, 6 )

add_machines_operators(cnx, cursor, 2, 1 )
add_machines_operators(cnx, cursor, 2, 3 )
add_machines_operators(cnx, cursor, 2, 4 )

add_machines_operators(cnx, cursor, 3, 5 )

# M2M machine-operator #

add_machines_components(cnx, cursor, 1, 1 )
add_machines_components(cnx, cursor, 1, 2 )
add_machines_components(cnx, cursor, 1, 3 )

add_machines_components(cnx, cursor, 2, 1 )
add_machines_components(cnx, cursor, 2, 3 )
add_machines_components(cnx, cursor, 2, 4 )

add_machines_components(cnx, cursor, 3, 1 )

cursor.close()
cnx.close()










### connetc to DB
cnx = mysql.connector.connect(user='vpalladi', password='vito8a82', database='testRiki')

### get the cursor
cursor = cnx.cursor()
    
add_order(cnx, cursor, datetime.now(), 1, 1, 1000 )
add_order(cnx, cursor, datetime.now(), 1, 2, 1000 )


add_order(cnx, cursor, datetime.now(), 2, 1, 100000 )
add_order(cnx, cursor, datetime.now(), 2, 2, 100000 )
add_order(cnx, cursor, datetime.now(), 2, 3, 100000 )
add_order(cnx, cursor, datetime.now(), 2, 4, 100000 )


cursor.close()
cnx.close()




