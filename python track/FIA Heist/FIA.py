def decode_intercepted_string(s):
    decoded = []
    for char in s:
        if char == "<-" and decoded:
            decoded.pop()
        elif char != "<-":
            decoded.append(char)
    return "".join(decoded)

# Example usage:
intercepted_string = "SmoothhHO<-<-<- OperL<-ator"
decoded_string = decode_intercepted_string(intercepted_string)
print(decoded_string)
