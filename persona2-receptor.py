import socket
import sys
import pickle

HEADER = 10
servidor = ('localhost',55555)
bufferSize = 1024

def verifica_primo(n):
	c=0
	x=2
	if n>=2:
		while x<=n/2:
			if n%x==0:
				c=c+1
				x=x+1
			else:
				x=x+1
		if c==0:
			return True
		else:
			return False
	else:
		return False
def genera_primos(n):
	lp=[]
	x=2
	while n!=0:
		if verifica_primo(x)==True:
			lp.append(x)
			x=x+1
			n=n-1
		else:
			x=x+1
	return lp
def pyq():
	
	p=int(input("\tValor de (p)="))
	while verifica_primo(p)==False:
		print("\t(p) tiene que ser un numero primo !!!")
		p=int(input("\tValor de (p)="))
	q=int(input("\tValor de (q)="))
	while verifica_primo(q)==False or q==p:
		print("\t(q) tiene que ser un numero primo diferente de (p) !!!")
		q=int(input("\tValor de (q)="))
	lpq=[p,q]
	return lpq
	
def calculae(ø):
	e=2
	le=[]
	while e>1 and e<ø :
		if mcd(e,ø)==1:
			le.append(e)
			e=e+1
		else:
			e=e+1
	print("\nVALORES PARA (e)="+str(le))
	e=int(input("\n\tValor de (e)="))
	while mcd(e,ø)!=1:
		print("\n\tEliga un valor de la lista !!!")
		e=int(input("\n\tValor de (e)="))
	return e

def mcd(e,ø):
	m=ø%e
	while m!=0:
		ø=e
		e=m
		m=ø%e
	return e

def congruente(e,ø):
	k=1
	m=(1+(k)*(ø))%(e)
	while m!=0:
		k=k+1
		m=(1+(k)*(ø))%(e)
	d=int((1+(k)*(ø))/(e))
	return d

def cifrarmensaje(msj,key):
	msj=msj.upper()
	lm=msj.split(" ")
	cmc=""
	lmc=[]
	for i in lm:
		pal=cifrarpalabra(i,key)
		lmc.append(pal)
	for j in lmc:
		cmc=cmc+str(j)+" "
	return cmc

def cifrarpalabra(m,k):
	lpc=[]
	lp=[]
	n,e=k
	cpc=""
	for i in m:
		x=buscarpos(i)
		lp.append(x)
	for j in lp:
		c=(j**e)%n
		lpc.append(c)
	for k in lpc:
		cpc=cpc+str(k)+" "
	return cpc	
	

def buscarpos(x):
	alf="ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
	c=0
	for i in alf:
		if x==i:
			return c
		else:
			c=c+1	

def descifrarmensaje(msj,key):
	msj=msj.upper()
	lm=msj.split("  ")
	cmc=""
	lmc=[]
	for i in lm:
		pal=descifrarnumero(i,key)
		lmc.append(pal)
	for j in lmc:
		cmc=cmc+str(j)+" "
	return cmc

def descifrarnumero(m,k):
	lnc=[]
	ln=[]
	n,d=k
	cnc=""
	men=m.split(" ")
	for i in men:
		x=int(i)
		ln.append(x)
	for j in ln:
		m=(j**d)%n
		lnc.append(m)
	for k in lnc:
		l=buscarlet(k)
		cnc=cnc+str(l)
	return cnc

def buscarlet(x):
	alf="ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
	c=0
	for i in alf:
		if x==c:
			return i
		else:
			c=c+1	



print("\t * * * * * * * * * * * * * * * * * * * * * * * * * *")
print("\t*\t                         ▄▀█▀█▀▄\t    *")
print("\t*\t                        ▀▀▀▀▀▀▀▀▀\t    *")
print("\t*\t         █              ▄ ░░░░░▄\t    *")
print("\t*\t ▄ █    ▐▌▌   █  ▄─▄   ▐▌▌░░░░░▌▌\t    *")
print("\t*\t▐█▐▐▌█▌▌█▌█▌▄█▐▌▐█▐▐▌█▌█▌█░░░░░▌▌\t    *")
print("\t*\t█▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀█\t    *")
print("\t*\t█░█░░░█ █▀▀ █░░ █▀▀ █▀▀█ █▀▄▀█ █▀▀ ░█\t    *")
print("\t*\t█░█▄█▄█ █▀▀ █░░ █░░ █░░█ █░▀░█ █▀▀ ░█\t    *")
print("\t*\t█░░▀░▀░ ▀▀▀ ▀▀▀ ▀▀▀ ▀▀▀▀ ▀░░░▀ ▀▀▀ ░█\t    *")
print("\t*\t▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀\t    *")
print("\t * * * * * * * * * * * * * * * * * * * * * * * * * *")
print("""
\t\t\t   ▄███▀▄     ▄▀███▄
\t\t\t   ██████▀▀ ▀▀██████
\t\t\t  ████ █  ▄▄▄  █ ████
\t\t\t  ██▀█ █ █▄▀▄█ █ █▀██
\t\t\t ▀▀█▄▄█▀ ▀███▀ ▀█▄▄█▀▀
""")

