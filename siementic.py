import anytree
import visitor
from prettytable import PrettyTable

#####################################
# Node class
class Node(anytree.Node):
    def accept(self, visitor):
        for child in self.children:
            child.accept(visitor)
        visitor.visit(self)

#####################################
# Leaf nodes
class IdNode(Node):
    def __init__(self, name, parent=None, children=None, **kwargs):
        super().__init__(name, parent, children, **kwargs)

class NumericNode(Node):
    def __init__(self, name, parent=None, children=None, **kwargs):
        super().__init__(name, parent, children, **kwargs)

class TypeNode(Node):
    def __init__(self, name, parent=None, children=None, **kwargs):
        super().__init__(name, parent, children, **kwargs)
        
class AddNode(Node):
    def __init__(self, name, parent=None, children=None, **kwargs):
        super().__init__(name, parent, children, **kwargs)
        
class MultNode(Node):
    def __init__(self, name, parent=None, children=None, **kwargs):
        super().__init__(name, parent, children, **kwargs)

class RelationNode(Node):
    def __init__(self, name, parent=None, children=None, **kwargs):
        super().__init__(name, parent, children, **kwargs)
    
class VisibilityNode(Node):
    def __init__(self, name, parent=None, children=None, **kwargs):
        super().__init__(name, parent, children, **kwargs)
        
#####################################
# Subtree nodes
class ArraySizeNode(Node):
    def __init__(self, name, parent=None, children=None, **kwargs):
        super().__init__(name, parent, children, **kwargs)

class FuncListNode(Node):
    def __init__(self, name, parent=None, children=None, **kwargs):
        super().__init__(name, parent, children, **kwargs)

class ImplNode(Node):
    def __init__(self, name, parent=None, children=None, **kwargs):
        super().__init__(name, parent, children, **kwargs)

class StructNode(Node):
    def __init__(self, name, parent=None, children=None, **kwargs):
        super().__init__(name, parent, children, **kwargs)
 
class AssignNode(Node):
    def __init__(self, name, parent=None, children=None, **kwargs):
        super().__init__(name, parent, children, **kwargs)
  
class VarDeclNode(Node):
    def __init__(self, name, parent=None, children=None, **kwargs):
        super().__init__(name, parent, children, **kwargs)

class MemberDeclNode(Node):
    def __init__(self, name, parent=None, children=None, **kwargs):
        super().__init__(name, parent, children, **kwargs)

class FunctionNode(Node):
    def __init__(self, name, parent=None, children=None, **kwargs):
        super().__init__(name, parent, children, **kwargs)
        
class InheritNode(Node):
    def __init__(self, name, parent=None, children=None, **kwargs):
        super().__init__(name, parent, children, **kwargs)

class ProgramNode(Node):
    def __init__(self, name, parent=None, children=None, **kwargs):
        super().__init__(name, parent, children, **kwargs)

class MemberListNode(Node):
    def __init__(self, name, parent=None, children=None, **kwargs):
        super().__init__(name, parent, children, **kwargs)

class FuncDeclNode(Node):
    def __init__(self, name, parent=None, children=None, **kwargs):
        super().__init__(name, parent, children, **kwargs)

class FuncParamsNode(Node):
    def __init__(self, name, parent=None, children=None, **kwargs):
        super().__init__(name, parent, children, **kwargs)

class ReturnTypeNode(Node):
    def __init__(self, name, parent=None, children=None, **kwargs):
        super().__init__(name, parent, children, **kwargs)

class FuncBodyNode(Node):
    def __init__(self, name, parent=None, children=None, **kwargs):
        super().__init__(name, parent, children, **kwargs)

class IfNode(Node):
    def __init__(self, name, parent=None, children=None, **kwargs):
        super().__init__(name, parent, children, **kwargs)

class ThenNode(Node):
    def __init__(self, name, parent=None, children=None, **kwargs):
        super().__init__(name, parent, children, **kwargs)

class ElseNode(Node):
    def __init__(self, name, parent=None, children=None, **kwargs):
        super().__init__(name, parent, children, **kwargs)

class WhileNode(Node):
    def __init__(self, name, parent=None, children=None, **kwargs):
        super().__init__(name, parent, children, **kwargs)

class ReadNode(Node):
    def __init__(self, name, parent=None, children=None, **kwargs):
        super().__init__(name, parent, children, **kwargs)

class WriteNode(Node):
    def __init__(self, name, parent=None, children=None, **kwargs):
        super().__init__(name, parent, children, **kwargs)

class ReturnNode(Node):
    def __init__(self, name, parent=None, children=None, **kwargs):
        super().__init__(name, parent, children, **kwargs)

class DotNode(Node):
    def __init__(self, name, parent=None, children=None, **kwargs):
        super().__init__(name, parent, children, **kwargs)

class FuncCallNode(Node):
    def __init__(self, name, parent=None, children=None, **kwargs):
        super().__init__(name, parent, children, **kwargs)

class IndiceListNode(Node):
    def __init__(self, name, parent=None, children=None, **kwargs):
        super().__init__(name, parent, children, **kwargs)

class VariableNode(Node):
    def __init__(self, name, parent=None, children=None, **kwargs):
        super().__init__(name, parent, children, **kwargs)

