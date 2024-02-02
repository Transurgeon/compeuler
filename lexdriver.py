from lexer import LexFridman
import os

path = "assignment1/tests/"
for filename in os.listdir(path):
    if filename.endswith(".src"):
        lex = LexFridman(path + filename)
        lex.getTokens()
        lex.outputTokens()
        lex.outputErrors()