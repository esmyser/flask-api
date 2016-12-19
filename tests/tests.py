from flask_testing import TestCase  
from app import db, app
from models import Item

import os

SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']

class MyTest(TestCase):

    def create_app(self):
        app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI
        return app

    def setUp(self):  
        db.create_all()
        ## create users:
        item = Item('get the milk', 0)
        item2 = Item('yoga', 1)
        db.session.add(item)
        db.session.add(item2)
        db.session.commit()

    def test_get_all_items(self):  
        items = Item.query.all()
        assert len(items) == 2, 'Expect all items to be returned'

    def test_get_item(self):  
        item = Item.query.filter_by(order=1).first()
        assert item.order == 1, 'Expect the correct item to be returned'

    def tearDown(self):
        db.session.remove()
        db.drop_all()

