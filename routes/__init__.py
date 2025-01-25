# src/routes/__init__.py
def register_routes(app):
    from routes.auth_routes import auth_bp
    from routes.person_routes import person_bp
    from routes.product_routes import product_bp
    from routes.comment_routes import comment_bp

    app.register_blueprint(auth_bp, url_prefix="/auth")
    app.register_blueprint(person_bp, url_prefix="/persons")
    app.register_blueprint(product_bp, url_prefix="/products")
    app.register_blueprint(comment_bp, url_prefix="/comments")
