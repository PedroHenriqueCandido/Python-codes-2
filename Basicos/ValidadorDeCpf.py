def calcular_digito(cpf_base):
  
    soma = 0
    for i in range(len(cpf_base)):
        soma += int(cpf_base[i]) * (len(cpf_base) + 1 - i)
    
    digito = soma % 11
    if digito < 2:
        return 0
    else:
        return 11 - digito

def validar_cpf(cpf):
    
    
  
    cpf = ''.join([caracter for caracter in cpf if caracter.isdigit()])
    
  
    if len(cpf) != 11:
        return False

   
    if not cpf.isdigit():
        return False
    
    if cpf == cpf[0] * 11:
        return False
    

    cpf_base = cpf[:9]  
    digito1 = calcular_digito(cpf_base)
    digito2 = calcular_digito(cpf_base + str(digito1))
    
    
    if cpf[9] == str(digito1) and cpf[10] == str(digito2):
        return True
    else:
        return False

def main():
    cpf = input("Digite o CPF (apenas números ou com pontos e traços): ")
    
    if validar_cpf(cpf):
        print("CPF válido!")
    else:
        print("CPF inválido!")

main() 
