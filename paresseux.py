from lexer import LexFridman
from kento import Token, TokenType
from typing import List

class Paresseux:
    def __init__(self, lexer: LexFridman) -> None:
        self.peekIndex = 1
        self.lex = lexer
        self.lex.getTokens() # get all tokens from the lexer
        self.currToken = self.lex.tokens[0]
        self.peekToken = self.lex.tokens[self.peekIndex]

    def matchCurr(self, types):
        return self.currToken.type in types
    
    def matchPeek(self, types):
        return self.peekToken.type in types

    def matchSequence(self, sequence: List[Token]):
        for s in sequence:
            if self.matchCurr({s}):
                self.nextToken()
            else:
                return
    
    def nextToken(self):
        if self.peekIndex < len(self.lex.tokens):
            self.currToken = self.peekToken
            self.skipToken()
            if self.peekIndex < len(self.lex.tokens) - 1:
                self.peekIndex  = self.peekIndex + 1
                self.peekToken = self.lex.tokens[self.peekIndex]
        else:
            self.currToken = Token(TokenType.EOF, "$", -1) # add an end of file token
    
    def skipToken(self):
        if self.matchCurr({TokenType.INVALIDCHAR, TokenType.BLOCKCMT, TokenType.INLINECMT}):
            self.nextToken()
            
    def skipErrors(self):
        pass
    
    # Grammar rules
    # START -> prog 
    def parse(self):
        print("starting parsing sequence")
        self.prog()
        
    # prog -> rept-prog0 
    def prog(self):
        print("PROG")
        self.structOrImplOrFunc()
        #self.structOrImplOrFunc()
        print(self.currToken)

    # structOrImplOrFunc -> structDecl | implDef | funcDef 
    def structOrImplOrFunc(self):
        print("structOrImplOrFunc")
        return self.structDecl() or self.implDef() or self.funcDef()
    
    def structDecl(self):
        pass
    
    def implDef(self):
        pass
    
    # funcDef -> funcHead funcBody 
    def funcDef(self):
        print("funcDef")
        self.funcHead()
        self.funcBody()
    
    def visibility(self):
        pass
    
    def memberDecl(self):
        pass
    
    # funcDecl -> funcHead ; 
    def funcDecl(self):
        print("funcDecl")
        self.funcHead()
        self.nextToken()
        self.checkToken(TokenType.CLOSECUBR)
        return True
    
    # funcHead -> func id ( fParams ) arrow returnType 
    def funcHead(self):
        print("funcHead")
        self.matchSequence([TokenType.FUNC, TokenType.ID, TokenType.OPENPAR])
        self.fParams()
        self.matchSequence([TokenType.CLOSEPAR, TokenType.ARROW])
        self.returnType()
    
    # funcBody -> { rept-funcBody1 } 
    def funcBody(self):
        print("funcBody")
        self.matchCurr({TokenType.OPENCUBR})
        self.nextToken()
        self.rept_funcBody1()
        self.matchCurr({TokenType.CLOSESQBR})
        self.nextToken()
        return True
    
    # rept-funcBody1 -> varDeclOrStat rept-funcBody1 | EPSILON 
    def rept_funcBody1(self):
        print("rept-funcBody1")
        if self.varDeclOrStat():
            self.rept_funcBody1()
        else:
            return True
    
    # varDeclOrStat -> varDecl | statement 
    def varDeclOrStat(self):
        print("varDeclOrStat")
        return self.varDecl() or self.statement()
    
    # varDecl -> let id : type rept-varDecl4 ; 
    def varDecl(self):
        print("varDecl")
        self.matchSequence([TokenType.LET, TokenType.ID, TokenType.COLON])
        self.type()
        self.rept_varDecl4()
        self.matchCurr({TokenType.SEMI})
    
    # rept-varDecl4 -> arraySize rept-varDecl4 | EPSILON 
    def rept_varDecl4(self):
        print("rept_varDecl4")
        if self.arraySize():
            self.rept_varDecl4()
        else:
            return True
        
    # statement -> id statement2 | if ( relExpr ) then statBlock else statBlock ; | while ( relExpr ) statBlock ; | read ( variable ) ; | write ( expr ) ; | return ( expr ) ;
    def statement(self):
        if self.matchCurr({TokenType.ID}):
            self.nextToken()
            self.statement2()
    
    # statement2 -> rept-idnest1 statement3 | ( aParams ) statement4 
    def statement2(self):
        if self.rept_idnest1():
            self.statement3()
        elif self.matchCurr({TokenType.OPENPAR}):
            self.aParams()
    
    # statement3 -> . id statement2 | assignOp expr ; 
    def statement3(self):
        pass
    
    # statement4 -> . id statement2 | ; 
    def statement4(self):
        pass
    
    # rept-idnest1 -> indice rept-idnest1 | EPSILON
    def rept_idnest1(self):
        if self.indice():
            self.rept_idnest1()
        else:
            return True
    
    # statBlock -> { rept-statBlock1 } | statement | EPSILON 
    def statBlock(self):
        pass
    
    # expr -> arithExpr expr2 
    def expr(self):
        pass
    
    # expr2 -> relOp arithExpr | EPSILON 
    def expr2(self):
        pass
    
    # relExpr -> arithExpr relOp arithExpr 
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
        self.matchCurr({TokenType.OPENSQBR})
        self.nextToken()
        self.arithExpr()
        self.matchCurr({TokenType.CLOSESQBR})
        self.nextToken()
    
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
        if not self.matchCurr({TokenType.ID}):
            return True
        else:
            self.matchSequence([TokenType.ID, TokenType.COLON])
        self.type()
        self.rept_fParams3()
        self.rept_fParams4()
    
    def rept_fParams3(self):
        pass
    
    def rept_fParams4(self):
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
        if self.matchCurr({TokenType.EQ}):
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
    