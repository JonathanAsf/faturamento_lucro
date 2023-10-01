print("Descubra o faturamento e o lucro de qualquer produto da sua loja")
produto = input("Digite o nome do produto: ")
preco_vendido = float(input("Digite o valor unitário da(o) {} no seu estabelecimento: ".format(produto)))
qtde_venda = int(input("Digite a quantidade de {} que foram vendidas: ".format(produto)))
faturamento =  preco_vendido*qtde_venda
print("O faturamento total do produto foi de: R${}".format(faturamento))
custo = float(input("Digite o valor investido na(o) {}".format(produto)))
lucro = faturamento - custo
if faturamento > custo:
    print("O lucro na venda de {} foi de: R${}".format(produto, lucro))
else:
    print("O prejuízo na venda de {} foi de R$ {}".format(produto,lucro))
