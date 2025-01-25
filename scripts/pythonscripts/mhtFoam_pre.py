import tkinter as tk
from tkinter import *
from tkinter import simpledialog, messagebox, Tk, Frame, Label, LEFT, RIGHT, Button, Entry,font
from edit_lybraries import  generate_dictionary_3, changeFileDict, changeFileDict_2
from edit_lybraries import generate_dictionary_1, generate_dictionary_2
from edit_lybraries import generate_dictionary_4,changeFileDict_4,generate_dictionary_5
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
        cttk.set_appearance_mode("White")
        
        largura_tela_1 = self.root_1.winfo_screenwidth()
        altura_tela_1 = self.root_1.winfo_screenheight()
        self.largura_tela = largura_tela_1//4
        self.altura_tela = altura_tela_1//3
        self.root_1.geometry(f'1200x1000+{self.largura_tela}+{self.altura_tela}')
    def interface(self):
        ## Aqui deixa já aberto as seguintes funções
        self.define_titulo()
        self.botoes_main_wind()
        self.tumor_data_entries = {}
        self.fluid_data_entries = {}
        self.data_t = {"tumors": []}
        self.data_tmag = {"magnetic_fluid": []}
        self.jason_quantities = []
    def define_titulo(self):
        """
        Função responsável pela construção da parte relativa ao título na interface
        """
        # Construção do container para título da janela
        
        self.primeiroContainer = cttk.CTkFrame(root_1)
        self.primeiroContainer.pack(pady=10, padx=20)
        
        #Texto da intro do mhtFoam

        texto1= """mhtFoam simulates the heating proccess of circular and 
        elliptical tumours subjected to magnetic hyperthermia. Please navigate
        through the buttons bellow in order to configure your simulation.

v 2.0"""

        # Atribuição do título dentro da janela (1a informação exibida)
        
        self.titulo = cttk.CTkLabel(self.primeiroContainer, 
                           text=texto1,
                           justify="center",font=("Ubuntu",16))
        self.titulo.pack(pady=5, padx=5)
    def botoes_main_wind(self):
        ## Aqui define toda a estrutura da janela principal

        # cria os containers para posicionar os botões e formulários
        self.mainconteiner_root1 = cttk.CTkFrame(root_1)
        self.mainconteiner_root1.pack(pady=10, padx=20)

        # Container para form do mesh properties
        self.segundoContainer = cttk.CTkFrame(self.mainconteiner_root1)
        self.segundoContainer.pack(side=LEFT,pady=10, padx=20)
        self.titulo_segundoContainer = cttk.CTkLabel(self.segundoContainer, 
                           text="""Mesh Parameters""",
                           justify="center")
        self.titulo_segundoContainer.pack(pady=2, padx=2)

        # Container para form do time properties
        self.segundoContainer_main= cttk.CTkFrame(self.mainconteiner_root1)
        self.segundoContainer_main.pack(side=TOP,pady=10, padx=20,fill="both", expand=True)
        self.titulo_segundoContainer_main = cttk.CTkLabel(self.segundoContainer_main, 
                           text="""Time Parameters""",
                           justify="center")
        self.titulo_segundoContainer_main.pack(side=TOP,pady=2, padx=2)
        
        #Container para form do field properties
        self.segundoContainer_main_down= cttk.CTkFrame(self.mainconteiner_root1)
        self.segundoContainer_main_down.pack(side=BOTTOM,pady=10, padx=20,fill="both", expand=True)
        self.titulo_segundoContainer_main_down = cttk.CTkLabel(self.segundoContainer_main_down, 
                           text="""Field Parameters""",
                           justify="center")
        self.titulo_segundoContainer_main_down.pack(side=TOP,pady=2, padx=2)

        #Container para botão do tumor properties
        self.middleContainer = cttk.CTkFrame(root_1)
        self.middleContainer.pack(pady=10, padx=20)
        
        self.terceiroContainer = cttk.CTkFrame(root_1)
        self.terceiroContainer.pack(pady=10, padx=20)
        
        # Botão para gerar setup  
        self.relatorio = cttk.CTkButton(self.terceiroContainer, text="Configure simulation",
                           width=12,  # Ajustado para largura em pixels
                           height=30,corner_radius=8,command=self.gera_setup)
        self.relatorio.pack(side=LEFT,padx=5)
        
        # Botão para iniciar simulação
        self.simu = cttk.CTkButton(self.terceiroContainer, text="Run simulation",
                           width=12,  # Ajustado para largura em pixels
                           height=30,corner_radius=8,command=self.simulation)
        self.simu.pack(side=RIGHT,padx=5)

        ##################################################
        ###Forms do mesh properties

        # Construção do container para a entrada de xmax
        self.segundo2Container = cttk.CTkFrame(self.segundoContainer)
        self.segundo2Container.pack(pady=8, padx=20,fill="both", expand=True)

        self.xmaxLabel = cttk.CTkLabel(self.segundo2Container, 
                              text="Size of the domain in x direction (m): ")
        self.xmaxLabel.pack(side="left")
        self.xmax = cttk.CTkEntry(self.segundo2Container, 
                         width=300, 
                         placeholder_text="0.09")
        self.xmax.pack(side="right")
        
        # Construção do container para a entrada de ymax
        self.terceiro2Container = cttk.CTkFrame(self.segundoContainer)
        self.terceiro2Container.pack(pady=8, padx=20,fill="both", expand=True)

        self.ymaxLabel = cttk.CTkLabel(self.terceiro2Container, 
                              text="Size of the domain in y direction (m): ")
        self.ymaxLabel.pack(side="left")
        self.ymax = cttk.CTkEntry(self.terceiro2Container, 
                         width=300, 
                         placeholder_text="0.09")
        self.ymax.pack(side="right")
        
        # Construção do container para a entrada de zmax
        self.quarto2Container = cttk.CTkFrame(self.segundoContainer)
        self.quarto2Container.pack(pady=8, padx=20,fill="both", expand=True)

        self.zmaxLabel = cttk.CTkLabel(self.quarto2Container, 
                              text="Size of the domain in z direction (m): ")
        self.zmaxLabel.pack(side="left")
        self.zmax = cttk.CTkEntry(self.quarto2Container, 
                         width=300, 
                         placeholder_text="0.01")
        self.zmax.pack(side="right")
        
        # Construção do container para a entrada de xnode
        self.quinto2Container = cttk.CTkFrame(self.segundoContainer)
        self.quinto2Container.pack(pady=8, padx=20,fill="both", expand=True)

        self.xnodeLabel = cttk.CTkLabel(self.quinto2Container, 
                              text="Amount of nodes in the x direction: ")
        self.xnodeLabel.pack(side="left")
        self.xnode = cttk.CTkEntry(self.quinto2Container, 
                         width=300, 
                         placeholder_text="500")
        self.xnode.pack(side="right")
        
        # Construção do container para a entrada de ynode
        self.sexto2Container = cttk.CTkFrame(self.segundoContainer)
        self.sexto2Container.pack(pady=8, padx=20,fill="both", expand=True)

        self.ynodeLabel = cttk.CTkLabel(self.sexto2Container, 
                              text="Amount of nodes in the y direction: ")
        self.ynodeLabel.pack(side="left")
        self.ynode = cttk.CTkEntry(self.sexto2Container, 
                         width=300, 
                         placeholder_text="500")
        self.ynode.pack(side="right")
        
        # Construção do container para a entrada de znode
        self.setimo2Container = cttk.CTkFrame(self.segundoContainer)
        self.setimo2Container.pack(pady=8, padx=20,fill="both", expand=True)

        self.znodeLabel = cttk.CTkLabel(self.setimo2Container, 
                              text="Amount of nodes in the z direction: ")
        self.znodeLabel.pack(side="left")
        self.znode = cttk.CTkEntry(self.setimo2Container, 
                         width=300, 
                         placeholder_text="1")
        self.znode.pack(side="right")
        
        #botão de gerar jason
        self.autenticar = cttk.CTkButton(self.segundoContainer, text="Ok",
                           width=150,  # Ajustado para largura em pixels
                           height=40,command=self.gera_json_malha)
        self.autenticar.pack(side=BOTTOM,padx=5,fill="none", expand=False)
        ######################

        ###Forms do time properties

        self.data={}

        ##Endtime
        
        self.controlcontainer1=cttk.CTkFrame(self.segundoContainer_main)
        self.controlcontainer1.pack(pady=10, padx=10,fill="both", expand=True)

        self.endtimeLabel = cttk.CTkLabel(self.controlcontainer1, 
                              text="Final simulation time (s): ")
        self.endtimeLabel.pack(side="left")
        self.endtime = cttk.CTkEntry(self.controlcontainer1, 
                         width=300, 
                         placeholder_text="600")
        self.endtime.pack(side="right")

        
        ##Timestep

        self.controlcontainer2=cttk.CTkFrame(self.segundoContainer_main)
        self.controlcontainer2.pack(pady=10, padx=10,fill="both", expand=True)

        self.timestepLabel = cttk.CTkLabel(self.controlcontainer2, 
                              text="Time step (s): ")
        self.timestepLabel.pack(side="left")
        self.timestep = cttk.CTkEntry(self.controlcontainer2, 
                         width=300, 
                         placeholder_text="0.1")
        self.timestep.pack(side="right")
        
        ## Botão para confirmar
        self.autenticarcontrol = cttk.CTkButton(self.segundoContainer_main, text="Ok",
                           width=150,  # Ajustado para largura em pixels
                           height=40,command=self.save_control)
        self.autenticarcontrol.pack(side=BOTTOM,padx=5,fill="none", expand=False)

        #########################

        ## Forms do Field parameters

        # Entrada do campo magnético
        self.fieldcontainer1=cttk.CTkFrame(self.segundoContainer_main_down)
        self.fieldcontainer1.pack(pady=10, padx=10,fill="both", expand=True)

        self.magnetic_fieldLabel = cttk.CTkLabel(self.fieldcontainer1, 
                              text="Maximum applied field (A/m): ")
        self.magnetic_fieldLabel.pack(side="left")
        self.magnetic_field = cttk.CTkEntry(self.fieldcontainer1, 
                         width=300, 
                         placeholder_text="1.0e+5")
        self.magnetic_field.pack(side="right")

        # Entrada da frequência do campo
        self.fieldcontainer2=cttk.CTkFrame(self.segundoContainer_main_down)
        self.fieldcontainer2.pack(pady=10, padx=10,fill="both", expand=True)

        self.freqLabel = cttk.CTkLabel(self.fieldcontainer2, 
                              text="Frequency of the applied field (Hz): ")
        self.freqLabel.pack(side="left")
        self.freq = cttk.CTkEntry(self.fieldcontainer2, 
                         width=300, 
                         placeholder_text="1.84e+05")
        self.freq.pack(side="right")

        # Entrada da parte imaginária do campo magnético

        self.fieldcontainer3=cttk.CTkFrame(self.segundoContainer_main_down)
        self.fieldcontainer3.pack(pady=10, padx=10,fill="both", expand=True)
        
        self.comp_susLabel = cttk.CTkLabel(self.fieldcontainer3, 
                              text="Imaginary part of the complex susceptibility: ")
        self.comp_susLabel.pack(side="left")
        self.comp_sus = cttk.CTkEntry(self.fieldcontainer3, 
                         width=300, 
                         placeholder_text="1.6285e-02")
        self.comp_sus.pack(side="right")

        # Entrada do volume de partículas magnéticas

        self.fieldcontainer4=cttk.CTkFrame(self.segundoContainer_main_down)
        self.fieldcontainer4.pack(pady=10, padx=10,fill="both", expand=True)

        self.fi_fieldLabel = cttk.CTkLabel(self.fieldcontainer4, 
                              text="Volume fraction of particles: ")
        self.fi_fieldLabel.pack(side="left")
        self.fi = cttk.CTkEntry(self.fieldcontainer4, 
                         width=300, 
                         placeholder_text="0.033")
        self.fi.pack(side="right")

        # Botão de confirmação
        self.autenticar_field = cttk.CTkButton(self.segundoContainer_main_down, text="Ok",
                           width=150,  # Ajustado para largura em pixels
                           height=40,command=self.gera_json_field)
        self.autenticar_field.pack(side=BOTTOM,padx=5,fill="none", expand=False)

        #####################################################################

        # Forms para adicionar parâmetros dos tumores e pontos de injeção

        self.tumor_windows = []
        self.fluid_windows = []
        ## Abre janel
        
        ## Containers principais
        self.middleContainer_sub = cttk.CTkFrame(self.middleContainer)
        self.middleContainer_sub.pack(side=LEFT,pady=8, padx=10)
        self.middleContainer_sub2= cttk.CTkFrame(self.middleContainer)
        self.middleContainer_sub2.pack(side=RIGHT,pady=8, padx=10)

        ##Container secundários para form do tumor properties
        
        self.uniqueContainer = cttk.CTkFrame(self.middleContainer_sub)
        self.uniqueContainer.pack(pady=10, padx=8)

        # Título do container relativo ao tumor
        self.tumor_count_numlabel = cttk.CTkLabel(self.uniqueContainer, 
                              text="How many tumors ")
        self.tumor_count_numlabel.pack(side="left")
       
        ## Variável de entrada que conta os tumores
        tumor_count_num = cttk.CTkEntry(self.uniqueContainer, 
                         width=300, 
                         placeholder_text="2")
        tumor_count_num.pack(side="left")

        ##Container secundário para form do magnetic fluid properties

        self.uniqueContainer2 = cttk.CTkFrame(self.middleContainer_sub2)
        self.uniqueContainer2.pack(pady=10, padx=8)

        # Título do container relativo ao fluido magnético
        self.fluid_count_numlabel = cttk.CTkLabel(self.uniqueContainer2, 
                              text="Amount of magnetic fluid's injection points ")
        self.fluid_count_numlabel.pack(side="left")
        
        ## Variável de entrada que conta os pontos de injeção
        fluid_count_num = cttk.CTkEntry(self.uniqueContainer2, 
                         width=300, 
                         placeholder_text="2")
        fluid_count_num.pack(side="left")
        
        ## Botão de ok tumor
        self.tumorbutton = cttk.CTkButton(self.middleContainer_sub, text="Ok",
                           width=150,  # Ajustado para largura em pixels
                           height=40,command=lambda: self.submit_tumor(tumor_count_num))
        self.tumorbutton.pack(side=BOTTOM,padx=5)

        ## Botão de ok fluido magnético
        self.fluidbutton = cttk.CTkButton(self.middleContainer_sub2, text="Ok",
                           width=150,  # Ajustado para largura em pixels
                           height=40,command=lambda: self.submit_fluid(fluid_count_num))
        self.fluidbutton.pack(side=BOTTOM,padx=5)
        
        ######################################################################
        
        ## Botão para adicionar Pré-visualização
        
        self.visu = cttk.CTkButton(self.terceiroContainer, text="Pre-visualization",
                           width=12,  # Ajustado para largura em pixels
                           height=30,corner_radius=8,command=self.visual)
        self.visu.pack(side=LEFT,padx=5)

    ## Aqui conta a quantidade de tumores e abre a quantidade de janelas correspondente a entrada
    def submit_tumor(self,tumor_count_num):
            #nonlocal tumor_count
            tumor_count = int(tumor_count_num.get())
            self.open_tumor_data_screens(tumor_count)
            self.tumor_count.destroy()
            return tumor_count
    ## Aqui conta a quantidade de pontos de injeção e abre a quantidade de janelas correspondente a entrada
    def submit_fluid(self,fluid_count_num):
            #nonlocal fluid_count
            fluid_count = int(fluid_count_num.get())
            self.open_fluid_data_screens(fluid_count)
            self.fluid_count.destroy()
            return fluid_count

    ## Aqui salva as informações temporais em arquivo json

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
        #self.control.destroy()

    #Função para fechar tela após o ok ser pressionado (tumores)
    def window_destroymesh(self):
        self.confirmationmesh.destroy()
    #Função para fechar tela após o ok ser pressionado (fluido magnético)
    def window_destroymeshfield(self):
        self.confirmationfield.destroy()
    
    ###########################################   

    ### Funções para gerar Arquivos Json (Field properties)
    def gera_json_field(self):
        import json

        inputDict_fields_properties = {}
        inputDict_fields_properties["Magnetic_intensity"] = self.magnetic_field.get()
        inputDict_fields_properties["Magnetic_frequency"] = self.freq.get()
        inputDict_fields_properties["complex_susceptibility"] = self.comp_sus.get()
        inputDict_fields_properties["volume_fraction"] = self.fi.get()

        json_string_m = json.dumps(inputDict_fields_properties, indent=4)
        self.outJson_m="inputDict_mhtQuantities.json"
        self.jason_quantities.append(self.outJson_m)
        
        with open(self.outJson_m,"w") as f:
            f.write(json_string_m)
        f.close()

        #Container principal
        self.confirmationfield = cttk.CTkToplevel(root_1)
        

        self.confContainerfield = cttk.CTkFrame(self.confirmationfield)
        self.confContainerfield.pack(pady=10, padx=20)
        
        ## Título do container
        self.confirmationfield.title("Confirmation")
        self.confirmationfieldLabel = cttk.CTkLabel(self.confContainerfield, 
                              text="Field properties successfully saved")
        self.confirmationfieldLabel.pack(side="left")

        ## Botão de confirmação
        self.confirmationfieldbutton = cttk.CTkButton(self.confirmationfield, text="Ok",
                           width=150,  # Ajustado para largura em pixels
                           height=40,command=self.window_destroymeshfield)
        self.confirmationfieldbutton.pack(side=BOTTOM,padx=5)

    ## Aqui gera o arquivo json para os dados do domínio de cálculo e malha

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
        
        # Título do container
        self.confirmationmesh.title("Confirmation")
        self.confirmationmeshLabel = cttk.CTkLabel(self.confContainermesh, 
                              text="Mesh properties successfully saved")
        self.confirmationmeshLabel.pack(side="left")
        
        ## Botão de confirmação
        self.confirmationmeshbutton = cttk.CTkButton(self.confirmationmesh, text="Ok",
                           width=150,  # Ajustado para largura em pixels
                           height=40,command=self.window_destroymesh)
        self.confirmationmeshbutton.pack(side=BOTTOM,padx=5)

    # Tela que pergunta quantos tumores é definido aqui
    def tumors(self):
        ## Conta quantidade de telas relativa a quantidade de tumores e fecha tela
        def submit():
            nonlocal tumor_count
            tumor_count = int(tumor_count_num.get())
            self.open_tumor_data_screens(tumor_count)
            #self.tumor_count.destroy()
        tumor_count = None

    # Tela que pergunta quantos pontos de injeção é definido aqui
    def fluids(self):
        ## Conta quantidade de telas relativa a quantidade de tumores e fecha tela
        def submit():
            nonlocal fluid_count
            fluid_count = int(fluid_count_num.get())
            self.open_fluid_data_screens(fluid_count)
            #self.fluid_count.destroy()
        fluid_count = None
        
    ##Aqui define em que posição da tela vai abrir e chama a função que abre as novas telas para cada tumor
    def open_tumor_data_screens(self, tumor_count):
        self.count1=int(tumor_count)
        for i in range(0,tumor_count):
            self.largura_tela2=self.largura_tela+(i-1)*80
            self.altura_tela2=self.altura_tela+(i-1)*100
            self.collect_tumor_data(i,tumor_count)

    ##Aqui define em que posição da tela vai abrir e chama a função que abre as novas telas para cada ponto de injeção
    def open_fluid_data_screens(self, fluid_count):
        self.count2=int(fluid_count)
        for i in range(0,fluid_count):
            self.largura_tela2=self.largura_tela+(i-1)*80
            self.altura_tela2=self.altura_tela+(i-1)*100
            self.collect_fluid_data(i,fluid_count)

    #############################################
    def collect_fluid_data(self, index, fluid_count):
        
        self.current_index_f=index
        self.fluid_data_entries[index] = {}
        
        ##Abre Tela
        self.fluid_window = cttk.CTkToplevel(root_1)
        self.fluid_window.title(f"Magnetic fluid's Injection Site {index + 1}")
        self.fluid_window.geometry(f'380x220+{self.largura_tela2}+{self.altura_tela2}')
        self.fluid_windows.append(self.fluid_window)
        
        # Campo para entrada do volume

        self.primeiro5Container_f= cttk.CTkFrame(self.fluid_window)
        self.primeiro5Container_f.pack(pady=10, padx=20)

        self.volumeLabel = cttk.CTkLabel(self.primeiro5Container_f, 
                              text="Volume (m³): ")
        self.volumeLabel.pack(side="left")
        self.volume = cttk.CTkEntry(self.primeiro5Container_f, 
                         width=300, 
                         placeholder_text="9.902e-08")
        self.volume.pack(side="left")
        self.fluid_data_entries[index]["volume"] = self.volume
        
        # Campo para entrada da posição x

        self.segundo5Container_f = cttk.CTkFrame(self.fluid_window)
        self.segundo5Container_f.pack(pady=10, padx=20)

        self.posxLabel_f = cttk.CTkLabel(self.segundo5Container_f, 
                              text="x position of the magnetic fluid drop: ")
        self.posxLabel_f.pack(side="left")
        self.posx_f = cttk.CTkEntry(self.segundo5Container_f, 
                         width=300, 
                         placeholder_text="0.045")
        self.posx_f.pack(side="left")
        self.fluid_data_entries[index]["posx_f"] = self.posx_f
        
        # Campo para entrada da posição y
        self.terceiro5Container_f = cttk.CTkFrame(self.fluid_window)
        self.terceiro5Container_f.pack(pady=10, padx=20)

        self.posyLabel_f = cttk.CTkLabel(self.terceiro5Container_f, 
                              text="y position of the magnetic fluid drop: ")
        self.posyLabel_f.pack(side="left")
        self.posy_f = cttk.CTkEntry(self.terceiro5Container_f, 
                         width=300, 
                         placeholder_text="0.045")
        self.posy_f.pack(side="left")
        self.fluid_data_entries[index]["posy_f"] = self.posy_f
        
        
        ## Botão de ok
        self.autenticar_magfluid = cttk.CTkButton(self.fluid_window, text="Ok",
                           width=150,  # Ajustado para largura em pixels
                           height=40,command=lambda win=self.fluid_window, idx=index, total=fluid_count: self.gera_json_fluid(win, idx, total))
        self.autenticar_magfluid.pack(side=BOTTOM,padx=5)

        ##############################################
    ## Tela para coleta de info de tumor
    def collect_tumor_data(self, index, tumor_count):
        
        self.current_index=index
        self.tumor_data_entries[index] = {}
        
        ##Abre Tela
        self.tumor_window = cttk.CTkToplevel(root_1)
        self.tumor_window.title(f"Tumor {index + 1} Data")
        self.tumor_window.geometry(f'300x300+{self.largura_tela2}+{self.altura_tela2}')
        self.tumor_windows.append(self.tumor_window)
        
        # raio,excentricidade,posição x, posição y, inclinação em graus
        
        # Campo para entrada do raio
        self.primeiro5Container = cttk.CTkFrame(self.tumor_window)
        self.primeiro5Container.pack(pady=10, padx=20)

        self.radiusLabel = cttk.CTkLabel(self.primeiro5Container, 
                              text="Equivalent radius: ")
        self.radiusLabel.pack(side="left")
        self.radius = cttk.CTkEntry(self.primeiro5Container, 
                         width=300, 
                         placeholder_text="0.005")
        self.radius.pack(side="left")
        self.tumor_data_entries[index]["radius"] = self.radius
        

        # Campo para entrada da excentricidade
        self.segundo5Container = cttk.CTkFrame(self.tumor_window)
        self.segundo5Container.pack(pady=10, padx=20)

        self.eccenLabel = cttk.CTkLabel(self.segundo5Container, 
                              text="eccentricity: ")
        self.eccenLabel.pack(side="left")
        self.eccen = cttk.CTkEntry(self.segundo5Container, 
                         width=300, 
                         placeholder_text="0.9")
        self.eccen.pack(side="right")
        self.tumor_data_entries[index]["eccen"] = self.eccen
        
        # Campo para entrada da posição x
        self.terceiro5Container = cttk.CTkFrame(self.tumor_window)
        self.terceiro5Container.pack(pady=10, padx=20)

        self.posxLabel = cttk.CTkLabel(self.terceiro5Container, 
                              text="x position of the tumor: ")
        self.posxLabel.pack(side="left")
        self.posx = cttk.CTkEntry(self.terceiro5Container, 
                         width=300, 
                         placeholder_text="0.045")
        self.posx.pack(side="left")
        self.tumor_data_entries[index]["posx"] = self.posx
        
        # Campo para entrada da posição y
        self.quarto5Container = cttk.CTkFrame(self.tumor_window)
        self.quarto5Container.pack(pady=10, padx=20)

        self.posyLabel = cttk.CTkLabel(self.quarto5Container, 
                              text="y position of the tumor: ")
        self.posyLabel.pack(side="left")
        self.posy = cttk.CTkEntry(self.quarto5Container, 
                         width=300, 
                         placeholder_text="0.045")
        self.posy.pack(side="left")
        self.tumor_data_entries[index]["posy"] = self.posy
        
        # Campo para entrada da inclinação
        self.quinto5Container = cttk.CTkFrame(self.tumor_window)
        self.quinto5Container.pack(pady=10, padx=20)

        self.inclinationLabel = cttk.CTkLabel(self.quinto5Container, 
                              text="Inclination of the tumor (º): ")
        self.inclinationLabel.pack(side="left")
        self.inclination = cttk.CTkEntry(self.quinto5Container, 
                         width=300, 
                         placeholder_text="30")
        self.inclination.pack(side="left")
        self.tumor_data_entries[index]["inclination"] = self.inclination
        
        ## Botão de ok

        self.autenticar_tumor = cttk.CTkButton(self.tumor_window, text="Ok",
                           width=150,  # Ajustado para largura em pixels
                           height=40,command=lambda win=self.tumor_window, idx=index, total=tumor_count: self.gera_json_tumor(win, idx, total))
        self.autenticar_tumor.pack(side=BOTTOM,padx=5)
    
    #Função associada à fechar as telas de entrada dos parâmetros dos tumores
    def window_destroy(self):
            self.tumor_window.destroy()
            self.confirmation.destroy()
            #self.tumor_count.destroy()
    def windowmag_destroy(self):
            self.fluid_window.destroy()
            self.confirmation_f.destroy()
            #self.fluid_count.destroy()
    
    ## Gera rquivo json com os dados dos tumores
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
            
            self.confirmation.title("Confirmation")
            self.confirmationLabel = cttk.CTkLabel(self.confContainer, 
                              text="Tumours data successfuly saved")
            self.confirmationLabel.pack(side="left")
            
            ## Botão de ok
            self.confirmationbutton = cttk.CTkButton(self.confContainer1, text="Ok",
                           width=150,  # Ajustado para largura em pixels
                           height=40,command=self.window_destroy)
            self.confirmationbutton.pack(side=LEFT,padx=5)
        else:
            window.destroy()

    def gera_json_fluid(self,window,index,fluid_count):
        """Aqui salva os dados dos fluidos magnéticos no arquivo jason"""
        import json        
        indexx_f=index+1
        ## Salva os dados coletados em inputDict_ID
        inputDict_magflu = {
            f"volume_{indexx_f}": self.fluid_data_entries[index]["volume"].get(),
            f"posx_{indexx_f}": self.fluid_data_entries[index]["posx_f"].get(),
            f"posy_{indexx_f}": self.fluid_data_entries[index]["posy_f"].get(),
        }
        
        ##Salva em self.data_t
        self.data_tmag["magnetic_fluid"].append(inputDict_magflu)
        #self.data_t.append(inputDict_ID)
        
        json_string_f = json.dumps(inputDict_magflu, indent=4)
        self.outJson3="inputDict_magflu.json"
        self.jason_quantities.append(self.outJson3)
        
        #Abaixo fecha as janelas onde entramos com os dados dos tumores a medida que clica-se "Gerar Json"
        #A última tela gera uma janela de confirmação e só ela que gera a mensagem de confirmação
        
        ##Salva no jason
        if len(self.data_tmag["magnetic_fluid"]) == fluid_count:
            with open(self.outJson3, "w") as f:
                json.dump(self.data_tmag, f, indent=4)
   
            ##Abre janela de confirmação e containers
            self.confirmation_f = cttk.CTkToplevel(root_1)
            
            self.confContainerf = cttk.CTkFrame(self.confirmation_f)
            self.confContainerf.pack(pady=10, padx=20)
            self.confContainer1f =cttk.CTkFrame(self.confirmation_f)
            self.confContainer1f.pack(pady=10, padx=20)
            
            self.confirmation_f.title("Confirmation")
            self.confirmation_fLabel = cttk.CTkLabel(self.confContainerf, 
                              text="Magnetic fluid's injection data successfuly saved")
            self.confirmation_fLabel.pack(side="left")
            
            ## Botão de ok
            self.confirmationf_fbutton = cttk.CTkButton(self.confContainer1f, text="Ok",
                           width=150,  # Ajustado para largura em pixels
                           height=40,command=self.windowmag_destroy)
            self.confirmationf_fbutton.pack(side=LEFT,padx=5)
        else:
            window.destroy()  
    def gera_setup(self):
        """Aqui gera o setup"""
    	# Gerar o setup é substituir os dados coletados nos respectivos arquivos
        import json
        import os
        allpre_dir = "../../tutorials/mhtFoam/2d_circular_tumour"
        # Muda o diretório de trabalho para o local do Allpre
        os.chdir(allpre_dir)
        # Limpa pasta e prepara a simulação copiando arquivos da pasta 0 e system de volta
        os.system("./Allclean")
        os.system("./Allpre")
        # Gera o json caso o usuario se esqueça
        self.gera_json_tumor
        self.gera_json_malha
        self.gera_json_fluid

        indexx=self.current_index+1
        indexx_f=self.current_index_f+1
        base_dir = "../../scripts/pythonscripts"

        # Construir os caminhos completos para cada arquivo JSON
        json_file_path1 = os.path.join(os.path.dirname(os.path.abspath(__file__)), "inputDict_blockMeshDict.json")
        json_file_path3 = os.path.join(os.path.dirname(os.path.abspath(__file__)), "inputDict_controlDict.json")
        json_file_path2 = os.path.join(os.path.dirname(os.path.abspath(__file__)), "inputDict_ID.json")
        json_file_path4 = os.path.join(os.path.dirname(os.path.abspath(__file__)), "inputDict_magflu.json")
        json_file_path5 = os.path.join(os.path.dirname(os.path.abspath(__file__)), "inputDict_mhtQuantities.json")
        

        ## Aqui chama o outro arquivo substitute_values_2 e altera os arquivos de acordo com as funções de lá

        with open(json_file_path1,'r') as f:
            data = json.load(f)
        inputDict = generate_dictionary_2(data)
        changeFileDict(inputDict)

        with open(json_file_path3,'r') as f:
            data = json.load(f)
        inputDict = generate_dictionary_1(data)
        changeFileDict(inputDict)

        with open(json_file_path2,'r') as f:
            data = json.load(f)
        inputDict = generate_dictionary_3(data,indexx)
        changeFileDict_2(inputDict)

        with open(json_file_path4,'r') as f:
            data = json.load(f)
        inputDict = generate_dictionary_4(data,indexx_f)
        changeFileDict_4(inputDict)

        with open(json_file_path5,'r') as f:
            data = json.load(f)
        inputDict = generate_dictionary_5(data)
        changeFileDict(inputDict)

    def visual(self):
        """Aqui é a função de pré visualização da configuração escolhida"""
        
        ##Abre janela
        visuwind = cttk.CTkToplevel(root_1)
        visuwind.title("Preview window")
        
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
        allpre_dir = "../../../tutorials/mhtFoam/2d_circular_tumour"
        import os
        os.chdir(allpre_dir)
        os.system("./Allrun &")
        
# Inicializa a interface gráfica
root_1 = cttk.CTk()
app = Main_wind(root_1)
zaragui = app # Inicialização

zaragui.interface()

root_1.mainloop()


