from words import WordDictionary
from hangman import HangManGame


if __name__ == "__main__":
    dictionary = WordDictionary("words.txt")
    while True:
        hangman = HangManGame(dictionary.words)
        hangman.play()
        line = raw_input()
        if len(line)>0 and line[0] == 'q':
            break
