# Informe um valor e veja quanto de desconto você terá em R$, receba a % do desconto que quer receber;

valor = float(input("digite o valor em reais:"))
desconto = float(input("Digite a '%' de desconto:"))

des = (valor * desconto) / 100
result = valor-desconto
print(f"""
        Valor de Desconto: {des}
        Valor Final: {result} 
""")