from flask import Flask
from flask_cors import CORS
from flask_jwt_extended import JWTManager
from config import Config
from models import db
from routes.products import products_bp
from routes.orders import orders_bp
from routes.auth import auth_bp

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    CORS(app)
    db.init_app(app)
    JWTManager(app)

    app.register_blueprint(products_bp)
    app.register_blueprint(orders_bp)
    app.register_blueprint(auth_bp)

    return app

app = create_app()

@app.route('/')
def home():
    return {"message": "RP Nutrition backend is running!"}

if __name__ == '__main__':
    app.run(debug=True)
