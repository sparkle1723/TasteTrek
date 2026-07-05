from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_wtf.csrf import CSRFProtect
from os import path

db = SQLAlchemy()
login_manager = LoginManager()
login_manager.login_view = 'auth.login'
login_manager.login_message_category = 'warning'
csrf = CSRFProtect()


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'tastetrek_secret_key_2026'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tastetrek.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['WTF_CSRF_ENABLED'] = True
    app.config['WTF_CSRF_ERROR_VIEW'] = 'main.csrf_error'

    db.init_app(app)
    login_manager.init_app(app)
    csrf.init_app(app)

    from tastetrek.routes.main import main_bp
    from tastetrek.routes.auth import auth_bp
    from tastetrek.routes.events import events_bp
    from tastetrek.routes.bookings import bookings_bp

    app.register_blueprint(main_bp)
    app.register_blueprint(auth_bp, url_prefix='/auth')
    app.register_blueprint(events_bp, url_prefix='/events')
    app.register_blueprint(bookings_bp, url_prefix='/bookings')

    from tastetrek import models
    from tastetrek.models import User

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    with app.app_context():
        if not path.exists(path.join(app.instance_path, 'tastetrek.db')):
            db.create_all()
            from tastetrek.seed_data import seed_database
            seed_database()

    @app.errorhandler(404)
    def not_found(e):
        return render_template('404.html'), 404

    @app.errorhandler(403)
    def forbidden(e):
        return render_template('403.html'), 403

    @app.errorhandler(500)
    def server_error(e):
        return render_template('500.html'), 500

    return app
