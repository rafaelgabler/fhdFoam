#------------------------------------------------------------------------------
# bash script for running multiple openFoam simulations in a single call
# This script perfoms the following setps:
# 
# 1 - Creates a new folder named "varreduras" where the simulations will be located;
# 2 - Defines the numerical values of a given parameter that will be altered in each run;
# 3 - Sets the name of the original configuration folder that will be cloned in each new run;
# 4 - Clones the original case and storages the original configuration folder in each new case folder;
# 5 - Modifies a specific entry in a particular dictionary for each new case;
# 6 - Calls a sequence of openFoam commands to pre-process each new case;
# 7 - Runs all the simulations simultaneously;
#------------------------------------------------------------------------------


# Creating a new folder named "varreduras":

mkdir varreduras

# Defining the values of the variable for the sweep:

varreduras="
5.0e-9
6.0e-9
7.0e-9
8.0e-9
9.0e-9
"
# Setting the name of the original folder containing the base configuration files:

caseLabel="effective_diff"

# Main loop that will clone the original case into the new folders, change the values
# of the variable "diff" in the mhtQuantities dictionary in the constant folder of each
# case according to the values defined in step number 2 and finally run de blockMesh and
# setFields command:

for caseName in $varreduras
do
# Cloning original case
foamCloneCase $caseLabel varreduras/"$caseLabel"_"$caseName"

# Editing the entry "diff" in the mhtQuantities dictionary at the constant folder of each case

foamDictionary varreduras/"$caseLabel"_"$caseName"/constant/mhtQuantities -entry \
			"diff" -set $caseName;

# Creating the mesh and defining the initial fields in each folder

( cd varreduras/"$caseLabel"_"$caseName" && blockMesh && setFields)

done

# Running all simulations 
			
for caseName in $varreduras
do			
( cd varreduras/"$caseLabel"_"$caseName" && nohup mhtFoam_new &) &
done
