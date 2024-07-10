from database.models import session, Member, Consumption
from datetime import datetime

##############################
# Este archivo maneja la lógica relacionada con los usuarios y sus operaciones.
##############################

class UserController:

    # UserController: Este controlador maneja la lógica detrás de las operaciones relacionadas con los usuarios, como agregar créditos y registrar consumiciones (UserDetailView).
    # __init__: En el inicializador del controlador, se vincula el método add_credit al evento de presionar el botón de "Agregar Crédito" (add_credit_button.bind(on_press=self.add_credit)) y el método register_consumption al evento de presionar el botón de "Registrar Consumición" (register_consumption_button.bind(on_press=self.register_consumption)).
    # add_credit: Este método es llamado cuando se presiona el botón de "Agregar Crédito". Extrae el monto ingresado por el usuario desde la vista (view.balance_input.text). Luego, actualiza el saldo del usuario (user.balance += amount) y confirma los cambios en la base de datos (session.commit()).
    # register_consumption: Este método es llamado cuando se presiona el botón de "Registrar Consumición". Extrae la descripción y el monto de la consumición ingresados por el usuario desde la vista (view.description_input.text, view.amount_input.text). Luego, crea un nuevo objeto Consumption con estos datos, lo agrega a la sesión y actualiza el saldo del usuario (user.balance -= amount). Finalmente, confirma los cambios en la base de datos (session.commit()).
    # get_user: Este método debería implementarse para obtener el usuario actual, por ejemplo, a través de la vista. En la implementación real, se debería acceder al usuario actualmente autenticado para realizar las operaciones.

    def __init__(self, view):
        self.view = view
        self.view.add_credit_button.bind(on_press=self.add_credit)
        self.view.register_consumption_button.bind(on_press=self.register_consumption)

    def add_credit(self, instance):
        user = self.get_user()
        amount = float(self.view.balance_input.text)
        
        # Actualizar el saldo del usuario
        user.balance += amount
        
        # Confirmar los cambios en la base de datos
        session.commit()
        
        # Imprimir un mensaje para confirmar la operación
        print(f"Added {amount} credits to {user.username}")

    def register_consumption(self, instance):
        user = self.get_user()
        description = self.view.description_input.text
        amount = float(self.view.amount_input.text)
        
        # Crear un nuevo objeto Consumption con los datos ingresados
        new_consumption = Consumption(member_id=user.id, description=description, amount=amount, time=datetime.now())
        
        # Agregar el nuevo consumo a la sesión y actualizar el saldo del usuario
        session.add(new_consumption)
        user.balance -= amount
        
        # Confirmar los cambios en la base de datos
        session.commit()
        
        # Imprimir un mensaje para confirmar la operación
        print(f"Registered consumption for {user.username}: {description} - {amount} credits")

    def get_user(self):
        # Implementar lógica para obtener el usuario actual (puede ser a través de la vista)
        pass
