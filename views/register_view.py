from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

##############################
# Vista de registro de usuarios.
##############################

class RegisterView(Screen):

    # RegisterView: Es una pantalla que contiene un formulario de registro con campos de texto
    # para el nombre de usuario, la contraseña y el rol, y un botón de registro.

    def __init__(self, **kwargs):
        super(RegisterView, self).__init__(**kwargs)
        self.layout = BoxLayout(orientation='vertical')
        
        self.username_label = Label(text='Username:')
        self.username_input = TextInput()
        
        self.password_label = Label(text='Password:')
        self.password_input = TextInput(password=True)
        
        self.role_label = Label(text='Role:')
        self.role_input = TextInput()
        
        self.register_button = Button(text='Register')
        
        # Añadir widgets al layout
        self.layout.add_widget(self.username_label)
        self.layout.add_widget(self.username_input)
        self.layout.add_widget(self.password_label)
        self.layout.add_widget(self.password_input)
        self.layout.add_widget(self.role_label)
        self.layout.add_widget(self.role_input)
        self.layout.add_widget(self.register_button)
        
        self.add_widget(self.layout)
