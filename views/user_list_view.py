from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView

##############################
# Vista de listado de usuarios.
##############################

class UserListView(Screen):

    # UserListView: Es una pantalla que contiene una lista de usuarios y un botón de actualización.

    def __init__(self, **kwargs):
        super(UserListView, self).__init__(**kwargs)
        self.layout = BoxLayout(orientation='vertical')
        
        self.user_list = ScrollView()
        
        # Añadir widgets al layout
        self.add_widget(self.user_list)
        self.refresh_button = Button(text='Refresh')
        self.layout.add_widget(self.refresh_button)
        
        self.add_widget(self.layout)
