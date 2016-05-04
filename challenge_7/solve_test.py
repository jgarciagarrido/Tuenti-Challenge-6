from tiles import read_tile
from tiles_matrix import TileMatrix

if __name__ == "__main__":

    cases = int(input())
    for i in xrange(cases):
        rows, columns, tile = read_tile()
        print "Case #%d: %d %d" %(i + 1, rows, columns)
