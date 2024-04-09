##Classe Ponto e Retangulo: Faça um programa completo utilizando funções e classes que:
    #a. Possua uma classe chamada Ponto, com os atributos x e y.
    #b. Possua uma classe chamada Retangulo, com os atributos largura e altura.
    #c. Possua uma função para imprimir os valores da classe Ponto
    #d. Possua uma função para encontrar o centro de um Retângulo.
    #e. Você deve criar alguns objetos da classe Retangulo.
    #f. Cada objeto deve ter um vértice de partida, por exemplo, o vértice inferior esquerdo do retângulo, que deve ser um objeto da classe Ponto.
    #g. A função para encontrar o centro do retângulo deve retornar o valor para um objeto do tipo ponto que indique os valores de x e y para o centro do objeto.
    #h. O valor do centro do objeto deve ser mostrado na tela
    #i. Crie um menu para alterar os valores do retângulo e imprimir o centro deste retângulo. 

class Ponto:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def imprimir(self):
        print("Ponto: (", self.x, ",", self.y, ")")
        
class Retangulo:
    def __init__(self, largura, altura, ponto_inicial):
        self.largura = largura
        self.altura = altura
        self.ponto_inicial = ponto_inicial
        
    def encontrar_centro(self):
        x_centro = self.ponto_inicial.x + self.largura / 2
        y_centro = self.ponto_inicial.y + self.altura / 2
        return Ponto(x_centro, y_centro)
    
    def imprimir_centro(self):
        centro = self.encontrar_centro()
        print("Centro do retângulo:")
        centro.imprimir()


def criar_retangulo():
    largura = float(input("Digite a largura do retângulo: "))
    altura = float(input("Digite a altura do retângulo: "))
    x = float(input("Digite a coordenada x do vértice inferior esquerdo: "))
    y = float(input("Digite a coordenada y do vértice inferior esquerdo: "))
    ponto_inicial = Ponto(x, y)
    return Retangulo(largura, altura, ponto_inicial)

def menu():
    print("\nMenu:")
    print("1. Criar retângulo")
    print("2. Imprimir centro do retângulo")
    print("0. Sair")

def main():
    retangulo = None
    while True:
        menu()
        escolha = input("Escolha uma opção: ")
        
        if escolha == '1':
            retangulo = criar_retangulo()
        elif escolha == '2':
            if retangulo:
                retangulo.imprimir_centro()
            else:
                print("Crie um retângulo primeiro.")
        elif escolha == '0':
            print("Encerrando o programa...")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()