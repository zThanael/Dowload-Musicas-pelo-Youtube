from PySimpleGUI import PySimpleGUI as sg
from pytube import YouTube
import moviepy.editor as mp
import re
import os

def dowloadMP3(dict):
    link = dict['link']
    path = dict['path']
    yt = YouTube(link)
    #Fazer o dowload
    ys = yt.streams.filter
    ys = yt.streams.filter(only_audio=True).first().download(path)
    #Converter o video(mp4) para mp3
    for file in os.listdir(path): #percorrer na pasta
        if re.search('mp4', file):  #se o arquivo for .mp4                        
            mp4_path = os.path.join(path , file) #cria variavel para armazenar o caminho dele
            mp3_path = os.path.join(path, os.path.splitext(file)[0]+'.mp3') #nome do caminho
            new_file = mp.AudioFileClip(mp4_path)  #cria o arquivo mp3 com o audio
            new_file.write_audiofile(mp3_path) #escreve o nome do arquivo mp3
            os.remove(mp4_path)

#Layout
def janela_cliente():
    sg.theme('Reddit')
    layout = [
    [sg.Text('Digite o Link da musica:', size=(18,0)), sg.Input(key = 'link', size=(50,0))], #input que retornara no dicionar com a key='link' e o valor que for digitado
    [sg.Text('Selecione a pasta:', size=(18,0)), sg.InputText('Default Folder',size = (40,0),key = 'path'), sg.FolderBrowse('Arquivo', size = (7,0))],
    [sg.Button('Baixar', size=(20,0),)]
    ]
    return sg.Window('Dowloader MP3 Music',layout=layout, finalize=True)
#criar as janelas
janela = janela_cliente()
#ler os eventos
while True:
    event,values = janela.Read()
    #quando a janela for fechada
    if event == sg.WIN_CLOSED:
        break
    if event == 'Baixar':
        dowloadMP3(values)
        sg.popup("Download Completo")
        

