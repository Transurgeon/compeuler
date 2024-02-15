from lexer import LexFridman
from paresseux import Paresseux
parse = Paresseux(LexFridman("assignment1/tests/test_lexer.src"))
for _ in range(len(parse.lex.tokens)): 
    print(parse.peekToken)
    parse.nextToken()