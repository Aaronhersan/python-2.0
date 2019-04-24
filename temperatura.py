import os
import glob
import time
import MySQLdb
##import RPi.GPIO as GPIO

os.system('modprobe w1-gpio')
os.system('modprobe w1-therm')

##BD==1
db = MySQLdb.connect("localhost","bianca","bianca","simti")
cursor = db.cursor()
##BD==2
db_aws = MySQLdb.connect("simti1234.bitnamiapp.com","root","2TkK-9%R.fWq","simti")
cursor_aws = db_aws.cursor()

base_dir = '/sys/bus/w1/devices/'
temp_ids = ["28-0517c1b4bdff/w1_slave","28-0517c1a49cff/w1_slave","28-0517c1a3f7ff/w1_slave"]
##temp_ids = ["28-0517c1b4bdff/w1_slave","28-0517c1a49cff/w1_slave","28-0517c1a3f7ff/w1_slave","28-0517c203f5ff/w1_slave" ]

def read_temp(device_file):
	f = open(device_file, 'r')
	lines = f.readlines()
	f.close()
    
while lines[0].strip()[-3:] != 'YES':
	time.sleep(0.2)
	lines = read_temp_raw()
	equals_pos = lines[1].find('t=')
if equals_pos != -1:
	temp_string = lines[1][equals_pos+2:]
	temp_c = float(temp_string) / 1000.0
	return temp_c

## funcion para chequear conecion con el internet
def check_internet():
    url='http://www.google.com/'
    timeout=5
    try:
            _ = requests.get(url, timeout=timeout)
            print("Coneccion establecidad")
            return True
    except requests.ConnectionError:
        print("Internet is not working")
    return False

def insert_temp(sensor,value,db):
        status = check_internet()
        sql = """INSERT INTO `mediciones`(`id_sensor`, `valor`,'guardado', `fecha`) VALUES (%s,%s,now()) """ %(sensor,status,value)
        print(db)
        if db == 1:
                cursor.execute(sql)
                db.commit()
        else:
                cursor.execute("INSERT INTO 'mediciones' ('updaed') VALUES (false)")
                cursor_aws.execute(sql)
                db_aws.commit()
 	# Rollback in case there is any error
 	if db == 1:
  		db.rollback()
 	else:
  		dbaws.rollback()
 
	while True:

for i in range(len(temp_ids)):
	value=read_temp(base_dir+temp_ids[i])
	print "Sensor= ",i+1, "Temp: ", value 
	insert_temp(i+1,value,"1")
	insert_temp(i+1,value,"2")
	time.sleep(0.1)
	print "----------\n"

db.close()
dbaws.close()
