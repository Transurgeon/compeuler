from lexer import LexFridman
from kento import Token, TokenType
class Paresseux:
    def __init__(self, lexer: LexFridman) -> None:
        self.peekIndex = 1
        self.lex = lexer
        self.lex.getTokens()
        self.currToken = self.lex.tokens[0]
        self.peekToken = self.lex.tokens[self.peekIndex]
        
    def checkToken(self, type):
        return type == self.currToken.type
    
    def checkNext(self, type):
        return type == self.peekToken.type
    
    def nextToken(self):
        if self.peekIndex < len(self.lex.tokens) - 1:
            self.currToken = self.peekToken
            self.peekIndex  = self.peekIndex + 1
            self.peekToken = self.lex.tokens[self.peekIndex]
    
    def match(self):
        pass
    
    def skipErrors(self):
        pass
    
    # Grammar rules
    # START -> prog 
    def parse(self):
        print("starting parse")
        self.prog()
        
    # prog -> rept-prog0 
    def prog(self):
        print("PROG")
        while self.currToken.type != TokenType.EOF:
            self.structOrImplOrFunc()

    def structOrImplOrFunc(self):
        pass
    
    def structDecl(self):
        pass
    
    def implDef(self):
        pass
    
    def funcDef(self):
        pass
    
    def visibility(self):
        pass
    
    def memberDecl(self):
        pass
    
    def funcDecl(self):
        pass
    
    def funcHead(self):
        pass
    
    def funcBody(self):
        pass
    
    def varDeclOrStat(self):
        pass
    
    # varDecl -> let id : type rept-varDecl4 ; 
    def varDecl(self):
        pass
    
    def statement(self):
        pass
    
    # might not be needed in reformed grammar
    def assignStat(self):
        pass
    
    # statBlock -> { rept-statBlock1 } | statement | EPSILON 
    def statBlock(self):
        pass
    
    def expr(self):
        pass
    
    def relExpr(self):
        pass
    
    # arithExpr -> term rightrec-arithExpr 
    def arithExpr(self):
        pass
    
    # sign -> + | - 
    def sign(self):
        if self.currToken.type in {TokenType.PLUS, TokenType.MINUS}:
            self.nextToken()
            return True
        return False
    
    # term -> factor rightrec-term 
    def term(self):
        pass
    
    def factor(self):
        pass
    
    def variable(self):
        pass
    
    # functionCall -> rept-functionCall0 id ( aParams ) 
    def functionCall(self):
        pass
    
    # idnest -> . id idnest2 
    def idnest(self):
        pass
    
    # idnest2 -> ( aParams ) | rept-idnest1 
    def idnest2(self):
        pass
    
    # indice -> [ arithExpr ] 
    def indice(self):
        pass
    
    # arraySize -> [ arraySize2
    def arraySize(self):
        if self.currToken.type not in {TokenType.OPENSQBR}:
            return False
        self.nextToken()
        return self.arraySize2()
    
    # arraySize2 -> intLit ] | ] 
    def arraySize2(self):
        if self.currToken.type in {TokenType.INTEGER}:
            self.nextToken()
        if self.currToken.type in {TokenType.CLOSESQBR}:
            self.nextToken()
            return True
        return False
    
    # type -> integer | float | id 
    def type(self):
        if self.currToken.type in {TokenType.INTEGER, TokenType.FLOAT, TokenType.ID}:
            self.nextToken()
            return True
    
    # returnType -> type | void 
    def returnType(self):
        if self.type() or self.currToken.type in {TokenType.VOID}:
            self.nextToken()
            return True
    
    # fParams -> id : type rept-fParams3 rept-fParams4 | EPSILON 
    def fParams(self):
        pass
    
    # aParams -> expr rept-aParams1 | EPSILON 
    def aParams(self):
        pass
    
    # fParamsTail -> , id : type rept-fParamsTail4 
    def fParamsTail(self):
        pass
    
    # aParamsTail -> , expr 
    def aParamsTail(self):
        if self.currToken.type not in {TokenType.COMMA}:
            return False
        self.nextToken()
        return self.expr()
    
    # assignOp -> = 
    def assignOp(self):
        if self.currToken.type in {TokenType.EQ}:
            self.nextToken()
            return True
    
    # relOp -> eq | neq | lt | gt | leq | geq 
    def relOp(self):
        relationOperators = {
            TokenType.EQ,
            TokenType.NOTEQ,
            TokenType.LT,
            TokenType.GT,
            TokenType.LEQ,
            TokenType.GEQ
        }
        if self.currToken.type in relationOperators:
            self.nextToken()
            return True
    
    # addOp -> + | - | or 
    def addOp(self):
        if self.currToken.type in {TokenType.PLUS, TokenType.MINUS, TokenType.OR}:
            self.nextToken()
            return True
        return False
    
    # multOp -> * | / | and 
    def multOp(self):
        if self.currToken.type in {TokenType.MULT, TokenType.DIV, TokenType.AND}:
            self.nextToken()
            return True
        return False
    