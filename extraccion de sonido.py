# -*- coding: utf-8 -*-
"""
UNIVERSIDAD AUTÓNOMA DEL ESTADO DE MÉXICO
CU UAEM ZUMPANGO
UA: REDES NEURONALES
Tema: 
Alumno: Samano Rivera Luis Fernando
Profesor: Dr. Asdrúbal López Chau
descripcion :
Created on Mon Dec  6 14:30:11 2021

@author: FERNANDO
"""

import librosa
import IPython.display as ipd
import matplotlib as plt 

audio_path = 'perro.wav'
librosa.load(audio_path, sr=44100)
ipd.Audio(audio_path)
x , sr = librosa.load(audio_path)
print(type(x), type(sr))

#display Spectrogram 
X = librosa.stft (x) 
Xdb = librosa.amplitude_to_db (abs (X)) 
plt.figure (figsize = (14, 5)) 
librosa.display.specshow (Xdb, sr = sr, x_axis = 'tiempo ', y_axis =' hz ') 
#Si pring registro de frecuencias   
# librosa.display.specshow (Xdb, sr = sr, x_axis =' time ', y_axis =' log ') 
plt.colorbar ()