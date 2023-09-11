def decimal_to_binary(n):
    if n == 0:
        return "0"
    else:
        return str(bin(n))[2:]

def decimal_to_octal(n):
    if n == 0:
        return "0"
    else:
        return str(oct(n))[2:]

def decimal_to_hexadecimal(n):
    if n == 0:
        return "0"
    else:
        return hex(n)[2:]

n = int(input("Digite um número decimal: "))
print("Binário: ", decimal_to_binary(n))
print("Octal: ", decimal_to_octal(n))
print("Hexadecimal: ", decimal_to_hexadecimal(n))