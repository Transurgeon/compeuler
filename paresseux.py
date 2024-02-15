from lexer import LexFridman

class Paresseux:
    def __init__(self, lexer: LexFridman) -> None:
        self.currToken = []
        self.next = []
        self.tokens = lexer.getTokens()
    
    def checkToken(self, type):
        pass
    
    def checkNext(self, type):
        pass
    
    def matchToken(self, type):
        pass
    
    def nextToken(self, type):
        pass
    
    def skipErrors(self):
        pass
    
    # Grammar rules
    def prog(self):
        pass
    
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
    
    def varDecl(self):
        pass
    
    def statement(self):
        pass
    
    def assignStat(self):
        pass
    
    def statBlock(self):
        pass
    
    def expr(self):
        pass
    
    def relExpr(self):
        pass
    
    def arithExpr(self):
        pass
    
    def sign(self):
        pass
    
    def term(self):
        pass
    
    def factor(self):
        pass
    
    def variable(self):
        pass
    
    def functionCall(self):
        pass
    
    def idnest(self):
        pass
    
    def indice(self):
        pass
    
    def arraySize(self):
        pass
    
    def type(self):
        pass
    
    def returnType(self):
        pass
    
    def fParams(self):
        pass
    
    def aParams(self):
        pass
    
    def fParamsTail(self):
        pass
    
    def aParamsTail(self):
        pass
    
    def assignOp(self):
        pass
    
    def relOp(self):
        pass
    
    def addOp(self):
        pass
    
    def nultOp(self):
        pass
    