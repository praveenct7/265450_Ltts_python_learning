from ast import literal_eval

def get_type(input_data):
    try:
        return type(literal_eval(input_data))
    except (ValueError, SyntaxError):
        return str

print(get_type("1")) 
print(get_type("1.2354"))   
print(get_type("True"))     
print(get_type("abcd")) 
print(get_type("2+3j")) 