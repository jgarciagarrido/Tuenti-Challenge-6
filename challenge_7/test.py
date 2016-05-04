import unittest
from tiles_matrix import TileMatrix
class TestTilesMatrix(unittest.TestCase):
    def test_find_max_sum_case_1(self):
        tile = TileMatrix(2,2,[[1,2],[3,4]])
        result = tile.find_max_sum_by_size(1,1)
        self.assertEqual(result, 4)
        result = tile.find_max_sum_by_size(1,2)
        self.assertEqual(result, 7)
        result = tile.find_max_sum_by_size(2,1)
        self.assertEqual(result, 6)
        result = tile.find_max_sum_by_size(2,1)
        self.assertEqual(result, 6)

if __name__ == '__main__':
    unittest.main()
