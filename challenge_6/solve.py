from piet import PVM, Interpreter

if __name__ == "__main__":
    pvm = PVM()
    interpreter = Interpreter('alice_shocked.png', pvm)
    while True:
        interpreter.step()
