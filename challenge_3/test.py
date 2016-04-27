import unittest
import yaml

class TestPyYAML(unittest.TestCase):
    def test_yaml(self):
        f = open("sampleInput.txt")
        program = yaml.load(f)
        self.assertIn('code', program)
        self.assertIn('tapes', program)


if __name__ == '__main__':
    unittest.main()
