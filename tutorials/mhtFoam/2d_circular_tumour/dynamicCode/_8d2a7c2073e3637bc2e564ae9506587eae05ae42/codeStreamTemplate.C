/*---------------------------------------------------------------------------*\
  =========                 |
  \\      /  F ield         | OpenFOAM: The Open Source CFD Toolbox
   \\    /   O peration     |
    \\  /    A nd           | www.openfoam.com
     \\/     M anipulation  |
-------------------------------------------------------------------------------
    Copyright (C) YEAR AUTHOR, AFFILIATION
-------------------------------------------------------------------------------
License
    This file is part of OpenFOAM.

    OpenFOAM is free software: you can redistribute it and/or modify it
    under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    OpenFOAM is distributed in the hope that it will be useful, but WITHOUT
    ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or
    FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General Public License
    for more details.

    You should have received a copy of the GNU General Public License
    along with OpenFOAM.  If not, see <http://www.gnu.org/licenses/>.

Description
    Template for use with codeStream.

\*---------------------------------------------------------------------------*/

#include "dictionary.H"
#include "Ostream.H"
#include "Pstream.H"
#include "pointField.H"
#include "tensor.H"
#include "unitConversion.H"

//{{{ begin codeInclude
#line 24 "/home/brandao/Desktop/Bash_preprocessing_mhtFoam-main/GIT/fhdFoam/tutorials/mhtFoam/2d_circular_tumour/0/ID/#codeStream"
#include "fvCFD.H"
                #include "Ostream.H"
//}}} end codeInclude

// * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * //

namespace Foam
{

// * * * * * * * * * * * * * * * Local Functions * * * * * * * * * * * * * * //

//{{{ begin localCode

//}}} end localCode


// * * * * * * * * * * * * * * * Global Functions  * * * * * * * * * * * * * //

extern "C" void codeStream_8d2a7c2073e3637bc2e564ae9506587eae05ae42(Foam::Ostream& os, const Foam::dictionary& dict)
{
//{{{ begin code
    #line 41 "/home/brandao/Desktop/Bash_preprocessing_mhtFoam-main/GIT/fhdFoam/tutorials/mhtFoam/2d_circular_tumour/0/ID/#codeStream"
const IOdictionary& d = static_cast<const IOdictionary&>(dict);
        const fvMesh& mesh = refCast<const fvMesh>(d.db());
        const scalar pi = 3.141592653589793;
        scalarField ID(mesh.nCells(), 0.);
        //########### Aqui entra as informações dos tumores(raio,excentricidade,posições e inclinação)

        //Tumor_1
        scalar radius_1 = 6524;
        scalar eccen_1 = 6524;
        scalar posx_1 = 6524;
        scalar posy_1 = 264;
        scalar inclination_1 = 6524;
        scalar inclination_rad_1 = inclination_1 * pi / 180.0;
        scalar be_1 = radius_1*pow((1-pow(eccen_1,2)),0.25);
        scalar ae_1 = pow(pow(be_1,2)*(pow(1-pow(eccen_1,2),-1)),0.5);

        //Tumor_2
        scalar radius_2 = 6524;
        scalar eccen_2 = 6524;
        scalar posx_2 = 6524;
        scalar posy_2 = 524;
        scalar inclination_2 = 5642;
        scalar inclination_rad_2 = inclination_2 * pi / 180.0;
        scalar be_2 = radius_2*pow((1-pow(eccen_2,2)),0.25);
        scalar ae_2 = pow(pow(be_2,2)*(pow(1-pow(eccen_2,2),-1)),0.5);

        //##########
        
        forAll(ID, i)
        {
                const scalar x = mesh.C()[i][0];
                const scalar y = mesh.C()[i][1];
                const scalar z = mesh.C()[i][2];
        //###### Aqui entra as informações para definir região do tumor (circular ou elíptica)
        scalar y_rot_1 = (y-posy_1)*cos(inclination_rad_1)-(x-posx_1)* sin(inclination_rad_1);
        scalar x_rot_1 = (y-posy_1)*sin(inclination_rad_1)+(x-posx_1)* cos(inclination_rad_1);
                if ( pow(y_rot_1,2) <= ((1 - pow(x_rot_1,2)/pow(ae_1,2) )*pow(be_1,2)) )
                {
                        ID[i] = 1.;
                }

        scalar y_rot_2 = (y-posy_2)*cos(inclination_rad_2)-(x-posx_2)* sin(inclination_rad_2);
        scalar x_rot_2 = (y-posy_2)*sin(inclination_rad_2)+(x-posx_2)* cos(inclination_rad_2);
                if ( pow(y_rot_2,2) <= ((1 - pow(x_rot_2,2)/pow(ae_2,2) )*pow(be_2,2)) )
                {
                        ID[i] = 1.;
                }

       
        //######
       
        }
        ID.writeEntry("", os);
//}}} end code
}


// * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * //

} // End namespace Foam

// ************************************************************************* //

