
class Token:
    def __init__(self, type, lex, location):
        self.type = type
        self.lexeme = lex
        self.location = location


class LexFridman:
    def __init__(self, text):
        self.text = text
        self.currentChar = ""
        self.currentIdx = 0
        self.nextChar = ""
        self.nextIdx = 1
        self.errors = []
        self.line = 0
        
    
    def peek(self):
        list = []
    def checkToken(self):
        list = []
    def validateToken(self):
        list = []
    
    
    
f = open("assignment1/lexnegativegrading.src")
text = f.read()
lex = LexFridman(text)
print(lex.text)