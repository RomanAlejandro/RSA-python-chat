# RSA-python-chat
Este un chat realizado en python para compreder mejor el funcionamiento del algoritmo de cifrado RSA
![imagen](https://user-images.githubusercontent.com/71668076/141693791-42e55d07-1253-4077-9e91-12093de0f8a5.png)

RSA

¿QUE ES RSA?
Este es un algoritmo asimétrico cifrador de bloques, que utiliza una clave pública, la cual se distribuye (en forma autenticada preferentemente), y otra privada, la cual es guardada en secreto por su propietario.
Una clave es un número de gran tamaño, que una persona puede conceptualizar como un mensaje digital, como un archivo binario o como una cadena de bits o bytes.
Cuando se envía un mensaje, el emisor busca la clave pública de cifrado del receptor y una vez que dicho mensaje llega al receptor, éste se ocupa de descifrarlo usando su clave oculta.

UN POCO DE HISTORIA
Un poco de historia, este es inventado 1977 y lleva la primera letra del apellido de sus creadores Ron Rives, Adi Shamir y Leonard Adleman, formando asi el algoritmo RSA, esta basa su fortaleza en la dificultad de factorizar de dos numeros primos grandes, algo que es de alta dificulta para la capacidad de las computadoras.
 

ALGORITMO DEL PROGRAMA
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


Y Si tenemos:
 
Tenemos dos primos p y q, p=3 y q = 11, los multiplicaremos entre ellos, dandonos N= p*q = 3 * 11 = 33, claro que si fueramos el atacante lo resolveriamos muy rapido con una claves asi, ya que dos numeros que multiplicados entre si me den 33, bueno esto si es sencillo para este paso pero recordemos que p y q son numeros primos enormes.
Bueno ahora usaremos la formula de  
Dandonos:
 
Ademas debemos de escoger un ‘e’ que sea menor a phi φ y ahora hay que calcular D
 
7 por d es congruente a 1 mod 20 y el resultado nos da 4, ahora tendremos nuestra clave publica y privada (7,33) y (4, 33), y ahora le puedo dar la clave publica a las personas que vayan a recibir un mensaje,y ellos apartir del (7,33) no podran sacar que yo tengo el (4,33).
Ahora para encriptar y desencriptar es de la siguiente manera:
 
Parece sencillo pero recordemos que ‘e’ puedes ser un numero mucho mayor y para descifrar seria con el mensaje encriptado elevado a D mod n.
 
SEGURIDAD RSA
La seguridad de este algoritmo radica en que no hay maneras rápidas conocidas de factorizar un número grande en sus factores primos utilizando computadoras tradicionales.
