
cases = int(input())

for i in range(cases):
    diners = int(input())
    if diners == 0:
        tables = 0
    elif diners <= 4:
        tables = 1
    else:
        diners_at_side = 2 - (diners % 2)
        tables = (diners - diners_at_side) / 2
    print "Case #%d: %d" %(i + 1, tables)
