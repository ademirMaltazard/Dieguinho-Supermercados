# -------------------------------------------------------------------------
# app.py

from flask import Flask
from database import db
from routes.person_routes import person_bp
from routes.home_route import home_bp
from routes.product_routes import product_bp
from routes.comment_routes import comment_bp
from routes.auth_routes import auth_bp

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:@localhost/dieguinhoSupermercado'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'Segredo'

db.init_app(app)

# Registrar Blueprints
app.register_blueprint(home_bp, url_prefix='/')
app.register_blueprint(person_bp, url_prefix='/api/person')
app.register_blueprint(product_bp, url_prefix='/api/product')
app.register_blueprint(comment_bp, url_prefix='/api/comment')
app.register_blueprint(auth_bp, url_prefix='/api/auth')

if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)
