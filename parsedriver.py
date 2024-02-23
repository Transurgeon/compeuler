from lexer import LexFridman
from paresseux import Paresseux
import os

path = "assignment2/tests/"
for filename in os.listdir(path):
    if filename.endswith(".src"):
        lex = LexFridman(path + filename)
        parser = Paresseux(lex)
        parser.parse()
        # output derivations
        name, _ = filename.split(".")
        fout = open(path + name + ".outderivation", "w")
        fout.write(parser.derivation)
        fout = open(path + name + ".syntaxerrors", "w")
        fout.write(parser.syntaxErrors)