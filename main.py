# main.py
import lexer
from parser import parse, symbol_table

def test_parser(input_string):
    result = parse(input_string)
    if result:
        print(f"Valid input")
        print(f"Type: {result[0]}, Value: {result[1]}")
        #print(f"Result: {eval(input_string)}")
        print(f"Symbol Table: {symbol_table}")
        print("-" * 20)
    else:
        print("Invalid input")
        print("Parsing failed!")

# Example usage
if __name__ == "__main__":
    #data = input("Enter the data: ")
    test_parser("wak = 2+4")
    test_parser("if wak < 10 hehe = 9999 else hehe = 666666")
    #test_parser(data)
