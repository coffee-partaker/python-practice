'''

Welcome to GDB Online.
GDB online is an online compiler and debugger tool for C, C++, Python, Java, PHP, Ruby, Perl,
C#, VB, Swift, Pascal, Fortran, Haskell, Objective-C, Assembly, HTML, CSS, JS, SQLite, Prolog.
Code, Compile, Run and Debug online from anywhere in world.

'''
print ('Python Dictionary')

def agendar_contato (nome, numero):
    __agenda[nome] = numero
    
def pegar_contato_info(info):
    if info in __agenda.values():
        reverse__agenda = {}
        
        for key in __agenda:
            value = __agenda[key]
            reverse__agenda[value] = key
        return reverse__agenda[info]
    
    elif info in __agenda:
        return __agenda[info]
        
    else:
        return 'Informação não cadastrada'
        
def excluir_contato(info):
    try: #Se for uma key
        del __agenda[info]
        return info + ' foi excluído da agenda'
    except:
        try: #Se for value
            key = pegar_contato_info(info)#retorna uma key
            del __agenda[key]
            return key + ' foi excluído da agenda'
        except:#Se não existir
            return "Contato não cadastrado"
    
__agenda = {}  
    
    
nome = "Joao" 
num = "98756-8555"
agendar_contato(nome, num)
agendar_contato("Maria", "98758-3335")

print(__agenda)
print(excluir_contato(num))
print(__agenda)

'''
print(pegar_contato_info(num))
print(pegar_contato_info("Maria"))
#print(pegar_contato_info("Marcelo"))
print(__agenda)
print(excluir_contato(nome))
print(__agenda)
'''

