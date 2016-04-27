combos = [
    ['D','RD','R','P'],
    ['R','D','RD','P'],
    ['D','LD','L','K']
]

def has_missed_this_combo(moves, combo):
    has_the_previous_moves = moves[0:3] == combo[0:-1]
    not_has_the_action = moves != combo
    return has_the_previous_moves and not_has_the_action

def find_combos_missed_in_position(moves, index):
    for combo in combos:
        end_moves = index + 4
        potential_combo= moves[index:end_moves]
        if has_missed_this_combo(potential_combo, combo):
            return 1
    return 0

def find_combos_missed(moves):
    missed_combos = 0
    for index in xrange(len(moves)-1):
        missed_combos += find_combos_missed_in_position(moves,index)
    return missed_combos

if __name__ == "__main__":
    cases = int(input())
    for i in xrange(cases):
        line_range = raw_input()
        moves = line_range.split("-")
        combos_missed = find_combos_missed(moves)
        print  "Case #%d: %d" % (i + 1, combos_missed)
