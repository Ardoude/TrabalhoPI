from fileinput import filename
import utils
import tkinter as tk
from PIL import ImageTk, Image

# Constantes
btnHeight = 1  # Altura padrão dos botões
btnWidth = 20  # Largura padrão dos botões
imgPath = None # Imagem a ser classificada
filename = ""

# Configuração da tela
janela = tk.Tk(className= ' Trabalho Prático - Processamento de Imagens')
janela.geometry("350x500")
    

# Métodos utilitários
def carregarImagem():
    global filename
    filename = utils.browseFiles()
    imgPath = ImageTk.PhotoImage( Image.open(filename).resize( (255, 255), resample=3) )
    labelImagem.config(image = imgPath, height=255, width=255)
    labelImagem.img = imgPath

def calcCaract():
    print(filename)
    utils.entrophy(filename)


# Criação de componentes
titulo = tk.Label(
    text="Trabalho de PI",
    height=2,
    width=10
)
btnTreinarBase = tk.Button(
    text="Treinar Base",
    height= btnHeight,
    width= btnWidth
)
btnAbrirImagem = tk.Button(
    text="Abrir Imagem",
    height= btnHeight,
    width= btnWidth,
    command= carregarImagem
)
btnCalcularCaracteristicas = tk.Button(
    text="Calcular Características",
    height= btnHeight,
    width= btnWidth,
    command=calcCaract
)
btnRecortarImagem = tk.Button(
    text="Recortar Imagem",
    height= btnHeight,
    width= btnWidth
)
btnClassificar = tk.Button(
    text="Classificar Imagem",
    height= btnHeight,
    width= btnWidth
)
labelImagem = tk.Label(
    image=imgPath,
    height=15,
    width=30
)
btnCarregaDiretorio = tk.Button(
    text="Carregar Diretório",
    height= btnHeight,
    width= btnWidth,
)


# Adicionar componentes à tela
titulo.pack()
btnCarregaDiretorio.pack()
btnTreinarBase.pack()
btnAbrirImagem.pack()
btnRecortarImagem.pack()
btnCalcularCaracteristicas.pack()
btnClassificar.pack()
labelImagem.pack()

janela.mainloop()