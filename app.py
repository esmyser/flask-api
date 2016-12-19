from flask import Flask, Response, request, jsonify
from flask_cors import CORS, cross_origin
from flask_sqlalchemy import SQLAlchemy

import os
import psycopg2
import urllib.parse
import uuid

app = Flask(__name__)

# CORS
app.config['CORS_HEADERS'] = 'Content-Type'
CORS(app)

# # Database
# # would have to split this into two git repos to get it to work with heroku (Procfile, requirements.txt, runtime.txt need to be in root folder)
# app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DATABASE_URL']
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# db = SQLAlchemy(app)
# from models import Todo

todos = [{
    'id': uuid.uuid4(),
    'text': 'testing 123 can you see me?',
    'completed': False,
    'order': 0
}]

@app.route('/todos', methods=['GET', 'POST'])
@cross_origin()
def index():
    if request.method == 'POST':
        # order = len(Todo.query.all())
        # print(order)
        # todo = Todo(order, request.form['text'])
        # print(todo)
        # db.session.add(todo)
        # db.session.commit()
        print('adding the todo: ')
        todo = {
            'id': uuid.uuid4(),
            'text': request.form['text'],
            'completed': False,
            'order': len(todos)
        }
        print(todo)
        todos.append(todo)
        print(todos)
        return jsonify(**todo)
    else:
        # todos = Todo.query.all()
        print('getting all todos: ')
        print(todos)
        return jsonify({ 'todos': todos })

# @app.route('/todos/<int:todo_id>')
# def show_todo():
#     return "placeholder"

# @app.route('/todos/<int:todo_id>/edit', methods=['PUT'])
# def edit_todo():
#     return "placeholder"

# @app.route('/todos/<int:todo_id>/toggle', methods=['PUT'])
# def finish_todo():
#     return "placeholder"

# @app.route('/todos/<int:todo_id>/delete', methods=['DELETE'])
# def delete_todo():
#     return "placeholder"

if __name__ == '__main__':
    app.run(debug=True)
    
