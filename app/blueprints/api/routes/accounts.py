from app.blueprints.api import bp as api
from flask import jsonify, request
from app.blueprints.auth.models import Account

@api.route('/accounts', methods=['GET'])
def accounts():
    return jsonify([p.to_dict() for p in Account.query.all()]), 200

@api.route('/account/<int:id>', methods=['GET'])
def account(id):
    return jsonify({}), 200

@api.route('/account/create', methods=['POST'])
def create_account():
    a = Account()
    a.from_dict(request.json)
    a.set_password(a.password)
    a.save()
    return jsonify(a.to_dict()), 201

@api.route('/account/<int:id>/edit', methods=['PUT'])
def edit_account():
    return jsonify({}), 201

@api.route('/account/<int:id>/delete', methods=['DELETE'])
def delete_account():
    return jsonify({}), 201