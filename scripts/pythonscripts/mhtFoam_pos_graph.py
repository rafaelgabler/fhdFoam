
class main_pos:
    def __init__(self):
        print("Criando gráficos...")
    def visual_pos(self):
        import os
        import numpy as np
        import matplotlib
        matplotlib.use('TkAgg') 
        import matplotlib.pyplot as plt
        from mpl_toolkits.mplot3d import Axes3D
        # Obter o diretório do script
        script_dir = os.path.dirname(os.path.realpath(__file__))
        # Caminho para os arquivos de dados
        file_path = os.path.join(script_dir, '../../tutorials/mhtFoam/2d_circular_tumour/postProcessing/probes/0/T')
        file_path2 = os.path.join(script_dir, '../../tutorials/mhtFoam/2d_circular_tumour/postProcessing/probes/0/W')


        start_index = None
        start_index2 = None
        # Carregar os dados do arquivo T
        data = []
        with open(file_path, 'r') as file:
            lines = file.readlines()
            for line in lines:
                if line.startswith('Time'):
                    start_index = lines.index(line) + 1
                    break

        # Carregar os dados numéricos de T
        data = np.loadtxt(lines[start_index:], dtype=float)
        time = data[:, 0]  # Tempo
        temperatures = data[:, 1:]  # Temperaturas

        # Carregar os dados do arquivo W
        data2 = []
        with open(file_path2, 'r') as file2:
            lines2 = file2.readlines()
            for line2 in lines2:
                if line2.startswith('Time'):
                    start_index2 = lines2.index(line2) + 1
                    break

        # Carregar os dados numéricos de W
        data2 = np.loadtxt(lines2[start_index2:], dtype=float)
        perfusion = data2[:, 1:]  # Perfusão sanguínea

        # Plotando o gráfico de Temperatura
        plt.figure(figsize=(10, 6))
        for i in range(temperatures.shape[1]):
            plt.plot(time, temperatures[:, i], label=f'Tumor {i+1}')
        plt.title('Temperature in the center of the tumors')
        plt.xlabel('Time (s)')
        plt.ylabel('Temperature (K)')
        plt.legend()
        plt.grid(True)
        plt.show()

        # Plotando o gráfico de Perfusão
        plt.figure(figsize=(10, 6))
        for i in range(perfusion.shape[1]):
            plt.plot(time, perfusion[:, i], label=f'Tumor {i+1}')
        plt.title('Blood perfusion in the center of the tumors')
        plt.xlabel('Time (s)')
        plt.ylabel('Perfusion (1/s)')
        plt.legend()
        plt.grid(True)
        plt.show()
        ########################################################################
        ##                                                                    ##
        ##                             Gráfico 2d                             ##
        ##                                                                    ##
        ########################################################################
        import matplotlib.pyplot as plt
        from mpl_toolkits.mplot3d import Axes3D
        import json

        # Abrir o arquivo JSON com informações de domínio
        with open('inputDict_blockMeshDict.json', 'r') as json_file:
            domain_info = json.load(json_file)

        with open('inputDict_controlDict.json', 'r') as json_file:
            domain_info2 = json.load(json_file)

        # Extrair as informações de domínio
        xmax = float(domain_info["xmax"])
        ymax = float(domain_info["ymax"])
        xnode = int(domain_info["xnode"])
        ynode = int(domain_info["ynode"])

        endtime = int(domain_info2["endtime"])

        # Caminho para o arquivo de temperaturas
        script_dir = os.path.dirname(__file__)  # Pega o diretório do script
        file_path3 = os.path.join(script_dir, f'../../tutorials/mhtFoam/2d_circular_tumour/{endtime}/T')

        # Ler os dados de temperatura do arquivo
        with open(file_path3, 'r') as file:
            lines = file.readlines()

        # Encontrar a linha que contém o campo "internalField"
        for i, line in enumerate(lines):
            if line.strip().startswith("internalField"):
                start_line = i + 1  # A linha após "internalField"
                break

        # Extrair os dados de temperatura
        num_temperatures = int(lines[start_line].strip())
        temperature_data = [float(lines[start_line + 2 + i].strip()) for i in range(num_temperatures)]

        # Converter os dados de temperatura em um array NumPy
        #temperatures = np.array(temperature_data)
        temperatures = np.array(temperature_data).reshape((ynode, xnode))
        # Gerar as coordenadas de cada nó
        x = np.linspace(0, xmax, xnode)
        y = np.linspace(0, ymax, ynode)
        X, Y = np.meshgrid(x, y)

        #print(f"Nós em X: {xnode}, Nós em Y: {ynode}")
        #print(f"Número total esperado de temperaturas: {xnode * ynode}")
        #print(f"Número total de temperaturas no arquivo: {len(temperature_data)}")

        # GRÁFICO 2D
        fig_2d, ax_2d = plt.subplots(figsize=(10, 8))
        contour = ax_2d.contourf(X, Y, temperatures, cmap='plasma', shading='auto')

        # Adicionar barra de cores
        fig_2d.colorbar(contour, ax=ax_2d,label="T(K)")
        #cbar = fig_2d.colorbar(contour, ax=ax_2d)
        #cbar.set_label("T (K)")
        # Adicionar título e rótulos
        ax_2d.set_title(f'Temperature distribution at the instant {endtime} s')
        ax_2d.set_xlabel('X size (m)')
        ax_2d.set_ylabel('Y size (m)')

        # Mostrar o gráfico 2D
        plt.show()
        


if __name__ == "__main__":
    app = main_pos()
    app.visual_pos()
