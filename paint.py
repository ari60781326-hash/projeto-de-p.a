from tkinter import ttk
from tkinter import *
import sys
import os # imagem de icone
import tkinter.colorchooser as colorchooser  # cores

# por enquanto, quadrado == retangulo

# inicia a figura / quando o mouse é pressionado
def iniciar_figura(event):
    global new_fig, ini_x, ini_y
    
    ini_x = event.x
    ini_y = event.y 
    
    if tipo_fig_var.get() == "Reta":
        new_fig  = ("Reta", (event.x, event.y, event.x, event.y))
    
    elif tipo_fig_var.get() == "Circulo":
        new_fig  = ("Circulo", (event.x, event.y, 0))
        
    elif tipo_fig_var.get() == "Elipse":
        new_fig  = ("Elipse", (event.x, event.y, 0))
        
    elif tipo_fig_var.get() == "Quadrado":
        new_fig  = ("Quadrado", (event.x, event.y, event.x, event.y))
    
    else:
        new_fig = ("Rabisco", [(event.x, event.y)])

# quando continua pressionando o mouse
def update_fig(event):
    global new_fig, fim_x, fim_y, raio
    
    fim_x = event.x
    fim_y = event.y
    
    if new_fig[0] == "Rabisco": # desenha em "mão livre"
        new_fig[1].append((event.x, event.y))
        
    elif new_fig[0] == "Circulo": # cria circulo
        raio = ( (ini_x - fim_x)**2 + (ini_y - fim_y)**2 ) ** 0.5
        new_fig = ('Circulo', (ini_x, ini_y, raio))
        
    elif new_fig[0] == "Elipse": # cria elipse
        new_fig = ('Elipse', (new_fig[1][0],
                                new_fig[1][1],
                                event.x, event.y))
        
    elif new_fig[0] == "Quadrado": # cria quadrado
        new_fig = ('Quadrado', (new_fig[1][0],
                                new_fig[1][1],
                                event.x, event.y))
        
    elif new_fig[0] == "Reta": # cria reta
        new_fig = ("Reta", (new_fig[1][0],
                             new_fig[1][1], 
                             event.x, event.y))
    desenhar_fig()
    desenhar_new_fig()
 
 # quando solta o mouse
 
def incluir_figura_nova(event): 
    if not incompleta(new_fig): # para evitar incluir figuras incompletas, como uma Reta sem comprimento ou um rabisco com um único ponto
        figuras.append((new_fig, cor_borda, cor_preenchimento)) # salva a figura junto com a cor
    desenhar_fig()

def desenhar_fig():
    canvas.delete("all")
    # desmembra figuras
    for figura_info, c_borda, c_preenchimento in figuras:
        fig, values = figura_info
        if fig == "Reta":
            canvas.create_line(values[0], values[1], values[2], values[3], fill=c_borda)
        
        elif fig == 'Circulo':
            x, y, r = values
            canvas.create_oval(x-r, y-r, x+r, y+r, outline=c_borda, fill=c_preenchimento)

        elif fig == 'Elipse':
            canvas.create_oval(values[0], values[1], values[2], values[3], outline=c_borda, fill=c_preenchimento)
            
        elif fig == 'Quadrado':
            canvas.create_rectangle(values[0], values[1], values[2], values[3], outline=c_borda, fill=c_preenchimento)
        
        else : # fig == "Rabisco"
            canvas.create_line(values, fill=c_borda)

def desenhar_new_fig():
    global cor_preenchimento, cor_borda
    fig, values = new_fig
    if fig == "Reta":
        canvas.create_line(values[0], values[1], values[2], values[3], dash=(4, 2), fill=cor_borda)
        
    elif fig == 'Circulo':
        x, y, r= values
        canvas.create_oval(x-r, y-r, x+r, y+r, outline=cor_borda, fill=cor_preenchimento, dash=(4, 2))

    elif fig == 'Elipse':
        canvas.create_oval(values[0], values[1], values[2], values[3], outline=cor_borda, fill=cor_preenchimento, dash=(4, 2))
            
    elif fig == 'Quadrado':
        canvas.create_rectangle(values[0], values[1], values[2], values[3], outline=cor_borda, fill=cor_preenchimento, dash=(4, 2))
            
    else : # fig == "Rabisco"
        canvas.create_line(values, dash=(4, 2), fill=cor_borda)

def incompleta(figura):
    fig, values = figura
    if fig == "Reta" or fig == 'Quadrado' or fig == 'Elipse':
        return (values[0], values[1]) == (values[2], values[3])
    
    elif fig == 'Circulo':
        return values[2] == 0 # se o raio for 0, está incompleta
    
    else : # fig == "rabisco"
        return len(values) <= 1




        
