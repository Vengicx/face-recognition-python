import numpy as np
import cv2

cap = cv2.VideoCapture(0)

def make_1080p():
    cap.set(3, 1920)
    cap.set(4, 1080)

def make_720p():
    cap.set(3, 1280)
    cap.set(4, 720)

def make_480p():
    cap.set(3, 640)
    cap.set(4, 480)

def change_res(width, height):
    cap.set(3, width)
    cap.set(4, height)

def rescale_frame(frame, percent=75): #funcao para deixar a janela da camera com certo tamanho
    scale_percent = 75
    width = int(frame.shape[1] * scale_percent / 100)
    height = int(frame.shape[0] * scale_percent / 100)
    dim = (width, height)
    return cv2.resize(frame, dim, interpolation = cv2.INTER_AREA)
# make_1080p() # abre o frame com imagem em 1080p (se a webcam suportar)
# make_720p() # abre o frame com imagem em 720p (se a webcam suportar)
# make_480p() # abre o frame com imagem em 480p (se a webcam suportar)
# change_res(4000, 2000) #deixa a resolução no tamanho desejado (no caso, width: 4000 e height: 2000)

while True:
    ret, frame = cap.read()
    frame = rescale_frame(frame, percent=30) #vai deixar com 30% do tamanho
    cv2.imshow('frame', frame) #imgshow

    #segunda janela para comparar o tamanho com a primeira
    frame2 = rescale_frame(frame, percent=80) #vai deixar com 80% do tamanho
    cv2.imshow('frame2', frame2) #imgshow
    
    if cv2.waitKey(20) & 0xFF == ord('q'):
        break
