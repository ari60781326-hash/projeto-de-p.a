class GerenteDeCores:   
    ''' 
    Define as cores das figuras
    '''
    def __init__ (self):
        self.cor_linha= 'black' #cor padrao, pra que seria rosa?
        self.cor_de_preenchimento=''
        
        
    def color_select_outline(self, nova_cor): #cor que o usuario escolheu
        self.cor_linha= nova_cor

    def color_select_fill(self, nova_cor): #cor que o usuario escolheu
        self.cor_de_preenchimento= nova_cor
        
    def wtfIsThisColor (self):
        return self.cor_linha #a cor que vai usar nas figuras
    
    def cor_atual_da_linha (self):
        return self.wtf_is_this_color()

    def cor_atual_do_preenchimento(self):
        return self.cor_linha


#talvez eu volte aqui
        
