from tkinter import filedialog
import classificador
import numpy as np
from skimage import io, color, img_as_ubyte
from skimage.feature import graycomatrix, graycoprops
import skimage.measure
from PIL import Image
import os
import glob
import cv2
import time

grayImg = None

# Abre o explorador de arquivos em busca da imagem
def browseFiles():
    filename = filedialog.askopenfilename(initialdir = "/", 
                                            title = "Select a File", 
                                            filetypes = (
                                                ( "all files", "*.*" ),
                                                ( "Text files", "*.txt*") 
                                            )
                                        )
    return filename

# Calcula entropia da imagem juntamente com a energia e homogeneidade para 4 ângulos de cada uma das 5 matrizes de co-corrência(C1, C2, C4, C8 e C16)
def calcCaract(img, details):
    global grayImg
    # Converte para tons de cinza
    rgbImg = io.imread(img)
    tempoInicial = time.time()
    if len(rgbImg.shape) == 2: #Já está em tom de cinza
        grayImg = img_as_ubyte(rgbImg)
    else:
        rgbImg = cv2.cvtColor(rgbImg, cv2.COLOR_BGR2HSV)
        grayImg = img_as_ubyte(color.rgb2gray(rgbImg))

    io.imsave("./auxImg.png", grayImg)
    grayImg = Image.open('auxImg.png').quantize(32)
    entropy = (skimage.measure.shannon_entropy(grayImg))

    # Definir características a serem calculadas
    distances = [1, 2, 4, 8, 16] # Matrizes de co-ocorrencia
    angles = [0, np.pi/4, np.pi/2, 3*np.pi/4] # 0°, 45°, 90° e 135°
    properties = ['energy', 'homogeneity']

    # Calcula matrizes de co-ocorrencia
    glcm = graycomatrix(grayImg, 
                        distances=distances, 
                        angles=angles,
                        symmetric=True,
                        normed=True)

    # Calcula propriedades da textura e concatena em um array
    feats = np.hstack([graycoprops(glcm, prop).ravel() for prop in properties])
    tempoFinal = time.time()

    os.remove('./auxImg.png') # Apagar imagem
    if details==0:
        return feats
    else:
        return entropy, feats, (tempoFinal-tempoInicial)
    
# Treinar base
def treinarBase(path):
    data = []
    target = []
    subpastas = os.listdir(path) # Pastas onde se encontram os arquivos a serem usados no treino
    #print(subpastas)
    tInicial = time.time()
    for pasta in subpastas: # Percorrer imagens e extrair informação
        caminho = path + "/" + pasta
        for file in glob.glob(caminho + "/*.png"): # Obter os arquivos .png
            caracteristicas = calcCaract(file, 0)
            data.append(caracteristicas)
            target.append(int(pasta))
        print("Pasta " + pasta + " carregada")
    print("Base carregada")
    tempoProcessamento = time.time() - tInicial
    # Enviar dados para o classificador
    classificador.carregarBase(data, target)

    # Treinar base e obter resultados
    accuracy, sensibilidade, especificidade, tempoTreino, tempoClassificacao, matrizDeConfusao = classificador.treinarBase()
    return accuracy, sensibilidade, especificidade, tempoTreino, tempoClassificacao, matrizDeConfusao, tempoProcessamento


def classificarImagem(filename):
    return classificador.classificar(calcCaract(filename, 0))