# tamanho da Reta ------> canvas.itemconfig(fig, width= tamanho), sendo esse tamanho int


# paleta de cores
def selct_cor_borda():
    cor_escolhida = colorchooser.askcolor(title="Escolha uma cor para a Borda")[1] or cor_borda

    cor_padrao(cor_escolhida, 'borda')
    print(f'Cor da Borda: {cor_escolhida}')

def selct_cor_preenchimento():
    cor_escolhida = colorchooser.askcolor(title="Escolha uma cor para o Preenchimento")[1] or cor_preenchimento
    
    cor_padrao(cor_escolhida, 'preenchimento')
    print(f'Cor do Preenchimento: {cor_escolhida}')

def remover_preenchimento():
    global cor_preenchimento
    cor_preenchimento = '' # String vazia. Retira a cor interna

def cor_padrao(cor_selecionada, tipo= 'borda'):
    global cor_borda, cor_preenchimento #pra poder alterar as cores independentes
    if tipo == 'borda':
        cor_borda = cor_selecionada
        print(f'Cor da Borda:{cor_selecionada}')
        
    elif tipo == 'preenchimento':
        cor_preenchimento = cor_selecionada
        print(f'Cor do Preenchimento:{cor_selecionada}')


def limpar_tela():
    global figuras
    figuras.clear()
    canvas.delete("all")
    print("Tela limpa")




 #----------main------------#
figuras = []       # Todas as figuras desenhadas
cor_borda = 'black' # cor da borda
cor_preenchimento = '' # cor do preenchimento da figura -> iniciando transparente/sem prenchimento
cores = ["red", "green", "blue", "yellow", "orange",
          "brown", "pink", "black", "white"]
new_fig = None # Figura que está sendo desenhada, mas ainda não foi incluída em figuras
raio = None


root = Tk()
frame = Frame(root)

# Personalização da janela
root.title("Paint CAR") # Título/Nome do app/janela
#root.iconbitmap('icon') # Ícone do app/janela (colocar)

# Widgets arranjados com Layout grid dentro de frame
paddings = {'padx': 5, 'pady': 5} 

# label
label = Label(frame,  text='Figuras:')
label.grid(column=0, row=0, sticky=W, **paddings)

# option menu
tipo_fig_var = StringVar(root) # Guarda o tipo de figura selecionado no option menu
option_menu = OptionMenu(frame, tipo_fig_var,
                             'Reta', 'Rabisco', 'Circulo', 'Quadrado', 'Elipse')
option_menu.grid(column=1, row=0, sticky=W, **paddings)

frame_menu = Frame(root, bg="gray", pady=25)
frame_menu.pack(fill=X)

# subframe cores
frame_cores = Frame(frame_menu, bg="lightgray")
frame_cores.pack(side=LEFT, padx=10)

for i, cor in enumerate(cores):
    btao = Button(
        frame_cores,
        bg=cor,
        width=2,
        height=1,
    )
    btao.grid(row=0, column=i, padx=2)
    # Botão Esquerdo define borda
    btao.bind('<Button-1>', lambda event, cor_clicada=cor: cor_padrao(cor_clicada, "borda"))
    # Botão Direito define fundo
    btao.bind('<Button-3>', lambda event, cor_clicada=cor: cor_padrao(cor_clicada, "preenchimento"))

# botao escolher cor da borda
botao_paleta = Button(frame_menu, text="Cor da Borda", command=selct_cor_borda)
botao_paleta.pack(side=LEFT, padx=10)

# botao escolher cor do preenchimento
botao_paleta_p = Button(frame_menu, text="Cor de Fundo", command=selct_cor_preenchimento)
botao_paleta_p.pack(side=LEFT, padx=10)

# botao limpar tela
botao_limpar = Button(frame_menu, text="Limpar tela", command=limpar_tela)
botao_limpar.pack(side=LEFT, padx=10)


# Área de desenho
canvas = Canvas(frame, bg='white', width=1200, height=800)
canvas.grid(column=0, row=1, columnspan=2, sticky=W, **paddings)

frame.pack()
ini_x = None
ini_y = None
fim_x = None
fim_y = None


# o que acontece quando o mouse interage com o canvas      
canvas.bind('<ButtonPress-1>', iniciar_figura)
canvas.bind('<B1-Motion>', update_fig)
canvas.bind('<ButtonRelease-1>', incluir_figura_nova)       





root.mainloop()
