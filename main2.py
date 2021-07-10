import wibu_lexer
import wibu_parser
import wibu_interpreter

from sys import *

#masukan langsung
if __name__ == '__main__':
    lexer = wibu_lexer.BasicLexer()
    parser = wibu_parser.BasicParser()
    env = {}

    while True:
        try:
            text = input('wibu > ')
        except EOFError:
            break
        if text:
            tree = parser.parse(lexer.tokenize(text))
            wibu_interpreter.BasicExecute(tree, env)
