from lexer import LexFridman
from paresseux import Paresseux
parse = Paresseux(LexFridman("assignment2/tests/thanos-sort.src"))
parse.parse()