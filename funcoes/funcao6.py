def tabela_loja():
    tabela_precos = []
    preco_unitario = 1.99
   
    for quantidade in range(1, 51):
        valor_conta = quantidade * preco_unitario
        tabela_precos.append((quantidade, valor_conta))
   
    return tabela_precos
 
def imprimir_tabela_precos(tabela_precos):
    for quantidade, valor in tabela_precos:
        print(f"{quantidade:<10} R$ {valor:>10.2f}")
 
tabela = tabela_loja()
imprimir_tabela_precos(tabela)