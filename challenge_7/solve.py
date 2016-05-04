from tiles import read_tile
from tiles_matrix import TileMatrix

if __name__ == "__main__":

    cases = int(input())
    for i in xrange(cases):
        rows, columns, tile = read_tile()
        tile_matrix = TileMatrix(rows, columns, tile)
        if not tile_matrix.has_a_positive_number():
            result = "0"
        elif tile_matrix.find_infinity_sum():
            result = "INFINITY"
        else:
            result = tile_matrix.find_max_sum()
        print "Case #%d: %s" %(i + 1, result)
