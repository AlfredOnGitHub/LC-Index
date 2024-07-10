from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

##############################
# Vista del registro de inventario.
##############################

class ConsumptionView(Screen):

    # ConsumptionView: Es una pantalla que contiene un formulario para registrar una
    # nueva consumición con campos para la descripción y el monto, y un botón de registro.

    def __init__(self, **kwargs):
        super(ConsumptionView, self).__init__(**kwargs)
        self.layout = BoxLayout(orientation='vertical')
        
        self.description_label = Label(text='Description:')
        self.description_input = TextInput()
        
        self.amount_label = Label(text='Amount:')
        self.amount_input = TextInput()
        
        self.register_button = Button(text='Register')
        
        # Añadir widgets al layout
        self.layout.add_widget(self.description_label)
        self.layout.add_widget(self.description_input)
        self.layout.add_widget(self.amount_label)
        self.layout.add_widget(self.amount_input)
        self.layout.add_widget(self.register_button)
        
        self.add_widget(self.layout)
