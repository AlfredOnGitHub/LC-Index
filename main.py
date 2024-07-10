# main.py

from kivy.app import App
from kivy.uix.screenmanager import ScreenManager
from database import SessionLocal   # Importa SessionLocal desde __init__.py para desarrollo
#from database.database_init import SessionLocal # Importa SessionLocal desde database_init.py para producción
from database.database_init import init_db
from database.models import Member
from views.login_view import LoginView
from views.register_view import RegisterView
from views.user_list_view import UserListView
from views.user_detail_view import UserDetailView
from views.consumption_view import ConsumptionView
from controllers.login_controller import LoginController
from controllers.register_controller import RegisterController
from controllers.user_controller import UserController

# Función para crear el usuario administrador si no existe
def create_admin_user():
    session = SessionLocal()

    # Verificar si ya existe un usuario administrador
    admin = session.query(Member).filter_by(role='admin').first()
    if admin:
        print("Usuario administrador ya existe.")
    else:
        # Si no existe, solicitar crear un nuevo usuario administrador
        admin_username = input("Ingrese nombre de usuario para el administrador: ")
        admin_password = input("Ingrese contraseña para el administrador: ")

        # Crear el usuario administrador
        admin = Member(username=admin_username, password=admin_password, role='admin')
        session.add(admin)
        session.commit()

        print(f"Usuario administrador '{admin_username}' creado exitosamente.")

    session.close()

# Llamada para crear el usuario administrador al iniciar la aplicación
create_admin_user()

# Clase principal de la aplicación Kivy
class ClubManagementApp(App):
    def build(self):
        self.screen_manager = ScreenManager()

        # Crear instancias de las vistas
        self.login_view = LoginView(name='login')
        self.register_view = RegisterView(name='register')
        self.user_list_view = UserListView(name='user_list')
        self.user_detail_view = UserDetailView(name='user_detail')
        self.consumption_view = ConsumptionView(name='consumption')

        # Añadir las vistas al ScreenManager
        self.screen_manager.add_widget(self.login_view)
        self.screen_manager.add_widget(self.register_view)
        self.screen_manager.add_widget(self.user_list_view)
        self.screen_manager.add_widget(self.user_detail_view)
        self.screen_manager.add_widget(self.consumption_view)

        # Crear instancias de los controladores y vincularlos con las vistas correspondientes
        LoginController(self.login_view)
        RegisterController(self.register_view)
        UserController(self.user_detail_view)

        return self.screen_manager

# Ejecutar la aplicación si este archivo es el punto de entrada
if __name__ == '__main__':
    ClubManagementApp().run()
