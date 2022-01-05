import serial
import time
import requests
import json
import traceback
import RPi.GPIO as gpio
import os
import sys

def conector():
    
    print("connected to: " + ser.portstr)
    lectura=''
    subcadena=''
    contador_err=0
    while True:
        ser.write(str.encode('P'))
        for line in ser.readline():
            lectura=lectura+chr(line)
        try: 
            indice_c = lectura.index(' ') #obtenemos la posición del carácter c
            indice_h = lectura.index('k') #obtenemos la posición del carácter h)
            subcadena = lectura[indice_c:indice_h]
            print("valor del peso: "+subcadena)
            
            url = "http://iot.igromi.com:8080/api/v1/"+str(sys.argv[1])+"/telemetry"
            headers = {"Content-Type": "application/json"}
            
            x={"peso": subcadena}
            
            response = requests.post(url, headers=headers, json=x)
            print(response.status_code)
            if(response.status_code==200):
                print("Respuesta correcta thingsboard")
                os.system(" python3 /home/pi/lectorBasculas/verde.py")
            else:
                print("Error thingsboard")
                #os.system(" python3 /home/pi/lectorBasculas/rojo.py")
            return 0
        except:
            #print('error lectura: '+str(contador_err))
            #traceback.print_exc()
            contador_err=contador_err+1
            if contador_err > 500:
                return 0 
 
ser = serial.Serial(
    port="/dev/ttyUSB0",\
    baudrate=9600,\
    parity=serial.PARITY_NONE,\
    stopbits=serial.STOPBITS_ONE,\
    bytesize=serial.EIGHTBITS,\
        timeout=0)
conector()
ser.close()
