'''

Welcome to GDB Online.
GDB online is an online compiler and debugger tool for C, C++, Python, Java, PHP, Ruby, Perl,
C#, VB, Swift, Pascal, Fortran, Haskell, Objective-C, Assembly, HTML, CSS, JS, SQLite, Prolog.
Code, Compile, Run and Debug online from anywhere in world.

'''
print("Bem vindo ao Conversor Decimal-Binário versão de fábrica!!!")
string = input("Digite um numero Decimal: ")

if string[0] == '-':
    valor = 1
    
else:
    valor = 0
    
try:
    string = string.replace('-', '')
    num = int(string)

except: 
    print("Erro: Não foi fornecido um número válido")
    
else:
    if num == 0:
        lista.append(num)
    
    else:
        quo = int (num)
        lista = []
        while(quo != 1):
            quo = quo // 2
            lista.append(num % 2)
    
    lista.append(quo)
    lista.reverse()
    print("O primeiro bit representa o sinal")
    lista.insert(0, valor)
    print(lista)
