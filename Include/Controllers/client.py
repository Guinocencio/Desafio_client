from flask import Blueprint, Response, request
from Include.models import db
from Include.Entity.Client import Client
import json

app = Blueprint('client', __name__)


@app.route('/')
def index():
    client = Client.query.all()
    result = [u.to_dict() for u in client]
    return Response(response=json.dumps(result), status=200, content_type="application/json")


@app.route('/view/<int:id>', methods=['GET'])
def view(id):
    client = Client.query.get(id)
    return Response(response=json.dumps(client.to_dict()), status=200, content_type="application/json")


@app.route('/add', methods=['GET', 'POST'])
def add():
    client = Client(request.json['name'], request.json['email'], request.json['groupClient_id'])
    db.session.add(client)
    db.session.commit()
    return Response(response=json.dumps(client.to_dict()), status=200, content_type="application/json")


@app.route('/edit/<int:id>', methods=['PUT'])
def edit(id):
    client = Client.query.get(id)
    client.name = request.json['name']
    client.email = request.json['email']
    client.groupClient_id = request.json['groupClient_id']
    db.session.commit()
    return Response(response=json.dumps(client.to_dict()), status=201, content_type="application/json")


@app.route('/delete/<int:id>', methods=['DELETE'])
def delete(id):
    client = Client.query.get(id)
    db.session.delete(client)
    db.session.commit()
    return Response(response=json.dumps(client.to_dict()), status=201, content_type="application/json")
