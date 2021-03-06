# **HABI TEST**

## **Introducción**

Habi desea tener una herramienta en la que sus usuarios puedan consultar los inmuebles
disponibles para la venta. En esta herramienta los usuarios deben ser capaces de ver tanto los
inmuebles vendidos como los disponibles. Con el objetivo de hacer más fácil la búsqueda, se
espera que los usuarios puedan aplicar diferentes filtros a la búsqueda.
Adicionalmente, se espera que los usuarios puedan darle “me gusta” a los inmuebles con el fin
de tener un ranking interno de los inmuebles más llamativos.

La prueba se despliega en un servidor de Amazon para que se puedan conectar desde cualquier equipo.

## **Tecnologías de uso**

-Django
-Django REST
-AWS EC2

## **Punto 1 Servicio de consulta**

### **Funcionalidades**

- Solo se realiza consulta de estados pre_venta, en_venta y vendidos.
- Se puede filtrar por inmueble de forma simultanea (Año de construcción, Ciudad, Estado)
- La consulta arrojará los resultados (Dirección, Ciudad, Estado, Precio de venta y Descripción)

Se realiza la configuración primero del vector de los estados que el usuario puedes consultar. Luego se hace un filtrado inicial de todas las propiedades que cumplen con el filtro, luego si existen, se aplica el filtro de los query params y se retorna el json para el uso del front.

#### **Servicio de filtro de propiedades Punto 1**

Consultas de propiedades para usuarios

<http://habiapptest-env.eba-m5d8s2ir.us-west-2.elasticbeanstalk.com/api/search-property/>

Esta consulta traerá todas las propiedades que estén en estado pre_venta, en_venta y vendido.

Para aplicar filtros se debe seguir la siguiente convención

##### **Año**

Para realizar filtros sobre un año en particular se debe enviar como un query param como se muestra en ejemplo 1. En este caso la búsqueda arrojará las propiedades que hayan sido construidas en el año 2011.

###### **Ejemplo 1**

<http://habiapptest-env.eba-m5d8s2ir.us-west-2.elasticbeanstalk.com/api/search-property/?year=2011>

##### **Ciudad**

Para realizar filtros sobre una ciudad en particular se debe enviar como un query param como se muestra en ejemplo 2. En este caso la búsqueda arrojará las propiedades que estén ubicadas en Medellín.

###### **Ejemplo 2**

<http://habiapptest-env.eba-m5d8s2ir.us-west-2.elasticbeanstalk.com/api/search-property/?city=medellin>

##### **Estado**

Para realizar filtros sobre un estado en particular se debe enviar como un query param el id del estado que se desea filtrar las propiedades.

| ID  | Estado    |
| --- | --------- |
| 3   | pre_venta |
| 4   | en_venta  |
| 5   | vendido   |

Como se muestra en ejemplo 3, en este caso la búsqueda arrojará las propiedades que estén en estado pre_venta.

###### **Ejemplo 3**

<http://habiapptest-env.eba-m5d8s2ir.us-west-2.elasticbeanstalk.com/api/search-property/?state_id=3>

###### **Combinación de parámetros**

<http://habiapptest-env.eba-m5d8s2ir.us-west-2.elasticbeanstalk.com/api/search-property/?state_id=3&city=medellin>

## **Punto 2 Servicio de Me gusta Punto 2**

Con este servicio se espera que los usuarios registrados puedan darle me gusta a cualquier propiedad y dicha acción quede almacenada en la base de datos.

En la siguiente imagen se puede apreciar el modelo relacional que se presenta para almacenar en la tabla likes a que usuario le gusta cual propiedad.

![alt text](/docs/modelo_relacional.PNG)

En el modelo se observa que es necesario la creación de dos tablas, una tabla de usuarios que hace referencia a los usuarios registrados actualmente y una tabla de likes, que es la que por medio de las conexiones(FK) almacenará a cual usuario le gusta la propiedad.

### **Código de SQL para la creación de las tablas**

```sql
CREATE TABLE Users_info (
    id int NOT NULL,
    user_name char NOT NULL,
    email char NOT NULL,
    Token char NOT NULL,
    PRIMARY KEY (id)
);

CREATE TABLE Likes (
    id int NOT NULL,
    PRIMARY KEY (id),
    FOREIGN KEY (user_id) REFERENCES Users_info(id),
    FOREIGN KEY (property_id) REFERENCES Property(id)
);
```
