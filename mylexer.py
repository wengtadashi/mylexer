class MyLexer:

    def __init__(self):
        self.tokens = []

    def read(self, string):


class MyAutomata:

    NUMBER = 1
    ID = 2
    OPERATOR = 3

    OPERATORS = [
        '+',
        '-',
        '*',
        '/',
        '%',
        '=',
        '(',
        ')',
    ]

    STATE_TYPE = {
        1: NUMBER,
        2: ID,
        3: OPERATOR,
    }

    def __init__(self):
        self.initState = 0
        self.currentState = 0
        self.isFinish = False
        self.isError = False

    def returnToken(self, token):
        return (token, STATE_TYPE[self.currentState])

    def run(self, token):
        for c in token:

            if self.isError:
                return False

            self.nextState(c)

        self.returnToken(token)

    def nextState(self, c):
        if self.currentState is 0:
            print('current state is 0')
        elif self.currentState is 1:
            print('current state is 1')
        elif self.currentState is 2:
            print('current state is 2')
        elif self.currentState is 3:
            print('current state is 3')
