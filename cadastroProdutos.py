# Inicialização das variáveis para contagem de produtos e valores
total = totmil = menor = maior = cont = 0
precomil = 0  # Total gasto com produtos que custam mais de R$1000
barato = " "  # Nome do produto mais barato
caro = " "    # Nome do produto mais caro

# Laço principal para cadastro de vários produtos
while True:
    # Solicita o nome do produto e o valor
    prod = str(input("Nome do produto: "))
    cont += 1  # Conta o número de produtos cadastrados
    preco = float(input("Valor do produto: "))
    total += preco  # Acumula o valor total gasto com os produtos

    # Verifica se o produto custa mais de R$1000 e contabiliza
    if preco >= 1000:
        precomil += preco
        totmil += 1

    # Inicializa a comparação para o primeiro produto
    if cont == 1:
        menor = preco  # A primeira vez, o produto é o mais barato
        barato = prod  # A primeira vez, o produto é o mais barato
        maior = preco  # A primeira vez, o produto é o mais caro
        caro = prod    # A primeira vez, o produto é o mais caro
    else:
        # Verifica se o preço do produto é o menor ou o maior
        if preco < menor:
            menor = preco  # Atualiza o menor preço
            barato = prod  # Atualiza o nome do produto mais barato
        if preco > maior:
            maior = preco  # Atualiza o maior preço
            caro = prod    # Atualiza o nome do produto mais caro

    # Pergunta se o usuário deseja continuar o cadastro
    resp = " "
    while resp not in "SN":
        resp = str(input("Quer continuar? [S/N]")).strip().upper()[0]
    
    # Se a resposta for "N", encerra o laço
    if resp == "N":
        break

# Exibe as informações do cadastro final
print(f"O produto {barato} é o mais barato e custou R${menor:.2f}")
print(f"O produto {caro} é o mais caro e custou R${maior:.2f}")
print(f"{totmil} produtos custaram mais de R$1000.00")
print(f"Esses {totmil} produtos deram um total de R${precomil:.2f}")
print(f"Total: R${total:.2F}")
print("{:-^40}".format(" FIM DO PROGRAMA!"))