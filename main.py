import time

from lark import Lark

print("Checking Grammar on LALR verision")
with open("systemverilog.lark") as f, open("lark.lark") as grammar_f:
    parser = Lark(grammar_f.read(), parser="lalr")
    t0 = time.time()
    parser.parse(f.read())
print("Grammar valid")

# Main Program

with open("test-subject.sv") as f, open("systemverilog.lark") as grammar_f:
    parser = Lark(grammar_f.read(), parser="earley")
    t0 = time.time()
    parser.parse(f.read())
    print(f"Earley Duration: {time.time()-t0}")
    
with open("test-subject.sv") as f, open("systemverilog.lalr.lark") as grammar_f:
    parser = Lark(grammar_f.read(), parser="lalr")
    t0 = time.time()
    parser.parse(f.read())
    print(f"LALR Duration: {time.time()-t0}")
