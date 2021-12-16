import serial
import time
import os

ser = serial.Serial(
    port='COM6',\
    baudrate=9600,\
    parity=serial.PARITY_NONE,\
    stopbits=serial.STOPBITS_ONE,\
    bytesize=serial.EIGHTBITS,\
        timeout=0)

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
        print(int(subcadena))
        time.sleep(1)
        os.system('curl -v -X POST -d "{\"peso\":'+subcadena+'}" iot.igromi.com:8080/api/v1/bascula1iGromi/telemetry --header "Content-Type:application/json"')
        os._exit(0)
    except:
        #print('error lectura: '+str(contador_err))
        contador_err=contador_err+1
        if contador_err > 200:
            os._exit(0)  
ser.close()