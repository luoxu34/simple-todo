# -*- coding: utf-8 -*-

import datetime
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()

class ToDo(db.Model):
    __tablename__ = 'todos'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(128), nullable=False)
    complete = db.Column(db.Boolean, default=False)
    notes = db.Column(db.String(1024), nullable=True)
    create_time = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    deadline = db.Column(db.DateTime, nullable=True)
    tag = db.Column(db.String(64), default='default')

    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def to_dict(self):
        _dict = {}

        _dict['id'] = self.id
        _dict['title'] = self.title
        _dict['complete'] = self.complete
        _dict['notes'] = self.notes
        _dict['create_time'] = self.create_time
        _dict['deadline'] = self.deadline
        _dict['tag'] = self.tag

        return _dict
