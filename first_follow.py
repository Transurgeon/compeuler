from kento import TokenType

follow = {
    "ADDOP": {TokenType.ID, TokenType.INTNUM, TokenType.FLOATNUM, TokenType.OPENPAR, TokenType.NOT, TokenType.PLUS, TokenType.MINUS},
    "ARRAYSIZE2": {TokenType.SEMI, TokenType.OPENSQBR, TokenType.CLOSEPAR, TokenType.COMMA},
    "EXPR2": {TokenType.COMMA, TokenType.CLOSEPAR, TokenType.SEMI},
    "FACTOR2": {TokenType.MULT, TokenType.DIV, TokenType.AND, TokenType.DOT, TokenType.CLOSESQBR, TokenType.EQ, TokenType.NOTEQ, TokenType.LT, TokenType.GT, TokenType.LEQ, TokenType.GEQ, TokenType.PLUS, TokenType.MINUS, TokenType.OR, TokenType.COMMA, TokenType.CLOSEPAR, TokenType.SEMI},
    "FUNCBODY": {TokenType.STRUCT, TokenType.IMPL, TokenType.FUNC, TokenType.CLOSECUBR},
    "FUNCHEAD": {TokenType.SEMI, TokenType.OPENCUBR},
    "FPARAMS": {TokenType.CLOSEPAR},
    "FUNCTIONCALL": set(),
    "IDNEST2": {TokenType.MULT, TokenType.DIV, TokenType.AND, TokenType.DOT, TokenType.ID, TokenType.CLOSESQBR, TokenType.EQ, TokenType.NOTEQ, TokenType.LT, TokenType.GT, TokenType.LEQ, TokenType.GEQ, TokenType.PLUS, TokenType.MINUS, TokenType.OR, TokenType.COMMA, TokenType.CLOSEPAR, TokenType.SEMI},
    "FUNCDECL": {TokenType.CLOSECUBR, TokenType.PUBLIC, TokenType.PRIVATE},
    "ARITHEXPR": {TokenType.CLOSESQBR, TokenType.EQ, TokenType.NOTEQ, TokenType.LT, TokenType.GT, TokenType.LEQ, TokenType.GEQ, TokenType.COMMA, TokenType.CLOSEPAR, TokenType.SEMI},
    "RELOP": {TokenType.ID, TokenType.INTNUM, TokenType.FLOATNUM, TokenType.OPENPAR, TokenType.NOT, TokenType.PLUS, TokenType.MINUS},
    "APARAMSTAIL": {TokenType.COMMA, TokenType.CLOSEPAR},
    "REPTAPARAMS1": {TokenType.CLOSEPAR},
    "REPTFPARAMS3": {TokenType.CLOSEPAR, TokenType.COMMA},
    "FPARAMSTAIL": {TokenType.COMMA, TokenType.CLOSEPAR},
    "REPTFPARAMS4": {TokenType.CLOSEPAR},
    "REPTFPARAMSTAIL4": {TokenType.COMMA, TokenType.CLOSEPAR},
    "REPTFUNCBODY1": {TokenType.CLOSECUBR},
    "REPTFUNCTIONCALL0": {TokenType.ID},
    "REPTIMPLDEF3": {TokenType.CLOSECUBR},
    "REPTOPTSTRUCTDECL22": {TokenType.OPENCUBR},
    "REPTPROG0": set(),
    "MEMBERDECL": {TokenType.CLOSECUBR, TokenType.PUBLIC, TokenType.PRIVATE},
    "ARRAYSIZE": {TokenType.SEMI, TokenType.OPENSQBR, TokenType.CLOSEPAR, TokenType.COMMA},
    "REPTVARIABLE0": set(),
    "INDICE": {TokenType.ASSIGN, TokenType.MULT, TokenType.DIV, TokenType.AND, TokenType.OPENSQBR, TokenType.ID, TokenType.DOT, TokenType.CLOSESQBR, TokenType.EQ, TokenType.NOTEQ, TokenType.LT, TokenType.GT, TokenType.LEQ, TokenType.GEQ, TokenType.PLUS, TokenType.MINUS, TokenType.OR, TokenType.COMMA, TokenType.CLOSEPAR, TokenType.SEMI},
    "REPTVARIABLE2": set(),
    "IDNEST": {TokenType.MULT, TokenType.DIV, TokenType.AND, TokenType.DOT, TokenType.ID, TokenType.CLOSESQBR, TokenType.EQ, TokenType.NOTEQ, TokenType.LT, TokenType.GT, TokenType.LEQ, TokenType.GEQ, TokenType.PLUS, TokenType.MINUS, TokenType.OR, TokenType.COMMA, TokenType.CLOSEPAR, TokenType.SEMI},
    "REPTVARIABLEORFUNC": {TokenType.MULT, TokenType.DIV, TokenType.AND, TokenType.CLOSESQBR, TokenType.EQ, TokenType.NOTEQ, TokenType.LT, TokenType.GT, TokenType.LEQ, TokenType.GEQ, TokenType.PLUS, TokenType.MINUS, TokenType.OR, TokenType.COMMA, TokenType.CLOSEPAR, TokenType.SEMI},
    "RETURNTYPE": {TokenType.SEMI, TokenType.OPENCUBR},
    "RIGHTRECARITHEXPR": {TokenType.CLOSESQBR, TokenType.EQ, TokenType.NOTEQ, TokenType.LT, TokenType.GT, TokenType.LEQ, TokenType.GEQ, TokenType.COMMA, TokenType.CLOSEPAR, TokenType.SEMI},
    "MULTOP": {TokenType.ID, TokenType.INTNUM, TokenType.FLOATNUM, TokenType.OPENPAR, TokenType.NOT, TokenType.PLUS, TokenType.MINUS},
    "SIGN": {TokenType.ID, TokenType.INTNUM, TokenType.FLOATNUM, TokenType.OPENPAR, TokenType.NOT, TokenType.PLUS, TokenType.MINUS},
    "START": set(),
    "PROG": set(),
    "REPTSTATBLOCK1": {TokenType.CLOSECUBR},
    "RELEXPR": {TokenType.CLOSEPAR},
    "STATBLOCK": {TokenType.ELSE, TokenType.SEMI},
    "STATEMENT3": {TokenType.ELSE, TokenType.SEMI, TokenType.LET, TokenType.IF, TokenType.WHILE, TokenType.READ, TokenType.WRITE, TokenType.RETURN, TokenType.CLOSECUBR},
    "ASSIGNOP": {TokenType.ID, TokenType.INTNUM, TokenType.FLOATNUM, TokenType.OPENPAR, TokenType.NOT, TokenType.PLUS, TokenType.MINUS},
    "EXPR": {TokenType.COMMA, TokenType.CLOSEPAR, TokenType.SEMI},
    "STATEMENT4": {TokenType.ELSE, TokenType.SEMI, TokenType.LET, TokenType.ID, TokenType.IF, TokenType.WHILE, TokenType.READ, TokenType.WRITE, TokenType.RETURN, TokenType.CLOSECUBR},
    "STATEMENT2": {TokenType.ELSE, TokenType.SEMI, TokenType.LET, TokenType.ID, TokenType.IF, TokenType.WHILE, TokenType.READ, TokenType.WRITE, TokenType.RETURN, TokenType.CLOSECUBR},
    "OPTSTRUCTDECL2": {TokenType.OPENCUBR},
    "REPTSTRUCTDECL4": {TokenType.CLOSECUBR},
    "STRUCTORIMPLORFUNC": {TokenType.STRUCT, TokenType.IMPL, TokenType.FUNC},
    "STRUCTDECL": {TokenType.STRUCT, TokenType.IMPL, TokenType.FUNC},
    "IMPLDEF": {TokenType.STRUCT, TokenType.IMPL, TokenType.FUNC},
    "FUNCDEF": {TokenType.STRUCT, TokenType.IMPL, TokenType.FUNC, TokenType.CLOSECUBR},
    "TERM": {TokenType.CLOSESQBR, TokenType.EQ, TokenType.NOTEQ, TokenType.LT, TokenType.GT, TokenType.LEQ, TokenType.GEQ, TokenType.PLUS, TokenType.MINUS, TokenType.OR, TokenType.COMMA, TokenType.CLOSEPAR, TokenType.SEMI},
    "FACTOR": {TokenType.MULT, TokenType.DIV, TokenType.AND, TokenType.CLOSESQBR, TokenType.EQ, TokenType.NOTEQ, TokenType.LT, TokenType.GT, TokenType.LEQ, TokenType.GEQ, TokenType.PLUS, TokenType.MINUS, TokenType.OR, TokenType.COMMA, TokenType.CLOSEPAR, TokenType.SEMI},
    "RIGHTRECTERM": {TokenType.CLOSESQBR, TokenType.EQ, TokenType.NOTEQ, TokenType.LT, TokenType.GT, TokenType.LEQ, TokenType.GEQ, TokenType.PLUS, TokenType.MINUS, TokenType.OR, TokenType.COMMA, TokenType.CLOSEPAR, TokenType.SEMI},
    "TYPE": {TokenType.CLOSEPAR, TokenType.OPENCUBR, TokenType.COMMA, TokenType.OPENSQBR, TokenType.SEMI},
    "REPTVARDECL4": {TokenType.SEMI},
    "VARDECLORSTAT": {TokenType.LET, TokenType.ID, TokenType.IF, TokenType.WHILE, TokenType.READ, TokenType.WRITE, TokenType.RETURN, TokenType.CLOSECUBR},
    "VARDECL": {TokenType.PUBLIC, TokenType.PRIVATE, TokenType.LET, TokenType.ID, TokenType.IF, TokenType.WHILE, TokenType.READ, TokenType.WRITE, TokenType.RETURN, TokenType.CLOSECUBR},
    "STATEMENT": {TokenType.ELSE, TokenType.SEMI, TokenType.LET, TokenType.ID, TokenType.IF, TokenType.WHILE, TokenType.READ, TokenType.WRITE, TokenType.RETURN, TokenType.CLOSECUBR},
    "VARIABLE": {TokenType.CLOSEPAR},
    "VARIABLE2": {TokenType.CLOSEPAR},
    "REPTVARIABLE": {TokenType.CLOSEPAR},
    "VARIDNEST2": {TokenType.CLOSEPAR, TokenType.DOT},
    "APARAMS": {TokenType.CLOSEPAR},
    "VARIDNEST": {TokenType.CLOSEPAR, TokenType.DOT},
    "REPTIDNEST1": {TokenType.ASSIGN, TokenType.MULT, TokenType.DIV, TokenType.AND, TokenType.ID, TokenType.DOT, TokenType.CLOSESQBR, TokenType.EQ, TokenType.NOTEQ, TokenType.LT, TokenType.GT, TokenType.LEQ, TokenType.GEQ, TokenType.PLUS, TokenType.MINUS, TokenType.OR, TokenType.COMMA, TokenType.CLOSEPAR, TokenType.SEMI},
    "VISIBILITY": {TokenType.LET, TokenType.FUNC}
}

