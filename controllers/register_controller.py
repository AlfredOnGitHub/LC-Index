from database.models import session, Member

##############################
# Este archivo maneja la lógica del registro de nuevos usuarios.
##############################

class RegisterController:

    # RegisterController: Este controlador maneja la lógica detrás del formulario de registro (RegisterView).
    # __init__: En el inicializador del controlador, se vincula el método register al evento de presionar el botón de registro (register_button.bind(on_press=self.register)).
    # register: Este método es llamado cuando se presiona el botón de registro. Extrae el nombre de usuario, la contraseña y el rol ingresados por el usuario desde la vista (view.username_input.text, view.password_input.text, view.role_input.text). Luego, crea un nuevo objeto Member con estos datos.
    # new_member: Es el nuevo objeto Member que se va a agregar a la base de datos.
    # session.add(new_member): Agrega el nuevo miembro a la sesión.
    # session.commit(): Confirma los cambios en la base de datos.

    def __init__(self, view):
        self.view = view
        self.view.register_button.bind(on_press=self.register)

    def register(self, instance):
        username = self.view.username_input.text
        password = self.view.password_input.text
        role = self.view.role_input.text
        
        # Crear un nuevo objeto Member con los datos ingresados
        new_member = Member(username=username, password=password, role=role)
        
        # Agregar el nuevo miembro a la sesión y confirmar los cambios en la base de datos
        session.add(new_member)
        session.commit()
        
        # Imprimir un mensaje para confirmar el registro del usuario
        print(f"User {username} registered")
