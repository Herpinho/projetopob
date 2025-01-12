
import cv2
import numpy as np
import tkinter as tk
from tkinter import filedialog
from deepface import DeepFace
import os
recognizer = cv2.face.LBPHFaceRecognizer_create()
def treino():
    retratos_treino = [
                    cv2.imread("Fotos de Treino/MD1.jpg",cv2.IMREAD_GRAYSCALE),
                    cv2.imread("Fotos de Treino/MD2.jpg",cv2.IMREAD_GRAYSCALE),
                    cv2.imread("Fotos de Treino/MD3.jpg",cv2.IMREAD_GRAYSCALE),
                    cv2.imread("Fotos de Treino/MD4.jpg",cv2.IMREAD_GRAYSCALE),
                    cv2.imread("Fotos de Treino/MD5.jpg",cv2.IMREAD_GRAYSCALE),
                    cv2.imread("Fotos de Treino/ML1.jpg",cv2.IMREAD_GRAYSCALE),
                    cv2.imread("Fotos de Treino/ML2.jpg",cv2.IMREAD_GRAYSCALE),
                    cv2.imread("Fotos de Treino/ML3.jpg",cv2.IMREAD_GRAYSCALE),
                    cv2.imread("Fotos de Treino/ML4.jpg",cv2.IMREAD_GRAYSCALE),
                    cv2.imread("Fotos de Treino/ML5.jpg",cv2.IMREAD_GRAYSCALE),

                    ]
    labels = [0,0,0,0,0,1,1,1,1,1]

    retratos_treino = [np.asarray(img) for img in retratos_treino]
    labels = np.array(labels)
    recognizer.train(retratos_treino, np.array(labels))

def selecionar_foto():
    root = tk.Tk()
    root.withdraw()
    ficheiro = filedialog.askopenfilename(
        title="Selecione uma foto sua",
        filetypes=[("Image Files","*.jpg *.jpeg *.png *.bmp")]
    )
    if ficheiro: 
        return ficheiro
    else: return False
def reconhecimento_facial(ficheiro):
        imagem = cv2.imread(ficheiro,cv2.IMREAD_GRAYSCALE)
        label, confidence = recognizer.predict(imagem)
        print(label)
        match label:
            case 0:
                label = "Miguel Duarte"
            case 1:
                label = "Miguel Lança"
        return label,confidence
def reconhecimento_emocao(ficheiro):
        emocao = DeepFace.analyze(img_path=ficheiro,actions=['emotion'])
        match emocao[0]['dominant_emotion']:
            case 'sad':
                emocao_sujeito = 'Triste'
            case 'happy':
                emocao_sujeito = 'Feliz'
            case 'disgust':
                emocao_sujeito = 'Nojo/a'
            case 'fear':
                emocao_sujeito = 'Medo'
            case 'surprise':
                emocao_sujeito = 'Surpreso/a'
            case 'neutral':
                emocao_sujeito = 'Neutro/a'
            case 'angry':
                emocao_sujeito = 'Chateado/a'
        return emocao_sujeito,emocao[0]['emotion'][emocao[0]['dominant_emotion']]
def pixelizacao(foto ,pixel_size = 15):
    foto = cv2.imread(foto)
    return cv2.resize(cv2.resize(foto, (foto.shape[1] // pixel_size, foto.shape[0] // pixel_size)), (foto.shape[1], foto.shape[0]), interpolation=cv2.INTER_NEAREST)