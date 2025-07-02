# CLASSE

class Quadrado:
    '''
    Classe que representa um quadrado.

    Atributos:
        lado (float): Tamanho do lado do quadrado em centímetros.

    Métodos:
        mudar_lado(novo_lado): Altera o valor do lado do quadrado.
        calcular_area(): Retorna a área do quadrado.
        mostrar_lado(): Retorna o valor atual do lado do quadrado.
    '''
    def __init__(self, lado):
        self.lado = lado
        
    def mudar_lado(self, novo_lado):
        self.lado = novo_lado 
    
    def calcular_area(self):
        return self.lado**2  
    
    def mostrar_lado(self):
        return self.lado
    
# FUNÇÃO

def coletandodados():    
    '''
     Função responsável por interagir com o usuário:
     
    - Coleta o valor do lado do quadrado.
    - Mostra a área correspondente.
    - Permite ao usuário atualizar o lado do quadrado.
    '''
    while True:
        try:
            lado_inicial_quadrado = float(input("Qual o lado do quadrado em cm: ").replace(",","."))
            break
        except ValueError:
            print("Entrada inválida! Digite apenas números validos")
            
    O_quadrado = Quadrado(lado_inicial_quadrado)
    print("\n--- Dados do Quadrado ---\n")
    print(f"Lado: {O_quadrado.lado} cm\n Área: {O_quadrado.calcular_area()} cm²")             
    
    while True:
        mudar_lado = str(input("Quer trocar o valor do lado do Quadrado: [S/N]")).strip().upper()
        if mudar_lado == "N":
            print("Encerrando o programa...")
            break
        elif mudar_lado == "S":
            try:
                novo_lado = float(input("Digite o valor do novo lado em cm: ").replace(",","."))
                O_quadrado.mudar_lado(novo_lado)
                print("\n--- Dados do Quadrado Atualizados ---\n")
                print(f"Lado: {O_quadrado.lado} cm\n Área: {O_quadrado.calcular_area()} cm²")       
            except ValueError:
                print("Entrada inválida! Digite apenas números validos")
        else:
            print("Opção inválida. Digite apenas 'S' ou 'N'.")
            continue 
                      
# PROGRAMA PRINCIPAL 

if __name__ == "__main__":
    coletandodados()           