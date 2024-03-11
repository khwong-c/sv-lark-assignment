# How to work with this?

## Prepare the environment

```
git clone ...
cd ...
python3 -m virtualenv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Run the demo

```
python demo.py
> Earley Duration: 3.2321507930755615
> LALR Duration: 0.07520771026611328
```

## Objective:
1. Edit `systemverilog.lalr.lark` to enable "LALR" Parsing Algorithm
2. Run `python main.py` and ensure the LARK parser can handle the test code with the "LALR" algorithm.
3. Don't change the `test-subject.sv` file.

