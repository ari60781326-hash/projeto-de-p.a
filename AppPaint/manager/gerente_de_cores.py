class GerenteDeCores:   
    ''' 
    Define as cores das figuras
    '''
    def __init__ (self):
        self.cor_linha= 'black' #cor padrao, pra que seria rosa?
        self.cor_de_preenchimento=''
        
        
    def color_select_outline(self, novaCor): #cor que o usuario escolheu
        self.cor_linha= novaCor

    def color_select_fill(self, novaCor): #cor que o usuario escolheu
        self.cor_de_preenchimento= novaCor
        
    def wtfIsThisColor (self):
        return self.cor_linha #a cor que vai usar nas figuras
    
    def cor_atual_da_linha (self):
        return self.wtfIsThisColor()

    def cor_atual_do_preenchimento(self):
        return self.cor_linha


#talvez eu volte aqui
        
