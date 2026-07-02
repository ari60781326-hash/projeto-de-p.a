#a fabrica tá na mesma pasta de gerente de desenhos
from .fabrica_de_figuras import FabricaDeFiguras


class GerenteDeDesenhos:
    '''
    define os desenhos, desenhar é legal quando é voce desenha no papel, 
    mas quando eh voce que faz o papel eh outra historia
'''
    def __init__(self, canvas, gerente_de_cores): #percebi que parte do que tem aqui tinha no main
        self.figuras= []#armazenar figuras
        self.canvas=canvas #os desenhos serao feitos aqui
        self.desenhoatual= None
        self.desenho= 'reta'#padrao, iria preferir que fosse rabisco, talvez troque pra rabisco depois
        self.gerente_de_cores= gerente_de_cores
        
    def iniciar_figura(self, event):
        ...
        
    def update_fig(self,event):
        ...
        
    def incluir_figura_nova(self,event):
        ...
    
    def desenhar_fig (self):
        ...
        
    def desenhar_new_fig (self):
        ...
        
    def clean_all (self):
        ...
