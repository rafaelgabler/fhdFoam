import tkinter as tk
from tkinter import *
from tkinter import simpledialog, messagebox, Tk, Frame, Label, LEFT, RIGHT, Button, Entry,font
import customtkinter as cttk
from matplotlib.figure import Figure
from matplotlib.patches import Ellipse
from PIL import ImageTk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np
import json


class Main_wind:
    ## Abre a tela inicial e estabelece algumas informações a serem usadas no meio do código
    def __init__(self, root_1):
        self.root_1 = root_1
        self.root_1.title("fhdFoam")
        self.fontePadrao = ("Adobe Myungjo Std M", "13")
        self.fonteBotoes = ("Arial", "12")
        cttk.set_appearance_mode("Dark")
        
        largura_tela_1 = self.root_1.winfo_screenwidth()
        altura_tela_1 = self.root_1.winfo_screenheight()
        self.largura_tela = largura_tela_1//4
        self.altura_tela = altura_tela_1//3
        self.root_1.geometry(f'550x350+{self.largura_tela}+{self.altura_tela}')
    
    def interface(self):
        ## Aqui deixa já aberto as seguintes funções
        self.define_titulo()
        self.botoes_main_wind()
    
    def define_titulo(self):
        """
        Função responsável pela construção da parte relativa ao título na interface
        """
        # Construção do container para título da janela
        
        self.primeiroContainer = cttk.CTkFrame(root_1)
        self.primeiroContainer.pack(pady=20, padx=20)
        
        #Texto da intro do mhtFoam
        texto1= """fhdFoam is an open source project that aims to provide openFoam 
        based solvers to simulate problems in the context of ferrohydrodynamics. 
        The project is based on different solvers for different physics. 
        Please choose bellow what physics you want to simulate.
        
        """

        # Atribuição do título dentro da janela (1a informação exibida)
        
        self.titulo = cttk.CTkLabel(self.primeiroContainer, 
                           text=texto1,
                           justify="center")
        self.titulo.pack(pady=5, padx=5)
  
    def botoes_main_wind(self):
        # cria os containers para posicionar os botões

        self.segundoContainer = cttk.CTkFrame(root_1)
        self.segundoContainer.pack(pady=20, padx=20)
        
        
        #Botão para mhtFoam

        texto2= """mhtFoam was designed to simulate the heating process of
        tumours subjected to magnetic hyperthermia.
        """

        self.titulo2 = cttk.CTkLabel(self.segundoContainer, 
                           text=texto2,
                           justify="center")
        self.titulo2.pack(pady=5, padx=5)

        self.mhtfoam = cttk.CTkButton(self.segundoContainer, text="mhtFoam",
                           width=150,  # Ajustado para largura em pixels
                           height=40,corner_radius=8,command=self.call_mhtfoam)
        self.mhtfoam.pack(side=BOTTOM,padx=5)

        
    def call_mhtfoam(self):
        
        """
        Função responsável por chamar o script mhtFoam_pre.py
        """

        import os
        #python_script_dir = "scripts/pythonscripts"
        # Muda o diretório de trabalho para o local do Allpre
        # os.chdir(python_script_dir)
        # Chama o script mhtFoam_pre.py 
        os.system("python3 mhtFoam_pre.py")
        
# Inicializa a interface gráfica
root_1 = cttk.CTk()
app = Main_wind(root_1)
zaragui = app # Inicialização

zaragui.interface()

root_1.mainloop()