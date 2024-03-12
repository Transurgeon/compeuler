from lexer import LexFridman
from past import Past
import os

path = "assignment3/tests/"
for filename in os.listdir(path):
    if filename.endswith(".src"):
        lex = LexFridman(path + filename)
        parser = Past(lex)
        parser.parse()