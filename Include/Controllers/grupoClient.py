from flask import Blueprint, Response, request
from Include.Entity.models import db, GrupoClient
import json

app = Blueprint('grupoClient', __name__)


@app.route('/')
def index():
    grupoClient = GrupoClient.query.all()
    result = [gc.to_dict() for gc in grupoClient]
    # rows = db.session.execute("SELECT name, email FROM user ").fetchall()
    # result = [dict(r) for r in rows]
    return Response(response=json.dumps(result), status=200, content_type="application/json")


@app.route('/view/<int:id>', methods=['GET'])
def view(id):
    groupClient = GrupoClient.query.get(id)
    return Response(response=json.dumps(groupClient.to_dict()), status=200, content_type="application/json")


@app.route('/add', methods=['POST'])
def add():
    grupoClient = GrupoClient(request.json['name'])
    db.session.add(grupoClient)
    db.session.commit()
    return Response(response=json.dumps(grupoClient.to_dict()), status=200, content_type="application/json")


@app.route('/edit/<int:id>', methods=['PUT'])
def edit(id):
    grupoClient = GrupoClient.query.get(id)
    grupoClient.name = request.json['name']
    db.session.commit()
    return Response(response=json.dumps(grupoClient.to_dict()), status=201, content_type="application/json")


@app.route('/delete/<int:id>', methods=['DELETE'])
def delete(id):
    grupoClient = GrupoClient.query.get(id)
    db.session.delete(grupoClient)
    db.session.commit()
    return Response(response=json.dumps(grupoClient.to_dict()), status=201, content_type="application/json")
