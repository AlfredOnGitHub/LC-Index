# SW-mngmt

Software de gestión de usuarios en desarrollo.

Aplicación web creada con Django que permite a los usuarios realizar cómodamente la gestión de su local privado.

## Requisitos Previos

Python 3.X
Django 3.X o superior
Pillow
Python-dotenv

## Instalación
Descargaremos el repositorio y accederemos a la carpeta en cuestión:
```
git clone https://github.com/AlfredOnGitHub/sw-mngmt.git
cd sw-mngmt
```
Crearemos e iniciaremos el entorno virtual:
```
python -m venv env
Linux: source env/bin/activate
Windows: env/Scripts/activate
```
Instalamos las dependencias:
```
pip install -r requirements.txt
```
Por último, es necesario crear el archivo .env para su correcta ejecución. Dicho archivo completa las siguientes variables de entorno:
```
SECRET_KEY
DEBUG
EMAIL_BACKEND
EMAIL_HOST
EMAIL_PORT
EMAIL_USE_TLS
EMAIL_HOST_USER
EMAIL_HOST_PASSWORD
DEFAULT_FROM_EMAIL
```

## Colab
Soon