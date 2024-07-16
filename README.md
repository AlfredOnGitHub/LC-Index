# SW-mngmt

Software de gestión de usuarios en desarrollo.

Aplicación web creada con Django que permite a los usuarios realizar cómodamente la gestión de su local privado.

## Características

- Registro de usuarios con verificación de email.
- Inicio de sesión y autenticación de usuarios.
- Subida y previsualización de fotos de perfil.
- Redimensionamiento automático de imágenes de perfil.
- Sistema de activación de cuenta por correo electrónico.

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
    source env/bin/activate  # En Windows usa `env\Scripts\activate`
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

### Registro de Usuario

La página de registro (/register/) permite a los nuevos usuarios registrarse proporcionando su nombre de usuario, email, contraseña y una foto de perfil opcional. La foto seleccionada se previsualiza antes de enviar el formulario.

### Activación de Cuenta

Después de registrarse, los usuarios deben activar su cuenta a través del enlace enviado a su correo electrónico.


## Estructura del Proyecto

    - mainapp/forms.py:
        RegisterForm: Formulario de registro personalizado que incluye email y foto de perfil.

    - mainapp/models.py:
        Organization: Modelo que extiende al usuario de Django para incluir una foto de perfil.

    - mainapp/views.py:
        index: Vista para la página de inicio y autenticación de usuarios.
        register: Vista para manejar el registro de nuevos usuarios y el envío de un correo electrónico de activación.
        resize_image: Función para redimensionar la imagen de perfil.
        activate: Vista para manejar la activación de la cuenta del usuario a través del enlace enviado por correo electrónico.

    - settings.py:
        Configuración de las variables de entorno para el envío de correos electrónicos y gestión de archivos multimedia.

## Contribuciones

Las contribuciones son bienvenidas. Por favor, sigue el flujo de trabajo estándar de GitHub:

    Haz un fork del repositorio.
    Crea una nueva rama (git checkout -b --jiracode--/nueva-funcionalidad).
    Realiza tus cambios y haz commits (git commit -m 'Añadir nueva funcionalidad').
    Envía tus cambios a tu fork (git push origin --jiracode--/nueva-funcionalidad).
    Abre un Pull Request en GitHub.

