import sys
from itertools import izip

class TileMatrix():
    def __init__(self, rows, columns, tile):
        self.rows = rows
        self.columns = columns
        self.tile = tile
        self.max_sum = - sys.maxint + 1

    def find_infinity_sum(self):
        sum_rows = []
        for i in xrange(self.rows):
            sum_row = sum(self.tile[i])
            sum_rows.append(sum_row)
            self.max_sum = max(self.max_sum, sum_row)
            if sum_row>0:
                return True
        if sum(sum_rows)>0:
            return True
        for j in xrange(self.columns):
            column = [row[j] for row in self.tile]
            sum_column = sum(column)
            self.max_sum = max(self.max_sum, sum_column)
            if sum_column>0:
                return True
        return False

    def has_a_positive_number(self):
        for i in xrange(self.rows):
            for j in xrange(self.columns):
                if self.tile[i][j]>0:
                    return True
        return False

    def find_max_sum(self):
        self.max_sum = - sys.maxint + 1
        tiles_sample = [row * 2 for row in self.tile]*2
        for y in xrange(self.rows):
            for x in xrange(self.columns):
                for n in xrange(1,self.rows):
                    area_rows = tiles_sample[y:y+n]
                    sum_rows = [row[x] for row in area_rows]
                    sum_area = sum(sum_rows)
                    self.max_sum = max(self.max_sum, sum_area)
                    for m in xrange(1,self.columns-1):
                        column = [row[x+m] for row in area_rows]
                        sum_rows = [sum_row+item for (sum_row, item) in izip(sum_rows, column)]
                        sum_area = sum(sum_rows)
                        self.max_sum = max(self.max_sum, sum_area)
        return self.max_sum
