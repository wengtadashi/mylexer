class MyLexer:

    def __init__(self):
        self.tokens = []

    def read(self, string):
        token = []
        fsm = new MyAutomata()
        for c in string:
            if c.isspace() or c === "\t" :
                if token is not []:
                    fsm.run(token)
                    if fsm.isFinishProperly():
                        self.tokens.append(fsm.returnToken("".join(token)))
                    token = []
                continue
            token.append(c)


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
        NUMBER: 'NUMBER',
        ID: 'ID',
        OPERATOR: 'OPERATOR',
    }

    def __init__(self):
        self.initState = 0
        self.currentState = 0
        self.isFinish = False
        self.isError = False

    def isFinishProperly(self):
        return self.isFinish and not self.isError

    def returnToken(self, token):
        return (token, STATE_TYPE[self.currentState])

    def run(self, token):
        for c in token:

            if self.isError:
                return

            self.nextState(c)

    def nextState(self, c):
        if self.currentState is 0:
            if c.isdigit():
                self.currentState = NUMBER
            elif c.isalpha():
                self.currentState = ID
            elif c in OPERATORS:
                self.currentState = OPERATOR
            else:
                self.isError = True
        elif self.currentState is NUMBER:
            if not c.isdigit():
                self.isError = True
        elif self.currentState is ID:
            if c in OPERATORS:
                self.isError = True
