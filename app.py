from flask import Flask
from models.employee import db
from routes.employee_routes import employee_bp



app = Flask(__name__)
app.config.from_object('config.Config')

db.init_app(app)

# Registrar blueprints
app.register_blueprint(employee_bp)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # Crea las tablas si no existen
    app.run(debug=True)

from flask_migrate import Migrate

migrate = Migrate(app, db)