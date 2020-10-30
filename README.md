# sistemasoperativos2

## A. Archivos  
Mark ha comprado una computadora nueva, y para estrenarla, desea organizar bien los elementos que tenia antes en su computadora, y que no pudo organizar bien. Para esto, Mark crea una carpeta en el escritorio llamada Mark, así como él, para tener todos sus elementos ahí. Debido a que Mark es un poco torpe, solo sabe crear la carpeta de origen de todos sus archivos, pero no sabe colocar carpetas dentro de carpetas, por lo que pide tu ayuda para hacerlo.

Mark te dará una serie de instrucciones, como mkdir que es para crear una carpeta dentro de la carpeta donde te encuentres (siempre inicias en la carpeta Mark, que es la de origen) seguido del nombre de la carpeta. También te dará la instrucción de cd, seguido del nombre de la carpeta a la que Mark desea que accedas, o puede ser '..', que indica que vuelvas a la carpeta en la que estabas anteriormente.

Finalmente, Mark quiere que le imprimas todas las carpetas, y sus contenidos, comenzando con la carpeta de origen 'Mark' y sus contenidos de manera tabulada con guiones.

##### Input  
La primera línea de la entrada contendrá n, el número de instrucciones que Mark te otorgará en el formato mkdir NOMBRE o en el formato cd ACCESO con las condiciones ya mencionadas.

##### Output  
Comenzando desde la carpeta de origen, imprime el nombre de la carpeta y dos puntos, en las siguientes lineas imprime el contenido de la carpeta de origen tabulando con dos '-' según la cantidad de carpetas accedidas. Para mayor detalle, revisa las salidas.

##### Casos de prueba  
### input 1  
10  
mkdir papeles  
mkdir hojas  
cd papeles  
mkdir hojas  
cd ..  
cd hojas  
mkdir papeles  
mkdir contaduria  
cd contaduria  
mkdir ramdon  

### output  
Mark:  
--papeles:  
----hojas:  
--hojas:  
----papeles:  
----contaduria:  
------ramdon:  

### input 2  
8  
mkdir algo  
cd algo  
mkdir algo2  
cd algo2  
mkdir algo3  
cd ..  
cd ..  
mkdir fin

### output  
Mark:  
--algo:  
----algo2:  
------algo3:  
--fin:


### Note
Jamás se te dará la instrucción cd '..' mientras estés en la carpeta de origen. No se intentará crear carpetas con nombres repetidos al interior de una carpeta.
