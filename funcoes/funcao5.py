def somaImposto(taxaImposto, custo):
    valor_imposto = (taxaImposto / 100) * custo
    novo_custo = custo + valor_imposto
    return novo_custo
 
taxa = 10
custo_item = 666
novo_custo = somaImposto(taxa, custo_item)
print(f"O novo custo do item é de: {novo_custo:.2f}")