import unittest
from app import app

class TestApp(unittest.TestCase):
	def test_home(self):
		tester = app.test_client(self)
		response = tester.get('/')
		self.assertEqual(response.status_code, 200)

if _name_ == '_main_':
	unittest.main()
