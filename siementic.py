import anytree
import visitor
from prettytable import PrettyTable

#####################################
# Node class
class Node(anytree.Node):
    def __init__(self, name, parent=None, children=None, **kwargs):
        super().__init__(name, parent, children, **kwargs)
        self.moonVarName = ""
        self.type = ""
        
    def accept(self, visitor):
        # allow for pre visit children node function calls
        method_name = 'pre_visit_' + type(self).__name__
        visit_method = getattr(visitor, method_name, None)
        if visit_method:
            visit_method(self)
        # otherwise accept the children the standard way
        for child in self.children:
            child.accept(visitor)
        visitor.visit(self)


#####################################
# Leaf nodes
class IdNode(Node):
    def __init__(self, name, parent=None, children=None, **kwargs):
        super().__init__(name, parent, children, **kwargs)
        self.type = ""

class IntNode(Node):
    def __init__(self, name, parent=None, children=None, **kwargs):
        super().__init__(name, parent, children, **kwargs)
        self.type = "integer"

class FloatNode(Node):
    def __init__(self, name, parent=None, children=None, **kwargs):
        super().__init__(name, parent, children, **kwargs)
        self.type = "float"

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
        self.table_output = ""
        self.struct_name = ""

class StructNode(Node):
    def __init__(self, name, parent=None, children=None, **kwargs):
        super().__init__(name, parent, children, **kwargs)
        self.symbol_table = PrettyTable()
        self.symbol_table.field_names = ['Name', 'Kind', 'Type', 'Offset', 'Link']
        self.symbol_data = []
        self.table_entry = []
        self.table_output = ""
        self.struct_name = ""
        self.curr_offset = 0
 
class AssignNode(Node):
    def __init__(self, name, parent=None, children=None, **kwargs):
        super().__init__(name, parent, children, **kwargs)
        self.type = ""

class VarDeclNode(Node):
    def __init__(self, name, parent=None, children=None, **kwargs):
        super().__init__(name, parent, children, **kwargs)
        self.table_entry = []
        self.mem_size = 0

class MemberDeclNode(Node):
    def __init__(self, name, parent=None, children=None, **kwargs):
        super().__init__(name, parent, children, **kwargs)
        self.table_entry = []

class FunctionNode(Node):
    def __init__(self, name, parent=None, children=None, **kwargs):
        super().__init__(name, parent, children, **kwargs)
        self.symbol_table = PrettyTable()
        self.symbol_table.field_names = ['Name', 'Kind', 'Type', 'Offset', 'Link']
        self.symbol_data = []
        self.table_entry = []
        self.table_output = ""
        self.curr_offset = 0
        
class InheritNode(Node):
    def __init__(self, name, parent=None, children=None, **kwargs):
        super().__init__(name, parent, children, **kwargs)

class ProgramNode(Node):
    def __init__(self, name, parent=None, children=None, **kwargs):
        super().__init__(name, parent, children, **kwargs)
        self.symbol_table = PrettyTable()
        self.symbol_table.field_names = ['Name', 'Kind', 'Type', 'Offset', 'Link']
        self.symbol_data = []

class MemberListNode(Node):
    def __init__(self, name, parent=None, children=None, **kwargs):
        super().__init__(name, parent, children, **kwargs)

class FuncDeclNode(Node):
    def __init__(self, name, parent=None, children=None, **kwargs):
        super().__init__(name, parent, children, **kwargs)
        self.table_entry = []

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
        self.type = ""

class DotNode(Node):
    def __init__(self, name, parent=None, children=None, **kwargs):
        super().__init__(name, parent, children, **kwargs)
        self.type = ""

class FuncCallNode(Node):
    def __init__(self, name, parent=None, children=None, **kwargs):
        super().__init__(name, parent, children, **kwargs)
        self.type = ""

class IndiceListNode(Node):
    def __init__(self, name, parent=None, children=None, **kwargs):
        super().__init__(name, parent, children, **kwargs)

class VariableNode(Node):
    def __init__(self, name, parent=None, children=None, **kwargs):
        super().__init__(name, parent, children, **kwargs)
        self.type = ""

