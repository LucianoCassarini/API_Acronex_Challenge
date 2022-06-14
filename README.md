
# API_Acronex_Challenge

Esta API de máquinas agrícolas fue desarrollada con Django y PostgreSQL.

### Dependencias:

- `pip install Django==4.0.5`

- `pip install psycopg2`

### Configuración para levantar la API de forma local:
Antes que nada se debe crear una DB vacía, en este caso, esta configuración fue probada con una DB de PostgreSQL.

Luego, dentro del proyecto, acceder a la carpeta **API_Acronex** y abrir el archivo **setings.py**, en este archivo se encuentra un bloque de código como este:

```
DATABASES = { 
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'api_acronex_DB',
        'USER': 'postgres',
        'PASSWORD': 'admin',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```

En este bloque seteamos el 'NAME:' con el nombre que le dimos a la DB anteriormente creada, 'USER' con el usuario con el que la creamos (por defecto este es postgres) y 'PASSWORD' con la contraseña de la misma.

Para estas pruebas el 'HOST': 'localhost' y el puerto de escucha por defecto es el 'PORT': '5432'.

Para terminar la conexión entre nuestro proyecto y la DB vamos a ejecutar en consola los siguientes comandos:

- ``` python manage.py makemigrations```

- ``` python manage.py migrate```

Por ultimo, para tener acceso al panel de Administrador proporcionado por django, hay que crear un superusuario, para esto ejecutar en consola el comando:

- ``` python manage.py createsuperuser```

## Referencias de la API local

| Tipo |  Referencia  | Descripción                |
| :-------- | :------- | :-------------------------|
| `GET` | `/api/maquinaria/` | Consulta todas las maquinas existentes|
| `GET` | `/api/maquinaria/<id>` | Consulta una máquina existente por por ID|
| `GET` | `/api/maquinaria/?nombre=<nombre>` | Consultar una máquina existente por nombre |
| `GET` | `/api/maquinaria/?clase=<clase>` | Consultar una máquina existente por clase |
| `GET` | `/api/maquinaria/?nombre=<nombre>&clase=<clase>` | Consultar una máquina existente por nombre o clase |
| `POST` | `/api/maquinaria/` | Da de alta una nueva maquina |
| `PUT` | `/api/maquinaria/<id>` | Actualiza una maquina existente |
| `PUT` | `/api/maquinaria/darBaja/<id>` | Da de baja una maquina existente sin eliminarla|
| `DELETE` | `/api/maquinaria/<id>` | Elimina una maquina existente |