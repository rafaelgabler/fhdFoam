Info<< "Reading field T\n" << endl;

volScalarField T
(
    IOobject
    (
        "T",
        runTime.timeName(),
        mesh,
        IOobject::MUST_READ,
        IOobject::AUTO_WRITE
    ),
    mesh
);

Info<< "Reading field ID\n" << endl;

volScalarField ID
(
    IOobject
    (
        "ID",
        runTime.timeName(),
        mesh,
        IOobject::MUST_READ,
        IOobject::AUTO_WRITE
    ),
    mesh
);

Info<< "Reading field W\n" << endl;

volScalarField W
(
    IOobject
    (
        "W",
        runTime.timeName(),
        mesh,
        IOobject::MUST_READ,
        IOobject::AUTO_WRITE
    ),
    mesh
);

Info<< "Reading field U\n" << endl;

volVectorField U
(
    IOobject
    (
        "U",
        runTime.timeName(),
        mesh,
        IOobject::MUST_READ,
        IOobject::AUTO_WRITE
    ),
    mesh
);


Info<< "Reading transportProperties\n" << endl;

IOdictionary transportProperties
(
    IOobject
    (
        "transportProperties",
        runTime.constant(),
        mesh,
        IOobject::MUST_READ_IF_MODIFIED,
        IOobject::NO_WRITE
    )
);


Info<< "Reading diffusivity DT\n" << endl;

dimensionedScalar DT("DT", dimViscosity, transportProperties);

IOdictionary mhtQuantities
(
    IOobject
    (
        "mhtQuantities",
        runTime.constant(),
        mesh,
        IOobject::MUST_READ_IF_MODIFIED,
        IOobject::NO_WRITE
    )
);
/* Dimension set - OpenFOAM
1 - kg
2 - m
3 - s
4 - K
5 - mol
6 - A
7 - cd
*/


// Pi
dimensionedScalar pi("pi", dimensionSet(0,0,0,0,0,0,0), 3.1416); 

// Magnetic permeability of free space
dimensionedScalar mu0("mu0", dimensionSet(1,1,-2,0,0,-2,0), 1.256e-6); 

// Maximum applied field
dimensionedScalar H0("H0", dimensionSet(0,-1,0,0,0,1,0), mhtQuantities);

// Particle magnetization Md
dimensionedScalar MD("MD", dimensionSet(0,-1,0,0,0,1,0), mhtQuantities);

// Volume fraction of particles
dimensionedScalar fi("fi", dimensionSet(0,0,0,0,0,0,0), mhtQuantities);

// Applied field frequency
dimensionedScalar freq("freq", dimensionSet(0,0,-1,0,0,0,0), mhtQuantities);

// Imaginary part of the complex susceptibility
dimensionedScalar qui_imag("qui_imag", dimless, mhtQuantities);

// Correction term for computing MF spreading
dimensionedScalar corr("corr", dimless, mhtQuantities);

// Blood density
dimensionedScalar rhob("rhob", dimensionSet(1,-3,0,0,0,0,0), mhtQuantities);

// Blood specific heat
dimensionedScalar cb("cb", dimensionSet(0,2,-2,-1,0,0,0), mhtQuantities);

// Blood arterial temperature
dimensionedScalar Tb("Tb", dimensionSet(0,0,0,1,0,0,0), mhtQuantities);

// Initial average density
dimensionedScalar rho("rho", dimensionSet(1,-3,0,0,0,0,0), 1.0e+3);

// Initial CP
dimensionedScalar cp("cp", dimensionSet(0,2,-2,-1,0,0,0), 4.0e+3);

// Healthy tissue density
dimensionedScalar rho1("rho1", dimensionSet(1,-3,0,0,0,0,0), mhtQuantities);

// Tumour tissue density
dimensionedScalar rho2("rho2", dimensionSet(1,-3,0,0,0,0,0), mhtQuantities);

// Specific heat of the healthy tissue
dimensionedScalar cp1("cp1", dimensionSet(0,2,-2,-1,0,0,0), mhtQuantities);

// Specific heat of the tumour tissue
dimensionedScalar cp2("cp2", dimensionSet(0,2,-2,-1,0,0,0), mhtQuantities);

// Metabolic generation inside healthy tissue
dimensionedScalar Q1("Q1", dimensionSet(1,-1,-3,0,0,0,0), mhtQuantities);

// Metabolic generation inside tumour tissue
dimensionedScalar Q2("Q2", dimensionSet(1,-1,-3,0,0,0,0), mhtQuantities);

// Teste
dimensionedScalar zero("zero", dimensionSet(0,0,-1,0,0,0,0),0);

// Creating a unit scalar with dimension of temperature	
dimensionedScalar T1("T1", dimensionSet(0,0,0,1,0,0,0), 1);

//
#include "createPhi.H"

#include "createFvOptions.H"
