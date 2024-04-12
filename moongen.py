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
    
    @visitor.when(VariableNode)
    def visit(self, node):
        node.moonVarName = node.children[0].moonVarName
    
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
        node.moonVarName = node.children[0].moonVarName
        localRegister = self.registers.pop()
        
        self.moonExecCode += self.moonCodeIndent + "% processing: output(" + node.moonVarName + ")\n"
        self.moonExecCode += self.moonCodeIndent + "lw " + localRegister + "," + node.moonVarName + "(r0)\n"
        self.moonExecCode += self.moonCodeIndent + "% put value on stack\n"
        self.moonExecCode += self.moonCodeIndent + "sw -8(r14)," + localRegister
        self.moonExecCode += self.moonCodeIndent + "% link buffer to stack\n"
        self.moonExecCode += self.moonCodeIndent + "addi " + localRegister + ",r0, buf\n"
        self.moonExecCode += self.moonCodeIndent + "sw -12(r14)," + localRegister + "\n"
        self.moonExecCode += self.moonCodeIndent + "% convert int to string for output\n"
        self.moonExecCode += self.moonCodeIndent + "jl r15, intstr\n"
        self.moonExecCode += self.moonCodeIndent + "sw -8(r14), r13\n"
        self.moonExecCode += self.moonCodeIndent + "% output to console\n"
        self.moonExecCode += self.moonCodeIndent + "jl r15, putstr\n"

        self.registers.append(localRegister)
    
    @visitor.when(ReturnNode)
    def visit(self, node):
        pass
    
    @visitor.when(ArithExprNode)
    def visit(self, node):
        node.moonVarName = node.children[0].moonVarName
    
    @visitor.when(RelExprNode)
    def visit(self, node):
        pass
        
    @visitor.when(AssignNode)
    def visit(self, node):
        localRegister = self.registers.pop()
        left, right = node.children
        self.moonExecCode += self.moonCodeIndent + "% processing: "  + left.moonVarName + " := " + right.moonVarName + "\n";
        self.moonExecCode += self.moonCodeIndent + "lw " + localRegister + "," + left.moonVarName + "(r0)\n";
        self.moonExecCode += self.moonCodeIndent + "sw " + right.moonVarName + "(r0)," + localRegister + "\n";
        self.registers.append(localRegister)
        
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
        # perform different operation depending on operand
        match operation.name:
            case "+":
                oper = "addi "
            case "-":
                oper = "subi "
            case "|":
                oper = "ori "
            case _:
                oper = ""
        # generate moon code blocks for addop node
        moonExecCode = self.moonCodeIndent + f"% processing: {node.moonVarName}" + ":= " + leftOp.moonVarName + operation.name + rightOp.moonVarName + "\n"
        moonExecCode += self.moonCodeIndent + "lw " + leftChildRegister + "," + leftOp.moonVarName + "(r0)\n"
        moonExecCode += self.moonCodeIndent + oper + localRegister + "," + leftChildRegister + "," + rightOp.moonVarName + "\n"
        moonExecCode += self.moonCodeIndent + "sw " + node.moonVarName + "(r0)," + localRegister + "\n"
        
        self.moonDataCode += self.moonCodeIndent + "% space for " + leftOp.moonVarName + " + " + rightOp.moonVarName + "\n"
        self.moonDataCode += f"{node.moonVarName:<10} res {node.size}\n"
        self.moonExecCode += moonExecCode
        
    @visitor.when(MultOpNode)
    def visit(self, node):
        node.moonVarName = 't' + str(self.tempVarNum)
        self.tempVarNum += 1
        leftChildRegister, rightChildRegister, localRegister = self.registers[-3:]
        leftOp, operation, rightOp = node.children
        # perform different operation depending on operand
        match operation.name:
            case "*":
                oper = "muli "
            case "/":
                oper = "divi "
            case "&":
                oper = "andi "
            case _:
                oper = ""
        # generate moon code blocks for multop node
        moonExecCode = self.moonCodeIndent + f"% processing: {node.moonVarName}" + ":= " + leftOp.moonVarName + operation.name + rightOp.moonVarName + "\n"
        moonExecCode += self.moonCodeIndent + "lw " + leftChildRegister + "," + leftOp.moonVarName + "(r0)\n"
        moonExecCode += self.moonCodeIndent + oper + localRegister + "," + leftChildRegister + "," + rightOp.moonVarName + "\n"
        moonExecCode += self.moonCodeIndent + "sw " + node.moonVarName + "(r0)," + localRegister + "\n"
        
        self.moonDataCode += self.moonCodeIndent + "% space for " + leftOp.moonVarName + operation.name + rightOp.moonVarName + "\n"
        self.moonDataCode += f"{node.moonVarName:<10} res {node.size}\n"
        self.moonExecCode += moonExecCode
    