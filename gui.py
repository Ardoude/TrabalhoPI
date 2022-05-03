import tkinter as tk
from PIL import ImageTk, Image 

# Constantes
btnHeight = 1
btnWidth = 20
imgPath = ""

# Configuração da tela
janela = tk.Tk(className= ' Trabalho Prático - Processamento de Imagens')
janela.geometry("800x600")

# Criação de componentes
titulo = tk.Label(
    text="Trabalho de PI",
    height=2,
    width=10
)
btnCarregaDiretorio = tk.Button(
    text="Carregar Diretório",
    height= btnHeight,
    width= btnWidth
)
btnTreinarBase = tk.Button(
    text="Treinar Base",
    height= btnHeight,
    width= btnWidth
)
btnAbrirImagem = tk.Button(
    text="Abrir Imagem",
    height= btnHeight,
    width= btnWidth
)
btnCalcularCaracteristicas = tk.Button(
    text="Calcular Características",
    height= btnHeight,
    width= btnWidth
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
    text="Imagem",
    image = imgPath,
    bg="green",
    height=15,
    width=30
)

#image1 = Image.open(imgPath)

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