def verificaString(string):
    string = string.lower()  
    count = string.count('a')  
    return count

string = input("Informe uma string: ")
qtd = verificaString(string)
if qtd > 0:
    print(f"A letra 'a' aparece {qtd} vezes.")
else:
    print("A letra 'a' não aparece na string.")
