import time
from lark import Lark

with open("systemverilog.lark") as f, open("lark.lark") as grammar_f:
    parser = Lark(grammar_f.read(), parser="earley")
    t0 = time.time()
    parser.parse(f.read())
    print(f"Earley Duration: {time.time()-t0}")
    
with open("systemverilog.lark") as f, open("lark.lark") as grammar_f:
    parser = Lark(grammar_f.read(), parser="lalr")
    t0 = time.time()
    parser.parse(f.read())
    print(f"LALR Duration: {time.time()-t0}")
