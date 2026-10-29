import unittest
import app as todo_app

class TodoApiTest(unittest.TestCase):

    def setUp(self):
        todo_app.app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///:memory:"
        todo_app.app.config["TESTING"] = True
        self.client = todo_app.app.test_client()
        self.ctx = todo_app.app.app_context()
        self.ctx.push()
        todo_app.db.drop_all()
        todo_app.db.create_all()

    def tearDown(self):
        todo_app.db.session.remove()
        self.ctx.pop()

    def test_만든_것이_목록에_그대로_나온다(self):
        self.client.post("/api/todos/", json={"text":})