Parte 2 — Explicación escrita

Sobre PUT /equipos/{equipo_id} (actualizar):

1. ¿Qué recibe el endpoint y qué devuelve?
Pues básicamente recibe el equipo_id, que llega por la URL, y ya, en el cuerpo de la
peticion, recibe los datos nuevos que uno quiere ponerle al equipo, o sea nombre y
categoria, y esos vienen validados con el modelo EquipoCreate. Y lo que devuelve, si
todo sale bien, es el equipo ya actualizado, con el mismo id de siempre pero con el
nombre y la categoria cambiados.

2. ¿Cómo localiza el equipo a actualizar dentro de la lista (por id)?
Yo use un next() con bucle que esta dentro, que va recorriendo la
lista de equipos buscando cual tiene el mismo id que el que llego. Y le puse que si
no encuentra nada, en vez de tirar un error de Python, mejor me devuelva None,
para poder manejarlo yo con calma despues.

3. ¿Cómo valida el nombre duplicado excluyendo al propio equipo que se edita?
¿Por qué es importante esa exclusión?
Se revisa si algun otro equipo ya tiene ese mismo nombre y le agrego la
condicion de que el id sea distinto al que estoy editando. Eso es importante
porque, si no le pongo esa exclusion, uno querria solo actualizar la categoria y
dejar el nombre igual, y el codigo se pondria a comparar el equipo consigo mismo,
iba a pensar que ya existe ese nombre y me iba a tirar el error 400 sin que en
verdad hubiera ningun problema.

4. ¿Cómo maneja el caso de "equipo no encontrado"? ¿Qué código HTTP devuelve
y por qué?
Si el next() no encuentra nada, la variable queda en None, entonces ahí entra un
if que detecta eso y lanza un HTTPException con codigo 404. Uso el 404 porque es
el codigo que se usa cuando uno pide algo que no existe, entonces tiene sentido
usarlo ahí, para diferenciarlo del 400 que es cuando el nombre ya esta duplicado.


Sobre DELETE /equipos/{equipo_id} (eliminar):

5. ¿Qué recibe el endpoint y qué devuelve?
Solo recibe el equipo_id por la URL, ya que para borrar no hace falta mandar nada
mas, solo decir cual es el que se quiere eliminar. Y devuelve el equipo que se
acaba de borrar, para que uno vea justo que fue lo que se elimino.

6. ¿Cómo elimina el equipo de la lista?
Primero lo busco con el mismo next() de antes, y ya cuando lo tengo, uso
_equipos.remove() para sacarlo de la lista.

7. ¿Cómo maneja el caso de "equipo no encontrado"? ¿Qué código HTTP devuelve
y por qué?
Es el mismo caso de antes, si no lo encuentra queda en None y ahí se dispara el
mismo HTTPException de 404. Tiene sentido reutilizar la misma logica porque al
final el problema es el mismo en los dos casos, uno esta pidiendo hacer algo con
un id que no existe.


Sobre la arquitectura:

8. ¿Por qué la lógica va en equipo_service.py y los endpoints en equipos.py?
¿Qué ventaja tiene separar estas capas?
Pues porque equipos.py se encarga solo de la parte de recibir la peticion y
decidir que ruta es, mientras que en equipo_service.py es donde de verdad pasa
todo, ahí es donde se busca, se valida y se guarda o se borra el equipo. La
ventaja de tenerlo separado es que si un dia cambio como llegan los datos no
tengo que tocar la logica, y si cambio como se guardan los datos, por ejemplo si
algun dia se pasa a una base de datos de verdad, no tengo que tocar los
endpoints. Osea que queda todo mas ordenado y es mas facil de modificar sin
dañar lo demas.

9. ¿Qué papel juegan EquipoCreate y EquipoResponse de schemas/equipo.py?
EquipoCreate es el que valida lo que entra, o sea el nombre y la categoria con
sus limites de caracteres, y se usa tanto en el POST como en el PUT porque en
los dos casos el cliente manda esos mismos dos datos. Y EquipoResponse es el
que define como se ve lo que la API devuelve hacia afuera, entonces cuando uno
pone response_model=EquipoResponse en cada endpoint, hace que FastAPI se
encargue solo de que la respuesta siempre salga con esa forma.

10. ¿Qué es HTTPException y por qué se usa para reflejar errores?
Es como una herramienta que trae FastAPI para poder cortar la ejecucion de un
endpoint y mandar de una vez un error con el codigo que uno le diga. La uso en
vez de solo hacer un return con un mensaje de error porque asi la respuesta si
queda con el codigo HTTP correcto, el 404 o el 400, y eso importa porque en
Swagger, o en cualquier otra app que use la API, uno puede darse cuenta si algo
salio mal con solo mirar el codigo, sin tener que leerse todo el mensaje.
