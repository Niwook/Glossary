# Glossary
Aplicación que ayuda a un estudiante de idiomas a llevar un control sobre el vocabulario que está adquiriendo y que a su vez le permita obtener información secundaria que apoye dicho control.

Cada vez que un estudiante encuentra una palabra desconocida tiene que buscar su significado para entender el texto que está leyendo; pero en una gran cantidad de ocasiones no recordará si la buscó en otra ocasión o si la búsqueda se realizó en el mismo contexto y, por tanto, con el mismo significado; en otro totalmente distinto. Con esta aplicación el estudiante sabrá si ya ha buscado esa palabra con anterioridad.

Cada vez que el estudiante encuentre una palabra que desconoce realizará una búsqueda en la aplicación para saber su significado. Si la palabra ya ha sido buscada con anterioridad mostrará el o los significados con los que se guardó en un principio o el de las posibles actualizaciones que se han realizado con posterioridad. De igual manera mostrará un número que indica las veces que se ha realizado una búsqueda sobre ese término. Por otro lado, si la palabra nunca ha sido buscada, el sistema mostrará un menú en el que se le indicará si desea introducir esa palabra en el sistema, realizar otra búsqueda o salir de la aplicación.

LA SOLUCIÓN:

				--- G L O S S A R Y  -  P C W  86 ---

GLOSSARY-PCW 86 es una aplicación creada con Python y Sqlite3 que corre en una terminal de linux.

La aplicación consiste en un sistema que se encarga de almacenar palabras en inglés y sus respectivas traducciones al español. 

Una parte muy importante es aquella que se encarga de registrar las veces que se busca un termino y que nos indica la cantidad de veces que se ha buscado; de modo que podemos llevar un control sobre la memorización de aquellas palabras con más difucultad para ser memorizadas.

Cada vez que el estudiante encuentre una palabra que desconoce realizará una búsqueda en la aplicación para saber su significado. Si la palabra ya ha sido buscada:
	- Introducir el término a buscar.
	- Imprimir una tabla con:
		- El término buscado.
	 	- El plurar irregular en caso de que lo tenga ( 0, 1 o 2).
	 	- La fecha en la que se introdujo el término en cuestión en el sistema.
		- La fecha de la última vez que se accedió al término.
		- El número de veces que ha sido listado dicho término (puede ser 0, 1 o N)
		- El significado del término buscado (pudiendo ser 1 o N). 
		- La fecha en la que se introdujo el significado.
		- Las categorías a las que pertenecen dichos significados (sust, adj, verb, prep, etc).
	- Mostrar un menú con las opciones de: Editar, Insertar y Eliminar.
	
Por otro lado, si la palabra nunca ha sido buscada, el sistema mostrará un menú en el que se le indicará si desea:
	- Introducir esa palabra en el sistema.
	- Realizar otra búsqueda.
	- Ir al menú de la aplicación.
	- Salir del programa.

---INTRODUCIR UN TÉRMINO EN EL SISTEMA---

- Capturar la fecha y hora de inserción en la base de datos.
- Introducir el plurar irregurlar ( 0 o 1).
- Introducir/Asignar un significado (1 o N).
	- Dado un significado verificar si se encuentra dado de alta en la base de datos.
	- Si el significado ya se encuentra dado de alta en al término.
	- Pero si no lo está, darlo alta.
- Asignar una categoría para dicho significado (1 o N).
