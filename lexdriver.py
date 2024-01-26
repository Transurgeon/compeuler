from lexer import LexFridman

f = open("assignment1/test_lexer.src")
text = f.read()
lex = LexFridman(text)
lex.getTokens()
fout = open("assignment1/test_lexer_tokens.src", "w")
prevLine = 1
for tok in lex.tokens:
    if tok:
        if tok.line != prevLine:
            fout.write("\n" + str(tok))
            prevLine = tok.line
        else:
            fout.write(str(tok))
ferr = open("assignment1/test_lexer_errors.src", "w")
for e in lex.errors:
    ferr.write(e + "\n")
    