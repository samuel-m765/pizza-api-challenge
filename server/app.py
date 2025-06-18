from flask import Flask
from . import db, migrate
from .controllers.restaurant_pizza_controller import restaurant_pizza_bp
from .controllers.pizza_controller import pizza_bp
from .controllers.restaurant_controller import restaurant_bp
def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///school.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['DEBUG'] = True  # ✅ Already present
    app.config['ENV'] = 'development'  # ✅ Add this line

    db.init_app(app)
    migrate.init_app(app, db)

    # Register Blueprints
    app.register_blueprint(restaurant_bp, url_prefix='/restaurants')
    app.register_blueprint(pizza_bp, url_prefix='/pizzas')
    app.register_blueprint(restaurant_pizza_bp, url_prefix='/restaurant_pizzas')

    return app
