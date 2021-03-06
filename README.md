# RSA-python-chat :snake:
![chat python RSA](https://user-images.githubusercontent.com/71668076/142019835-8c3f6bc8-7b91-4e76-b11a-94e9aa56abf6.jpg)


# RSA :closed_lock_with_key:

¿QUE ES RSA? 

Este es un algoritmo asimétrico cifrador de bloques, que utiliza una clave pública, la cual se distribuye (en forma autenticada preferentemente), y otra privada, la cual es guardada en secreto por su propietario.
Una clave es un número de gran tamaño, que una persona puede conceptualizar como un mensaje digital, como un archivo binario o como una cadena de bits o bytes.
Cuando se envía un mensaje, el emisor busca la clave pública de cifrado del receptor y una vez que dicho mensaje llega al receptor, éste se ocupa de descifrarlo usando su clave oculta.

# UN POCO DE HISTORIA :pencil:

Un poco de historia, este es inventado 1977 y lleva la primera letra del apellido de sus creadores Ron Rives, Adi Shamir y Leonard Adleman, formando asi el algoritmo RSA, esta basa su fortaleza en la dificultad de factorizar de dos numeros primos grandes, algo que es de alta dificulta para la capacidad de las computadoras.

# DIAGRAMA DE FLUJO :memo:
Este un chat realizado en python para compreder mejor el funcionamiento del algoritmo de cifrado RSA
![imagen](https://user-images.githubusercontent.com/71668076/141693791-42e55d07-1253-4077-9e91-12093de0f8a5.png)


# ALGORITMO DEL PROGRAMA :memo:
1.	INICIO
2.	Hacemos los cálculos de parámetros (p,q,n,e)
3.	Sacamos la Llave pública (n,e).
4.	Sacamos la Llave privada (n,q).
5.	Mandamos nuestra llave.
6.	Recibimos la llave publica de la otra persona.
7.	Escribimos nuestro mensaje
8.	Ciframos nuestro mensaje con la llave publica de la otra persona:
C  M^e mod n.
9.	Enviamos nuestro mensaje.
10.	Recibimos el mensaje de la otra persona.
11.	Desencriptamos con nuestra llave privada:
M  C^d mod n.
12.	Mensaje original de la otra persona.
13.	Si mensaje original de la otra persona  bye
Si no volver a paso 7.
14.	FIN

# EJEMPLO :eyes:
Y Si tenemos:

![imagen](https://user-images.githubusercontent.com/71668076/141694333-7e60955a-afc0-4378-aeb4-6f335b4d3a75.png)


Tenemos dos primos p y q, p=3 y q = 11, los multiplicaremos entre ellos, dandonos N= p*q = 3 * 11 = 33, claro que si fueramos el atacante lo resolveriamos muy rapido con una claves asi, ya que dos numeros que multiplicados entre si me den 33, bueno esto si es sencillo para este paso pero recordemos que p y q son numeros primos enormes.
Bueno ahora usaremos la formula de :

![imagen](https://user-images.githubusercontent.com/71668076/141694340-facac716-ef77-46ae-bb40-af84b5160df8.png)

Dandonos:

![imagen](https://user-images.githubusercontent.com/71668076/141694345-94670e9e-f71a-4f4f-adad-37db8fb977c2.png)

 
Ademas debemos de escoger un ‘e’ que sea menor a phi φ y ahora hay que calcular D

![imagen](https://user-images.githubusercontent.com/71668076/141694351-1c26daec-5e83-48f2-be48-0df7bd5accbb.png)
 
7 por d es congruente a 1 mod 20 y el resultado nos da 4, ahora tendremos nuestra clave publica y privada (7,33) y (4, 33), y ahora le puedo dar la clave publica a las personas que vayan a recibir un mensaje,y ellos apartir del (7,33) no podran sacar que yo tengo el (4,33).
Ahora para encriptar y desencriptar es de la siguiente manera:
 
![imagen](https://user-images.githubusercontent.com/71668076/141694361-a86fed1c-66e4-4807-8057-e0b62f845e8a.png)

 
Parece sencillo pero recordemos que ‘e’ puedes ser un numero mucho mayor y para descifrar seria con el mensaje encriptado elevado a D mod n.
 
# SEGURIDAD RSA :lock_with_ink_pen:
La seguridad de este algoritmo radica en que sus calculos son base a numeros primos los cuales son dificiles de calcular con una maquina tradicional, para poder vulnerar este algoritmo se requiere una gran portencia de computo, no afirmo que sea anti vulneraciones pero si es un algoritno nuy robusto, como lo que mandamos son nuestras llaves publicas no pasaria nada si las interseptan ya que requieren de nuestra llave privada para poder descifrar lo que dice el mensaje

![imagen](https://user-images.githubusercontent.com/71668076/141694366-936a6464-cf36-4359-9fdb-e2974dca8a41.png)
![imagen](https://user-images.githubusercontent.com/71668076/141700768-9ec1420f-09c2-49b1-b0fb-5dce02ae2bb7.png)
![hot-dog-trooper-dogs](https://user-images.githubusercontent.com/71668076/143131367-e4f5a26c-8e1c-4c23-901a-d6e1e6327e32.gif)



# CORRER EL PROGRAMA :octocat:
Corremos primero el servidor y después el cliente:

![imagen](https://user-images.githubusercontent.com/71668076/141857981-d5d807ca-2ab0-4fd7-993a-3949ec35a78d.png)



Para cliente ingresamos valores, debemos usar números primos grandes para hacer la operación y garantizar que con una computadora normal no pueda descifrarlo, ya que como sabemos los números primos son complejos de procesar.

# EJEMPLO CORRIENDO EL PROGRAMA :speech_balloon:
Para servidor:

![imagen](https://user-images.githubusercontent.com/71668076/141858891-5b647323-79bf-4248-8d59-5d0ccc7f09c2.png)

P = 367 y Q = 541
No dará muchos valores que son enormes y escogeremos uno para e:
![imagen](https://user-images.githubusercontent.com/71668076/141858918-3f854172-2dce-428e-b636-977ed72b892a.png)

Ahora esperaremos la llave publica de la otra persona (cliente) :
![imagen](https://user-images.githubusercontent.com/71668076/141858976-7e8ef276-8d8d-4d9b-b899-4ee6b9989396.png)

P = 199 y Q = 211
No dará muchos valores que son enormes y escogeremos uno para e
![imagen](https://user-images.githubusercontent.com/71668076/141859152-0467f2fd-0137-4439-9744-6c4f2e251242.png)
![imagen](https://user-images.githubusercontent.com/71668076/141859355-575b15a3-d6cf-4d04-beb8-d733a3ecf05d.png)
![imagen](https://user-images.githubusercontent.com/71668076/141859392-90fcb5f2-2e5b-4421-9be7-8e9c76893d7e.png)
![imagen](https://user-images.githubusercontent.com/71668076/141859468-e744a0e7-20c6-41d1-a87d-07016dc578da.png)
Y así pueden estar mandándose mensajes hasta recibir un bye, chau o adios:
![imagen](https://user-images.githubusercontent.com/71668076/141859560-5ecfa9df-89d6-47dc-a139-ae7ef01dc4a1.png)

# DEMOSTRACION :alien:
[![Watch the video](https://user-images.githubusercontent.com/71668076/143130732-0a5c0d8e-eb9b-4ed0-b979-a73c781062ec.png)](https://www.youtube.com/watch?v=vm49zQBB7DE&ab_channel=RomanAlejandroGallegosMarquez)


# FIN :coffee:
Este proyecto fue algo desafiante ya que no recordaba mucho como programar, pero bien dice el sabio, lo que bien se aprende
jamas se olvida. :shipit:
# RESUMEN :notebook:
En resumen solo necesitas que tu programa haga esto:

PROCESO RSA (algoritmo)
 - ASEGURAR QUE P y Q SEAN PRIMOS
 - QUE E SEA COOPRIMO DE ESTOS
 - SUS RESPECTIVOS CALCULOS
 
SABER COMO CIFRAR Y DESCIFRAR UN MENSAJE (rsa)
 - CIFRA: Con la llave publica de la otra persona :closed_lock_with_key:
 - DESCIFRA: Con tu propia llave privada :key::unlock:
 
INVESTIGAR SOBRE SOCKET (para establecer una conexion con otra terminal)
 - MANDAR MENSAJE :mailbox_with_mail:
 - RESPONDERLO :e-mail: :mailbox_with_no_mail:
 - INTERCAMBIAR LAS LLAVES PUBLICAS (que este lo tengo en un apartado de la carpeta serialización)

# HERRAMIENTA DE ELABORACIÓN DE DIAGRAMAS DE FLUJO:
 - https://lucid.app


# FUENTES: :pushpin:
 - https://docs.python.org/es/3.9/library/socket.html
 - https://docs.python.org/es/3/library/pickle.html
 - https://rico-schmidt.name/pymotw-3/socket/tcp.html
 - https://pythontic.com/modules/socket/udp-client-server-example
 - https://stackoverflow.com/questions/53576851/socket-programming-in-python-using-pickle
 - https://www.youtube.com/watch?v=Lbfe3-v7yE0&t=324s&ab_channel=sentdex
 - https://docs.python.org/3/library/stdtypes.html
 - https://www.youtube.com/watch?v=ojX9YPxhoX0&list=LL&index=2&t=166s&ab_channel=LuisMunoz
 - https://www.youtube.com/watch?v=kiowXySiuP8&list=LL&index=29&ab_channel=DavidAlejandroNinaRojas

 
![goodbye-harrypotter](https://user-images.githubusercontent.com/71668076/142060439-65e30cdb-b4a5-414a-8306-856ebc927c65.gif)


