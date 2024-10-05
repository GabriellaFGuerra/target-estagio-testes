
def fibonacci(num):
    if num == 0:
        return 0
    if num == 1:
        return 1
    
    return fibonacci(num - 1) + fibonacci(num - 2)

if __name__ == "__main__":
    num = int(input("Digite um número para a sequência de Fibonacci: "))
    print(f"O número {num} na sequência de Fibonacci é: {fibonacci(num)}")
