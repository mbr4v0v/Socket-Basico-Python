README
Recuerdos de cuando programaba en UNIX SOCKETS
Basado en https://beej.us/guide/bgnet/

Begin, Out of context
-  Generar un EXECUTABLE desde Python
-  El error podria ser porque no estas ubicado en la raiz del archivo, por lo cual si tienes un directorio raiz y una carpeta donde se ubica este archivo, debes generar el exe desde la carpeta correcta. Para generar un exe de un archivo en especifico utiliza: pyinstaller --onefile main.py
-  Para generar un exe con mas archivos indicando cual es tu archivo principal:  pyinstaller -F main.py
End, Out of context


#El programa de SOCKETS 
importing socket module
import socket
getting the hostname by socket.gethostname() method
hostname = socket.gethostname()
getting the IP address using socket.gethostbyname() method
ip_address = socket.gethostbyname(hostname)
printing the hostname and ip_address
print(f"Hostname: {hostname}")
print(f"IP Address: {ip_address}")


