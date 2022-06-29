import unittest
from peewee import *
from app import TimelinePost

MODELS = [TimelinePost]
test_db = SqliteDatabase(':memory')

class TestTimelinePost(unittest.TestCase):
    def setUp(self):
        test_db.bind(MODELS, bind_refs=False, bind_backrefs=False)
        test_db.connect()
        test_db.create_tables(MODELS)

    def tearDown(self):
        test_db.drop_tables()
        test_db.close()
    
    def test_timeline_post():
        a = TimelinePost.create(name='John Doe', email='john@example.com', contents="Hello, I am John")
        assert a.id == 1
        b = TimelinePost.create(name='Jane Doe', email='jane@example.com', contents="Hello, I am Jane")
        assert b.id == 2