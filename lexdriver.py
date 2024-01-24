from enum import Enum

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

class Token:
    def __init__(self, type: TokenType, lex: str, location: int):
        self.type = type
        self.lexeme = lex
        self.location = location
    
    def __str__(self) -> str:
        return "["+ self.type.name + ", " + self.lexeme + ", " + str(self.location) + "]"

    # verifies if an identifier is a reserved keyword
    def verifyKeyword(self) -> bool:
        return True
    

class LexFridman:
    def __init__(self, text: str):
        self.text = text
        self.currentChar = ""
        self.currentIdx = 0
        self.errors = []
        self.tokens = []
        self.currentLine = 1
        
    def getNextChar(self):
        if self.currentIdx < len(self.text):
            self.currentIdx += 1
            self.currentChar = self.text[self.currentIdx]

    def peekNextChar(self):
        if self.currentIdx + 1 < len(self.text):
            return self.text[self.currentIdx + 1]
        
    def getStrings(self):
        str = ""
        while self.currentIdx < len(self.text) - 1:
            str += self.currentChar
            self.getNextChar()
            if self.currentChar == ' ':
                self.skipWhiteSpace()
                self.tokens.append(str)
                str = ""
        
    def skipWhiteSpace(self):
        while self.currentChar == ' ' or self.currentChar == '\t':
            self.getNextChar()
    
    def nextToken(self):
        char, line = self.currentChar, self.currentLine
        match char:
            # match operators
            case '\n':
                self.currentLine += 1
            case '=':
                print("in peek", self.peekNextChar())
                if self.peekNextChar() == '=':
                    self.getNextChar()
                    return Token(TokenType.EQ, '==', line)
                else:
                    return Token(TokenType.ASSIGN, char, line)
            case '+':
                return Token(TokenType.PLUS, char, line)
            case '|':
                return Token(TokenType.OR, char, line)
            case '(':
                return Token(TokenType.OPENPAR, char, line)
            case ';':
                return Token(TokenType.SEMI, char, line)
            case '-':
                return Token(TokenType.MINUS, char, line)
            case '&':
                return Token(TokenType.AND, char, line)
            case ')':
                return Token(TokenType.CLOSEPAR, char, line)
            case ',':
                return Token(TokenType.COMMA, char, line)
            case '*':
                return Token(TokenType.MULT, char, line)
            case '!':
                return Token(TokenType.NOT, char, line)
            case '{':
                return Token(TokenType.OPENCUBR, char, line)
            case '}':
                return Token(TokenType.CLOSECUBR, char, line)
            case ':':
                if self.peekNextChar() == ':':
                    return Token(TokenType.COLONCOLON, '::', line)
                else:
                    return Token(TokenType.COLON, char, line)
            case ':':
                return Token(TokenType.COLON, char, line)
        return 4
    
    def getTokens(self):
        for i in range(50):
            self.tokens.append(self.nextToken())
            self.getNextChar()
            self.skipWhiteSpace()
            
        
f = open("assignment1/lexpositivegrading.src")
text = f.read()
lex = LexFridman(text)
lex.getTokens()
for t in lex.tokens:
    print(t)