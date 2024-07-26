# LC-Index

Software de gestión de usuarios en desarrollo.

Aplicación web creada con Django que permite a los usuarios realizar cómodamente la gestión de su local privado.
  
## Requisitos

- Python 3.x
- Django 3.x
- Pillow
- Un servidor SMTP para enviar correos electrónicos.

## Instalación

    1. Clona el repositorio:
    ```
    git clone https://github.com/tu_usuario/tu_repositorio.git
    cd tu_repositorio
    ```
    2. Crea y activa un entorno virtual:
    ```
    python -m venv env
    source env/bin/activate  
    
    # En Windows usa `env\Scripts\activate`
    ```
    3. Instala las dependencias:
    ```
    pip install -r requirements.txt
    ```
    4. Configurar las variables de entorno:
    
        - Crea un archivo .env en el directorio raíz del proyecto con el siguiente contenido:
        ```
        EMAIL_HOST=smtp.example.com
        EMAIL_PORT=587
        EMAIL_USE_TLS=True
        EMAIL_HOST_USER=your_email@example.com
        EMAIL_HOST_PASSWORD=your_email_password
        DEFAULT_FROM_EMAIL=webmaster@example.com
        ```
    5. Realiza las migraciones de la base de datos:
    ```
    python manage.py migrate
    ```
    6. Inicia el servidor
    ```
    python manage.py runserver
    ```

## Uso
### Página de Inicio

La página principal (/) permite a los usuarios iniciar sesión introduciendo su nombre de usuario y contraseña.


## Estructura del Proyecto

    - mainapp/views.py:
        index: Vista para la página de inicio y autenticación de usuarios.

## Contribuciones

Las contribuciones son bienvenidas. Por favor, sigue el flujo de trabajo estándar de GitHub:

    Haz un fork del repositorio.
    Crea una nueva rama (git checkout -b --jiracode--/nueva-funcionalidad).
    Realiza tus cambios y haz commits (git commit -m 'Añadir nueva funcionalidad').
    Envía tus cambios a tu fork (git push origin (feature/release/bugfix/hotfix)/KAN-XX)
    Abre un Pull Request en GitHub.

