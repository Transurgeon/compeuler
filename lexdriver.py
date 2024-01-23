from enum import Enum

class Token:
    def __init__(self, type: str, lex, location: int):
        self.type = type
        self.lexeme = lex
        self.location = location
    
    def __str__(self) -> str:
        return "["+ self.type + ", " + self.lexeme + ", " + str(self.location) + "]"

class TokenType(Enum):
    # Reserved Keywords
    IF = 1
    THEN = 2
    ELSE = 3
    INTEGER = 4
    FLOAT = 5
    VOID = 6
    PUBLIC = 7
    PRIVATE = 8
    FUNC = 9
    VAR = 10
    STRUCT = 11
    WHILE = 12
    READ = 13
    WRITE = 14
    RETURN = 15
    SELF = 16
    INHERITS = 17
    LET = 18
    IMPL = 19
    # Operators
    EQ = 101
    PLUS = 102
    OR = 103
    OPENPAR = 104
    SEMI = 105
    NOTEQ = 106
    MINUS = 107
    AND = 108
    CLOSEPAR = 109
    COMMA = 110
    LT = 111
    MULT = 112
    NOT = 113
    OPENCUBR = 114
    DOT = 115
    GT = 116
    DIV = 117
    CLOSECUBR = 118
    COLON = 119
    LEQ = 120
    ASSIGN = 121
    OPENSQBR = 122
    COLONCOLON = 123
    GEQ = 124
    CLOSESQBR = 125
    ARROW = 126
    # lexeme
    ID = 201
    ALPHANUM = 202
    INTNUM = 203
    FLOATNUM = 204
    INLINECMT = 205
    BLOCKCMT = 206

class LexFridman:
    def __init__(self, text: str):
        self.text = text
        self.currentChar = ""
        self.currentIdx = 0
        self.errors = []
        self.tokens = []
        self.line = 0
        self.getStrings()
        
    def getNextChar(self):
        if self.currentIdx < len(self.text):
            self.currentIdx += 1
            self.currentChar = self.text[self.currentIdx]

    def getStrings(self):
        while self.currentIdx < len(self.text) - 1:
            self.getNextChar()

    def updateLineCount(self):
        self.line += 1
        
    def skipWhiteSpace(self):
        self.getNextChar()
    
    def nextToken(self):
        if self.currentChar == '\n':
            self.updateLineCount
            return
    
    def validateToken(self):
        list = []
    
f = open("assignment1/lexnegativegrading.src")
text = f.read()
lex = LexFridman(text)
# print(lex.text)
tok = Token("hi", "hi", 2)
print(tok)