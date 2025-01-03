import tkinter as tk
from tkinter import *
from tkinter import simpledialog, messagebox, Tk, Frame, Label, LEFT, RIGHT, Button, Entry,font
from substitute_values_2 import generate_dictionary_1, generate_dictionary_2, generate_dictionary_3, changeFileDict, changeFileDict_2
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
        self.root_1.title("mhtFoam")
        self.fontePadrao = ("Adobe Myungjo Std M", "11")
        self.fonteBotoes = ("Arial", "10")
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
        #self.define_titulo()
        self.tumor_data_entries = {}
        self.data_t = {"tumors": []}
        self.jason_quantities = []
    def define_titulo(self):
        """
        Função responsável pela construção da parte relativa ao título na interface
        """
        # Construção do container para título da janela
        
        self.primeiroContainer = cttk.CTkFrame(root_1)
        self.primeiroContainer.pack(pady=20, padx=20)
        
        #Texto da intro do mhtFoam
        texto1= """O solver mhtFoam simula o processo de magnetohipertermia
aplicado a tratamento de tumores. Entre com as informações
do domínio de cáculo/malha, do tempo e com as informações dos tumores
através dos botões abaixo.

v 2.0"""

        # Atribuição do título dentro da janela (1a informação exibida)
        
        self.titulo = cttk.CTkLabel(self.primeiroContainer, 
                           text=texto1,
                           justify="center")
        self.titulo.pack(pady=5, padx=5)
    def botoes_main_wind(self):
        # cria os containers para posicionar os botões

        self.segundoContainer = cttk.CTkFrame(root_1)
        self.segundoContainer.pack(pady=20, padx=20)
        
        
        self.terceiroContainer = cttk.CTkFrame(root_1)
        self.terceiroContainer.pack(pady=20, padx=20)
        
        # Botão para gerar setup
        
        self.relatorio = cttk.CTkButton(self.terceiroContainer, text="Gerar Setup",
                           width=12,  # Ajustado para largura em pixels
                           height=30,corner_radius=8,command=self.gera_setup)
        self.relatorio.pack(side=LEFT,padx=5)
        
        
        # Botão para iniciar simulação
        
        self.simu = cttk.CTkButton(self.terceiroContainer, text="Iniciar simulação",
                           width=12,  # Ajustado para largura em pixels
                           height=30,corner_radius=8,command=self.simulation)
        self.simu.pack(side=RIGHT,padx=5)
        
        #Botão para adicionar parâmetros da malha

        self.malha = cttk.CTkButton(self.segundoContainer, text="Parâmetros da malha",
                           width=150,  # Ajustado para largura em pixels
                           height=40,corner_radius=8,command=self.leitura_blockMeshDict)
        self.malha.pack(side=LEFT,padx=5)
        
        # Botão para adicionar parâmetros temporais
    
        self.tempo = cttk.CTkButton(self.segundoContainer, text="Parâmetros temporais",
                           width=150,  # Ajustado para largura em pixels
                           height=40,corner_radius=8,command=self.leitura_ControlDict)
        self.tempo.pack(side=LEFT,padx=5)
       
        # Botão para adicionar parâmetros dos tumores
        
        self.tumor = cttk.CTkButton(self.segundoContainer, text="Parâmetros dos tumores",
                           width=150,  # Ajustado para largura em pixels
                           height=40,corner_radius=8,command=self.tumors)
        self.tumor.pack(side=RIGHT,padx=5)
        
        ## Botão para adicionar Pré-visualização
        
        self.visu = cttk.CTkButton(self.terceiroContainer, text="Pré-visualização",
                           width=12,  # Ajustado para largura em pixels
                           height=30,corner_radius=8,command=self.visual)
        self.visu.pack(side=LEFT,padx=5)
        
    def leitura_ControlDict(self):
        """
        Função responsável pela construção da parte relacionada ao controlDict
        """
        self.data={}
        ##Abre containers para as informações a serem plotadas
        self.control=cttk.CTkToplevel(root_1)
        self.control.title("Parâmetros temporais")
        self.controlcontainer1=cttk.CTkFrame(self.control)
        self.controlcontainer1.pack(pady=10, padx=10)
        self.controlcontainer2=cttk.CTkFrame(self.control)
        self.controlcontainer2.pack(pady=10, padx=10)
        self.controlcontainer3=cttk.CTkFrame(self.control)
        self.controlcontainer3.pack(pady=10, padx=10)
        
        ##Endtime
            
        self.endtimeLabel = cttk.CTkLabel(self.controlcontainer1, 
                              text="Tempo final (s): ")
        self.endtimeLabel.pack(side="left")
        self.endtime = cttk.CTkEntry(self.controlcontainer1, 
                         width=300, 
                         placeholder_text="600")
        self.endtime.pack(side="right")

        
        ##Timestep
        self.timestepLabel = cttk.CTkLabel(self.controlcontainer2, 
                              text="Time step (s): ")
        self.timestepLabel.pack(side="left")
        self.timestep = cttk.CTkEntry(self.controlcontainer2, 
                         width=300, 
                         placeholder_text="0.1")
        self.timestep.pack(side="right")
        
        ## Botão para confirmar
        self.autenticarcontrol = cttk.CTkButton(self.controlcontainer3, text="Ok",
                           width=150,  # Ajustado para largura em pixels
                           height=40,command=self.save_control)
        self.autenticarcontrol.pack(side=RIGHT,padx=5)
    
    ## Salva as informações entradas em self.data
    def save_control(self):
        endtime =self.endtime.get()
        timestep=self.timestep.get()
        if endtime is not None:
            self.data["endtime"] = endtime
        if timestep is not None:
            self.data["timestep"] = timestep
            
        self.outJson3 = "inputDict_controlDict.json"
        self.jason_quantities.append(self.outJson3)
        ## Salva no jason
        with open(self.outJson3, "w") as arquivo:
            json.dump(self.data, arquivo, indent=4)
        
        ## Fecha a tela
        self.control.destroy()
        
    def leitura_blockMeshDict(self):
        
        """
        Função responsável pela construção da parte relacionada ao blockMeshDict
        """
        ## Abre a janela principal
        self.parametro_window = cttk.CTkToplevel(root_1)
        self.parametro_window.title("parâmetros do Domínio de Cálculo")
        
        # Construção do container para a entrada de xmax
        self.segundo2Container = cttk.CTkFrame(self.parametro_window)
        self.segundo2Container.pack(pady=20, padx=20)
        
        # Construção do container para a entrada de ymax
        self.terceiro2Container = cttk.CTkFrame(self.parametro_window)
        self.terceiro2Container.pack(pady=10, padx=20)
        
        # Construção do container para a entrada de zmax
        self.quarto2Container = cttk.CTkFrame(self.parametro_window)
        self.quarto2Container.pack(pady=10, padx=20)
        
        # Construção do container para a entrada de xnode
        self.quinto2Container = cttk.CTkFrame(self.parametro_window)
        self.quinto2Container.pack(pady=10, padx=20)
        
        # Construção do container para a entrada de ynode
        self.sexto2Container = cttk.CTkFrame(self.parametro_window)
        self.sexto2Container.pack(pady=10, padx=20)
        
        # Construção do container para a entrada de znode
        self.setimo2Container = cttk.CTkFrame(self.parametro_window)
        self.setimo2Container.pack(pady=10, padx=20)
        
        # Construção do container para a entrada de endTime
        self.oitavo2Container = cttk.CTkFrame(self.parametro_window)
        self.oitavo2Container.pack(pady=10, padx=20)
        
        # Informação exibida para entrada de xmax
        self.xmaxLabel = cttk.CTkLabel(self.segundo2Container, 
                              text="Size of the domain in x direction (m): ")
        self.xmaxLabel.pack(side="left")
        self.xmax = cttk.CTkEntry(self.segundo2Container, 
                         width=300, 
                         placeholder_text="0.09")
        self.xmax.pack(side="left")
        
        # Informação exibida para entrada de ymax
        self.ymaxLabel = cttk.CTkLabel(self.terceiro2Container, 
                              text="Size of the domain in y direction (m): ")
        self.ymaxLabel.pack(side="left")
        self.ymax = cttk.CTkEntry(self.terceiro2Container, 
                         width=300, 
                         placeholder_text="0.09")
        self.ymax.pack(side="left")
        
        # Informação exibida ao lado do campo para entrada de zmax
        self.zmaxLabel = cttk.CTkLabel(self.quarto2Container, 
                              text="Size of the domain in z direction (m): ")
        self.zmaxLabel.pack(side="left")
        self.zmax = cttk.CTkEntry(self.quarto2Container, 
                         width=300, 
                         placeholder_text="0.01")
        self.zmax.pack(side="left")
        
        # Informação exibida ao lado do campo para entrada de xnode
        self.xnodeLabel = cttk.CTkLabel(self.quinto2Container, 
                              text="Amount of nodes in the x direction: ")
        self.xnodeLabel.pack(side="left")
        self.xnode = cttk.CTkEntry(self.quinto2Container, 
                         width=300, 
                         placeholder_text="500")
        self.xnode.pack(side="right")
        
        # Informação exibida ao lado do campo para entrada de ynode
        self.ynodeLabel = cttk.CTkLabel(self.sexto2Container, 
                              text="Amount of nodes in the y direction: ")
        self.ynodeLabel.pack(side="left")
        self.ynode = cttk.CTkEntry(self.sexto2Container, 
                         width=300, 
                         placeholder_text="500")
        self.ynode.pack(side="right")
        
        # Informação exibida ao lado do campo para entrada de znode
        self.znodeLabel = cttk.CTkLabel(self.setimo2Container, 
                              text="Amount of nodes in the z direction: ")
        self.znodeLabel.pack(side="left")
        self.znode = cttk.CTkEntry(self.setimo2Container, 
                         width=300, 
                         placeholder_text="1")
        self.znode.pack(side="right")
        
        #botão de gerar jason
        self.autenticar = cttk.CTkButton(self.oitavo2Container, text="Ok",
                           width=150,  # Ajustado para largura em pixels
                           height=40,command=self.gera_json_malha)
        self.autenticar.pack(side=RIGHT,padx=5)
        
    # Blocos de geração de arquivos Jason
   
    def window_destroymesh(self):
        #Função para fechar tela após o ok ser pressionado
        self.parametro_window.destroy()
        self.confirmationmesh.destroy()
    def gera_json_malha(self):
        import json
        
        ## Coloca no inputDict_blockMeshDict as informações coletadas
        inputDict_blockMeshDict = {}
        inputDict_blockMeshDict["xmax"] = self.xmax.get()
        inputDict_blockMeshDict["ymax"] = self.ymax.get()
        inputDict_blockMeshDict["zmax"] = self.zmax.get()
        inputDict_blockMeshDict["xnode"] = self.xnode.get()
        inputDict_blockMeshDict["ynode"] = self.ynode.get()
        inputDict_blockMeshDict["znode"] = self.znode.get()
        
        # Aqui vai ser usado para plotar a imagem de pré-view depois
        self.xmax1=float(self.xmax.get())
        self.ymax1=float(self.ymax.get())
        
        ## Salva no jason
        json_string = json.dumps(inputDict_blockMeshDict, indent=4)
        self.outJson="inputDict_blockMeshDict.json"
        self.jason_quantities.append(self.outJson)
        
        with open(self.outJson,"w") as f:
            f.write(json_string)
        f.close()
        
        ## Monta o botão de confirmação e fecha as telas
        self.confirmationmesh = cttk.CTkToplevel(root_1)
            
        self.confContainermesh = cttk.CTkFrame(self.confirmationmesh)
        self.confContainermesh.pack(pady=10, padx=20)
        self.confContainer1mesh =cttk.CTkFrame(self.confirmationmesh)
        self.confContainer1mesh.pack(pady=10, padx=20)
            
        self.confirmationmesh.title("Confirmação")
        self.confirmationmeshLabel = cttk.CTkLabel(self.confContainermesh, 
                              text="Parâmetros da malha salvos com sucesso.")
        self.confirmationmeshLabel.pack(side="left")
            
        self.confirmationmeshbutton = cttk.CTkButton(self.confContainer1mesh, text="Ok",
                           width=150,  # Ajustado para largura em pixels
                           height=40,command=self.window_destroymesh)
        self.confirmationmeshbutton.pack(side=LEFT,padx=5)
        
        
    """Aqui abre as janelas para coleta dos parâmetros dos tumores"""
    

    # Tela que pergunta quantos tumores é definido aqui
    def tumors(self):
        ## Conta quantidade de telas relativa a quantidade de tumores e fecha tela
        def submit():
            nonlocal tumor_count
            tumor_count = int(tumor_count_num.get())
            self.open_tumor_data_screens(tumor_count)
            self.tumor_count.destroy()
        tumor_count = None

        self.tumor_windows = []
        ## Abre janela
        self.tumor_count=cttk.CTkToplevel()
        self.tumor_count.title("Parâmetros dos tumores")
        
        ## Container
        self.uniqueContainer = cttk.CTkFrame(self.tumor_count)
        self.uniqueContainer.pack(pady=10, padx=20)
        self.uniqueContainer1 = cttk.CTkFrame(self.tumor_count)
        self.uniqueContainer1.pack(pady=10, padx=20)
        
        self.tumor_count_numlabel = cttk.CTkLabel(self.uniqueContainer, 
                              text="How many tumors?")
        self.tumor_count_numlabel.pack(side="left")
        
        ## Variável de entrada que conta os tumores
        tumor_count_num = cttk.CTkEntry(self.uniqueContainer, 
                         width=300, 
                         placeholder_text="2")
        tumor_count_num.pack(side="left")
        
        ## Botão de ok
        self.tumorbutton = cttk.CTkButton(self.uniqueContainer1, text="Ok",
                           width=150,  # Ajustado para largura em pixels
                           height=40,command=submit)
        self.tumorbutton.pack(side=LEFT,padx=5)
        
        return tumor_count
        #self.open_tumor_data_screens(tumor_count_num)
        
    ##Aqui define em que posição da tela vai abrir e chama a função que abre as novas telas para cada tumor
    def open_tumor_data_screens(self, tumor_count):
        self.count1=int(tumor_count)
        for i in range(0,tumor_count):
            self.largura_tela2=self.largura_tela+(i-1)*80
            self.altura_tela2=self.altura_tela+(i-1)*100
            self.collect_tumor_data(i,tumor_count)
        #self.tumor_windows = []
        
    ## Tela para coleta de info de tumor
    def collect_tumor_data(self, index, tumor_count):
        
        self.current_index=index
        self.tumor_data_entries[index] = {}
        
        ##Abre Tela
        self.tumor_window = cttk.CTkToplevel(root_1)
        self.tumor_window.title(f"Tumor {index + 1} Data")
        self.tumor_window.geometry(f'300x370+{self.largura_tela2}+{self.altura_tela2}')
        self.tumor_windows.append(self.tumor_window)
        
        #abre os containers
        self.primeiro5Container = cttk.CTkFrame(self.tumor_window)
        self.primeiro5Container.pack(pady=10, padx=20)
        
        self.segundo5Container = cttk.CTkFrame(self.tumor_window)
        self.segundo5Container.pack(pady=10, padx=20)
        
        self.terceiro5Container = cttk.CTkFrame(self.tumor_window)
        self.terceiro5Container.pack(pady=10, padx=20)
        
        self.quarto5Container = cttk.CTkFrame(self.tumor_window)
        self.quarto5Container.pack(pady=10, padx=20)
        
        self.quinto5Container = cttk.CTkFrame(self.tumor_window)
        self.quinto5Container.pack(pady=10, padx=20)
        
        self.sexto5Container = cttk.CTkFrame(self.tumor_window)
        self.sexto5Container.pack(pady=10, padx=20)
        
        # Aqui fica as abas onde serão coletadas os dados do usuário
        # raio,excentricidade,posição x, posição y, inclinação em graus
        
        # Campo para entrada do raio
        self.radiusLabel = cttk.CTkLabel(self.primeiro5Container, 
                              text="Equivalent radius: ")
        self.radiusLabel.pack(side="left")
        self.radius = cttk.CTkEntry(self.primeiro5Container, 
                         width=300, 
                         placeholder_text="0.005")
        self.radius.pack(side="left")
        self.tumor_data_entries[index]["radius"] = self.radius
        

        # Campo para entrada da excentricidade
        self.eccenLabel = cttk.CTkLabel(self.segundo5Container, 
                              text="eccentricity: ")
        self.eccenLabel.pack(side="left")
        self.eccen = cttk.CTkEntry(self.segundo5Container, 
                         width=300, 
                         placeholder_text="0.9")
        self.eccen.pack(side="right")
        self.tumor_data_entries[index]["eccen"] = self.eccen
        
        # Campo para entrada da posição x
        self.posxLabel = cttk.CTkLabel(self.terceiro5Container, 
                              text="x position of the tumor: ")
        self.posxLabel.pack(side="left")
        self.posx = cttk.CTkEntry(self.terceiro5Container, 
                         width=300, 
                         placeholder_text="0.045")
        self.posx.pack(side="left")
        self.tumor_data_entries[index]["posx"] = self.posx
        
        # Campo para entrada da posição y
        self.posyLabel = cttk.CTkLabel(self.quarto5Container, 
                              text="y position of the tumor: ")
        self.posyLabel.pack(side="left")
        self.posy = cttk.CTkEntry(self.quarto5Container, 
                         width=300, 
                         placeholder_text="0.045")
        self.posy.pack(side="left")
        self.tumor_data_entries[index]["posy"] = self.posy
        
        # Campo para entrada da inclinação
        self.inclinationLabel = cttk.CTkLabel(self.quinto5Container, 
                              text="Inclination of the tumor (º): ")
        self.inclinationLabel.pack(side="left")
        self.inclination = cttk.CTkEntry(self.quinto5Container, 
                         width=300, 
                         placeholder_text="30")
        self.inclination.pack(side="left")
        self.tumor_data_entries[index]["inclination"] = self.inclination
        
        ## Botão de ok
        self.autenticar_tumor = cttk.CTkButton(self.sexto5Container, text="Ok",
                           width=150,  # Ajustado para largura em pixels
                           height=40,command=lambda win=self.tumor_window, idx=index, total=tumor_count:                      self.gera_json_tumor(win, idx, total))
        self.autenticar_tumor.pack(side=LEFT,padx=5)
    
    #Função associada à fechar as telas de entrada dos parâmetros dos tumores
    def window_destroy(self):
            self.tumor_window.destroy()
            self.confirmation.destroy()
            self.tumor_count.destroy()
            
    def gera_json_tumor(self,window,index,tumor_count):
        """Aqui salva os dados dos tumores no arquivo jason"""
        import json
        #self.indexx = indexx
        
        indexx=index+1
        ## Salva os dados coletados em inputDict_ID
        inputDict_ID = {
            f"radius_{indexx}": self.tumor_data_entries[index]["radius"].get(),
            f"eccen_{indexx}": self.tumor_data_entries[index]["eccen"].get(),
            f"posx_{indexx}": self.tumor_data_entries[index]["posx"].get(),
            f"posy_{indexx}": self.tumor_data_entries[index]["posy"].get(),
            f"inclination_{indexx}": self.tumor_data_entries[index]["inclination"].get()
        }
        
        ##Salva em self.data
        self.data_t["tumors"].append(inputDict_ID)
        #self.data_t.append(inputDict_ID)
        
        json_string = json.dumps(inputDict_ID, indent=4)
        self.outJson2="inputDict_ID.json"
        self.jason_quantities.append(self.outJson2)
        
        #Abaixo fecha as janelas onde entramos com os dados dos tumores a medida que clica-se "Gerar Json"
        #A última tela gera uma janela de confirmação e só ela que gera a mensagem de confirmação
        
        ##Salva no jason
        if len(self.data_t["tumors"]) == tumor_count:
            with open(self.outJson2, "w") as f:
                json.dump(self.data_t, f, indent=4)
            
            
            ##Abre janela de confirmação e containers
            self.confirmation = cttk.CTkToplevel(root_1)
            
            self.confContainer = cttk.CTkFrame(self.confirmation)
            self.confContainer.pack(pady=10, padx=20)
            self.confContainer1 =cttk.CTkFrame(self.confirmation)
            self.confContainer1.pack(pady=10, padx=20)
            
            self.confirmation.title("Confirmação")
            self.confirmationLabel = cttk.CTkLabel(self.confContainer, 
                              text="Parâmetros de todos os tumores salvos com sucesso.")
            self.confirmationLabel.pack(side="left")
            
            ## Botão de ok
            self.confirmationbutton = cttk.CTkButton(self.confContainer1, text="Ok",
                           width=150,  # Ajustado para largura em pixels
                           height=40,command=self.window_destroy)
            self.confirmationbutton.pack(side=LEFT,padx=5)
        else:
            window.destroy()

        
    def gera_setup(self):
        """Aqui gera o setup"""
    	# Gerar o setup é substituir os dados coletados nos respectivos arquivos
        import json
        import os
        # Limpa pasta e prepara a simulação copiando arquivos da pasta 0 e system de volta
        os.system("../../tutorials/mhtFoam/2d_circular_tumour/Allclean")
        os.system("../../tutorials/mhtFoam/2d_circular_tumour/Allpre")
        
        # Gera o json caso o usuario se esqueça
        self.gera_json_tumor
        self.gera_json_malha

        indexx=self.current_index+1
        
        ## Aqui chama o outro arquivo substitute_values_2 e altera os arquivos de acordo com as funções de lá
        with open(self.outJson,'r') as f:
            data = json.load(f)
        inputDict = generate_dictionary_2(data)
        changeFileDict(inputDict)
        with open(self.outJson3,'r') as f:
            data = json.load(f)
        inputDict = generate_dictionary_1(data)
        changeFileDict(inputDict)
        #for indexx in range(1,self.current_index+1):
        with open(self.outJson2,'r') as f:
            data = json.load(f)
        inputDict = generate_dictionary_3(data,indexx)
        changeFileDict_2(inputDict)

    def visual(self):
        """Aqui é a função de pré visualização da configuração escolhida"""
        
        ##Abre janela
        visuwind = cttk.CTkToplevel(root_1)
        visuwind.title("pré visualizar")
        
        ##Define configurações de onde vai ser plotado
        fig = Figure(figsize=(5, 5), dpi=100)
        ax = fig.add_subplot(111)
        
        ##Título e labels
        ax.set_title("Tumors Configuration")
        ax.set_xlabel("X size (m)")
        ax.set_ylabel("Y size (m)")
        ax.set_aspect('equal')
        
        ## Coloca grid
        ax.grid(True, which='both', linestyle='--', linewidth=0.5, color='gray', alpha=0.7)
        
        try:
            for i, tumor in enumerate(self.data_t["tumors"], start=1):  # Itera sobre os tumores na lista
            # Acessando os dados do tumor
                posx = float(tumor[f"posx_{i}"])
                posy = float(tumor[f"posy_{i}"])
                radius = float(tumor[f"radius_{i}"])
                eccen = float(tumor[f"eccen_{i}"])
                inclination = float(tumor[f"inclination_{i}"])

            # Gerando a forma
                t = np.linspace(0, 2 * np.pi, 100)
                ellipse_x = radius/(np.sqrt(1-eccen**2)) * np.cos(t)
                ellipse_y = radius * np.sin(t)
                ellipse_xmag=0.00287*np.cos(t)
                ellipse_ymag=0.00287*np.sin(t)
                
            
            # Rotação da elipse
                ##Tumor
                x_rot = posx +ellipse_x*np.cos(np.radians(inclination))-ellipse_y*np.sin(np.radians(inclination))
                y_rot = posy +ellipse_x*np.sin(np.radians(inclination))+ellipse_y*np.cos(np.radians(inclination))
                ##Fluido magnético
                x_mag= posx+ellipse_xmag
                y_mag= posy+ellipse_ymag
            # Plotando o tumor e o fluido
                ax.fill(x_rot, y_rot, color='blue', label=f"Tumor {i} at ({posx}, {posy})")
                ax.fill(x_mag, y_mag, color='black', label=f"Tumor {i} at ({posx}, {posy})")
                
        ## Coloquei aqui porque só o try dá erro, complemento do try
        except KeyError as item:
            print(f"Erro: Não achei o item {item} no dicionário de tumores.")
        

 
        ##Define os limites de acordo com os dados entrados para o blockMeshDict
        ax.set_xlim(0, self.xmax1)
        ax.set_ylim(0, self.ymax1)
        
        ##Desenha a imagem
        canvas = FigureCanvasTkAgg(fig, visuwind)
        canvas.draw()
        canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)
            
            
    def simulation(self):
        """
        Função utilizada para Iniciar simulação
        """
        import os
        os.system("./Allrun &")
        
# Inicializa a interface gráfica
root_1 = cttk.CTk()
app = Main_wind(root_1)
zaragui = app # Inicialização

zaragui.interface()

root_1.mainloop()


