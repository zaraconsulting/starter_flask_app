from app.blueprints.api import bp as api
from flask import jsonify, request
from app.blueprints.blog.models import Post

@api.route('/posts', methods=['GET'])
def posts():
    return jsonify([p.to_dict() for p in Post.query.all()]), 200

@api.route('/post/<int:id>', methods=['GET'])
def post(id):
    return jsonify({}), 200

@api.route('/post/create', methods=['POST'])
def create_post():
    p = Post()
    p.from_dict(request.json)
    p.save()
    print(p.to_dict())
    return jsonify(p.to_dict()), 201

@api.route('/post/<int:id>/edit', methods=['PUT'])
def edit_post():
    return jsonify({}), 201

@api.route('/post/<int:id>/delete', methods=['DELETE'])
def delete_post():
    return jsonify({}), 201