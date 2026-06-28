# Exercício: desenhar círculos.
#  O centro é a posição onde o mouse foi clicado
#  O raio é definido pela distância entre o centro e a posição atual do mouse

from tkinter import *
from tkinter import ttk

# Quando o mouse é pressionado
def inicia_linha(event):
    global ini_x, ini_y
    ini_x = event.x
    ini_y = event.y

# Quando o mouse é movido com o botão pressionado
def atualiza_linha(event):
    global fim_x, fim_y, raio
    fim_x = event.x
    fim_y = event.y
    desenhar()
    raio = ( (ini_x - fim_x)**2 + (ini_y - fim_y)**2 ) ** 0.5
    canvas.create_oval(ini_x-raio, ini_y-raio, ini_x+raio, ini_y+raio)
    canvas.create_rectangle(ini_x, ini_y//2, ini_x//2, ini_y)
    canvas.create_rectangle(ini_x, ini_y, ini_x,ini_y)
    
# Quando o mouse é solto
def incluir_linha(event):
    circulos.append((ini_x, ini_y, raio))
    retangulos.append((ini_x, ini_y))
    quadrados.append((ini_x,ini_y))
    
    
def desenhar():
    canvas.delete("all")
    for circulo in circulos:
        x, y, r = circulo
        canvas.create_oval(x-r, y-r, x+r, y+r)
    
    for retangulo in retangulos:
        x, y= retangulo
        canvas.create_rectangle(x,y//2,x//2,y)
        
    for quadrado in quadrados:
        x, y= quadrado
        canvas.create_rectangle(x,y,x,y)


#******* MAIN *******#

# Todas figuras geometricas desenhadas são armazenadas aqui
circulos = []
raio = None
retangulos= []
quadrados= []
root = Tk()
frame= Frame(root)

# Widgets arranjados com Layout grid dentro de frame
paddings = {'padx': 5, 'pady': 5} 

# label
label = ttk.Label(frame,  text='circulo ou retangulo:')
label.grid(column=0, row=0, sticky=W, **paddings)


tipo_figura_var = StringVar(root) # Guarda o tipo de figura selecionado no option menu (circulo ou quadrado)
option_menu = ttk.OptionMenu(frame, tipo_figura_var,
                             'circulo', 'retangulo')
option_menu.grid(column=1, row=0, sticky=W, **paddings)

canvas = Canvas(root, bg='white', width=600, height=600)
canvas.grid(column=0, row=1, columnspan=2, sticky=W, **paddings)



canvas.pack()

ini_x = None
ini_y = None
fim_x = None
fim_y = None
canvas.bind('<ButtonPress-1>', inicia_linha)
canvas.bind('<B1-Motion>', atualiza_linha)
canvas.bind('<ButtonRelease-1>', incluir_linha)

root.mainloop()
