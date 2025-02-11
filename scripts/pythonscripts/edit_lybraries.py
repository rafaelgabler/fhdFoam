import re
import json
import os

# Modifica o blockMeshDict e o controlDict
def changeFileDict(dict1):
    for file in dict1.keys():
        with open(file,"r") as f:
            entrie=f.read()
        f.close()
        #print(entrie)
        dfile = dict1[file]
        for entrie_line in dfile:
            for key in entrie_line:
                    exp = entrie_line[key]["exp"]
                    value = entrie_line[key]["value"]
                    entrie = re.sub(rf'{exp}', str(value), entrie)
        with open(file,"w") as f:
            f.write(entrie)
        f.close()

# Modifica o ID e o corr
def changeFileDict_2(tumor_dict):
    dir = os.path.dirname(os.path.abspath("../../tutorials/mhtFoam/2d_circular_tumour"))
    ## Arquivos a serem alterados
    #input_file = "../../tutorials/mhtFoam/2d_circular_tumour/0/ID"
    input_file = os.path.join(dir,"2d_circular_tumour/0/ID")
    input_file2 = os.path.join(dir,"2d_circular_tumour/system/controlDict")

    
    ## Contar tumores
    i=0
    
    ## Abre arquivos
    with open(input_file, "r") as file:
        lines = file.readlines()
    
    with open(input_file2, "r") as file:
        lines2 = file.readlines()


        
    # listas agregam alterações (Altera o ID) 
    tumor_data_lines = []
    tumor_data_lines_2 = []
    control_data_lines = []
    datax = []
    datay = []
    
    ## Itera dentro de tumor_data da outra função para recuperar os dados gravados no json
    for tumor_data in tumor_dict.values():
        #print(tumor_data)
        i=i+1
        ## pra identificar os dados de cada tumor
        tumor_data_lines.append(f"        //Tumor_{i}\n")
        ##Aqui modifica os dados que foram entrados diretamento com o usuário
        for param in tumor_data[input_file]:
            for key, value in param.items():
                scalar_name = key
                scalar_value = value["value"]
                tumor_data_lines.append(f"        scalar {scalar_name} = {scalar_value};\n")
                if scalar_name == f"posx_{i}":
                    datax.append(scalar_value)
                if scalar_name == f"posy_{i}":
                    datay.append(scalar_value)

    
        ## Agrega as demais linhas necessárias que não são diretamente entradas
        
        ## ID
        tumor_data_lines.append(f"        scalar inclination_rad_{i} = inclination_{i} * pi / 180.0;\n")
        tumor_data_lines.append(f"        scalar be_{i} = radius_{i}*pow((1-pow(eccen_{i},2)),0.25);\n")
        tumor_data_lines.append(f"        scalar ae_{i} = pow(pow(be_{i},2)*(pow(1-pow(eccen_{i},2),-1)),0.5);\n")
        tumor_data_lines.append("\n")
            
        tumor_data_lines_2.append(f"        scalar y_rot_{i} = (y-posy_{i})*cos(inclination_rad_{i})-(x-posx_{i})* sin(inclination_rad_{i});\n")
        tumor_data_lines_2.append(f"        scalar x_rot_{i} = (y-posy_{i})*sin(inclination_rad_{i})+(x-posx_{i})* cos(inclination_rad_{i});\n")
        tumor_data_lines_2.append(f"                if ( pow(y_rot_{i},2) <= ((1 - pow(x_rot_{i},2)/pow(ae_{i},2) )*pow(be_{i},2)) )\n")
        tumor_data_lines_2.append("                {\n")
        tumor_data_lines_2.append("                        ID[i] = 1.;\n")
        tumor_data_lines_2.append("                }\n")
        tumor_data_lines_2.append("\n")
    
    for i in range(len(datax)):
        xpos=datax[i-1]
        ypos=datay[i-1]
        control_data_lines.append(f"			({xpos} {ypos} 0.01)\n")
    # Onde escrever nos arquivos
    ##ID
    insertion_line = 48
    insertion_line_c = 68
    insertion_line_2=insertion_line+(i*10+18)
    #informacoes iniciais
    lines[insertion_line:insertion_line] = tumor_data_lines
    #equacao da elipse
    lines[insertion_line_2:insertion_line_2] = tumor_data_lines_2
    #controldict
    #lines2[insertion_line_c:insertion_line_c] = control_data_lines
    
    ## Escreve nos arquivos
    
    with open(input_file, "w") as file:
        file.writelines(lines)
    with open(input_file2, "w") as file:
        file.writelines(lines2)

