from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Order(db.Model):
    __tablename__ = 'orders'
    id = db.Column(db.Integer, primary_key=True)
    table_number = db.Column(db.Integer, nullable=False)
    status = db.Column(db.String(50), nullable=False)
    employee_id = db.Column(db.Integer, db.ForeignKey('employees.id'))

    employee = db.relationship('Employee', backref='orders')

class OrderItem(db.Model):
    __tablename__ = 'order_items'
    id = db.Column(db.Integer, primary_key=True)
    order_id = db.Column(db.Integer, db.ForeignKey('orders.id'))
    product_id = db.Column(db.Integer, db.ForeignKey('products.id'))
    quantity = db.Column(db.Integer, nullable=False)

    order = db.relationship('Order', backref='items')
    product = db.relationship('Product', backref='order_items')