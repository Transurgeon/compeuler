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
    INVALIDCHAR = 207

class Token:
    def __init__(self, type: TokenType, lex: str, line: int):
        self.type = type
        self.lexeme = lex
        self.line = line
    
    def __str__(self) -> str:
        return "["+ self.type.name + ", " + self.lexeme + ", " + str(self.line) + "]"

    # verifies if an identifier is a reserved keyword
    def verifyKeyword(self) -> None:
        try:
            if TokenType[self.lexeme.upper()].value < 100:
                self.type = TokenType[self.lexeme.upper()]
        except:
            pass
            
