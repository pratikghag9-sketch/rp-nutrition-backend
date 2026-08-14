from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

from models.product import Product
from models.order import Order, OrderItem
