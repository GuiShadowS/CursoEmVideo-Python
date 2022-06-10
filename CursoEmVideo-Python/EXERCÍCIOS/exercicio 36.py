# -*- coding: utf-8 -*-

'''
EXERCÍCIO 36
Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.
'''
# Recebe do usuário o valor da casa
vcasa = int(input("Digite o valor da casa: "))

# Recebe do usuário o valor do salário
salario = int(input("Digite o valor do salario: "))

# Recebe do usuário a quantidade em anos para pagar a casa
tempo = int(input("Tempo em anos para pagar: "))

# Calcula quanto sera o valor da parcela
parcela = vcasa / (tempo * 12)

# Calcula quanto será 30% do salário informado
renda = salario * 0.30

# Mostra na tela o valor da casa, o valor da prestação e em quantos anos será financiada
print("Para pagar uma casa de R$%.2f em %d anos, a prestação será de R$%.2f" %(vcasa, tempo, parcela))

# Bloco que verifica se os 30% do salario é menor ou igual o valor da parcela
if renda >= parcela:
    # Se for menor ou igual o emprestimo é aprovado
    print("Empréstimo pode ser concedido")
else:
    # Senão o emprestimo é cancelado
    print("Empréstimo negado")