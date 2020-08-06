from Include.models import db


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
