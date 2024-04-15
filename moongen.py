from siementic import *
import visitor

#####################################
# Code Generation Visitor
class MoonGenerationVisitor(Visitor):
    def __init__(self) -> None:
        self.scope_stack = ["global"]
        self.scope_data = []
        self.registers = ["r12", "r11", "r10", "r9", "r8", "r7", "r6", "r5", "r4", "r3", "r2", "r1"]
        self.tempVarNum = 0
        self.moonExecCode = ""
        self.moonDataCode = ""
        self.moonCodeIndent = "           " # 10 empty space characters for indent

    # pre-visit functions
    def pre_visit_ProgramNode(self, node):
        self.scope_data = node.symbol_data
        self.moonExecCode += self.moonCodeIndent + "entry\n"
        self.moonExecCode += self.moonCodeIndent + "addi r14,r0,topaddr\n"
        
    def pre_visit_StructNode(self, node):
        self.scope_stack.append(node.name)
    
    def pre_visit_FuncDeclNode(self, node):
        node.moonVarName = node.table_entry[0]
        
        self.moonExecCode += self.moonCodeIndent + "% processing function definition: "  + node.moonVarName + "\n"
        self.moonExecCode += f"{node.moonVarName:<10}"
        self.moonDataCode += f"{node.moonVarName + "link":<11} res 4\n"
        self.moonExecCode += self.moonCodeIndent + "sw " + node.name + "link(r0),r15\n"
        self.moonDataCode += f"{node.moonVarName + "return":<11} res 4\n"

    def pre_visit_FunctionNode(self, node):
        self.scope_data.append(node.table_entry)
    
    # visitor functions
    @visitor.on('node')
    def visit(self, node):
        pass
    
    @visitor.when(ProgramNode)
    def visit(self, node):
        self.moonExecCode += self.moonCodeIndent + "hlt"
        self.moonDataCode += self.moonCodeIndent + "% buffer space used for console output\n"
        self.moonDataCode += "buf        res 20\n"
        
    @visitor.when(IdNode)
    def visit(self, node):
        node.moonVarName = node.name
    
    @visitor.when(IntNode)
    def visit(self, node):
        node.moonVarName = 't' + str(self.tempVarNum)
        self.tempVarNum += 1
        localRegister = self.registers.pop()
        
        self.moonDataCode += self.moonCodeIndent + "% space for constant " + node.name + "\n"
        self.moonDataCode += f"{node.moonVarName:<10} res {4}\n"
        self.moonExecCode += self.moonCodeIndent + "% processing: " + node.moonVarName  + " := " + node.name + "\n"
        self.moonExecCode += self.moonCodeIndent + "addi " + localRegister + ",r0," + node.name + "\n"
        self.moonExecCode += self.moonCodeIndent + "sw " + node.moonVarName + "(r0)," + localRegister + "\n"
    
        self.registers.append(localRegister)
        
    @visitor.when(FloatNode)
    def visit(self, node):
        node.moonVarName = node.name
    
    @visitor.when(StructNode)
    def visit(self, node):
        self.scope_stack.pop()

    @visitor.when(FuncDeclNode)
    def visit(self, node):
        self.moonExecCode += self.moonCodeIndent + "lw r15," + node.name + "link(r0)\n"
        self.moonExecCode += self.moonCodeIndent + "jr r15\n"
        
    @visitor.when(FunctionNode)
    def visit(self, node):
        self.scope_data.pop()
    
    @visitor.when(VarDeclNode)
    def visit(self, node):
        tagName = node.table_entry[0]
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
        self.moonExecCode += self.moonCodeIndent + "sw -8(r14)," + localRegister + "\n"
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
        localRegister = self.registers.pop()
        
        self.moonExecCode += self.moonCodeIndent + "% processing: return("  + node.children[0].moonVarName + ")\n"
        self.moonExecCode += self.moonCodeIndent + "lw " + localRegister + "," + node.children[0].moonVarName + "(r0)\n"
        self.moonExecCode += self.moonCodeIndent + "sw " + node.moonVarName + "return(r0)," + localRegister + "\n"
        
        self.registers.append(localRegister)
    
    @visitor.when(ArithExprNode)
    def visit(self, node):
        node.moonVarName = node.children[0].moonVarName
    
    @visitor.when(RelExprNode)
    def visit(self, node):
        node.moonVarName = 't' + str(self.tempVarNum)
        self.tempVarNum += 1
        leftChildRegister, rightChildRegister, localRegister = self.registers[-3:]
        leftOp, operation, rightOp = node.children
        # perform different operation depending on operand
        match operation.name:
            case "==":
                oper = "ceq "
            case "!=":
                oper = "cne "
            case "<":
                oper = "clt "
            case "<=":
                oper = "cle "
            case ">":
                oper = "cgt "
            case ">=":
                oper = "cge "
            case _:
                oper = ""
        # generate moon code blocks for relop node
        moonExecCode = self.moonCodeIndent + f"% processing: {node.moonVarName}" + ":= " + leftOp.moonVarName + operation.name + rightOp.moonVarName + "\n"
        moonExecCode += self.moonCodeIndent + "lw " + leftChildRegister + "," + leftOp.moonVarName + "(r0)\n"
        moonExecCode += self.moonCodeIndent + "lw " + rightChildRegister + "," + rightOp.moonVarName + "(r0)\n"
        moonExecCode += self.moonCodeIndent + oper + localRegister + "," + leftChildRegister + "," + rightChildRegister + "\n"
        moonExecCode += self.moonCodeIndent + "sw " + node.moonVarName + "(r0)," + localRegister + "\n"
        
        self.moonDataCode += self.moonCodeIndent + "% space for " + leftOp.moonVarName + operation.name + rightOp.moonVarName + "\n"
        self.moonDataCode += f"{node.moonVarName:<10} res {node.size}\n"
        self.moonExecCode += moonExecCode
        
    @visitor.when(NotNode)
    def visit(self, node):
        node.moonVarName = 't' + str(self.tempVarNum)
        self.tempVarNum += 1
        leftChildRegister, rightChildRegister, localRegister = self.registers[-3:]
        leftOp, operation, rightOp = node.children
        
        moonExecCode = self.moonCodeIndent + f"% processing: {node.moonVarName}" + ":= " + leftOp.moonVarName + operation.name + rightOp.moonVarName + "\n"
        moonExecCode += self.moonCodeIndent + "lw " + leftChildRegister + "," + leftOp.moonVarName + "(r0)\n"
        moonExecCode += self.moonCodeIndent + "lw " + rightChildRegister + "," + rightOp.moonVarName + "(r0)\n"
        moonExecCode += self.moonCodeIndent + "not " + localRegister + "," + leftChildRegister + "," + rightChildRegister + "\n"
        moonExecCode += self.moonCodeIndent + "sw " + node.moonVarName + "(r0)," + localRegister + "\n"
        
        self.moonDataCode += self.moonCodeIndent + "% space for " + leftOp.moonVarName + operation.name + rightOp.moonVarName + "\n"
        self.moonDataCode += f"{node.moonVarName:<10} res {node.size}\n"
        self.moonExecCode += moonExecCode
        
    @visitor.when(AssignNode)
    def visit(self, node):
        localRegister = self.registers.pop()
        left, right = node.children
        self.moonExecCode += self.moonCodeIndent + "% processing: "  + left.moonVarName + " := " + right.moonVarName + "\n";
        self.moonExecCode += self.moonCodeIndent + "lw " + localRegister + "," + right.moonVarName + "(r0)\n";
        self.moonExecCode += self.moonCodeIndent + "sw " + left.moonVarName + "(r0)," + localRegister + "\n";
        self.registers.append(localRegister)

    @visitor.when(FuncCallNode)
    def visit(self, node):
        node.moonVarName = 't' + str(self.tempVarNum)
        self.tempVarNum += 1
        localRegister = self.registers.pop()
        table_entry = self
        param_idx = 0
        self.moonExecCode += self.moonCodeIndent + "% processing: function call to "  + node.children[0].moonVarName + " \n"
        for param in node.children[1].children:
            self.moonExecCode += self.moonCodeIndent + "lw " + localRegister + "," + param.moonVarName + "(r0)\n"
            param_name = node.children[0].moonVarName + "fp" + str(param_idx)
            self.moonExecCode += self.moonCodeIndent + "sw " + param_name + "(r0)," + localRegister + "\n"
            param_idx += 1
        
        self.moonExecCode += self.moonCodeIndent + "% func call (jump) for " + node.children[0].moonVarName + " \n"
        self.moonExecCode += self.moonCodeIndent + "jl r15," + node.moonVarName + "\n"
        self.moonDataCode += self.moonCodeIndent + "% space for function call expression factor\n"
        self.moonDataCode += f"{node.moonVarName:<10} res 4\n"
        self.moonExecCode += self.moonCodeIndent + "lw " + localRegister + "," + node.children[0].moonVarName + "return(r0)\n"
        self.moonExecCode += self.moonCodeIndent + "sw " + node.moonVarName + "(r0)," + localRegister + "\n"
        self.registers.append(localRegister)

    @visitor.when(AddOpNode)
    def visit(self, node):
        node.moonVarName = 't' + str(self.tempVarNum)
        self.tempVarNum += 1
        leftChildRegister, rightChildRegister, localRegister = self.registers[-3:]
        leftOp, operation, rightOp = node.children
        # perform different operation depending on operand
        match operation.name:
            case "+":
                oper = "add "
            case "-":
                oper = "sub "
            case "|":
                oper = "or "
            case _:
                oper = ""
        # generate moon code blocks for addop node
        moonExecCode = self.moonCodeIndent + f"% processing: {node.moonVarName}" + ":= " + leftOp.moonVarName + operation.name + rightOp.moonVarName + "\n"
        moonExecCode += self.moonCodeIndent + "lw " + leftChildRegister + "," + leftOp.moonVarName + "(r0)\n"
        moonExecCode += self.moonCodeIndent + "lw " + rightChildRegister + "," + rightOp.moonVarName + "(r0)\n"
        moonExecCode += self.moonCodeIndent + oper + localRegister + "," + leftChildRegister + "," + rightChildRegister + "\n"
        moonExecCode += self.moonCodeIndent + "sw " + node.moonVarName + "(r0)," + localRegister + "\n"
        
        self.moonDataCode += self.moonCodeIndent + "% space for " + leftOp.moonVarName + operation.name + rightOp.moonVarName + "\n"
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
                oper = "mul "
            case "/":
                oper = "div "
            case "&":
                oper = "and "
            case _:
                oper = ""
        # generate moon code blocks for multop node
        moonExecCode = self.moonCodeIndent + f"% processing: {node.moonVarName}" + ":= " + leftOp.moonVarName + operation.name + rightOp.moonVarName + "\n"
        moonExecCode += self.moonCodeIndent + "lw " + leftChildRegister + "," + leftOp.moonVarName + "(r0)\n"
        moonExecCode += self.moonCodeIndent + "lw " + rightChildRegister + "," + rightOp.moonVarName + "(r0)\n"
        moonExecCode += self.moonCodeIndent + oper + localRegister + "," + leftChildRegister + "," + rightChildRegister + "\n"
        moonExecCode += self.moonCodeIndent + "sw " + node.moonVarName + "(r0)," + localRegister + "\n"
        
        self.moonDataCode += self.moonCodeIndent + "% space for " + leftOp.moonVarName + operation.name + rightOp.moonVarName + "\n"
        self.moonDataCode += f"{node.moonVarName:<10} res {node.size}\n"
        self.moonExecCode += moonExecCode
    