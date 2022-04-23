print("Digite o comprimento da pista (em metros)! ")
distancia =float(input())
print("Digite o  número total de voltas a serem percorridas no grande prêmio!")
voltas =float(input())
distancia_total= distancia*voltas
print("Digite o   número de reabastecimentos desejados!")
n_abastacimentos = float(input())
print("Digite o consumo de combustível do carro em Km/L") 
consumo = float(input())

distancia_abastecimento_1= (distancia_total/1000)/n_abastacimentos
litro_min= distancia_abastecimento_1/consumo
print("O número mínimo de litros necessários para percorrer até o primeiro reabastecimento é", litro_min)