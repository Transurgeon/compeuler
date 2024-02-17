from lexer import LexFridman
from kento import Token, TokenType
from first_follow import first, follow
from typing import List, Set

class Paresseux:
    def __init__(self, lexer: LexFridman) -> None:
        self.lex = lexer
        self.lex.getTokens() # get all tokens from the lexer
        self.currToken = self.lex.tokens[0]
        self.peekIndex = 1
        self.peekToken = self.lex.tokens[self.peekIndex]
        self.derivation = "Starting Parsing Sequence \n"
        self.lastDeriv = ""

    def matchCurr(self, types):
        return self.currToken.type in types
    
    def matchPeek(self, types):
        return self.peekToken.type in types

    def matchSequence(self, sequence: List[Token]):
        for s in sequence:
            if not self.matchCurr({s}):
                return False
            self.nextToken()
    
    def nextToken(self):
        if self.peekIndex < len(self.lex.tokens):
            self.currToken = self.peekToken
            self.peekIndex  = self.peekIndex + 1
            if self.peekIndex < len(self.lex.tokens) - 1:
                self.peekToken = self.lex.tokens[self.peekIndex]
        else:
            self.currToken = Token(TokenType.EOF, "$", -1) # add an end of file token
            
    def skipErrors(self, name: str):
        first_set = first[name]
        follow_set = follow[name]
        
    # method to update the derivation during top down parsing
    def updateDerivation(self, prev, new):
        self.lastDeriv = self.lastDeriv.replace(prev, new, 1)
        self.derivation += self.lastDeriv + "\n"
    
    #####################################
    # GRAMMAR RULES 
    # START -> prog 
    def parse(self):
        self.updateDerivation("", "prog")
        self.prog()
        print("Parsing completed")
        
    # prog -> rept-prog0 
    def prog(self):
        self.updateDerivation("prog", "rept-prog0")
        self.rept_prog0()
        print(self.derivation)

    # rept-prog0 -> structOrImplOrFunc rept-prog0 | EPSILON 
    def rept_prog0(self):
        if self.matchCurr({TokenType.BLOCKCMT, TokenType.INVALIDCHAR, TokenType.INLINECMT}):
            self.nextToken()
        if self.matchCurr(first["REPTPROG0"]):
            self.updateDerivation("rept-prog0", "structOrImplOrFunc rept-prog0")
            self.structOrImplOrFunc()
            self.rept_prog0()
        else:
            self.updateDerivation("rept-prog0", "")
            return True
        
    # structOrImplOrFunc -> structDecl | implDef | funcDef 
    def structOrImplOrFunc(self):
        if self.matchCurr({TokenType.STRUCT}):
            self.updateDerivation("structOrImplOrFunc", "structDecl")
            self.structDecl()
        elif self.matchCurr({TokenType.IMPL}):
            self.updateDerivation("structOrImplOrFunc", "implDef")
            self.implDef()
        elif self.matchCurr({TokenType.FUNC}):
            self.updateDerivation("structOrImplOrFunc", "funcDef")
            self.funcDef()
    
    # structDecl -> struct id opt-structDecl2 { rept-structDecl4 } ; 
    def structDecl(self):
        pass
    
    # implDef -> impl id { rept-implDef3 }
    def implDef(self):
        pass
    
    # funcDef -> funcHead funcBody 
    def funcDef(self):
        self.updateDerivation("funcDef", "funcHead funcBody")
        self.funcHead()
        self.funcBody()
    
    # visibility -> public | private 
    def visibility(self):
        if self.matchCurr({TokenType.PUBLIC}):
            self.updateDerivation("visibility", "public")
        elif self.matchCurr({TokenType.PRIVATE}):
            self.updateDerivation("visibility", "private")
        
    # memberDecl -> funcDecl | varDecl 
    def memberDecl(self):
        if self.matchCurr(first["FUNCDECL"]):
            self.updateDerivation("memberDecl", "funcDecl")
            self.memberDecl()
        elif self.matchCurr(first["VARDECL"]):
            self.updateDerivation("memberDecl", "varDecl")
            self.varDecl()
    
    # funcDecl -> funcHead ; 
    def funcDecl(self):
        self.derivation("funcDecl", "funcHead ;")
        self.funcHead()
        self.matchCurr({TokenType.SEMI})
        self.nextToken()
    
    # funcHead -> func id ( fParams ) arrow returnType 
    def funcHead(self):
        self.updateDerivation("funcHead", "func id ( fParams ) arrow returnType")
        self.matchSequence([TokenType.FUNC, TokenType.ID, TokenType.OPENPAR])
        self.fParams()
        self.matchSequence([TokenType.CLOSEPAR, TokenType.ARROW])
        self.returnType()
    
    # funcBody -> { rept-funcBody1 } 
    def funcBody(self):
        self.updateDerivation("funcBody", "{ rept-funcBody1 }")
        self.matchCurr({TokenType.OPENCUBR})
        self.nextToken()
        self.rept_funcBody1()
        self.matchCurr({TokenType.CLOSESQBR})
        self.nextToken()
    
    # rept-funcBody1 -> varDeclOrStat rept-funcBody1 | EPSILON 
    def rept_funcBody1(self):
        if self.matchCurr(first["VARDECLORSTAT"]):
            self.updateDerivation("rept-funcBody1", "varDeclOrStat rept-funcBody1")
            self.varDeclOrStat()
            self.rept_funcBody1()
        else:
            self.updateDerivation("rept-funcBody1", "")
            return True
    
    # varDeclOrStat -> varDecl | statement 
    def varDeclOrStat(self):
        if self.matchCurr(first["VARDECL"]):
            self.updateDerivation("varDeclOrStat", "varDecl")
            self.varDecl()
        elif self.matchCurr(first["STATEMENT"]):
            self.updateDerivation("varDeclOrStat", "statement")
            self.statement()
    
    # varDecl -> let id : type rept-varDecl4 ; 
    def varDecl(self):
        if not self.matchSequence([TokenType.LET, TokenType.ID, TokenType.COLON]):
            return False
        self.type()
        self.rept_varDecl4()
        self.matchCurr({TokenType.SEMI})
    
    # rept-varDecl4 -> arraySize rept-varDecl4 | EPSILON 
    def rept_varDecl4(self):
        if self.arraySize():
            self.rept_varDecl4()
        else:
            return True
        
    # statement -> id statement2 | if ( relExpr ) then statBlock else statBlock ; | while ( relExpr ) statBlock ;
    # | read ( variable ) ; | write ( expr ) ; | return ( expr ) ;
    def statement(self):
        if self.matchCurr({TokenType.ID}):
            self.nextToken()
            self.statement2()
        elif self.matchCurr({TokenType.IF}):
            self.nextToken()
            self.par_relExpr()
            self.matchCurr({TokenType.THEN})
            self.nextToken()
            self.statBlock()
            self.matchCurr({TokenType.ELSE})
            self.nextToken()
            self.statBlock()
            self.matchCurr({TokenType.SEMI})
            self.nextToken()
        elif self.matchCurr({TokenType.WHILE}):
            self.nextToken()
            self.par_relExpr()
            self.statBlock()
            self.matchCurr({TokenType.SEMI})
            self.nextToken()
        elif self.matchCurr({TokenType.READ}):
            self.nextToken()
            self.matchCurr({TokenType.OPENPAR})
            self.nextToken()
            self.variable()
            self.matchCurr({TokenType.CLOSEPAR})
            self.nextToken()
            self.matchCurr({TokenType.SEMI})
            self.nextToken()
        elif self.matchCurr({TokenType.WRITE}):
            self.nextToken()
            self.par_relExpr()
            self.matchCurr({TokenType.SEMI})
            self.nextToken()
        elif self.matchCurr({TokenType.RETURN}):
            self.nextToken()
            self.par_relExpr()
            self.matchCurr({TokenType.SEMI})
            self.nextToken()
        else:
            return False
        return True
    
    # helper function to match for ( relExpr )
    def par_relExpr(self):
        self.matchCurr({TokenType.OPENPAR})
        self.nextToken()
        self.relExpr()
        self.matchCurr({TokenType.CLOSEPAR})
        self.nextToken()
        
    # statement2 -> ( aParams ) statement4 | rept-idnest1 statement3 
    def statement2(self):
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
        if self.matchCurr({TokenType.DOT}):
            self.nextToken()
            self.matchCurr({TokenType.ID})
            self.statement2()
        elif self.matchCurr({TokenType.SEMI}):
            self.nextToken()
        return True
    
    # rept-idnest1 -> indice rept-idnest1 | EPSILON
    def rept_idnest1(self):
        if self.indice():
            self.rept_idnest1()
        else:
            return True
    
    # statBlock -> { rept-statBlock1 } | statement | EPSILON 
    def statBlock(self):
        if self.matchCurr({TokenType.OPENCUBR}):
            self.nextToken()
            self.rept_statBlock1()
            self.matchCurr({TokenType.CLOSECUBR})
            self.nextToken()
        elif self.statement():
            return
        else:
            return
    
    # rept-statBlock1 -> statement rept-statBlock1 | EPSILON 
    def rept_statBlock1(self):
        if self.statement():
            self.rept_statBlock1()
        else:
            return True
    
    # expr -> arithExpr expr2 
    def expr(self):
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
        elif self.matchCurr({TokenType.INTNUM}):
            self.nextToken()
        elif self.matchCurr({TokenType.FLOATNUM}):
            self.nextToken()
        elif self.matchCurr({TokenType.OPENPAR}):
            self.nextToken()
            self.arithExpr()
            self.matchCurr({TokenType.CLOSEPAR})
            self.nextToken()
        elif self.matchCurr({TokenType.NOT}):
            self.nextToken()
            self.factor()
        elif self.sign():
            self.factor()
    
    # factor2 -> ( aParams ) | rept-idnest1 
    def factor2(self):
        if self.matchCurr({TokenType.OPENPAR}):
            self.nextToken()
            self.aParams()
            self.matchCurr({TokenType.CLOSEPAR})
            self.nextToken()
        else:
            self.rept_idnest1()
    
    # variable -> id variable2 
    def variable(self):
        self.matchCurr({TokenType.ID})
        self.variable2()
        return True
        
    # variable2 -> ( aParams ) varIdnest | rept-idnest1 reptvariable
    def variable2(self):
        if self.matchCurr({TokenType.OPENPAR}):
            self.nextToken()
            self.aParams()
            self.matchCurr({TokenType.CLOSEPAR})
            self.nextToken()
            self.varIdnest()
        else:
            self.rept_idnest1()
            self.reptvariable()
    
    # reptvariable -> varIdnest reptvariable | EPSILON 
    def reptvariable(self):
        if self.varIdnest():
            self.reptvariable()
        else:
            return True
    
    # varIdnest -> . id varIdnest2 
    def varIdnest(self):
        if not self.matchSequence([TokenType.DOT, TokenType.ID]):
            return False
        self.varIdnest2()
        return True
    
    # varIdnest2 -> ( aParams ) varIdnest | rept-idnest1 
    def varIdnest2(self):
        if self.matchCurr({TokenType.OPENPAR}):
            self.nextToken()
            self.aParams()
            self.matchCurr({TokenType.CLOSEPAR})
            self.nextToken()
            self.varIdnest()
        else:
            self.rept_idnest1()
            
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
        if self.matchCurr(first["TYPE"]):
            self.updateDerivation("returnType", "type")
        elif self.matchCurr({TokenType.VOID}):
            self.updateDerivation("returnType", "void")
            self.nextToken()
    
    # fParams -> id : type rept-fParams3 rept-fParams4 | EPSILON 
    def fParams(self):
        if not self.matchCurr({TokenType.ID}):
            self.updateDerivation("fParams", "")
            return True
        else:
            self.updateDerivation("fParams", "id : type rept-fParams3 rept-fParams4")
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
    