try:
    
    TCPCliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    TCPCliente.connect((socket.gethostname(), 1243))


    print("""
\t\t\t██████╗░░██████╗░█████╗░
\t\t\t██╔══██╗██╔════╝██╔══██╗
\t\t\t██████╔╝╚█████╗░███████║
\t\t\t██╔══██╗░╚═══██╗██╔══██║
\t\t\t██║░░██║██████╔╝██║░░██║
\t\t\t╚═╝░░╚═╝╚═════╝░╚═╝░░╚═╝
""")
    print("ESPERA . . . \nESTABLECIENDO CONEXION CON ")
    print("SERVIDOR : ", servidor ," \nESTABLECIDO EXITOSAMENTE\n")
    
    
    print("\n- - (*) ELEGIMOS VALORES DE NUMEROS PRIMOS PARA (p) y (q) ")
    lista_primos=genera_primos(20)
    print("\nLISTA DE NUMEROS PRIMOS ="+str(lista_primos)+"\n")
    p,q=pyq()
    print("\t(p)="+str(p)+"\n\t(q)="+str(q))
    
    print("\n- - (*) CALCULAMOS EL VALOR DE (n) ")
    n=p*q
    print("\t(n)=(p)*(q)")
    print("\t(n)=("+str(p)+")*("+str(q)+")")
    print("\t(n)="+str(n))
    
    print("\n- - (*) CALCULAMOS (ø) ")
    ø=(p-1)*(q-1)
    print("\t(ø)=(p-1)*(q-1)")
    print("\t(ø)=("+str(p)+"-1)*("+str(q)+"-1)")
    print("\t(ø)="+str(ø))
    
    print("\n- - (*) CALCULAMOS (e) ")
    print("\t(e)/  1<e<ø and mcd(e,ø)==1")
    e=calculae(ø)
    print("\t(e)="+str(e))

    print("\n- - (*) CALCULAMOS (d) ")
    print("\t(d)/  (d)*(e) =sea congruente a= (1)*(mod ø) ")
    d=congruente(e,ø)
    print("\t(d)="+str(d))

    print("\n- - (*) FINALMENTE OBTENEMOS LA LLAVE PUBLICA Y PRIVADA ")
    key_public = [n,e]
    key_private = [n,d]
    print("\n\tLLAVE PUBLICA="+str(key_public)+"\n\tLLAVE PRIVADA="+str(key_private))


#//////////////////#
    #key_public_receptor
    data_serial = pickle.dumps(key_public)
    data_len = str(len(data_serial))
    key_public_roman = bytes(f"{data_len:<{HEADER}}", 'utf-8')+data_serial
    print("NUESTRA LLAVE FUE ENVIADA AL RECEPTOR: ",key_public_roman)
    TCPCliente.send(key_public_roman)
    
    #RECIBIMOS
    #key_public_roman
    data_len2 = TCPCliente.recv(HEADER)
    data2 = b''
    data2 += TCPCliente.recv(int(data_len2))
    key_public_roman = pickle.loads(data2)
    print("LLAVE PUBLICA DEL CLIENTE: ",key_public_roman)
