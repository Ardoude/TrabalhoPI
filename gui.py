from pickle import FALSE, TRUE
import utils
import tkinter as tk
from tkinter import ACTIVE, DISABLED
from tkinter.filedialog import askdirectory
from PIL import ImageTk, Image

# Constantes
btnHeight = 1  # Altura padrão dos botões
btnWidth = 20  # Largura padrão dos botões
imgSelecionada = None # Imagem a ser classificada
filename = "" # Caminho da imagem selecionada
dirPath = "" # Diretorio com a base a ser treinada
baseTreinada = FALSE

# Configuração da tela
janela = tk.Tk(className= ' Trabalho Prático - Processamento de Imagens')
janela.geometry("350x500")
    

# Métodos utilitários
# Carrega imagem a qual se deseja classificar ou extrair características e a exibe na tela
def carregarImagem():
    global filename
    filename = utils.browseFiles()
    if filename!="":
        imgSelecionada = ImageTk.PhotoImage( Image.open(filename).resize( (255, 255), resample=3) )
        labelImagem.config(image = imgSelecionada, height=255, width=255)
        labelImagem.img = imgSelecionada
        # Ativar botões
        btnCalcularCaracteristicas.config(state=ACTIVE)
        if baseTreinada == TRUE:
            btnClassificar.config(state=ACTIVE)

# Calcular Entropia, Homogeneidade e energia da imagem selecionada
def calcCaract():
    entropia, caracteristicas, tempoGasto = utils.calcCaract(filename, 1)

    #imgProcessada = ImageTk.PhotoImage( Image.open('./teste.png').resize( (255, 255), resample=3) ) # Exibe imagem processada
    # Abrir nova janela para exibir características
    novaJanela = tk.Toplevel(janela)
    novaJanela.title("Características da imagem")
    novaJanela.geometry("400x500")
    tk.Label( novaJanela, text="CARACTERÍSTICAS\n").pack()
    tk.Label( novaJanela, text="Entropia: " + str(entropia)).pack()
    tk.Label( novaJanela, text="Homogeneidade e energia para as 5 matrizes e seus ângulos de rotação\n" + str(caracteristicas)).pack()
    tk.Label( novaJanela, text="Tempo gasto: " + str(round(tempoGasto, 4)) + "s").pack()
    #tk.Label( novaJanela, image=imgProcessada, height=255, width=255).pack() # Exibe imagem processada
    novaJanela.mainloop()

# Carrega caminho do diretório que possui a base a ser treinada
def carregaDiretorio():
    global dirPath
    dirPath = askdirectory(title='Selecione a Pasta')
    if dirPath!="":
        btnTreinarBase.config(state=ACTIVE)

# Treina base de dados
def treinarBase():
    if(dirPath!= ""):
        global baseTreinada
        accuracy, sensibilidade, especificidade, tempoTreino, tempoClassificacao, matrizDeConfusao, tempoProcessamento = utils.treinarBase(dirPath)
        baseTreinada = TRUE

        # Nova janela com dados do treino
        novaJanela = tk.Toplevel(janela)
        novaJanela.title("Informações de classificação")
        novaJanela.geometry("400x500")
        tk.Label( novaJanela, text="CLASSIFICAÇÃO\n").pack()
        tk.Label( novaJanela, text="Accuracy: " + str(accuracy)).pack()
        tk.Label( novaJanela, text="Sensibilidade: " + str(sensibilidade)).pack()
        tk.Label( novaJanela, text="Especificidade: " + str(especificidade)).pack()
        tk.Label( novaJanela, text="Tempo de treino: " + str(round(tempoTreino, 4)) + "s").pack()
        tk.Label( novaJanela, text="Tempo gasto classificando: " + str(round(tempoClassificacao, 4)) + "s").pack()
        tk.Label( novaJanela, text="Tempo gasto extraindo informações da base: " + str(round(tempoProcessamento, 3)) + "s").pack()
        tk.Label( novaJanela, text="Matriz de Confusão\n" + str(matrizDeConfusao)).pack()
        # Ativar botões
        if filename!="":
            btnClassificar.config(state=ACTIVE)
        novaJanela.mainloop()
        
# Classifica imagem selecionada com base no dataset treinado
def classificar():
    classe = utils.classificarImagem(filename)
    classificacao.config(text="Classe: "+ str(classe))


# Criação de componentes

titulo = tk.Label(
    text="Trabalho de PI",
    height=2,
    width=10
)
btnTreinarBase = tk.Button(
    text="Treinar Base",
    height= btnHeight,
    width= btnWidth,
    state= DISABLED,
    command= treinarBase
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
    state= DISABLED,
    command=calcCaract
)
btnRecortarImagem = tk.Button(
    text="Recortar Imagem",
    height= btnHeight,
    width= btnWidth,
    state= DISABLED
)
btnClassificar = tk.Button(
    text="Classificar Imagem",
    height= btnHeight,
    width= btnWidth,
    state= DISABLED,
    command= classificar
)
labelImagem = tk.Label(
    image=imgSelecionada,
    height=15,
    width=30
)
btnCarregaDiretorio = tk.Button(
    text="Carregar Diretório",
    height= btnHeight,
    width= btnWidth,
    command = carregaDiretorio
)
classificacao = tk.Label(
    text="",
    height=2,
    width=10
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
classificacao.pack()

janela.mainloop()