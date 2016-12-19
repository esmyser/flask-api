from flask import Flask, Response, request, jsonify
from flask_cors import CORS, cross_origin
from flask_sqlalchemy import SQLAlchemy

import os
import psycopg2
import urllib.parse
import uuid
import json

app = Flask(__name__)

# CORS
app.config['CORS_HEADERS'] = 'Content-Type'
CORS(app)

# Database
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DATABASE_URL']
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
from models import Todo

@app.route('/todos', methods=['GET', 'POST'])
@cross_origin()
def index():
    if request.method == 'POST':
        order = len(Todo.query.all())
        todo = Todo(order, request.form['text'])
        db.session.add(todo)
        db.session.commit()
        return jsonify(todo)
    else:
        # not working, objects not jsonify'able...
        todos = Todo.query.all()
        return jsonify({ 'todos': todos })

# @app.route('/todos/<todo_id>')
# def show_todo():
#     return "placeholder"

# @app.route('/todos/<todo_id>/edit', methods=['PUT'])
# def edit_todo():
#     return "placeholder"

# @app.route('/todos/<todo_id>/toggle', methods=['PUT'])
# def finish_todo():
#     return "placeholder"

# @app.route('/todos/<todo_id>/delete', methods=['DELETE'])
# def delete_todo():
#     return "placeholder"

if __name__ == '__main__':
    app.run(debug=True)
    
