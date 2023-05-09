import os
import validators
from pytube import YouTube
from pytube.cli import on_progress
from termcolor import colored
from pyfiglet import Figlet


os.system('cls')


def inputlink():
    link = input("Insira o link: ")
    valink = validators.url(link)
   
    if not valink:
        del link
        inputlink()
        return -1
    
  
    yt = YouTube(link, on_progress_callback = on_progress)

    print("Titulo = ", yt.title)
    print("Baixando..")

    ys = yt.streams.get_highest_resolution()

    ys.download()

f = Figlet(font='standard')
print(colored(f.renderText('DowTube'), 'red'))

inputlink()




    