def changeFileDict_6(tumor_dict):
    dir = os.path.dirname(os.path.abspath("../../tutorials/mhtFoam/2d_circular_tumour"))
    ## Arquivos a serem alterados
    #input_file = "../../tutorials/mhtFoam/2d_circular_tumour/0/ID"
    input_file = os.path.join(dir,"2d_circular_tumour/system/controlDict")
    
    ## Contar tumores
    i=0
    
    ## Abre arquivos
    with open(input_file, "r") as file:
        lines = file.readlines()
        
    # listas agregam alterações (Altera o ID) 
    tumor_data_lines = []
 
    ## Itera dentro de tumor_data da outra função para recuperar os dados gravados no json
    for tumor_data in tumor_dict.values():
        #print(tumor_data)
        i=i+1
        ##Aqui modifica os dados que foram entrados diretamento com o usuário
        for param in tumor_data[input_file]:
            for key, value in param.items():
                scalar_name = key
                scalar_value = value["value"]
                if scalar_name == f"posx_{i}" or scalar_name == f"posy_{i}":
                    scalar_name = xpos
                if scalar_name == f"posy_{i}":
                    scalar_name = ypos
                tumor_data_lines.append(f"			({xpos} {ypos}  1)\n")

    # Onde escrever nos arquivos
    ##ID
    insertion_line = 68
    lines[insertion_line:insertion_line] = tumor_data_lines
    
    ## Escreve nos arquivos
    
    with open(input_file, "w") as file:
        file.writelines(lines)

################
def changeFileDict_4(fluid_dict):
    dir = os.path.dirname(os.path.abspath("../../tutorials/mhtFoam/2d_circular_tumour"))
    ## Arquivos a serem alterados
    #input_file = "../../tutorials/mhtFoam/2d_circular_tumour/0/corr"
    input_file = os.path.join(dir,"2d_circular_tumour/0/corr")
  
    ## Contar tumores
    i=0
    
    ## Abre arquivos
    with open(input_file, "r") as file:
        lines = file.readlines()
        
    # listas agregam alterações (Altera o corr) 
    fluid_data_lines = []
    fluid_data_lines_2 = []

    
    ## Itera dentro de tumor_data da outra função para recuperar os dados gravados no json
    for fluid_data in fluid_dict.values():
        #print(tumor_data)
        i=i+1
        ## pra identificar os dados de cada tumor
        fluid_data_lines.append(f"        //Injection site {i}\n")
        fluid_data_lines.append(f"        // fluid magnetic on tumor {i}\n")
        ##Aqui modifica os dados que foram entrados diretamento com o usuário
        for param in fluid_data[input_file]:
            for key, value in param.items():
                scalar_name = key
                scalar_value = value["value"]
                fluid_data_lines.append(f"        scalar {scalar_name} = {scalar_value};\n")

        ## Agrega as demais linhas necessárias que não são diretamente entradas
        
        ## corr
        fluid_data_lines.append("\n")
        fluid_data_lines_2.append(f"                if ( pow(y-posy_{i},2) <= pow(((3*volume_{i}*(pow(10,-6)))/(4*pi)),(2.0/3.0)) - pow(x-posx_{i},2) )\n")
        fluid_data_lines_2.append("                {\n")
        fluid_data_lines_2.append("                        corr[i] = 1.;\n")
        fluid_data_lines_2.append("                }\n")
    
    # Onde escrever nos arquivos
    ##ID
    insertion_line = 48
    insertion_line_2=insertion_line+(i*8+6)
    lines[insertion_line:insertion_line] = fluid_data_lines
    lines[insertion_line_2:insertion_line_2] = fluid_data_lines_2
    

    ## Escreve nos arquivos
    
    with open(input_file, "w") as file:
        file.writelines(lines)

###############3
# Estabelece a relação do que modificar com o valor a ser modificado para o controlDict
def generate_dictionary_1(data,dir=None): 
    #print(data["endtime"])
    if dir is None:
        dir = os.path.dirname(os.path.abspath("../../tutorials/mhtFoam/2d_circular_tumour"))
    dict1 = {
        os.path.join(dir,"2d_circular_tumour/system/controlDict"):
         [
            {"endtime":{"exp":"{endtime}","value":data["endtime"]}},
            #{"endTime":{"exp":"\s+[0-9]+","value":tf}}
            {"timestep":{"exp":"{timestep}","value":data["timestep"]}}
         ]
         
    } 
    return dict1

