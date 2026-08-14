from flask import Blueprint, request, jsonify
from models import db
from models.order import Order, OrderItem
from models.product import Product

orders_bp = Blueprint('orders', __name__)

@orders_bp.route('/api/orders', methods=['POST'])
def create_order():
    data = request.get_json()

    order = Order(
        customer_name=data['customer_name'],
        phone=data['phone'],
        address=data.get('address', ''),
        total_amount=0
    )

    total = 0
    for item in data['items']:
        product = Product.query.get(item['product_id'])
        if not product:
            return jsonify({"error": f"Product {item['product_id']} not found"}), 400

        line_total = product.price * item['quantity']
        total += line_total

        order_item = OrderItem(
            product_id=product.id,
            quantity=item['quantity'],
            price_at_order=product.price
        )
        order.items.append(order_item)

    order.total_amount = total
    db.session.add(order)
    db.session.commit()

    return jsonify(order.to_dict()), 201

@orders_bp.route('/api/orders/<int:order_id>', methods=['GET'])
def get_order(order_id):
    order = Order.query.get_or_404(order_id)
    return jsonify(order.to_dict())
