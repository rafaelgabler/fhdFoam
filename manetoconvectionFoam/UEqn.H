    // Solve the momentum equation

    MRF.correctBoundaryVelocity(U);


//    volScalarField    modH = mag(H);
//    volScalarField    H2over2 = pow(mag(H),2)/2;

    fvVectorMatrix UEqn
    (
        fvm::ddt(U) + fvm::div(phi, U)
      + MRF.DDt(U)
      + turbulence->divDevReff(U)
     ==
        fvOptions(U)
        + (mu0 / rho)*chi0*beta_m*(T - TRef)*fvc::grad(H2over2)
    );

    UEqn.relax();

    fvOptions.constrain(UEqn);

    if (pimple.momentumPredictor())
    {
        solve
        (
            UEqn
         ==
            fvc::reconstruct
            (
                (
                  - ghf*fvc::snGrad(rhok)
                  - fvc::snGrad(p_rgh)
                )*mesh.magSf()
            )
        );

        fvOptions.correct(U);
    }
