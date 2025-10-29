# Manual de Usuario e Instalación

## 1. Requisitos Previos

Para ejecutar la aplicación se necesitan los siguientes elementos:

- **Python 3.10+** (cualquier versión reciente de Python 3 debería funcionar)

- **Librerías de Python**:
para ejecutar el proyecto se necesitan instalar las siguientes librerias:
- pandas
- flask
- requests
para instalar estas librerias se debe abrir la cmd y colocar el siguiente comando
- pip install (nombre de la libreria)  
por ejemplo:  pip install pandas
Estas librerías son necesarias para ejecutar el backend, manejar datos y consumir la API del clima.


## 2. Ejecucion del proyecto
hay 2 formas de ejecutar el proyecto:
- Usando la cmd, primero hay que ir a la direccion donde esta el archivo app.py, para esto usa el comando: cd (direcciond del archivo), y cuando estes ahi simplemente ejecuta: python app.py
- la segunda forma es mediante **Visual Estudio Code**, para esto se necesitara:
    - instalar el vs code
    - en vs code instalar las extensiones para python y git
pasos a seguir:
1. ir al repositorio en git y clonarlo (boton verde y copiar)
2. ir al vs code, en la parte de arriba seleccionar "view" y abrir la paleta de comandos y escribir Git: clone
3. copiar el enlace, al dar enter pedira ubicacion para guardar.
otra forma en vs code es si se tiene el paquete del proyecto, simplemente abrir vs code, abrir folder y buscar el paquete.
despues de abrir el proyeto se podran ver todos los archivos que tiene, para ejecutar abrir app.py y boton de run.
en ambas formas de ejecucion la terminal te dara algo como esto:
- Running on http://127.0.0.1:5000
simplemente presionar y llevara a la web.

## 3. Uso de la Aplicación (Manual de Usuario)

### 3.1 Abrir la aplicación
- Abrir un navegador e ingresar la dirección entregada por la consola
- Se mostrará la página principal (`index.html`) con información básica del clima y un formulario para ingresar los datos de la planta y de el ambiente.

### 3.2 Ingresar datos del cultivo
Completar los siguientes campos en el formulario:

- **Temperatura**: temperatura actual o promedio de la zona (°C).
- **Humedad**: humedad del suelo relativa actual (%).
- **Etapa de la planta**: germinacion en crecimiento, etc.
- **Necesidad de agua**: alta, media, baja.
- **Tipo de suelo**: arenoso, arcilloso, etc.
- **Tipo de riego**: goteo o aspersión.
- **Estado de lluvia**: indica si está lloviendo.

### 3.3 Obtener recomendaciones
- Al enviar el formulario, la aplicación calculará:
  1. Si se debe regar o mantener el plan de riego.
  2. Frecuencia recomendada de riego.
  3. Cantidad de agua a usar por metro cuadrado.

- La información se muestra en la página `resultado.html` junto con un **detalle explicativo**, indicando los factores considerados por el motor de inferencia.

## 4. Notas importantes
- La aplicación depende de la **API de OpenWeatherMap** para obtener datos de clima. Si no hay conexión o la API falla, se usarán valores por defecto.
- La lógica de riego se basa en los 3 conjuntos de reglas definidas.
