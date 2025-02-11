import tkinter as tk
from tkinter import *
from tkinter import simpledialog, messagebox, Tk, Frame, Label, LEFT, RIGHT, Button, Entry,font
import customtkinter as cttk
from matplotlib.figure import Figure
from matplotlib.patches import Ellipse
from PIL import ImageTk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np
import os
import json
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, Ellipse
import matplotlib.patches as patches

class Main_wind_pos:
    ## Abre a tela inicial e estabelece algumas informações a serem usadas no meio do código
    def __init__(self, root_1):
        self.root_1 = root_1
        self.root_1.title("mhtFoam post-processing")
        self.fontePadrao = ("Adobe Myungjo Std M", "11")
        self.fonteBotoes = ("Arial", "10")
        cttk.set_appearance_mode("Dark")
        self.extra_data_entries = {}
        
        largura_tela_1 = self.root_1.winfo_screenwidth()
        altura_tela_1 = self.root_1.winfo_screenheight()
        self.largura_tela = largura_tela_1//4
        self.altura_tela = altura_tela_1//3
        self.root_1.geometry(f'1000x500+{self.largura_tela}+{self.altura_tela}')
    def interface(self):
        ## Aqui deixa já aberto as seguintes funções
        self.extra_data_entries = {}
        self.data_t = {"extra": []}
        self.extra_windows = []
        self.jason_quantities = []
        ## Aqui deixa já aberto as seguintes funções
        self.define_titulo()
        self.view_screen()
        self.user_data()
    def define_titulo(self):
        """
        Função responsável pela construção da parte relativa ao título na interface
        """
        # Construção do container para título da janela

        self.primeiroContainer = cttk.CTkFrame(self.root_1, corner_radius=15, fg_color="#2B2B2B")
        self.primeiroContainer.pack(pady=10, padx=25, fill="x")
        
        #Texto da intro do mhtFoam

        texto1= """Welcome to the mhtFoam post-processing interface! Here you can visualize the results of the mhtFoam solver."""

        # Atribuição do título dentro da janela (1a informação exibida)

        self.titulo = cttk.CTkLabel(

        self.primeiroContainer,
        text=texto1,
        #justify="center",
        font=("Ubuntu", 15, "bold"),
        text_color="white",  # Melhor contraste no fundo escuro
        wraplength=498,  # Mantém a formatação organizada 
        justify="center"
        )
        self.titulo.pack(pady=8, padx=15)
    def view_screen(self):
        ## Abre a tela de visualização
        self.view_screen = cttk.CTkFrame(self.root_1, corner_radius=40)
        self.view_screen.pack(side=LEFT, pady=10, padx=25)
        script_dir = os.path.dirname(os.path.realpath(__file__))

        with open('inputDict_blockMeshDict.json', 'r') as json_file:
            domain_info = json.load(json_file)

        with open('inputDict_controlDict.json', 'r') as json_file:
            domain_info2 = json.load(json_file)
        with open('inputDict_ID.json', 'r') as json_file:
            domain_info3 = json.load(json_file)
        with open('inputDict_magflu.json', 'r') as json_file:
            domain_info4 = json.load(json_file)

        # Extrair as informações de domínio
        xmax = float(domain_info["xmax"])
        ymax = float(domain_info["ymax"])

        endtime = int(domain_info2["endtime"])
        fig, ax = plt.subplots(figsize=(5, 5), dpi=100)
        #ax = fig.add_subplot(111)
        ax.set_xlim(0, xmax)
        ax.set_ylim(0, ymax)
        ax.set_xlabel("X")
        ax.set_ylabel("Y")
        ax.set_aspect('equal')
        ax.set_title("Domínio da Simulação")
        ax.grid(True, which='both', linestyle='--', linewidth=0.5, color='gray', alpha=0.7)

        round_rect = patches.FancyBboxPatch(
            (0, 0), xmax, ymax,  # Posição e tamanho
            boxstyle="round,pad=0.1",  # Bordas arredondadas
            facecolor="white",  # Cor do fundo
            edgecolor="black",  # Cor da borda
            linewidth=2,  # Espessura da borda
            alpha=0.7  # Transparência
            )
        
        # Plotando os tumores
        tumor_count = 1
        
        if "tumors" not in domain_info3 or not domain_info3["tumors"]:
            print("Nenhum tumor encontrado!")
        else:
            for tumor in domain_info3["tumors"]:  # Iterar diretamente sobre a lista
                try:
                    radius = float(tumor[f"radius_{tumor_count}"])
                    eccen = float(tumor[f"eccen_{tumor_count}"])
                    posx = float(tumor[f"posx_{tumor_count}"])
                    posy = float(tumor[f"posy_{tumor_count}"])
                    inclination = float(tumor[f"inclination_{tumor_count}"])
                except KeyError:
                    print(f"Erro: Chave ausente no tumor {tumor_count}")
                    continue  # Pula para o próximo tumor
                
                if eccen == 0:
                    tumor_circle = Circle((posx, posy), radius, color='blue')
                    ax.add_patch(tumor_circle)
                else:
                    inclination_rad = np.radians(inclination)
                    semi_major_axis = radius
                    semi_minor_axis = radius * eccen

                    # Correção na geração da elipse
                    t = np.linspace(0, 2 * np.pi, 100)
                    ellipse_x = radius/(np.sqrt(1-eccen**2)) * np.cos(t)
                    ellipse_y = radius * np.sin(t)

                    # Rotação correta da elipse
                    x_rot = posx + ellipse_x * np.cos(inclination_rad) - ellipse_y * np.sin(inclination_rad)
                    y_rot = posy + ellipse_x * np.sin(inclination_rad) + ellipse_y * np.cos(inclination_rad)

                    ax.fill(x_rot, y_rot, color='blue')

                tumor_count += 1  # Incrementa corretamente para o próximo tumor

            ###############################################################################################
            ###############################################################################################
        #while True:
        fluid_count = 1
        if "magnetic_fluid" not in domain_info4 or not domain_info4["magnetic_fluid"]:
            print("Nenhum tumor encontrado!")
        else:
            for fluid in domain_info4["magnetic_fluid"]:  # Iterar diretamente sobre a lista
                try:
                    posxm = float(fluid[f"posx_{fluid_count}"])
                    posym = float(fluid[f"posy_{fluid_count}"])
                    volume = float(fluid[f"volume_{fluid_count}"])
                    volume_mag = volume*(10**(-6))
                except KeyError:
                    print(f"Erro: Chave ausente no tumor {fluid_count}")
                    continue  # Pula para o próximo tumor
                # Calcular o raio do fluido magnético a partir do volume
                radius = ((3 * volume_mag) / (4 * np.pi)) ** (1 / 3)

                # Criar um círculo para o fluido magnético
                fluid_circle = Circle(
                    (posxm, posym), 
                    radius, 
                    color='black'
                )
                ax.add_patch(fluid_circle)

                fluid_count += 1  # Incrementa para verificar o próximo fluido magnético
        # Criar e inserir o gráfico no frame
        #ax.add_patch(round_rect)
        canvas = FigureCanvasTkAgg(fig, master=self.view_screen)
        canvas.draw()
        canvas.get_tk_widget().pack()
    def user_data(self):
        # Aqui coleta os dados do usuário quanto a onde plotar os gráficos
        self.coleta_main_data = cttk.CTkFrame(self.root_1, corner_radius=15)
        self.coleta_main_data.pack(side=RIGHT, pady=10, padx=25)

        self.coleta_data = cttk.CTkFrame(self.coleta_main_data, corner_radius=15)
        self.coleta_data.pack( pady=10, padx=25)

        self.extra_count_numlabel = cttk.CTkLabel(self.coleta_data, 
                              text="Number of extraction points: ")
        self.extra_count_numlabel.pack(side="left")

        extra_count_num = cttk.CTkEntry(self.coleta_data, 
                         width=300, 
                         placeholder_text="2")
        extra_count_num.pack(side="right")

        self.tumorbutton = cttk.CTkButton(self.coleta_main_data, text="Ok",
                           width=150,  # Ajustado para largura em pixels
                           height=40,command=lambda: self.submit_extra(extra_count_num))
        self.tumorbutton.pack(side=BOTTOM,pady=5,padx=5)


    def submit_extra(self,extra_count_num):
            #nonlocal tumor_count
            points_count = int(extra_count_num.get())
            self.open_extra_data_screens(points_count)
            #self.points_count.destroy()
            return points_count
    def open_extra_data_screens(self, points_count):
        self.count1=int(points_count)
        for i in range(0,points_count):
            self.largura_tela2=self.largura_tela+(i-1)*80
            self.altura_tela2=self.altura_tela+(i-1)*100
            self.collect_extra_data(i,points_count)
    def collect_extra_data(self, index, points_count): 
        self.current_index=index
        self.extra_data_entries[index] = {}
        ##Abre Tela
        self.extra_window = cttk.CTkToplevel(root_1)
        self.extra_window.title(f"Point {index + 1} of extraction")
        self.extra_window.geometry(f'300x150+{self.largura_tela2}+{self.altura_tela2}')
        self.extra_windows.append(self.extra_window)
        
        # posição x, posição y
        
        # Campo para entrada da posição x
        self.primeiro5Container = cttk.CTkFrame(self.extra_window)
        self.primeiro5Container.pack(pady=10, padx=20)

        self.posxLabel = cttk.CTkLabel(self.primeiro5Container, 
                              text="x position: ")
        self.posxLabel.pack(side="left")
        self.posx = cttk.CTkEntry(self.primeiro5Container, 
                         width=300, 
                         placeholder_text="0.045")
        self.posx.pack(side="left")
        self.extra_data_entries[index]["posx"] = self.posx
        

        # Campo para entrada da posição y
        self.segundo5Container = cttk.CTkFrame(self.extra_window)
        self.segundo5Container.pack(pady=10, padx=20)

        self.posyLabel = cttk.CTkLabel(self.segundo5Container, 
                              text="y position: ")
        self.posyLabel.pack(side="left")
        self.posy = cttk.CTkEntry(self.segundo5Container, 
                         width=300, 
                         placeholder_text="0.045")
        self.posy.pack(side="right")
        self.extra_data_entries[index]["posy"] = self.posy
        
        ## Botão de ok

        self.autenticar_tumor = cttk.CTkButton(self.extra_window, text="Ok",
                           width=150,  # Ajustado para largura em pixels
                           height=40,command=lambda win=self.extra_window, idx=index, total=points_count: self.gera_json_extra(win, idx, total))
        self.autenticar_tumor.pack(side=BOTTOM,padx=5)
    def gera_json_extra(self,window,index,points_count):
        """Aqui salva os dados dos tumores no arquivo jason"""
        import json
        #self.indexx = indexx
        
        indexx=index+1
        ## Salva os dados coletados em inputDict_ID
        inputDict_extra = {
            f"posx_{indexx}": self.extra_data_entries[index]["posx"].get(),
            f"posy_{indexx}": self.extra_data_entries[index]["posy"].get(),

        }
        
        ##Salva em self.data
        self.data_t["extra"].append(inputDict_extra)
        #self.data_t.append(inputDict_ID)
        
        json_string = json.dumps(inputDict_extra, indent=4)
        self.outJson2="inputDict_extraction.json"
        self.jason_quantities.append(self.outJson2)
        
        #Abaixo fecha as janelas onde entramos com os dados dos tumores a medida que clica-se "Gerar Json"
        #A última tela gera uma janela de confirmação e só ela que gera a mensagem de confirmação
        
        ##Salva no jason
        if len(self.data_t["extra"]) == points_count:
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
                              text="points of extraction data successfuly saved")
            self.confirmationLabel.pack(side="left")
            
            ## Botão de ok
            self.confirmationbutton = cttk.CTkButton(self.confContainer1, text="Ok",
                           width=150,  # Ajustado para largura em pixels
                           height=40,command=self.destroywindow)
            self.confirmationbutton.pack(side=LEFT,padx=5)
        else:
            window.destroy()
    def destroywindow(self):
            self.extra_window.destroy()
            self.confirmation.destroy()
            self.change_file()
    def change_file(self):
        self.confirmation.destroy()
        # Carregar o arquivo controlDict
        dir = os.path.dirname(os.path.abspath("../../tutorials/mhtFoam/2d_circular_tumour"))
        control_dict_path = os.path.join(dir, "2d_circular_tumour/system/controlDict")

        with open(control_dict_path, 'r') as file:
            control_dict = file.readlines()

        with open('inputDict_extraction.json', 'r') as json_file:
            dados_pontos = json.load(json_file)
        # Preparar a lista de probeLocations com base nos dados do JSON
        probe_locations = ""
        extra_data = dados_pontos["extra"]
        for i, ponto in enumerate(extra_data):
            posx = ponto[f"posx_{i+1}"]
            posy = ponto[f"posy_{i+1}"]
            # Adicionando o ponto no formato (posx posy 0)
            probe_locations += f"        ({posx} {posy} 0)\n"

        # Agora, vamos procurar a linha 'probeLocations' no arquivo controlDict e substituir o conteúdo
        for i, line in enumerate(control_dict):
            if 'probeLocations' in line:
                # Substituir a parte do probeLocations com os pontos extraídos do JSON
                control_dict[i + 2] = probe_locations
                break  # Parar depois de modificar a seção
            
        # Salvar o arquivo modificado
        with open(control_dict_path, 'w') as file:
            file.writelines(control_dict)
        self.postprocess()
    def postprocess(self):
        import subprocess
        # Rodar o comando de pós-processamento
        caso_dir = "../../tutorials/mhtFoam/2d_circular_tumour"

        # Mudar o diretório de trabalho para o diretório do caso
        os.chdir(caso_dir)
        try:
            result = subprocess.run(['postProcess', '-fields', '(W T)'], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, timeout=100)
            if result.returncode == 0:
                print("postProcess concluído com sucesso!")
                self.rodar_grafico()              
        except subprocess.TimeoutExpired:
            print("Tempo limite para o postProcess foi alcançado!")
            # Pode adicionar uma ação alternativa ou continuar com o gráfico
            self.rodar_grafico()
        except subprocess.CalledProcessError as e:
            print(f"Erro ao executar postProcess: {e}")
            self.rodar_grafico()
    def rodar_grafico(self):
        print("Preparando tudo...")
        import subprocess
        caso_dir1="../../../scripts/pythonscripts"
        os.chdir(caso_dir1)
        try:
            # Rodar outro script Python
            subprocess.run(['python3', 'mhtFoam_pos_graph.py'], check=True)
            print("Script executado com sucesso!")
        except subprocess.CalledProcessError as e:
            print(f"Erro ao executar o outro arquivo: {e}")

root_1 = cttk.CTk()
app = Main_wind_pos(root_1)
zaragui = app # Inicialização

zaragui.interface()

root_1.mainloop()