#//////////////////#


    while True:
        print(" ----------------------------------------"+"\n  * * * * * * * * * * * * * * * * * * * "+"\n ----------------------------------------"+"""
\t\t        .--.
\t\t       |o_o |
\t\t       |:_/ |
\t\t      //   \ \\
\t\t     (|     | )
\t\t    /'\_   _/`\\
\t\t    \___)=(___/
""")
        pregunta = input("(-)TITA <3 : ")
        print(" ----------------------------------------"+"\n  * * * * * * * * * * * * * * * * * * * "+"\n ----------------------------------------\n")
        
        # MANDA Y CONTESTA PERO PRIMERO MANDA
        print("\n- - (*) AHORA PODEMOS CIFRAR MENSAJES CON EL METODO (RSA)")
        #mensaje=input("\n\tMensaje : ")
        mensaje_cifrado = cifrarmensaje(pregunta,key_public_roman)
        print("\tMensaje Cifrado : "+str(mensaje_cifrado))
        TCPCliente.sendto(str.encode(mensaje_cifrado), servidor)
        



        # RECIBE
        mensaje = TCPCliente.recvfrom(bufferSize) # LO QUE MANDA ROMAN
        print(" ----------------------------------------")
        respuesta = "[+] ROMAN : " + mensaje[0].decode()
        print(respuesta)
        print(""" ----------------------------------------
        \   ^__^
         \  (oo)\_______
            (__)\       )\/\
            
                ||----w |
                ||     ||""")
        
        
        print("\n- - (*) AHORA PODEMOS DESCIFRAR MENSAJES CON EL METODO (RSA)")
        mensaje_cifrado = input("\n\tMensaje Cifrado : ")
        mensaje_descifrado = descifrarmensaje(mensaje_cifrado,key_private)
        print("\tMensaje Descifrado : "+str(mensaje_descifrado))
        
        if (pregunta == "bye") or (pregunta == "adios") or (pregunta == "chau"):
            print("""


██████╗  ██████╗ ███╗   ███╗ █████╗ ███╗   ██╗
██╔══██╗██╔═══██╗████╗ ████║██╔══██╗████╗  ██║
██████╔╝██║   ██║██╔████╔██║███████║██╔██╗ ██║
██╔══██╗██║   ██║██║╚██╔╝██║██╔══██║██║╚██╗██║
██║  ██║╚██████╔╝██║ ╚═╝ ██║██║  ██║██║ ╚████║
╚═╝  ╚═╝ ╚═════╝ ╚═╝     ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝
                                              

⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡀⠤⠲⠦⠉⠉⠉⠏⠉⠒⢄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡠⠲⠃⢀⣤⠀⠀⠀⠲⠂⠀⠠⠆⠀⠙⢄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⢀⡔⠁⣤⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⢀⠊⠁⠀⢁⡴⠚⠉⣉⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣀⠠⠤⠔⠒⡄⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⡆⢰⠆⠀⠋⣠⠔⠉⠁⣀⡠⠄⠒⠂⠀⠀⠀⠀⠀⠀⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠔⠊⠁⠀⠀⠀⠀⠀⣠⡴⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢠⡆⠀⠀⠀⡜⠁⣠⠔⠋⢁⡔⠒⠒⠤⡀⠀⠀⠀⠀⡐⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠎⠀⠀⠀⢀⣀⣤⣶⡾⠋⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⡆⡶⠀⠀⢀⡜⠁⢀⣀⢸⠀⠀⠀⠀⠈⢆⠀⠀⡜⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠤⠊⠁⠀⢀⡀⣴⡿⠿⠛⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠰⡀⠀⠀⠘⠀⡞⠁⠀⠉⢇⠀⣿⣄⠀⠈⡆⠀⠕⠒⠉⣉⡒⡄⠀⠀⠀⠀⢀⠤⠊⠁⢀⡠⠔⠊⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠑⢄⡀⠀⠀⢇⠀⣤⡄⠈⢢⡈⠻⡖⢀⡞⣀⠔⠊⠁⠀⠀⠉⠐⠒⠠⢎⢁⡠⠔⠂⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠉⠉⢂⠘⢿⣦⡇⠉⠓⢶⡫⠞⠁⣀⣤⣤⣤⣤⣤⣤⣤⠴⠛⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢡⠦⠭⡇⠀⡠⠊⠀⣠⣮⣬⣿⣿⣿⣿⣿⣯⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⠁⢀⠔⡧⠊⠀⢀⡜⠁⠙⣿⣿⣿⡿⠟⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⣀⣡⠎⠀⠀⢠⠊⠀⠀⠀⣸⣿⣿⣷⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⠃⠀⠀⣰⣧⣀⣀⡠⣴⣿⣿⣿⣿⣿⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢧⣤⣤⣾⡿⠿⠋⠁⠀⢹⣿⣿⣿⣿⣿⣿⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠁⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⣿⣿⣿⣿⣿⣿⣿⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⠿⠛⠛⠛⠛⠻⢿⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡸⠀⠀⠀⠀⠀⠀⠀⡸⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⠁⡰⢤⣀⣀⡄⢠⠞⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀

 """)
            TCPCliente.close()
            sys.exit()

except socket.error as e:
    print("UPS OCURRIO UN ERROR CON EL SOCKET ", e)
finally:
    TCPCliente.close()










