from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from app.config import Config


db = SQLAlchemy()
migrate = Migrate()

def create_app(testing=False):
    app = Flask(__name__)
    app.config.from_object("app.config.Config")

    if testing:
        app.config["TESTING"] = True

    db.init_app(app)
    migrate.init_app(app, db)

    # API blueprints
    from app.routes.employees import employees_bp
    from app.routes.checks import checks_bp

    # Frontend blueprint
    from app.routes.frontend import frontend_bp

    app.register_blueprint(employees_bp, url_prefix="/api/employees")
    app.register_blueprint(checks_bp, url_prefix="/api/checks")
    app.register_blueprint(frontend_bp)  # 👈 frontend added

    return app

