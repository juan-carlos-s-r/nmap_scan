import nmap

#variables para guardar los datos 
host=input("Host: ")
parametros=input("Parametros: ")
argumentos=input("Argumentos: ")
sudo_d=input("Sudo (S/N): ")

#verificacion y asignacion de bool de sudo
if sudo_d=='S':
    sudo2=True
elif sudo_d=='N':
    sudo2=False
else:
    print("Dato no valido")

#creacion de objeto con portscanner
scan=nmap.PortScanner()

#verificacion de si un argumento necesita root y ejecucion de esto
def necesita_root():
    global host,parametros,argumentos,sudo2
    try:
        #ejecuta el escaneo
        scan_info=scan.scan(hosts=host,ports=parametros,arguments=argumentos,sudo=sudo2)
    except nmap.nmap.PortScannerError:#hace una excepcion por si necesita el root
        sudo_d=input("El argumento requiere root (S/N): ")
        if sudo_d=='S':
            sudo2=True
        elif sudo_d=='N':
            sudo2=False
        else:
            print("Dato no valido")
        necesita_root()
    else:
        #se imprime la informacion
        print(scan_info)

necesita_root()



