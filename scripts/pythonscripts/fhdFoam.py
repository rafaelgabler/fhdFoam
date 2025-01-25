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
        self.fontePadrao = ("Adobe Myungjo Std M", "18")
        self.fonteBotoes = ("Arial", "16")
        cttk.set_appearance_mode("White")
        
        largura_tela_1 = self.root_1.winfo_screenwidth()
        altura_tela_1 = self.root_1.winfo_screenheight()
        self.largura_tela = largura_tela_1//4
        self.altura_tela = altura_tela_1//3
        self.root_1.geometry(f'800x800+{self.largura_tela}+{self.altura_tela}')
    
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
        texto1= """fhdFoam is an open source project that aims to provide openFoam based solvers to simulate problems 
        in the context of ferrohydrodynamics. The project is based on different solvers for different physics. 
        
        Please choose from the options bellow what physics you want to simulate.        
        """


        # Load the image 
        image = PhotoImage(file="../../figs/fhdFoam_logo.png",
                           )
        # Create a label to display the image
        image_label = cttk.CTkLabel(self.primeiroContainer, 
                           image=image)
        image_label.pack()

        # Atribuição do título dentro da janela (1a informação exibida)
        
        self.titulo = cttk.CTkLabel(self.primeiroContainer, 
                           text=texto1,
                           justify="center")
        self.titulo.pack(pady=5, padx=5)
       


        # Display the image
        # my_label = CTkLabel(root, text="", image=my_image)
        # my_label.pack(pady=10)
  
    def botoes_main_wind(self):
        # cria os containers para posicionar os botões

        self.segundoContainer = cttk.CTkFrame(root_1)
        self.segundoContainer.pack(pady=20, padx=20)
        
        self.terceiroContainer = cttk.CTkFrame(root_1)
        self.terceiroContainer.pack(pady=20, padx=20)

        self.quartoContainer = cttk.CTkFrame(root_1)
        self.quartoContainer.pack(pady=20, padx=20)

        self.quintoContainer = cttk.CTkFrame(root_1)
        self.quintoContainer.pack(pady=20, padx=20)

        #Botão para mhtFoam

        texto2= """Magnetic hyperthermia of tumours
        """

        self.titulo2 = cttk.CTkLabel(self.segundoContainer, 
                           text=texto2,
                           justify="center")
    
        self.mhtfoam = cttk.CTkButton(self.segundoContainer, text="mhtFoam",
                           width=150,  # Ajustado para largura em pixels
                           height=40,corner_radius=8,command=self.call_mhtfoam)
        self.mhtfoam.pack(side=BOTTOM,padx=15)

        self.titulo2.pack(pady=5, padx=5)

        #Botão para magnetoconvectionFoam

        texto3= """Thermomagnetic convection
        """

        self.titulo3 = cttk.CTkLabel(self.terceiroContainer, 
                           text=texto3,
                           justify="center")
 
        self.titulo3.pack(pady=5, padx=5)
    
        self.magconvfoam = cttk.CTkButton(self.terceiroContainer, text="magnetoconvectionFoam",
                           width=150,  # Ajustado para largura em pixels
                           height=40,corner_radius=8,command=self.call_mhtfoam)
        self.magconvfoam.pack(side=BOTTOM,padx=15)

        #Botão para intermagFoam

        texto4= """Two phase magnetic fluid flow
        """

        self.titulo4 = cttk.CTkLabel(self.quartoContainer, 
                           text=texto4,
                           justify="center")
 
        self.titulo4.pack(pady=5, padx=5)
    
        self.intermagfoam = cttk.CTkButton(self.quartoContainer, text="intermagFoam",
                           width=150,  # Ajustado para largura em pixels
                           height=40,corner_radius=8,command=self.call_mhtfoam)
        self.intermagfoam.pack(side=BOTTOM,padx=15)  

       #Botão para icomagFoam

        texto5= """Non-equilibrium magnetization 
        """

        self.titulo5 = cttk.CTkLabel(self.quintoContainer, 
                           text=texto5,
                           justify="center")
 
        self.titulo5.pack(pady=5, padx=5)
    
        self.icomagfoam = cttk.CTkButton(self.quintoContainer, text="icomagFoam",
                           width=150,  # Ajustado para largura em pixels
                           height=40,corner_radius=8,command=self.call_mhtfoam)
        self.icomagfoam.pack(side=BOTTOM,padx=15)
                     
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