from utils.funtions import starting_flask
from blueprints.user.user import user
from blueprints.order.order import order
from blueprints.offer.offer import offer


app = starting_flask()
'''
В переменой app находится функция для запуска приложения.
'''

app.register_blueprint(user)
'''
Используя переменную вызываем blueprint user.
'''

app.register_blueprint(order)
'''
Используя переменную вызываем blueprint order.
'''

app.register_blueprint(offer)
'''
Используя переменную вызываем blueprint offer.
'''
