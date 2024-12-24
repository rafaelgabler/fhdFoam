# What is fhdFoam? 

**fhdFoam** is an open-source package based on modifications of original openFoam solvers designed to simulate magnetic fluid flows in different scenrarios based on the solution of ferrohydrodynamic governing equations. Or in simple words: fhdFoam is a set of OpenFOAM solvers for ferrohydrodynamic problems. 

Besides a set of solvers and tutorial cases, this repository also includes pre-programmed python and bash scripts designed to provide a graphical user interface to handle pre and post-proccess funcionalities. These scripts interact with the user through a GUI asking questions that are used to configure the simulations by altering dictionaries of the tutorial cases.

The philosophy of the project can be summarized as *"one solver for each physics"*. Since the general set of governing equations of ferrohydrodynamics can be quite complicated and subjected to different versions depending on the assumed hypothesis, we believe that providing different solvers for different physics is not only practical but also pedagogical. The idea of different set of equations for different problems can serve as a mean to teach ferrohydrodynamics for fluid dynamicists which are not used to the inclusion of magnetic effects on the Newtonian version of Navier-Stokes equations.

Currently, the project counts with the following solvers:

**magnetoconvectionFoam** - OpenFOAM solver for simulating the problem of thermomagnetic convection. This solver is based on the original buoyantBoussinesqPimpleFoam;

**intermagFoam** - OpenFOAM solver for simulating the motion of two immiscible phases where one of them is a magnetic fluid. Can be used to simulate magnetic drops being dragged by a magnetic field. This solver is based on the original interFoam;

**mhtFoam** - OpenFOAM solver for simulating the heating proccess of tumours subjected to magnetic hyperthermia. This solver is based on the original scalarTransportFoam;

**icomagFoam** - OpenFOAM solver, based on icomagFoam to solve the laminar magnetic fluid flow of a ferrofluid subjected to non-equilibrium magnetization dynamics using the classical Shliomis (1971) magnetization model;

# Pre-requisites

In order to use the full functionalities of this package, you must have the following programs installed in your system:

- openFoam v2306 or higher;
- paraview;
- python;

In order to properly use the graphical functionalities provided by this project the user must also the following python packages:

- 

# Configuration

In order to compile a given solver, it is recommended to put them in a folder named my_solvers in the openfoam user folder. If you do not have this folder, please create it. When you first install openFoam, you must create an openFoam user folder. To achieve this, please type the following command inside the openfoam bash:

`mkdir -p $FOAM_RUN`

Whenever you type: `ufoam` inside the openfoam bash it will direct you to this folder, where you should see a run folder.

Inside the openFoam user folder type `mkdir my_solvers` to create this folder.

To compile one of the fhdFoam solvers upload the solver folder inside my_folder and in the solver folder type: `wmake`

This will compile the code, that should be called inside a given case folder by its own name, which you can consult in the text file named files inside the Make folder in each solver.

## Gallery


<img src="figs/convection1.png" width="400" height="200">

Three magnet array used in the thermomagnetic convection problem simulated with magnetoconvectionFoam

<div class="figure-center"> <img src="figs/convection2.png" width="200" height="300" /> </div> 


## References

[1] Gontijo, Rafael Gabler, and Andrey Barbosa Guimarães. "Langevin dynamic simulations of magnetic hyperthermia in rotating fields." Journal of Magnetism and Magnetic Materials 565 (2023): 170171. 
[DOI: 10.1016/j.jmmm.2022.170171](https://doi.org/10.1016/j.jmmm.2022.170171).

[2] Tang, Yundong, et al. "Effect of nanofluid distribution on therapeutic effect considering transient bio-tissue temperature during magnetic hyperthermia." Journal of Magnetism and Magnetic Materials 517 (2021): 167391.[DOI: 10.1016/j.jmmm.2020.167391](https://doi.org/10.1016/j.jmmm.2020.167391).