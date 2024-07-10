from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

class LoginView(Screen):

    def __init__(self, **kwargs):
        super(LoginView, self).__init__(**kwargs)
        self.layout = BoxLayout(orientation='vertical')

        self.username_label = Label(text='Username:')
        self.username_input = TextInput()

        self.password_label = Label(text='Password:')
        self.password_input = TextInput(password=True)

        self.login_button = Button(text='Login')

        # Añadir widgets al layout
        self.layout.add_widget(self.username_label)
        self.layout.add_widget(self.username_input)
        self.layout.add_widget(self.password_label)
        self.layout.add_widget(self.password_input)
        self.layout.add_widget(self.login_button)

        self.add_widget(self.layout)
