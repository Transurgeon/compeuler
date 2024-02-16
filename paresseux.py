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
            if self.peekIndex < len(self.lex.tokens) - 1:
                self.peekIndex  = self.peekIndex + 1
                self.peekToken = self.lex.tokens[self.peekIndex]
        else:
            self.currToken = Token(TokenType.EOF, "$", -1) # add an end of file token
            
    def skipErrors(self):
        pass
    
    # Grammar rules
    # START -> prog 
    def parse(self):
        print("Starting Parsing Sequence")
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
    
    # structDecl -> struct id opt-structDecl2 { rept-structDecl4 } ; 
    def structDecl(self):
        pass
    
    # implDef -> impl id { rept-implDef3 }
    def implDef(self):
        pass
    
    # funcDef -> funcHead funcBody 
    def funcDef(self):
        print("funcDef")
        self.funcHead()
        self.funcBody()
        return True
    
    # visibility -> public | private 
    def visibility(self):
        return self.matchCurr({TokenType.PUBLIC, TokenType.PRIVATE})
        
    # memberDecl -> funcDecl | varDecl 
    def memberDecl(self):
        return self.funcDecl() or self.varDecl()
    
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
        if not self.matchSequence([TokenType.LET, TokenType.ID, TokenType.COLON]):
            return False
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
        
    # statement -> id statement2 | if ( relExpr ) then statBlock else statBlock ; | while ( relExpr ) statBlock ;
    # | read ( variable ) ; | write ( expr ) ; | return ( expr ) ;
    def statement(self):
        print("statement")
        if self.matchCurr({TokenType.ID}):
            self.nextToken()
            self.statement2()
            return True
    
    # statement2 -> ( aParams ) statement4 | rept-idnest1 statement3 
    def statement2(self):
        print("statement2")
        if self.matchCurr({TokenType.OPENPAR}):
            self.nextToken()
            self.aParams()
            self.matchCurr({TokenType.CLOSEPAR})
            self.nextToken()
            self.statement4()
        else:
            self.rept_idnest1()
            self.statement3()
    
    # statement3 -> . id statement2 | assignOp expr ; 
    def statement3(self):
        print("statement3")
        if self.matchCurr({TokenType.DOT}):
            self.nextToken()
            self.matchCurr({TokenType.ID})
            self.nextToken()
            self.statement2()
        elif self.assignOp():
            self.nextToken()
            self.expr()
            self.matchCurr({TokenType.SEMI})
            self.nextToken()
        return True
    
    # statement4 -> . id statement2 | ; 
    def statement4(self):
        print("statement4")
        if self.matchCurr({TokenType.DOT}):
            self.nextToken()
            self.matchCurr({TokenType.ID})
            self.statement2()
        elif self.matchCurr({TokenType.SEMI}):
            self.nextToken()
        return True
    
    # rept-idnest1 -> indice rept-idnest1 | EPSILON
    def rept_idnest1(self):
        print("rept-idnest1")
        if self.indice():
            self.rept_idnest1()
        else:
            return True
    
    # statBlock -> { rept-statBlock1 } | statement | EPSILON 
    def statBlock(self):
        pass
    
    # expr -> arithExpr expr2 
    def expr(self):
        print("expr")
        self.arithExpr()
        self.expr2()
        return True
    
    # expr2 -> relOp arithExpr | EPSILON 
    def expr2(self):
        print("expr2")
        if self.relOp():
            self.arithExpr()
        return True
    
    # relExpr -> arithExpr relOp arithExpr 
    def relExpr(self):
        print("relExpr")
        self.arithExpr()
        self.relOp()
        self.arithExpr()
    
    # arithExpr -> term rightrec-arithExpr 
    def arithExpr(self):
        self.term()
        self.rightrec_arithExpr()
        return True
    
    # rightrec-arithExpr -> EPSILON | addOp term rightrec-arithExpr 
    def rightrec_arithExpr(self):
        if self.addOp():
            self.term()
            self.rightrec_arithExpr()
        else:
            return True
    
    # sign -> + | - 
    def sign(self):
        if self.currToken.type in {TokenType.PLUS, TokenType.MINUS}:
            self.nextToken()
            return True
        return False
    
    # term -> factor rightrec-term 
    def term(self):
        self.factor()
        self.rightrec_term()
    
    # rightrec-term -> multOp factor rightrec-term | EPSILON
    def rightrec_term(self):
        if self.multOp():
            self.factor()
            self.rightrec_term()
        else:
            return True
    
    # factor -> id factor2 reptVariableOrFunc | intLit | floatLit | ( arithExpr ) | not factor | sign factor 
    def factor(self):
        if self.matchCurr({TokenType.ID}):
            self.nextToken()
            self.factor2()
            self.reptVariableOrFunc()
    
    # factor2 -> ( aParams ) | rept-idnest1 
    def factor2(self):
        if self.matchCurr({TokenType.OPENPAR}):
            self.nextToken()
            self.aParams()
            self.matchCurr({TokenType.CLOSEPAR})
            self.nextToken()
        else:
            self.rept_idnest1()
    
    def variable(self):
        pass
    
    # reptVariableOrFunc -> idnest reptVariableOrFunc | EPSILON 
    def reptVariableOrFunc(self):
        if self.idnest():
            self.reptVariableOrFunc()
        return True
    
    # functionCall -> rept-functionCall0 id ( aParams ) 
    def functionCall(self):
        self.rept_functionCall0()
        self.matchCurr({TokenType.ID})
        self.nextToken()
        self.matchCurr({TokenType.OPENPAR})
        self.nextToken()
        self.aParams()
        self.matchCurr({TokenType.CLOSEPAR})
        self.nextToken()
        return True
    
    # rept-functionCall0 -> idnest rept-functionCall0 | EPSILON 
    def rept_functionCall0(self):
        if self.idnest():
            self.rept_functionCall0()
        return True
    
    # idnest -> . id idnest2 
    def idnest(self):
        if not self.matchCurr({TokenType.DOT}):
            return False
        self.nextToken()
        self.matchCurr({TokenType.ID})
        self.nextToken()
        self.idnest2()
    
    # idnest2 -> ( aParams ) | rept-idnest1 
    def idnest2(self):
        if self.matchCurr({TokenType.OPENPAR}):
            self.nextToken()
            self.aParams()
            self.matchCurr({TokenType.CLOSEPAR})
            self.nextToken()
        else:
            self.rept_idnest1()
    
    # indice -> [ arithExpr ] 
    def indice(self):
        if not self.matchCurr({TokenType.OPENSQBR}):
            return False
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
        self.matchSequence([TokenType.ID, TokenType.COLON])
        self.type()
        self.rept_fParams3()
        self.rept_fParams4()
    
    # rept-fParams3 -> arraySize rept-fParams3 | EPSILON 
    def rept_fParams3(self):
        if self.arraySize():
            self.rept_fParams3()
        else:
            return True
    
    # rept-fParams4 -> fParamsTail rept-fParams4 | EPSILON 
    def rept_fParams4(self):
        if self.fParamsTail():
            self.rept_fParams4()
        else:
            return True
    
    # aParams -> expr rept-aParams1 | EPSILON 
    def aParams(self):
        if self.expr():
            self.rept_aParams1()
        else:
            return True
    
    # rept-aParams1 -> aParamsTail rept-aParams1 | EPSILON 
    def rept_aParams1(self):
        if self.aParamsTail():
            self.rept_aParams1()
        else:
            return True
        
    # fParamsTail -> , id : type rept-fParamsTail4 
    def fParamsTail(self):
        self.matchSequence([TokenType.COMMA, TokenType.ID, TokenType.COLON])
        self.type()
    
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
    