def generate_dictionary_5(data,dir=None): 
    #print(data["endtime"])
    if dir is None:
        dir = os.path.dirname(os.path.abspath("../../tutorials/mhtFoam/2d_circular_tumour"))
    dict1 = {
        os.path.join(dir,"2d_circular_tumour/constant/mhtQuantities"):
         [
            {"Magnetic_intensity":{"exp":"{Magnetic_intensity}","value":data["Magnetic_intensity"]}},
            {"Magnetic_frequency":{"exp":"{Magnetic_frequency}","value":data["Magnetic_frequency"]}},
            {"complex_susceptibility":{"exp":"{complex_susceptibility}","value":data["complex_susceptibility"]}},
            {"volume_fraction":{"exp":"{volume_fraction}","value":data["volume_fraction"]}}
         ]
         
    } 
    return dict1

# Estabelece a relação do que modificar com o valor a ser modificado para o blockMeshDict
#def generate_dictionary_2(data,dir="../../tutorials/mhtFoam/2d_circular_tumour"):
def generate_dictionary_2(data,dir=None):
    if dir is None:
        dir = os.path.dirname(os.path.abspath("../../tutorials/mhtFoam/2d_circular_tumour"))
    dict1 = {
        os.path.join(dir, "2d_circular_tumour/system/blockMeshDict"):
         [
             {"xmax":{"exp":"{xmax}","value":data["xmax"]}},
             {"ymax":{"exp":"{ymax}","value":data["ymax"]}},
             {"xnode":{"exp":"{xnode}","value":data["xnode"]}},
             {"ynode":{"exp":"{ynode}","value":data["ynode"]}}
        ]
    }
    return dict1

# Estabelece a relação do que modificar com o valor a ser modificado para o ID
def generate_dictionary_3(data,indexx,dir=None):
    #print(index)
    if dir is None:
        dir = os.path.dirname(os.path.abspath("../../tutorials/mhtFoam/2d_circular_tumour"))
    tumor_dict = {}
    fluid_dict = {}
    for i in range(1, indexx+1):  # Certifique-se de iterar até indexx inclusive
        tumor_dict[f"dict{i}"] = {
            os.path.join(dir, "2d_circular_tumour/0/ID"): [
                {f"radius_{i}": {"exp": "{radius}", "value": data["tumors"][i-1][f"radius_{i}"]}},
                {f"eccen_{i}": {"exp": "{eccen}", "value": data["tumors"][i-1][f"eccen_{i}"]}},
                {f"posx_{i}": {"exp": "{posx}", "value": data["tumors"][i-1][f"posx_{i}"]}},
                {f"posy_{i}": {"exp": "{posy}", "value": data["tumors"][i-1][f"posy_{i}"]}},
                {f"inclination_{i}": {"exp": "{inclination}", "value": data["tumors"][i-1][f"inclination_{i}"]}},
            ]
        }

    return tumor_dict
def generate_dictionary_6(data,indexx,dir=None):
    #print(index)
    if dir is None:
        dir = os.path.dirname(os.path.abspath("../../tutorials/mhtFoam/2d_circular_tumour"))
    tumor_dict = {}
    fluid_dict = {}
    for i in range(1, indexx+1):  # Certifique-se de iterar até indexx inclusive
        tumor_dict[f"dict{i}"] = {
            os.path.join(dir, "2d_circular_tumour/0/ID"): [
                {f"radius_{i}": {"exp": "{radius}", "value": data["tumors"][i-1][f"radius_{i}"]}},
                {f"eccen_{i}": {"exp": "{eccen}", "value": data["tumors"][i-1][f"eccen_{i}"]}},
                {f"posx_{i}": {"exp": "{posx}", "value": data["tumors"][i-1][f"posx_{i}"]}},
                {f"posy_{i}": {"exp": "{posy}", "value": data["tumors"][i-1][f"posy_{i}"]}},
                {f"inclination_{i}": {"exp": "{inclination}", "value": data["tumors"][i-1][f"inclination_{i}"]}},
            ]
        }

    return tumor_dict
def generate_dictionary_4(data,indexx_f,dir=None):
    #print(index)
    if dir is None:
        dir = os.path.dirname(os.path.abspath("../../tutorials/mhtFoam/2d_circular_tumour"))
    fluid_dict = {}
    for i in range(1, indexx_f+1):  # Certifique-se de iterar até indexx inclusive
        fluid_dict[f"dict{i}"] = {
            os.path.join(dir, "2d_circular_tumour/0/corr"): [
                {f"volume_{i}": {"exp": "{radius}", "value": data["magnetic_fluid"][i-1][f"volume_{i}"]}},
                {f"posx_{i}": {"exp": "{posx}", "value": data["magnetic_fluid"][i-1][f"posx_{i}"]}},
                {f"posy_{i}": {"exp": "{posy}", "value": data["magnetic_fluid"][i-1][f"posy_{i}"]}}
            ]
        }

    return fluid_dict
