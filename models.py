from app import db 

class Todo(db.Model):  
    __tablename__ = 'todos'

    id = db.Column(db.Integer, primary_key=True)
    order = db.Column(db.Integer)
    text = db.Column(db.Text)
    completed = db.Column(db.Boolean, default=False, nullable=False)

    def __init__(self, order, text):
        self.order = order
        self.text = text
        self.completed = False

    def __repr__(self):
        return '<{}>'.format(self.text)