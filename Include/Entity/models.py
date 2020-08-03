from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def configure(app):
    db.init_app(app)
    app.db = db


class Client(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(150))
    email = db.Column(db.String(50))
    groupClient_id = db.Column(db.Integer, db.ForeignKey('groupClient.id'))

    owner = db.relationship('GrupoClient', foreign_keys=groupClient_id)

    def __init__(self, name, email, groupClient_id):
        self.name = name
        self.email = email
        self.groupClient_id = groupClient_id

    def to_dict(self, columns=[]):
        if not columns:
            return {"id": self.id, "name": self.name, "email": self.email, "groupClient_id": self.groupClient_id}
        else:
            return {col: getattr(self, col) for col in columns}


class GrupoClient(db.Model):
    __tablename__ = "groupClient"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(150))

    def __init__(self, name):
        self.name = name

    def to_dict(self, columns=[]):
        if not columns:
            return {"id": self.id, "name": self.name}
        else:
            return {col: getattr(self, col) for col in columns}
