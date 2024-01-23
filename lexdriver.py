
class Token:
    def __init__(self, type, lex, location: int):
        self.type = type
        self.lexeme = lex
        self.location = location
    
    def __str__(self) -> str:
        return self.lexeme + str(self.location)

class LexFridman:
    def __init__(self, text: str):
        self.text = text
        self.currentChar = ""
        self.currentIdx = 0
        self.nextChar = ""
        self.nextIdx = 1
        self.errors = []
        self.tokens = []
        self.line = 0
        
    
    def peek(self):
        list = []
    def nextToken(self):
        if self.currentChar == ' ':
            return
        
    def validateToken(self):
        list = []
    
    
lexemes = {1 : 'id', 2: 'alphanum', 3: 'integer', 4: 'float', 5: 'fraction', 6: 'letter', 7: 'digit', 8: 'nonzero'}  
f = open("assignment1/lexnegativegrading.src")
text = f.read()
lex = LexFridman(text)
print(lex.text)
tok = Token("hi", "hi", 2)
print(tok)