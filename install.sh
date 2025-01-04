#------------------------------------------------------------------------------
# bash script for compiling fhdFoam's solvers
#
#------------------------------------------------------------------------------
 
echo "Compiling icomagFoam..."
echo ""
 cd solvers/icomagFoam && wclean && wmake
echo "Compiling mhtFoam..."
echo "" 
 cd ../mhtFoam && wclean && wmake 
echo "Compiling magnetoconvectionFoam..."
echo "" 
 cd ../magnetoconvectionFoam && wclean && wmake 
 echo "Compiling intermagFoam..."
echo "" 
 cd ../intermagFoam && wclean && wmake  
echo "" 
echo "All solvers have been successfully compiled."