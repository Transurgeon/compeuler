from lexer import LexFridman
from past import Past
import os

path = "assignment5/tests/"
for filename in os.listdir(path):
    if filename.endswith(".src"):
        lex = LexFridman(path + filename)
        parser = Past(lex)
        parser.parse()
        
### Test files for final project demo
"""
path = "tests/"
for filename in os.listdir(path):
    if filename.endswith(".src"):
        lex = LexFridman(path + filename)
        lex.getTokens()
        lex.outputTokens()
        lex.outputErrors()
        parser = Past(lex)
        parser.parse()
        # output derivations
        name, _ = filename.split(".")
        fout = open(path + name + ".outderivation", "w")
        fout.write(parser.derivation)
        fout = open(path + name + ".syntaxerrors", "w")
        fout.write(parser.syntaxErrors)
"""