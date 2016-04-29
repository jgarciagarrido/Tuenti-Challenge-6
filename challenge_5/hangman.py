import telnetlib
from words import WordSeeker

class HangManGame():
    def __init__(self, words):
        self.tn = telnetlib.Telnet("52.49.91.111", 9988)
        self.seeker = WordSeeker(words)
        self.current_screen = None
        self.lines_screen = None

    def begin_game(self):
        print self.tn.read_until("...")
        self.tn.write("\n")

    def read_screen(self):
        self.current_screen = self.tn.read_until(">", 1)
        self.lines_screen = self.current_screen.split("\n")

    def is_in_game(self):

        return self.lines_screen[-1] == ">"

    def process_game_screen(self):
        secret_word = self.lines_screen[-3].split()
        self.pattern = ""
        for letter in secret_word:
            if letter=="_":
                self.pattern += "."
            else:
                self.pattern += letter
        self.seeker.select_by_regex(self.pattern)

    def play(self):
        self.begin_game()
        try:
            while True:
                    self.read_screen()
                    print self.current_screen
                    if self.is_in_game():
                        self.process_game_screen()
                        letter = self.seeker.get_letter()
                        print letter
                        self.tn.write(letter+"\n")
                    else:
                        print self.current_screen
                        raw_input()
                        self.seeker.reset()
                        self.tn.write("\n")
        except Exception as e:
            print "Se Acabo, introduce q para salir"
