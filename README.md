# fhdFoam
OpenFOAM solvers for ferrohydrodynamic problems

magnetoconvection_Foam = OpenFOAM solver for thermomagnetic convection based on the original buoyantBoussinesqPimpleFoam;

intermagFoam = OpenFOAM solver for magnetic drops being dragged by a linear-gradient magnetic field, based on the original interFoam;

mhtFoam = OpenFOAM solver for magnetic hyperthermia in biological tissues, bases on the original scalarTransportFoam;

In order to compile a given solver, it is recommended to put them in a folder named my_solvers in the openfoam user folder.

If you do not have this folder, please create it.

In order to create an openFoam user folder please type the following command inside the openfoam bash:

mkdir -p $FOAM_RUN

Whenever you type: ufoam inside the openfoam bash it will direct you to this folder, where you should see a run folder.

Inside the openFoam user folder type mkdir my_solvers to create this folder.

To compile one of the fhdFoam solvers upload the solver folder inside my_folder and in the solver folder type: wmake

This will compile the code, that should be called inside a given case folder by its own name, which you can consult in the text file named files inside the Make folder in each solver.
