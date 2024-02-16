from lexer import LexFridman
from paresseux import Paresseux
parse = Paresseux(LexFridman("assignment2/tests/variable-idnest.src"))
for _ in range(len(parse.lex.tokens)): 
    print(parse.currToken)
    parse.nextToken()