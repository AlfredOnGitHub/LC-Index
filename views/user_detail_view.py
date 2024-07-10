from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from database.models import session, Member

class UserDetailView(Screen):

    def __init__(self, **kwargs):
        super(UserDetailView, self).__init__(**kwargs)
        self.layout = BoxLayout(orientation='vertical')

        self.username_label = Label(text='Username:')
        self.username_input = TextInput(readonly=True)

        self.balance_label = Label(text='Balance:')
        self.balance_input = TextInput(readonly=True)

        self.add_credit_button = Button(text='Add Credit')
        self.register_consumption_button = Button(text='Register Consumption')

        # Añadir widgets al layout
        self.layout.add_widget(self.username_label)
        self.layout.add_widget(self.username_input)
        self.layout.add_widget(self.balance_label)
        self.layout.add_widget(self.balance_input)
        self.layout.add_widget(self.add_credit_button)
        self.layout.add_widget(self.register_consumption_button)

        self.add_widget(self.layout)

        # Cargar datos del usuario al iniciar la vista
        self.load_user_data()

    def load_user_data(self):
        # Cargar datos del usuario actual
        user = session.query(Member).filter_by(username='usuario_actual').first()  # Ajustar 'usuario_actual' según el usuario logueado
        if user:
            self.username_input.text = user.username
            self.balance_input.text = str(user.balance)
