from siementic import *
import visitor

#####################################
# Code Generation Visitor
class MoonGenerationVisitor(Visitor):
    def __init__(self) -> None:
        self.scope_stack = ["global"]
        self.registers = ["r12", "r11", "r10", "r9", "r8", "r7", "r6", "r5", "r4", "r3", "r2", "r1"]
        self.tempVarNum = 0
        self.moonExecCode = ""
        self.moonDataCode = ""
        self.moonCodeIndent = "           " # 10 empty space characters for indent

    # pre-visit functions
    def pre_visit_StructNode(self, node):
        self.scope_stack.append(node.name)
    
    def pre_visit_FuncDeclNode(self, node):
        tagName = node.table_entry[0]
        node.moonVarName = tagName
        
        if tagName == "main":
            self.moonExecCode += self.moonCodeIndent + 'entry\n'
            self.moonExecCode += self.moonCodeIndent + 'addi r14,r0,topaddr\n'
        
        returnType = node.table_entry[2]

    def pre_visit_ImplNode(self, node):
        pass
    
    # visitor functions
    @visitor.on('node')
    def visit(self, node):
        pass
    
    @visitor.when(IdNode)
    def visit(self, node):
        node.moonVarName = self.scope_stack[-1] + "_" + node.name
    
    @visitor.when(IntNode)
    def visit(self, node):
        node.moonVarName = node.name
    
    @visitor.when(FloatNode)
    def visit(self, node):
        node.moonVarName = node.name
    
    @visitor.when(StructNode)
    def visit(self, node):
        self.scope_stack.pop()

    @visitor.when(FunctionNode)
    def visit(self, node):
        pass
    
    @visitor.when(VarDeclNode)
    def visit(self, node):
        tagName = self.scope_stack[-1] + "_" + node.table_entry[0]
        node.moonVarName = tagName
        node.children[0].moonVarName = tagName
        self.moonDataCode += self.moonCodeIndent + "% space for variable " + tagName + "\n"
        self.moonDataCode += f"{tagName:<10} res {node.table_entry[3]}\n"
    
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
        node.moonVarName = 't' + str(self.tempVarNum)
        self.tempVarNum += 1
        leftChildRegister, rightChildRegister, localRegister = self.registers[-3:]
        leftOp, operation, rightOp = node.children
        
        moonExecCode = ''
        moonExecCode += self.moonCodeIndent + f"% processing: {node.moonVarName}" + ":= " + leftOp.moonVarName + " + " + rightOp.moonVarName + "\n"
        moonExecCode += self.moonCodeIndent + "lw " + leftChildRegister + "," + leftOp.moonVarName + "(r0)\n"
        moonExecCode += self.moonCodeIndent + "addi " + localRegister + "," + leftChildRegister + "," + rightOp.moonVarName + "\n"
        self.moonDataCode += self.moonCodeIndent + "% space for " + leftOp.moonVarName + " + " + rightOp.moonVarName + "\n"
        self.moonDataCode += f"{node.moonVarName:<10} res {4}\n"
        moonExecCode += self.moonCodeIndent + "sw " + node.moonVarName + "(r0)," + localRegister + "\n"

        self.moonExecCode += moonExecCode
        
    @visitor.when(MultOpNode)
    def visit(self, node):
        pass
    