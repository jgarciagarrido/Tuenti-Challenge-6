def generate_translation():
    uppercases = [(chr(letter), letter-ord("A")+1) for letter in xrange(ord('A'), ord('Z')+1)]
    lowercases = [(chr(letter), -(letter-ord("a")+1)) for letter in xrange(ord('a'), ord('z')+1)]
    point = [('.',0)]
    return dict(uppercases+lowercases+point)

def read_tile():
    translation = generate_translation()
    line_range = raw_input()
    rows, columms = map(lambda x: int(x), line_range.split())
    tile = []
    for n in xrange(rows):
        line = raw_input()
        row_letters  = list(line)
        row = [translation[letter] for letter in row_letters]
        tile.append(row)

    return (rows, columms, tile)