class StatBlockNode(Node):
    def __init__(self, name, parent=None, children=None, **kwargs):
        super().__init__(name, parent, children, **kwargs)

class RelExprNode(Node):
    def __init__(self, name, parent=None, children=None, **kwargs):
        super().__init__(name, parent, children, **kwargs)
        self.type = ""

class ArithExprNode(Node):
    def __init__(self, name, parent=None, children=None, **kwargs):
        super().__init__(name, parent, children, **kwargs)
        self.type = ""

class AddOpNode(Node):
    def __init__(self, name, parent=None, children=None, **kwargs):
        super().__init__(name, parent, children, **kwargs)
        self.type = ""

class MultOpNode(Node):
    def __init__(self, name, parent=None, children=None, **kwargs):
        super().__init__(name, parent, children, **kwargs)
        self.type = ""

class NotNode(Node):
    def __init__(self, name, parent=None, children=None, **kwargs):
        super().__init__(name, parent, children, **kwargs)

class SignNode(Node):
    def __init__(self, name, parent=None, children=None, **kwargs):
        super().__init__(name, parent, children, **kwargs)
        self.type = ""

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

    @visitor.when(IntNode)
    def visit(self, node):
        pass

    @visitor.when(FloatNode)
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
        self.errors = ""
        self.warnings = ""

    @visitor.on('node')
    def visit(self, node):
        pass
    
    @visitor.when(ProgramNode)
    def visit(self, node):
        struct_dict = {}
        for c in node.children:
            if c.name == "struct":
                node.symbol_data.append(c.table_entry)
                struct_dict[c.struct_name] = c.table_output
            elif c.name == "impl":
                try:
                    self.output += struct_dict[c.struct_name] + c.table_output
                except:
                    self.errors += "Must define struct before impl on line: " + str(node.line)
            else:
                node.symbol_data.append(c.table_entry)
                self.output += c.table_output
        # update symbol table with data
        node.symbol_table.add_rows(node.symbol_data)
        # update output
        title = "Global table"
        self.output = node.symbol_table.get_string(title=title) + "\n" + self.output
        
    @visitor.when(StructNode)
    def visit(self, node):
        id, inherits, memberList = node.children
        # add inherits string to title if it exists
        inherit_string = inherits.children[0].name if inherits.children else ""
        # add members to struct symbol table
        for m in memberList.children:
            node.symbol_data.append(m.table_entry)
        # update symbol table with data
        node.symbol_table.add_rows(node.symbol_data)
        # update output and table entry
        node.table_entry = [id.name, "struct", None, 0, "Table " + id.name]
        node.struct_name = id.name
        title = "Table Name: " + id.name + ", Inherits: " + inherit_string
        node.table_output += node.symbol_table.get_string(title=title) + "\n"
        
    @visitor.when(FuncDeclNode)
    def visit(self, node):
        id, params, returnType = node.children
        node.table_entry = [id.name, "funcDecl", returnType.children[0].name, 0, None]

    @visitor.when(FunctionNode)
    def visit(self, node):
        id, params, returnType, body = node.children
        # add func params to the symbol table
        for p in params.children:
            node.symbol_data.append(p.table_entry)
        # add variable declarations to the symbol table
        for v in body.children:
            if v.name == "varDecl":
                # update both the current offset and the table entry
                node.curr_offset = node.curr_offset + v.mem_size
                # create copy to avoid referencing the variable's entry
                row = v.table_entry.copy()
                row[3] = node.curr_offset
                node.symbol_data.append(row)
        # update symbol table with data
        node.symbol_table.add_rows(node.symbol_data)
        # update function node's symbol table and append to output
        node.table_entry = [id.name, "function", returnType.children[0].name, 0, "Table " + id.name]
        title = "Table Name: " + id.name + ", Returns: " + returnType.children[0].name
        node.table_output += node.symbol_table.get_string(title=title) + "\n"

    @visitor.when(ImplNode)
    def visit(self, node):
        id, funcList = node.children
        node.struct_name = id.name
        for f in funcList.children:
            node.table_output += f.table_output
    
    @visitor.when(VarDeclNode)
    def visit(self, node):
        v_name, v_type, v_array = node.children
        v_arraySize = ""
        if v_type.name == "integer":
            node.mem_size = 4
        elif v_type.name == "float":
            node.mem_size = 8
        for s in v_array.children:
            if s.name == "emptySize":
                v_arraySize += "[]" 
            else:
                v_arraySize += "[" + s.name + "]"
                node.mem_size *= int(s.name)
        node.table_entry = [v_name.name, "variable", v_type.name + v_arraySize, node.mem_size, None]

    @visitor.when(MemberDeclNode)
    def visit(self, node):
        visib, decl = node.children
        # add visibility to members for the kind column
        new_entry = decl.table_entry
        new_entry[1] = visib.name + " " + new_entry[1]
        node.table_entry = new_entry

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
        self.errors = ""
        self.global_scope = []
        self.struct_scope = []
        self.func_scope = []

    @visitor.on('node')
    def visit(self, node):
        pass
    
    # pre visit nodes to get symbol table information
    def pre_visit_ProgramNode(self, node):
        self.global_scope = node.symbol_data
    
    def pre_visit_StructNode(self, node):
        self.struct_scope = node.symbol_data
    
    def pre_visit_FunctionNode(self, node):
        self.func_scope = node.symbol_data
    
    def pre_visit_ImplNode(self, node):
        pass
    
    # helper function to get type of variable in data
    def get_var_dtype(self, name):
        # check for matching dtype in function scope first
        for row in self.func_scope:
            if row[0] == name:
                return row[2]
        # check for matching dtype in struct scope second
        for row in self.struct_scope:
            if row[0] == name:
                return row[2]
        # finally check for matching dtype in global scope
        for row in self.global_scope:
            if row[0] == name:
                return row[2]
        return "variable undeclared error"
        
    # type checking visitors
    @visitor.when(MultOpNode)
    def visit(self, node):
        left, _, right = node.children
        if left.type == right.type:
            node.type = left.type
        else:
            node.type = "typeerror"
            self.errors += "error on line: " + str(node.line) + "\n"
            self.errors += "mismatch between nodes of type: " + left.name + right.name + "\n"
     
    @visitor.when(AddOpNode)
    def visit(self, node):
        left, _, right = node.children
        if left.type == right.type:
            node.type = left.type
        else:
            node.type = "typeerror"
            self.errors += "error on line: " + str(node.line) + "\n"
            self.errors += "mismatch between nodes of type: " + left.name + right.name + "\n"
    
    @visitor.when(ArithExprNode)
    def visit(self, node):
        node.type = node.children[0].type
    
    @visitor.when(RelExprNode)
    def visit(self, node):
        left, _, right = node.children
        if left.type == right.type:
            node.type = left.type
        else:
            node.type = "typeerror"
            self.errors += "error on line: " + str(node.line) + "\n"
            self.errors += "mismatch between nodes of type: " + left.name + right.name + "\n"

    @visitor.when(VariableNode)
    def visit(self, node):
        id, indiceList = node.children
        node.type = self.get_var_dtype(id.name)
    
    @visitor.when(AssignNode)
    def visit(self, node):
        left, right = node.children
        if left.type == right.type:
            node.type = left.type
        else:
            node.type = "typeerror"
            self.errors += "error on line: " + str(node.line) + "\n"
            self.errors += "mismatch between nodes of type: " + left.name + right.name + "\n"
        
    @visitor.when(DotNode)
    def visit(self, node):
        left, right = node.children
        node.type = self.get_var_dtype(right.name)

    @visitor.when(IdNode)
    def visit(self, node):
        node.type = self.get_var_dtype(node.name)
        
    @visitor.when(FuncCallNode)
    def visit(self, node):
        func, paramList = node.children
        func_params = [child.type for child in paramList.children]
        self.errors += str(func_params) + "\n"
        
        # check for functions declared in class scope
        if node.parent.name == 'dot':
            self.errors += str(node.parent) + "\n"
            
        # check for free functions declared in function scope
        else:
            pass