class StatBlockNode(Node):
    def __init__(self, name, parent=None, children=None, **kwargs):
        super().__init__(name, parent, children, **kwargs)

class RelExprNode(Node):
    def __init__(self, name, parent=None, children=None, **kwargs):
        super().__init__(name, parent, children, **kwargs)

class ArithExprNode(Node):
    def __init__(self, name, parent=None, children=None, **kwargs):
        super().__init__(name, parent, children, **kwargs)

class AddOpNode(Node):
    def __init__(self, name, parent=None, children=None, **kwargs):
        super().__init__(name, parent, children, **kwargs)

class MultOpNode(Node):
    def __init__(self, name, parent=None, children=None, **kwargs):
        super().__init__(name, parent, children, **kwargs)

class NotNode(Node):
    def __init__(self, name, parent=None, children=None, **kwargs):
        super().__init__(name, parent, children, **kwargs)

class SignNode(Node):
    def __init__(self, name, parent=None, children=None, **kwargs):
        super().__init__(name, parent, children, **kwargs)

class EmptySizeNode(Node):
    def __init__(self, name, parent=None, children=None, **kwargs):
        super().__init__(name, parent, children, **kwargs)

class VoidNode(Node):
    def __init__(self, name, parent=None, children=None, **kwargs):
        super().__init__(name, parent, children, **kwargs)

class ParamNode(Node):
    def __init__(self, name, parent=None, children=None, **kwargs):
        super().__init__(name, parent, children, **kwargs)

class ArgParamNode(Node):
    def __init__(self, name, parent=None, children=None, **kwargs):
        super().__init__(name, parent, children, **kwargs)

#####################################
# Default Visitor Pattern and empty visit members
class Visitor:
    @visitor.on('node')
    def visit(self, node):
        pass

    @visitor.when(IdNode)
    def visit(self, node):
        pass

    @visitor.when(NumericNode)
    def visit(self, node):
        pass

    @visitor.when(TypeNode)
    def visit(self, node):
        pass

    @visitor.when(AddNode)
    def visit(self, node):
        pass

    @visitor.when(MultNode)
    def visit(self, node):
        pass

    @visitor.when(RelationNode)
    def visit(self, node):
        pass

    @visitor.when(VisibilityNode)
    def visit(self, node):
        pass

    @visitor.when(ArraySizeNode)
    def visit(self, node):
        pass

    @visitor.when(FuncListNode)
    def visit(self, node):
        pass

    @visitor.when(ImplNode)
    def visit(self, node):
        pass

    @visitor.when(StructNode)
    def visit(self, node):
        pass

    @visitor.when(AssignNode)
    def visit(self, node):
        pass

    @visitor.when(VarDeclNode)
    def visit(self, node):
        pass

    @visitor.when(MemberDeclNode)
    def visit(self, node):
        pass

    @visitor.when(FunctionNode)
    def visit(self, node):
        pass

    @visitor.when(InheritNode)
    def visit(self, node):
        pass

    @visitor.when(ProgramNode)
    def visit(self, node):
        pass

    @visitor.when(MemberListNode)
    def visit(self, node):
        pass

    @visitor.when(FuncDeclNode)
    def visit(self, node):
        pass

    @visitor.when(FuncParamsNode)
    def visit(self, node):
        pass

    @visitor.when(ReturnTypeNode)
    def visit(self, node):
        pass

    @visitor.when(FuncBodyNode)
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

    @visitor.when(DotNode)
    def visit(self, node):
        pass

    @visitor.when(FuncCallNode)
    def visit(self, node):
        pass

    @visitor.when(IndiceListNode)
    def visit(self, node):
        pass

    @visitor.when(VariableNode)
    def visit(self, node):
        pass

    @visitor.when(StatBlockNode)
    def visit(self, node):
        pass

    @visitor.when(RelExprNode)
    def visit(self, node):
        pass

    @visitor.when(ArithExprNode)
    def visit(self, node):
        pass

    @visitor.when(AddOpNode)
    def visit(self, node):
        pass

    @visitor.when(MultOpNode)
    def visit(self, node):
        pass

    @visitor.when(NotNode)
    def visit(self, node):
        pass

    @visitor.when(SignNode)
    def visit(self, node):
        pass

    @visitor.when(EmptySizeNode)
    def visit(self, node):
        pass

    @visitor.when(VoidNode)
    def visit(self, node):
        pass

    @visitor.when(ParamNode)
    def visit(self, node):
        pass

    @visitor.when(ArgParamNode)
    def visit(self, node):
        pass

#####################################
# Symbol Table Concrete Visitor
class SymbolTableVisitor(Visitor):
    def __init__(self):
        super().__init__()
        self.symbol_table = {}
        
    @visitor.on('node')
    def visit(self, node):
        pass
    
    @visitor.when(StructNode)
    def visit(self, node):
        pass

    @visitor.when(FunctionNode)
    def visit(self, node):
        print(node)
        print("inside function", node.children[0].name)
    
    @visitor.when(ProgramNode)
    def visit(self, node):
        print(node)
        print("inside visitor pattern")
    
    @visitor.when(StructNode)
    def visit(self, node):
        pass