first = {
    "ADDOP": {TokenType.PLUS, TokenType.MINUS, TokenType.OR},
    "ARRAYSIZE2": {TokenType.INTNUM, TokenType.CLOSESQBR},
    "EXPR2": {TokenType.EQ, TokenType.NOTEQ, TokenType.LT, TokenType.GT, TokenType.LEQ, TokenType.GEQ},
    "FACTOR2": {TokenType.OPENPAR, TokenType.OPENSQBR},
    "FUNCBODY": {TokenType.OPENCUBR},
    "FUNCHEAD": {TokenType.FUNC},
    "FPARAMS": {TokenType.ID},
    "FUNCTIONCALL": {TokenType.ID, TokenType.DOT},
    "IDNEST2": {TokenType.OPENPAR, TokenType.OPENSQBR},
    "FUNCDECL": {TokenType.FUNC},
    "ARITHEXPR": {TokenType.ID, TokenType.INTNUM, TokenType.FLOATNUM, TokenType.OPENPAR, TokenType.NOT, TokenType.PLUS, TokenType.MINUS},
    "RELOP": {TokenType.EQ, TokenType.NOTEQ, TokenType.LT, TokenType.GT, TokenType.LEQ, TokenType.GEQ},
    "APARAMSTAIL": {TokenType.COMMA},
    "REPTAPARAMS1": {TokenType.COMMA},
    "REPTFPARAMS3": {TokenType.OPENSQBR},
    "FPARAMSTAIL": {TokenType.COMMA},
    "REPTFPARAMS4": {TokenType.COMMA},
    "REPTFPARAMSTAIL4": {TokenType.OPENSQBR},
    "REPTFUNCBODY1": {TokenType.LET, TokenType.ID, TokenType.IF, TokenType.WHILE, TokenType.READ, TokenType.WRITE, TokenType.RETURN},
    "REPTFUNCTIONCALL0": {TokenType.DOT},
    "REPTIMPLDEF3": {TokenType.FUNC},
    "REPTOPTSTRUCTDECL22": {TokenType.COMMA},
    "REPTPROG0": {TokenType.STRUCT, TokenType.IMPL, TokenType.FUNC},
    "MEMBERDECL": {TokenType.LET, TokenType.FUNC},
    "ARRAYSIZE": {TokenType.OPENSQBR},
    "REPTVARIABLE0": {TokenType.DOT},
    "INDICE": {TokenType.OPENSQBR},
    "REPTVARIABLE2": {TokenType.OPENSQBR},
    "IDNEST": {TokenType.DOT},
    "REPTVARIABLEORFUNC": {TokenType.DOT},
    "RETURNTYPE": {TokenType.VOID, TokenType.INTEGER, TokenType.FLOAT, TokenType.ID},
    "RIGHTRECARITHEXPR": {TokenType.PLUS, TokenType.MINUS, TokenType.OR},
    "MULTOP": {TokenType.MULT, TokenType.DIV, TokenType.AND},
    "SIGN": {TokenType.PLUS, TokenType.MINUS},
    "START": {TokenType.STRUCT, TokenType.IMPL, TokenType.FUNC},
    "PROG": {TokenType.STRUCT, TokenType.IMPL, TokenType.FUNC},
    "REPTSTATBLOCK1": {TokenType.ID, TokenType.IF, TokenType.WHILE, TokenType.READ, TokenType.WRITE, TokenType.RETURN},
    "RELEXPR": {TokenType.ID, TokenType.INTNUM, TokenType.FLOATNUM, TokenType.OPENPAR, TokenType.NOT, TokenType.PLUS, TokenType.MINUS},
    "STATBLOCK": {TokenType.OPENCUBR, TokenType.ID, TokenType.IF, TokenType.WHILE, TokenType.READ, TokenType.WRITE, TokenType.RETURN},
    "STATEMENT3": {TokenType.DOT, TokenType.ASSIGN},
    "ASSIGNOP": {TokenType.ASSIGN},
    "EXPR": {TokenType.ID, TokenType.INTNUM, TokenType.FLOATNUM, TokenType.OPENPAR, TokenType.NOT, TokenType.PLUS, TokenType.MINUS},
    "STATEMENT4": {TokenType.DOT, TokenType.SEMI},
    "STATEMENT2": {TokenType.OPENPAR, TokenType.DOT, TokenType.OPENSQBR, TokenType.ASSIGN},
    "OPTSTRUCTDECL2": {TokenType.INHERITS},
    "REPTSTRUCTDECL4": {TokenType.PUBLIC, TokenType.PRIVATE},
    "STRUCTORIMPLORFUNC": {TokenType.STRUCT, TokenType.IMPL, TokenType.FUNC},
    "STRUCTDECL": {TokenType.STRUCT},
    "IMPLDEF": {TokenType.IMPL},
    "FUNCDEF": {TokenType.FUNC},
    "TERM": {TokenType.ID, TokenType.INTNUM, TokenType.FLOATNUM, TokenType.OPENPAR, TokenType.NOT, TokenType.PLUS, TokenType.MINUS},
    "FACTOR": {TokenType.ID, TokenType.INTNUM, TokenType.FLOATNUM, TokenType.OPENPAR, TokenType.NOT, TokenType.PLUS, TokenType.MINUS},
    "RIGHTRECTERM": {TokenType.MULT, TokenType.DIV, TokenType.AND},
    "TYPE": {TokenType.INTEGER, TokenType.FLOAT, TokenType.ID},
    "REPTVARDECL4": {TokenType.OPENSQBR},
    "VARDECLORSTAT": {TokenType.LET, TokenType.ID, TokenType.IF, TokenType.WHILE, TokenType.READ, TokenType.WRITE, TokenType.RETURN},
    "VARDECL": {TokenType.LET},
    "STATEMENT": {TokenType.ID, TokenType.IF, TokenType.WHILE, TokenType.READ, TokenType.WRITE, TokenType.RETURN},
    "VARIABLE": {TokenType.ID},
    "VARIABLE2": {TokenType.OPENPAR, TokenType.OPENSQBR, TokenType.DOT},
    "REPTVARIABLE": {TokenType.DOT},
    "VARIDNEST2": {TokenType.OPENPAR, TokenType.OPENSQBR},
    "APARAMS": {TokenType.ID, TokenType.INTNUM, TokenType.FLOATNUM, TokenType.OPENPAR, TokenType.NOT, TokenType.PLUS, TokenType.MINUS},
    "VARIDNEST": {TokenType.DOT},
    "REPTIDNEST1": {TokenType.OPENSQBR},
    "VISIBILITY": {TokenType.PUBLIC, TokenType.PRIVATE}
}
