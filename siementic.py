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
        self.symbol_table = PrettyTable()
        self.symbol_table.field_names = ['Name', 'Kind', 'Type', 'Offset', 'Link']
        self.table_entry = []

class StructNode(Node):
    def __init__(self, name, parent=None, children=None, **kwargs):
        super().__init__(name, parent, children, **kwargs)
        self.symbol_table = PrettyTable()
        self.symbol_table.field_names = ['Name', 'Kind', 'Type', 'Offset', 'Link']
        self.table_entry = []
 
class AssignNode(Node):
    def __init__(self, name, parent=None, children=None, **kwargs):
        super().__init__(name, parent, children, **kwargs)
  
class VarDeclNode(Node):
    def __init__(self, name, parent=None, children=None, **kwargs):
        super().__init__(name, parent, children, **kwargs)
        self.table_entry = []

class MemberDeclNode(Node):
    def __init__(self, name, parent=None, children=None, **kwargs):
        super().__init__(name, parent, children, **kwargs)
        self.table_entry = []

class FunctionNode(Node):
    def __init__(self, name, parent=None, children=None, **kwargs):
        super().__init__(name, parent, children, **kwargs)
        self.symbol_table = PrettyTable()
        self.symbol_table.field_names = ['Name', 'Kind', 'Type', 'Offset', 'Link']
        self.table_entry = []
        
class InheritNode(Node):
    def __init__(self, name, parent=None, children=None, **kwargs):
        super().__init__(name, parent, children, **kwargs)

class ProgramNode(Node):
    def __init__(self, name, parent=None, children=None, **kwargs):
        super().__init__(name, parent, children, **kwargs)
        self.symbol_table = PrettyTable()
        self.symbol_table.field_names = ['Name', 'Kind', 'Type', 'Offset', 'Link']

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
        self.table_entry = []

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
        self.output = ""

    @visitor.on('node')
    def visit(self, node):
        pass
    
    @visitor.when(ProgramNode)
    def visit(self, node):
        for c in node.children:
            node.symbol_table.add_row(c.table_entry)
        title = "Global table" 
        self.output += node.symbol_table.get_string(title=title) + "\n"
        
    @visitor.when(StructNode)
    def visit(self, node):
        id, inherits, memberList = node.children
        node.table_entry = [id.name, "struct", None, 0, None]

    @visitor.when(FunctionNode)
    def visit(self, node):
        id, params, returnType, body = node.children
        # add func params to the symbol table
        for p in params.children:
            node.symbol_table.add_row(p.table_entry)
        # add variable declarations to the symbol table
        for v in body.children:
            if v.name == "varDecl":
                node.symbol_table.add_row(v.table_entry)
        # update function node's symbol table and append to output
        node.table_entry = [id.name, "function", returnType.children[0].name, 0, "Table " + id.name]
        title = "Table Name: " + id.name + ", Returns: " + returnType.children[0].name
        self.output += node.symbol_table.get_string(title=title) + "\n"

    @visitor.when(ImplNode)
    def visit(self, node):
        id, funcList = node.children
        node.table_entry = [id.name, "impl", None, 0, None]
    
    @visitor.when(VarDeclNode)
    def visit(self, node):
        v_name, v_type, v_array = node.children
        v_arraySize = ""
        for s in v_array.children:
            v_arraySize += "[]" if s.name == "emptySize" else "[" + s.name + "]"
        node.table_entry = [v_name.name, "variable", v_type.name + v_arraySize, 0, None]

    @visitor.when(MemberDeclNode)
    def visit(self, node):
        pass

    @visitor.when(ParamNode)
    def visit(self, node):
        p_name, p_type, p_array = node.children
        p_arraySize = ""
        for s in p_array.children:
            p_arraySize += "[]" if s.name == "emptySize" else "[" + s.name + "]"
        node.table_entry = [p_name.name, "parameter", p_type.name + p_arraySize, 0, None]


#####################################
# Type Checking Concrete Visitor
class TypeCheckingVisitor(Visitor):
    def __init__(self):
        super().__init__()

    @visitor.on('node')
    def visit(self, node):
        pass