import wibu_lexer
import wibu_parser
import wibu_interpreter

from sys import *

#Dengan masukan .wibu
lexer = wibu_lexer.BasicLexer()
parser = wibu_parser.BasicParser()
env = {}

file = open(argv[1])
text = file.readlines()
for line in text:
    tree = parser.parse(lexer.tokenize(line))
    wibu_interpreter.BasicExecute(tree, env)
