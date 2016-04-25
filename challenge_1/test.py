import unittest
from solve import hola
class TestChallenge1(unittest.TestCase):
    def test_true(self):
        self.assertTrue(hola())

if __name__ == '__main__':
    unittest.main()
