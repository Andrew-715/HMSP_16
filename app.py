from utils.funtions import starting_flask
from blueprints.user.user import user
from blueprints.order.order import order
from blueprints.offer.offer import offer
from utils.funtions import database_user, database_offer, database_order
from utils.models import User, Offer, Order
from setup_db import db

# В переменой app находится функция для запуска приложения.
app = starting_flask()

# Используя переменную вызываем blueprint user.
app.register_blueprint(user)

# Используя переменную вызываем blueprint order.
app.register_blueprint(order)

# Используя переменную вызываем blueprint offer.
app.register_blueprint(offer)

with app.app_context():

    database_user(db, User)
    # Импортируемая функция database_user добавляет уже заданные данные
    # из json_data.py в базу данных default.db

    database_order(db, Order)
    # Импортируемая функция database_offer добавляет уже заданные данные
    # из json_data.py в базу данных default.db

    database_offer(db, Offer)
    # Импортируемая функция database_order добавляет уже заданные данные
    # из json_data.py в базу данных default.db

if __name__ == '__main__':
    app.run(debug=True)
