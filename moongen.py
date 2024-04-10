from siementic import *
import visitor

#####################################
# Code Generation Visitor
class CodeGenerationVisitor(Visitor):
    def __init__(self) -> None:
        self.scope_stack = []
        self.registers = ["r1", "r2", "r3", "r4", "r5", "r6", "r7", "r8", "r9", "r10", "r11", "r12"]
        self.tempVarNum = 0
        self.moonExecCode = ""
        self.moonDataCode = ""
        self.moonCodeIndent = "           "
    
    # Helper functions
    def getClassSize(self):
        pass
    
    # pre-visit functions
    def pre_visit_StructNode(self, node):
        pass
    
    def pre_visit_FunctionNode(self, node):
        pass
    
    def pre_visit_ImplNode(self, node):
        pass
    
    # visitor functions
    @visitor.on('node')
    def visit(self, node):
        pass
    
    @visitor.when(FunctionNode)
    def visit(self, node):
        pass
    
    @visitor.when(VarDeclNode)
    def visit(self, node):
        pass
    
    @visitor.when(IfNode)
    def visit(self, node):
        pass
    
    @visitor.when(ThenNode)
    def visit(self, node):
        pass
        
    @visitor.when(ElseNode)
    def visit(self, node):
        pass
        
    @visitor.when(WhileNode)
    def visit(self, node):
        pass
     
    @visitor.when(ReadNode)
    def visit(self, node):
        pass
    
    @visitor.when(WriteNode)
    def visit(self, node):
        pass
    
    @visitor.when(ReturnNode)
    def visit(self, node):
        pass
        
    @visitor.when(RelExprNode)
    def visit(self, node):
        pass
        
    @visitor.when(AssignNode)
    def visit(self, node):
        pass
        
    @visitor.when(ArgParamNode)
    def visit(self, node):
        pass
    
    @visitor.when(FuncCallNode)
    def visit(self, node):
        pass
    
    @visitor.when(AddOpNode)
    def visit(self, node):
        pass
    
    @visitor.when(MultOpNode)
    def visit(self, node):
        pass
    
    
    
    