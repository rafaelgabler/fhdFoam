#------------------------------------------------------------------------------
# bash script for stuidying mesh refinement on openFoam application icomagFoam
# based on the parameter_sweep.sh script by Rafael G. Gontijo
# This script perfoms the following setps:
# 
# 1 - Creates a new folder named "mesh_study" where the simulations will be located;
# 2 - Recives the quantities of mesh elements in the x and y directions, respectively, for each run;
# 3 - Sets the name of the original configuration folder that will be cloned in each new run;
# 4 - Clones the original case and storages the original configuration folder in each new case folder;
# 5 - Modifies the mesh in blockMeshDict dictionary for each new case;
# 6 - Calls blockMesh command to pre-process each new case;
# 7 - Runs all the simulations simultaneously;
#------------------------------------------------------------------------------


# Creating a new folder named "mesh_study":

mkdir mesh_study

# Defining the quantities of cells in each direction for the sweep:

read -p "Quantities of cells in the x direction, separated by spacebars: " X
read -p "Quantities of cells in the y direction, separated by spacebars: " Y

meshes_x=($X)
meshes_y=($Y)

echo $meshes_x

if [ ${#meshes_x[@]} -ne ${#meshes_y[@]} ]; then
    echo "Error: The lists of x and y values should have the same size."
    exit 1
fi

# Setting the name of the original folder containing the base configuration files:

caseLabel="mesh"

# Main loop that will clone the original case into the new folders, change the meshes in the blockMeshDict dictionary in the system folder of each case according to the values defined in step number 2 and finally run de blockMesh and command:

for index in ${!meshes_x[@]}
do
# Cloning original case
foamCloneCase $caseLabel mesh_study/"$caseLabel"_"${meshes_x[$index]}"x"${meshes_y[$index]}"

# Editing the mesh in the blockMeshDict dictionary at the system folder of each case
block="(hex (0 1 2 3 4 5 6 7) ("${meshes_x[$index]}" "${meshes_y[$index]}" 1) simpleGrading (1 1 1));"
foamDictionary mesh_study/"$caseLabel"_"${meshes_x[$index]}"x"${meshes_y[$index]}"/system/blockMeshDict -entry \
			"blocks" -set "$block";

# Creating the mesh in each folder
# If your case requires setFields or simmilar commands to be run before running the simmulations, add them to the command line below

(cd mesh_study/"$caseLabel"_"${meshes_x[$index]}"x"${meshes_y[$index]}" && blockMesh)

done

# Running all simulations 
			
for index in ${!meshes_x[@]}
do			
(cd mesh_study/"$caseLabel"_"${meshes_x[$index]}"x"${meshes_y[$index]}" && nohup icomagFoam &) &
done
