import unittest
from shorten_url import shorten_url

class TestStringMethods(unittest.TestCase):

	def test_valid_answer(self):
		s = "www.google.com"
		self.assertTrue(shorten_url(s))

	def test_no_args(self):
		s = ""
		self.assertEqual(shorten_url(s), "/shortenUrl must take only 1 arguement")

	def test_two_args(self):
		s = 'hello world'
		self.assertEqual(shorten_url(s), "/shortenUrl must take only 1 arguement")



if __name__ == '__main__':
	unittest.main()