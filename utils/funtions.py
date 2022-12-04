from flask import Flask
from database import json_data



def starting_flask():
    '''
    Функция starting_flask обеспечивает запуск flask-приложения
    '''
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database/default.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    if __name__ == '__main__':
        app.run(debug=True)


def database_user(db, User):
    '''
    Функция database_user позволяет добавить данные из json_data
    в таблицу user.
    '''
    db.drop_all()
    db.create_all()

    for user_data in json_data.users:
        new_user = User(
            id = user_data['id'],
            first_name = user_data['first_name'],
            last_name = user_data['last_name'],
            age = user_data['age'],
            email = user_data['email'],
            role = user_data['role'],
            phone = user_data['phone']
        )

        db.session.add(new_user)
        db.session.commit()


def database_order(db, Order):
    '''
    Функция database_order позволяет добавить данные из json_data
    в таблицу order.
    '''
    db.drop_all()
    db.create_all()

    for user_data in json_data.orders:
        new_user = Order(
            id = user_data['id'],
            name = user_data['name'],
            description = user_data['description'],
            start_date = user_data['start_date'],
            end_date = user_data['end_date'],
            address = user_data['address'],
            price = user_data['price'],
            customer_id =  user_data['customer_id'],
            executor_id = user_data['executor_id']
        )

        db.session.add(new_user)
        db.session.commit()


def database_offer(db, Offer):
    '''
    Функция database_user позволяет добавить данные из json_data
    в таблицу user.
    '''
    db.drop_all()
    db.create_all()

    for user_data in json_data.offers:
        new_user = Offer(
            id = user_data['id'],
            order_id =  user_data['order_id'],
            executor_id = user_data['executor_id']
        )

        db.session.add(new_user)
        db.session.commit()
