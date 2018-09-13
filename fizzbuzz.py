a = [1, 2, 3]
b = ["a"]


def fizzbuzz(a, b):
    if type(a) == int and type(b) == int:
        return "Invalid input"
    
    if type(b) == int:
        return "Invalid input"
    
    combined_length = len(a) + len(b)
    
    if combined_length % 3 == 0 and combined_length % 5 == 0:
        return "fizzbuzz"
    
    if combined_length % 3 == 0:
        return "fizz"
    
    if combined_length % 5 == 0:
        return "buzz"
    else:
        return combined_length

print(fizzbuzz(a, b))
