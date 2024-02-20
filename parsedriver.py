from lexer import LexFridman
from paresseux import Paresseux
parse = Paresseux(LexFridman("assignment2/tests/polynomial.src"))
parse.parse()