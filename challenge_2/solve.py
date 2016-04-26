from operator import itemgetter


def read_manuscript(name):
    manuscript = open(name)
    content = manuscript.readline()
    return content.split()

def count_words(words):
    stats = {}
    for word in words:
        if word not in stats:
            stats[word] = 1
        else:
            stats[word] += 1
    return stats.items()

def most_frequent_words(stats):
    stats_ordered = sorted(stats, key=itemgetter(1), reverse=True)
    return stats_ordered[:3]

def stats_to_string(stats):
    stats_in_string = []
    for stat in stats:
        stats_in_string.append("%s %d" % stat)
    return ",".join(stats_in_string)

if __name__ == "__main__":
    manuscript_words = read_manuscript('corpus.txt')
    cases = int(input())
    for i in xrange(cases):
        line_range = raw_input()
        a,b = map(lambda x: int(x), line_range.split())
        stats = count_words(manuscript_words[a-1:b])
        tree_most_frequent = most_frequent_words(stats)
        print  "Case #%d: %s" % (i + 1, stats_to_string(tree_most_frequent))
