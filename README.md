# Interfaces

## Como correr el programa

Requiere python3.x y django 2.x

#### Para instalar Django (requiere python 3.x): 
pip install django

#### Ejecutar el programa:
python3 manage.py runserver ip:puerto

#### Se crea en 
ip:puerto/interfaces/

#### Ejemplo: 
python3 manage.py runserver localhost:8500
entrar a: localhost:8500/interfaces/

*********************

Como funciona Django (Muy resumido):

Existen 3 capas:

``` bash
|-Capa de los templates (interfaz de la página: html, css, js, etc)
|-Capa de las vistas (lógica del programa: puro python)
|-Capa de los modelos (datos del programa: base de datos modelada como objetos (ORM))
``` 

Una url en django esta relacionada con una vista y la vista con un template.

Las vistas se encuentran en views.py y son un método

El template se encuentra en /templates/interfaces/template.html

### Estructura de la aplicación (Muy simplificada):

Distribución de archivos y carpetas:

``` bash
myapp/
  |-manage.py
  |-grupo4test/
```
 
En myapp/grupo4test se encuentra el programa.

Archivos y carpetas relevantes:
```
myapp/interfaces/
  |-statics/ 
  |-templates/
  |-urls.py  
  |-views.py  
  |-models.py
```
 
## urls.py
Acá se definen las urls definidas para nuestra aplicación en Django.

Tiene la siguiente estructura:
``` python
path('path/to/.../url'/, views.'nombre vista', name='nombre referencial'),
```
Donde:
'path/to/.../url' es la dirección a la que hay que entrar para ingresar a esta página.
views.'nombre vista' es el nombre de la vista definda en views.py la cual será llamada al entrar a la url.

Ejemplo, para la url del formulario del cliente se tiene:

### Url del buscador:
    path('buscador/',views.buscador, name='buscador'),

Esto dice que si se entra a .../interfaces/buscador/ va a llamar a la vista 'buscador'.

## views.py y templates
Conjunto de vistas, cada vista tiene la siguiente estructura:

``` python
def vista1(request):
  . . .
  . . .
  . . .
  return render(request, template, {diccionario})
```

Como se nombró, una url está asociada a una vista. Al momento de ingresar una url, 
el programa llamará a la vista asociada, la vista hará el proceso lógico a partir del request con la que fue llamada (el request va a variar si es que se entró como cliente o admin, si es que se entró directo a la página o fue redireccionado hacia ella, si es que se envió un formulario, etc), luego retornará un render (puede retornar muchas coasas pero nosotros usaremos render el 99% de las veces). El render tiene el request con el que fue llamado la vista, un template en html asociado y un diccionario, un diccionario en python es de la forma: 
```python
{ 'key1' : value1 , 'key2': value2 }
```
El diccionario "envía" variables desde la parte lógica de la vista al template de html.

El template es la página en sí, está escrito en html y toma las variables enviadas desde la vista para crear la página.

Las variables enviadas desde la view usando el diccionario van entre "{{}}": 
```
{{ variable }} 
```
Se puede iterar y hacer condicionales dentro del template, usando:
```html
{% if condicional %}
	< do something > 
{% elif %}
	< do something >
{% else %}
	< do something >
{% endif %}
. 
. 
.
{% for element in list %}
	< do something >
{% endfor %}
```
Por ejemplo, si en la vista, el diccionario enviado tiene la forma: 
```python
{'error':'No se encontró el usuario'}
```
Al principio del template de html se puede poner:
```python
{% if error %}
	<p>{{ error }}</p>
{% endif %}
```
Por lo que imprimirá el error 'No se encontró el usuario'.

Ejemplo (muy resumido):

```python
def buscador(request):
	template = 'interfaces/buscador.html'
	buscadorForm = BuscadorForm() #se instancia el form para el buscador
	return render(request, template, {'form': buscadorForm})
```

Si se entra a ../interfaces/buscador se llama esta vista.
Esta vista crea una instancia de buscadorForm y se la envía al template que se encuentra en ../interfaces/buscador.html.

En el template.html se tiene 

```html
<form method="post">
	{% csrf_token %}
	{% for field in form %}
		<p>{{ field.label }}</p>
		<p>{{ field }}</p>
	{% endfor %}
	<input type="submit" name="submit" value="Enviar" />
</form>
```

```html
<form method="post">
  ...
</form>
```
Crea un form en html, usando metodo POST.

```html
{% csrf_token %}
```
Es un método de seguridad que se implementa en django, se debe incluir en los formularios.

```html
{% for field in form %}
		<p>{{ field.label }}</p>
		{{ field }}
{% endfor %}
```
Se itera sobre el form enviado desde la vista (recordar se envío 'form':buscadorForm).
Por cada campo de este form se imprime el label y se crea su campo.

```html
<input type="submit" name="submit" value="Enviar" />
```
Botón de html para el form.

## models.py

Modelos de datos de la aplicación, Django usa un ORM (object relational mapping (??) creo que es) hace un mapeo del modelo relacional de postgresql y lo lleva a un modelo de objetos.

Tienen la siguiente estructura:

``` python
class Paciente(models.Model):
  nombre = models.CharField(max_length=255)
	apellido = models.CharField(max_length=255)
  rut = models.IntegerField(unique=True)
	peso = models.IntegerField()
  .
  .
  .
```
Es casi lo mismo que la entidad del MER, lo único distinto ocurre cuando se tienen variables que son de otros modelos. 

variable tipo ManyToManyField(MODELO, null=[True/False]) se refiere a que está en una relación [0,1] a n con MODELO (0 si null es True, 1 si null es False), ejemplo para crear la relación del paciente que tiene UNA doctora sería de la forma:
``` python
doctor = models.oneToManyField(nutricionista, null=False)
```
Esto crea un modelo Paciente (y crea su respectiva tabla en la base de datos). Para hacer un "query" se llama a la Clase y usando métodos estaticos se obtiene el objeto a buscar.

### Ejemplo: 
Para obtener el paciente de nombre 'francisco' y apellido 'salas':

Usando sql:
``` sql
select paciente.nombre, paciente.apellido
from paciente
where 
  paciente.nombre = 'francisco' AND
  paciente.apellido = 'salas'
```

Usando ORM:

``` python
paciente = Paciente.objects.get(nombre='francisco', apellido='salas')
```

Donde Paciente es la clase definida anteriormente.

.objects y [.get | .filter] son los métodos para buscar instancias de objetos, como argumento se ponen los atributos a buscar.

Sobre este objeto uno puede acceder a todas las variables como uno trata cualquier objeto:

paciente.nombre retorna 'francisco'
paciente.apellido retorna 'salas'
paciente.peso restorna el peso, y así

Esta entidad de paciente se puede enviar directamente al template de django en el diccionario:
```python
def verPaciente(request):
	template = 'interfaces/paciente.html'
	paciente = Paciente.objects.get(nombre='francisco', apellido='salas')
	return render(request, template, {'paciente': paciente})
```
Puedo imprimir sus variables en el template de la forma:
```html
<p>{{paciente.nombre}}</p>
<p>{{paciente.apellido}}</p>
<p>{{paciente.peso}}</p>
{% for enfermedad in paciente.enfermedades %}
<p>{{ enfermedad }}</p>
{% endfor %}
.
.
.
```
