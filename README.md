# **HABI TEST**

## **Introducción**

Habi desea tener una herramienta en la que sus usuarios puedan consultar los inmuebles
disponibles para la venta. En esta herramienta los usuarios deben ser capaces de ver tanto los
inmuebles vendidos como los disponibles. Con el objetivo de hacer más fácil la búsqueda, se
espera que los usuarios puedan aplicar diferentes filtros a la búsqueda.
Adicionalmente, se espera que los usuarios puedan darle “me gusta” a los inmuebles con el fin
de tener un ranking interno de los inmuebles más llamativos.

## **Tecnologías de uso**

-Django
-Django REST

## **Punto 1 Servicio de consulta**

### **Funcionalidades**

- Solo se realiza consulta de estados pre_venta , en_venta y vendidos.
- Se puede filtrar por inmueble propiedades de forma simultanea (Año de construcción, Ciudad, Estado)
- La consulta Arroojara los resultados (Dirección, Ciudad, Estado, Precio de venta y Descripción)

## **Uso**

Consultas de propiedades para usuarios

<http://127.0.0.1:8000/api/search-porperty/>

Esta consulta traera todas las propiedas que esten en estado (pre_venta , en_venta y vendido).

Para aplicar filtros se debe seguir la siguiente convención

### **Año**

Para realizar filtros sobre un año en particular se debe enviar como un query param como se muestra en ejemplo 1 en este caso la busqueda arrojara las propiedas que hayan sido constuidas en el año 2011.

#### **Ejemplo 1**

<http://127.0.0.1:8000/api/search-porperty/?year=2011>

### **Ciudad**

Para realizar filtros sobre una ciudad en particular se debe enviar como un query param como se muestra en ejemplo 2 en este caso la busqueda arrojara las propiedas que esten ubicadas en medellin.

#### **Ejemplo 2**

<http://127.0.0.1:8000/api/search-porperty/?city=medellin>

### **Estado**

Para realizar filtros sobre un estado en particular se debe enviar como un query param el id del estado que se desea filtrar las propiedades

| ID  | Estado    |
| --- | --------- |
| 3   | pre_venta |
| 4   | en_venta  |
| 5   | vendido   |

como se muestra en ejemplo 3 en este caso la busqueda arrojara las propiedas que esten en estado pre_venta.

#### **Ejemplo 3**

<http://127.0.0.1:8000/api/search-porperty/?state_id=3>
