from anytree import Node
from prettytable import PrettyTable
table = PrettyTable()

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
# Visitor Pattern and its subclasses
class Visitor():
    pass
