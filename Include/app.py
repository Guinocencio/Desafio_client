from Include.Controllers.client import app as client_controller
from Include.Controllers.grupoClient import app as grupoClient_controller
from Include.models import configure as config_db
from Include.models import db
from flask import Flask
from flask_migrate import Migrate

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://desafio:123456@localhost/desafio'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

config_db(app)

migrate = Migrate(app, db)

app.register_blueprint(client_controller, url_prefix="/client/")
app.register_blueprint(grupoClient_controller, url_prefix="/group-client/")

if __name__ == '__main__':
    db.init_app(app=app)
    with app.test_request_context():
        db.create_all()
    app.run(debug=True)
