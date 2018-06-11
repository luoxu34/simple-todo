#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from flask import Flask
from flask_script import Manager, Server, Shell

from models import db
from views import ToDoView


basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
db.init_app(app)

@app.route('/')
def index():
    return '''<h1>This is Simple TODO RESTful API.</h1>'''

todo_view = ToDoView.as_view('todo_view')
app.add_url_rule('/todos/', defaults={'todo_id': None},
                 view_func=todo_view, methods=['GET',])
app.add_url_rule('/todos/', view_func=todo_view, methods=['POST',])
app.add_url_rule('/todos/<int:todo_id>', view_func=todo_view,
                 methods=['GET', 'PATCH', 'DELETE'])

def make_shell_context():
    return dict(app=app, db=db)

manager = Manager(app)
manager.add_command('runserver', Server(host='0.0.0.0', port=8080, use_debugger=True))
manager.add_command('shell', Shell(make_context=make_shell_context))


if __name__ == '__main__':
    manager.run()
