import unittest
from weather import weather

class TestStringMethods(unittest.TestCase):

	def test_valid_answer(self):
		s = "94704"
		self.assertTrue(weather(s))

	def test_non_zipcodes(self):
		s = "local"
		self.assertTrue(weather(s), "local is not a valid zipcode")
		s = '2'
		self.assertTrue(weather(s), "2 is not a valid zipcode")

	def test_no_args(self):
		s = ""
		self.assertEqual(weather(s), "/weather takes in only 1 arguement")

	def test_two_args(self):
		s = 'hello world'
		self.assertEqual(weather(s), "/weather takes in only 1 arguement")



if __name__ == '__main__':
	unittest.main()