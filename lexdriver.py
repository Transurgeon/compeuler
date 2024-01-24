from kento import Token, TokenType

class LexFridman:
    def __init__(self, text: str):
        self.text = text
        self.currentChar = ""
        self.currentIdx = -1
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
            case '<':
                if self.peekNextChar() == '>':
                    self.getNextChar()
                    return Token(TokenType.NOTEQ, '<>', line)
                elif self.peekNextChar() == '=':
                    self.getNextChar()
                    return Token(TokenType.LEQ, '<=', line)
                else:
                    return Token(TokenType.LT, char, line)
            case '>':
                if self.peekNextChar() == '=':
                    self.getNextChar()
                    return Token(TokenType.GEQ, '>=', line)
                else:
                    return Token(TokenType.GT, char, line)
            case '-':
                if self.peekNextChar() == '>':
                    self.getNextChar()
                    return Token(TokenType.ARROW, '->', line)
                else:
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
            case '.':
                return Token(TokenType.DOT, char, line)
            # match comments and division operator
            case '/':
                if self.peekNextChar() == '/':
                    startIdx = self.currentIdx
                    while self.currentChar != '\n':
                        self.getNextChar()
                    endIdx = self.currentIdx
                    self.currentLine += 1
                    self.getNextChar()
                    return Token(TokenType.INLINECMT, self.text[startIdx:endIdx], line)
                elif self.peekNextChar() == '*':
                    self.getNextChar()
                    print("block comment")
                else:
                    return Token(TokenType.DIV, char, line)
            # match remainder of operators
            case ':':
                if self.peekNextChar() == ':':
                    self.getNextChar()
                    return Token(TokenType.COLONCOLON, '::', line)
                else:
                    return Token(TokenType.COLON, char, line)
            case '[':
                return Token(TokenType.OPENSQBR, char, line)
            case ']':
                return Token(TokenType.CLOSESQBR, char, line)
            # match lexemes for id, float and integer
            case char if char.isalpha():
                startIdx = self.currentIdx
                while self.peekNextChar().isalnum() or self.peekNextChar() == '_':
                    self.getNextChar()
                endIdx = self.currentIdx
                tok = Token(TokenType.ID, self.text[startIdx:endIdx+1], line)
                tok.verifyKeyword()
                return tok
        return 4
    
    def getTokens(self):
        while self.currentIdx < len(self.text) - 1:
            self.tokens.append(self.nextToken())
            self.getNextChar()
            self.skipWhiteSpace()
                
        
f = open("assignment1/lexpositivegrading.src")
text = f.read()
lex = LexFridman(text)
lex.getTokens()
for t in lex.tokens:
    if t != 4:
        print(t)