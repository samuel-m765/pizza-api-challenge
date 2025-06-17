from server.models.restaurant import Restaurant
from server.models.pizza import Pizza
from server.models.restaurant_pizza import RestaurantPizza
from server.app import create_app, db


app = create_app()

with app.app_context():
    # Drop all tables and recreate them fresh
    db.drop_all()
    db.create_all()

    # Create some restaurants
    r1 = Restaurant(name="Kiki's Pizza", address="123 Pizza St")
    r2 = Restaurant(name="Luigi's Pizzeria", address="456 Pasta Rd")

    # Create some pizzas
    p1 = Pizza(name="Emma", ingredients="Dough, Tomato Sauce, Cheese")
    p2 = Pizza(name="Pepperoni", ingredients="Dough, Tomato Sauce, Cheese, Pepperoni")

    db.session.add_all([r1, r2, p1, p2])
    db.session.commit()

    # Create restaurant-pizza relationships with prices
    rp1 = RestaurantPizza(price=15, restaurant_id=r1.id, pizza_id=p1.id)
    rp2 = RestaurantPizza(price=18, restaurant_id=r1.id, pizza_id=p2.id)
    rp3 = RestaurantPizza(price=20, restaurant_id=r2.id, pizza_id=p2.id)

    db.session.add_all([rp1, rp2, rp3])
    db.session.commit()

    print("Database seeded successfully!")
