# Examen_GuillermoR_AD

#Primer Script En el primer script se utilizan las credenciales de twitter para poder obtener información y luego esa información almacenarla en una base de datos en couchdb, se utiliza la conexión local con el servidor remoto, en la parte del código se encuentra una función la cual nos permite almacenar los datos de twitter en la base de datos, con el try except se captura algún error al momento de crear la base de datos y si se da un error que igual la cree, la última línea de código es el criterior de búsqueda, en este caso sobre pokemon, diamante, perla, remake.

#Segundo Script Primero nos conectamos al servidor de mongodb de forma local y posterior a eso utilizamos las funciones necesarias para poder obtener información de una página web, es importante importar las librerías y el for en el código nos permite obtener los datos de esa etiqueta en la parte del documento para ser espeífico en su html y al final lo guarda en la base de datos que ya se crea en mongodb

#Tercer Script Utilizando la librería de facebook_scraper nos permite obtener datos de facebook, especificando la página de la que queremos que nos saque la información, en este caso "nokia", por lo tanto nos conectamos a mongodb y luego por medio de un for se recorre las 100 páginas de nokia que se han especficiado y se van guardando uno por uno los criterior de filtrado

#Cuarto Script Para el script se especifica el nombre de usuario y contrasña, junto con la base de datos para poder conectarse de sql lite a mongodb posterior a eso se recorre los arrglos y se selcciona la parte de los índices para identificarlos, el form permite recorrer las filas que contenga nuestra base de datos para posterior a eso almacenarla en la base de mongodb y al final se cierra el servidor.

#Quinto Script primero se espceifica la url para la conexión con couch y posterior a eso se realiza el try except para capturas los posibles errores en la conexión y posterior a eso se especifica el servidor de mongodb y también se hace el try except para los errores, después de especifica el nombre de la base de datos en couch de la cual se va a traer los datos y ponerlos en la base de datos en mongodb

#Sexto Script Este script nos permite conectarnos de mongodb a couch, por ende la temática es similar al quinto script solo que con la codición de que en el for dinal se especifica la forma de conexión con la base de datos en couch, ingresa a la base, luego al documento y dentro del documento va creando los registros, de igual forma se usa el try except para poder ver los errores al momento de crearlos

#Septimo Script El script nos permite conectarnos al servidor de mongodb atlas desde couchdb, por lo cual se espcifica la url del servidor de couchdb y se procede a usar el try except para tomar los errores en la conexión, posterior a eso se especifica el url del servidor de mongodb atlas para ser exactos del cluster, usando el nombre del usuario, la contraseña y el nombre de la base de datos dentro del cluster para poder hacer la conexión, posterior a esos especiofica el documento dentro de la base de daots, se usa el try except para los errores al momento de hacer la conexión y alfinal el for nos permite ir almacenando los datos de la base de datos especificada de couch hacia el servidor y cluster de mongodb atlas.

#Octavo Script Este Script nos permite conectarnos de mongodb a mongodb atlas, por medio de las url, se especifica la urla de ambos servidores, remoto y local y de esta forma también se espcifican las bases de datos a usarse, el for nos permite recorrer y llenar la base de datos.

#Noveno y Décimo Script Tomando en cuenta la documentación, se importan dos librerías para la detección de errores y posterior a eso se procede a ingresar los datos por mediod e los arreglos, el for final permitirá agregar la información al documento que se va a crear y por último tomando en cuenta la librería de pandas se crea el documento .csv para la visualización de los datos de mongodb atlas.
