class MyLexer:

    def __init__(self):
        self.tokens = []

    def read(self, string):
        for c in string:
            print("automata work")

class MyNumericAutomata:

    def __init__(self, token):
        self.currentState = 1
        self.token = token
        self.isDone = False
        self.interrupt = False

    def run(self):
        for c in self.token:
            if self.interrupt:
                break
            self.nextState(c)

    def nextState(self, c):
        if self.currentState in [1,2]:
            if c.isnumeric():
                self.currentState = 2
            else:
                self.interrupt = True
                self.done()

    def done(self):
        if self.currentState is 2:
            self.isDone = True
        else:
            self.isDone = False
