# CLASSE

class Bola:
    '''
    Classe que representa uma bola com cor, circunferência e material.

    Atributos:
        cor (str): A cor da bola.
        circunferencia (float): A circunferência da bola em centímetros.
        material (str): O material da bola.

    Métodos:
        trocarcor(nova_cor): Altera a cor da bola.
        mostrarcor(): Retorna a cor atual da bola.
    '''
    def __init__(self, cor, circunferencia, material):
        self.cor = cor
        self.circunferencia = circunferencia
        self.material = material
        
    def trocarcor(self, nova_cor):
        self.cor = nova_cor
        
    def mostrarcor(self):
        return self.cor
        
 # FUNÇÃO           
            
def coletandodados():
    '''
    Coleta os dados necessários para criar uma bola,
    mostra suas características e permite ao usuário trocar a cor se desejar.
    '''
    while True:
        cor_inicial_bola = str(input("Qual a cor da Bola: ")).strip()
        if cor_inicial_bola.isalpha():
            break
        else:
            print("Entrada inválida! Digite apenas letras, sem números ou símbolos.")
            
    while True:    
        try:       
            circunferencia = float(input("Qual a circunferência da bola em cm: ").replace(",","."))
            break
        except ValueError:
            print("Entrada inválida! Digite apenas números validos")
    
    while True:        
        material = str(input("Qual o material da bola: ")).strip()
        if material.isalpha():
            break
        else:
            print("Entrada inválida! Digite apenas letras, sem números ou símbolos.")
            
    A_bola = Bola(cor_inicial_bola, circunferencia, material)
    print("\n--- Dados da Bola ---\n")
    print(f"Cor: {A_bola.cor}\nCircunferência: {A_bola.circunferencia}\nMaterial: {A_bola.material}\n ")
     
    
    while True:                
        trocar_cor = str(input("Quer trocar a cor da bola [S/N]: ")).strip().upper()
        if trocar_cor == "N":
            print("\nEncerrando o programa.")
            break
        elif trocar_cor == "S":
            nova_cor=str(input("Qual a nova cor da bola: "))
            A_bola.trocarcor(nova_cor) 
            print("\n--- Dados da Bola Atualizados ---\n")
            print(f"Cor: {A_bola.cor}\nCircunferência: {A_bola.circunferencia}\nMaterial: {A_bola.material}\n ")  
        else:
            print("Opção inválida. Digite apenas 'S' ou 'N'.")
            continue
        

# PROGRAMA PRINCIPAL 

if __name__ == "__main__":
    coletandodados()        
        
    
                