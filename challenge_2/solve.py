def read_manuscript(name):
    manuscript = open(name)
    content = manuscript.readline()
    return content.split()

if __name__ == "__main__":
    manuscript_words = read_manuscript('corpussample.txt')
    print manuscript_words[11-1:22].count("Blue")
