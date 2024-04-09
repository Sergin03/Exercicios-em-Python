#21. Faça um programa que carregue uma lista com os modelos de cinco carros (exemplo de modelos: Porscher, Lande_rover, Honda_Civic, Honda_City, Toyota_Corolla). 
#Carregue uma outra lista com o consumo desses carros, isto é, quantos quilômetros cada um desses carros faz com um litro de combustível. Calcule e mostre:
#O modelo do carro mais econômico;    Quantos litros de combustível cada um dos carros cadastrados consome para percorrer uma distância de 1000 quilômetros e quanto isto custará, 
#considerando um que a gasolina custe R$ 2,25 o litro. Abaixo segue uma tela de exemplo. O disposição das informações deve ser o mais próxima possível ao exemplo. Os dados são fictícios e podem mudar a cada execução do programa.

# Lista dos modelos dos carros abaixo:
modelos = ["Porscher", "Lande_rover", "Honda_Civic", "Honda_City", "Toyota_Corolla"]

# Lista do consumo abaixo (quilômetros por litro): 
consumo = [10, 8, 12, 14, 11]

# Preço da gasolina
preco_gasolina = 2.25

# Calculando o modelo mais economico
indice_mais_economico = consumo.index(max(consumo))
modelo_mais_economico = modelos[indice_mais_economico]

print("O carro de menor consumo é o :", modelo_mais_economico)

print("\nConsumo para percorrer 1000 quilômetros:")
print("========================================")
print("Modelo\t\tLitros\t\tCusto (R$)")

# Calculando o consumo para percorrer 1000 quilômetros para cada carro
for modelo, consumo_carro in zip(modelos, consumo):
    litros_necessarios = 1000 / consumo_carro
    custo = litros_necessarios * preco_gasolina
    print(f"{modelo}\t\t{litros_necessarios:.2f}\t\t{custo:.2f}")