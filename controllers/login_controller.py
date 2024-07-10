from database.models import session, Member

class LoginController:

    def __init__(self, view):
        self.view = view
        self.view.login_button.bind(on_press=self.login)

    def login(self, instance):
        username = self.view.username_input.text
        password = self.view.password_input.text

        user = session.query(Member).filter_by(username=username, password=password).first()

        if user:
            # Aquí se debería cambiar a la vista de detalle del usuario
            print(f"Welcome {user.username}")
            self.view.manager.current = 'user_detail'  # Cambiar a la vista de detalle de usuario
        else:
            print("Invalid credentials")
