# Project Inventory System- FastAPI

## Descripción

Este proyecto es un ejemplo de una API RESTful desarrollada con FastAPI que permite realizar operaciones CRUD (Create, Read, Update, Delete) sobre un modelo de películas. Está diseñado con un enfoque académico para que los aprendices de programación backend puedan utilizarlo como punto de partida y empezar a trabajar en él.

## Funcionalidades

- Obtener las tablas de productos, proveedor y suministros
- Obtener el ID de las tres tablas
- Crear tablas de productos, proveedores y suministros
- Actualizar tablas de productos, proveedores y suministros 
- Borrar tablas de productos, proveedores y suministros

## Tecnologías utilizadas

- Python
- FastAPI
- Pydantic

## Instalación

1. Clone este repositorio en su máquina local:
   (clonado desde )

git clone git@github.com:JSand89/my-movie-app-c9.git


2. Navega hasta el directorio del proyecto:

cd mi-pelicula-app-c9

3. Tú o uno de tus compañeros deberíais cambiar la fuente del repositorio 

git remote -v

git remote remove origen

git remote add origen <nueva_url_del_repositorio>.

4. Ahora, tus compañeros deben clonar tu repositorio y tú debes darles permiso para editarlo

Desde el repositorio en GitHub, ve a "Configuración" y luego a la sección "Colaboradores" para añadirlos. Esto es para permitirles hacer cambios. No te preocupes, haremos este proceso en clase".

5. Instala las dependencias necesarias:

pip install -r requirements.txt


## Uso

1. Inicie la aplicación:

uvicorn main:app --reload


2. Accede a la documentación de la API en tu navegador:

http://localhost:8000/docs


3. Prueba las diferentes rutas disponibles para realizar operaciones CRUD sobre las películas.

fin.