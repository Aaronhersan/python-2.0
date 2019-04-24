import os
import glob
import time
import pymysql
import requests
#este import es para accesar a lasfunciones de insert delete update create del archivo test_db_local.py en la misma carpeta


##import RPi.GPIO as GPIO

os.system('modprobe w1-gpio')
os.system('modprobe w1-therm')

##BD==1
db = pymysql.connect("localhost","root","","base_datos_prueba")
cursor = db.cursor()
##BD==2
##db_aws = pymysql.connect("simti1234.bitnamiapp.com","root","2TkK-9%R.fWq","simti")
##cursor_aws = db_aws.cursor()


def local_save(sensor,status,guardado):
    sql = "INSERT INTO `mediciones`(`id_sensor`, `valor`,`guardado`, `fecha`) VALUES (%d,%d,%r,now())" %(sensor,status,guardado)
    cursor.execute(sql)
    db.commit()
    print("guardado")
    return True

def local_edit():
    sql = """SELECT * FROM mediciones WHERE guardado = False """
    cursor.execute(sql)
    valores = cursor.fetchall()
    print(format(valores))
	##Create a Dataset from selection
	## Example DT= Dataset(sql)
	##insert the result of the dataset, Example
	##"""INSERT INTO `mediciones`(`id_sensor`, `valor`,'guardado', `fecha`) VALUES (%s,%s,%r,%s) """ %(DS(0),DS(1),DS(2),DS(3))
    sql = """INSERT INTO `mediciones`(`id_sensor`, `valor`,`guardado`, `fecha`) VALUES (1,2,3,now())  """
    ##cursor_aws.execute(sql)
    ##db_aws.commit()
    ##sql = """UPDATE mediciones SET guardado = True WHERE guardado = False """
    cursor.execute(sql)
    db.commit()
    return True

def local_create():
    return True

def cloud_save():
    sql = """INSERT INTO `mediciones`(`id_sensor`, `valor`,`guardado`, `fecha`) VALUES (%s,%s,%r,now()) """ %(sensor,status,guardado)
    cursor_aws.execute(sql)
    ##db_aws.commit()
    return True

def cloud_edit():
    return True
local_edit()
db.close()
##dbaws.close()


