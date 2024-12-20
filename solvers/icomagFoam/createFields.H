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

dimensionedScalar nu
(
    "nu",
    dimViscosity,
    transportProperties
);

dimensionedScalar rho
(
    "rho",
    dimensionSet(1,-3,0,0,0,0,0),
    transportProperties
);

dimensionedScalar DT
(
    "DT",
    dimensionSet(0,2,-1,0,0,0,0),
    transportProperties
);

dimensionedScalar fi
(
    "fi",
    dimensionSet(0,0,0,0,0,0,0),
    transportProperties
);

dimensionedScalar tau
(
    "tau",
    dimensionSet(0,0,1,0,0,0,0),
    transportProperties
);

dimensionedScalar Md
(
    "Md",
    dimensionSet(0,-1,0,0,0,1,0),
    transportProperties
);

dimensionedScalar m
(
    "m",
    dimensionSet(0,2,0,0,0,1,0),
    transportProperties
);

dimensionedScalar Hmax
(
    "Hmax",
    dimensionSet(0,-1,0,0,0,1,0),
    transportProperties
);

dimensionedScalar mu0("mu0", dimensionSet(1,1,-2,0,0,-2,0), 1.256e-6); 

// VERIFICAR DIREITINHO A UNIDADE DA CONSTANTE DE BOLTZMANN AQUI :

dimensionedScalar kb("kb", dimensionSet(1,2,-2,-1,0,0,0), 1.3806e-23); 

Info<< "Reading field p\n" << endl;
volScalarField p
(
    IOobject
    (
        "p",
        runTime.timeName(),
        mesh,
        IOobject::MUST_READ,
        IOobject::AUTO_WRITE
    ),
    mesh
);

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


Info<< "Reading field M\n" << endl;
volVectorField M
(
    IOobject
    (
        "M",
        runTime.timeName(),
        mesh,
        IOobject::MUST_READ,
        IOobject::AUTO_WRITE
    ),
    mesh
);

Info<< "Reading field M0\n" << endl;
volVectorField M0
(
    IOobject
    (
        "M0",
        runTime.timeName(),
        mesh,
        IOobject::MUST_READ,
        IOobject::AUTO_WRITE
    ),
    mesh
);


Info<< "Reading field H\n" << endl;
volVectorField H
(
    IOobject
    (
        "H",
        runTime.timeName(),
        mesh,
        IOobject::MUST_READ,
        IOobject::AUTO_WRITE
    ),
    mesh
);

Info<< "Reading field alpha\n" << endl;
volScalarField alpha
(
    IOobject
    (
        "alpha",
        runTime.timeName(),
        mesh,
        IOobject::MUST_READ,
        IOobject::AUTO_WRITE
    ),
    mesh
);

Info<< "Reading field modH\n" << endl;
volScalarField modH
(
    IOobject
    (
        "modH",
        runTime.timeName(),
        mesh,
        IOobject::MUST_READ,
        IOobject::AUTO_WRITE
    ),
    mesh
);


#include "createPhi.H"


label pRefCell = 0;
scalar pRefValue = 0.0;
setRefCell(p, mesh.solutionDict().subDict("PISO"), pRefCell, pRefValue);
mesh.setFluxRequired(p.name());
