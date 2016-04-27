import yaml
import sys
class YATM():
    def __init__(self, program):
        self.program = program
        self.index = 0
        self.output = ''
        self.state = 'start'
        self.input = ''
        self.current_case = ' '

    def reset(self):
        self.index = 0
        self.output = ''
        self.state = 'start'
        self.input = ''

    def run_procedure(self, procedure):
        if 'write' in procedure:
            self.input[self.index] = procedure['write']
        if 'move' in procedure:
            if procedure['move']=="right":
                self.index += 1
            if procedure['move']=="left":
                self.index -= 1
            if self.index == len(self.input):
                self.input.append(' ')
            if self.index == -1:
                self.input = [' '] + self.input
                self.index = 0
        if 'state' in procedure:
            self.state = procedure['state']
        # print self.output
        # print self.index
        # print self.state


    def run_state(self):
        current_case = self.input[self.index]
        state_procedure = self.program['code'][self.state]
        procedure = state_procedure[current_case]
        self.run_procedure(procedure)

    def run_tape(self, index):
        self.input = list(self.program['tapes'][index])
        while self.state!='end':
            self.run_state()
        self.output = "".join(self.input)
        return self.output

    def run_all(self):
        for tape in self.program['tapes']:
            output = self.run_tape(tape)
            print "Tape #%d: %s" % (tape, output)
            self.reset()

if __name__ == "__main__":
    f = open(sys.argv[1])
    program = yaml.load(f)
    yatm_microservice = YATM(program)
    # print yatm_microservice.run_tape(2)
    yatm_microservice.run_all()
