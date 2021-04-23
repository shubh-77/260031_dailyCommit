from ast import literal_eval

def get_datatype(input_data):
    try:
        return type(literal_eval(input_data))
    except (ValueError, SyntaxError):
        # catch exception and return string
        return str

print(get_datatype("7"))        # prints <class 'int'>
print(get_datatype("3.142"))   # prints <class 'float'>
print(get_datatype("False"))     # prints <class 'bool'>
print(get_datatype("xyz")) 
print(get_datatype("6+9j")) 