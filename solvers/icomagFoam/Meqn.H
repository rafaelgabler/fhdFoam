{
 fvVectorMatrix MEqn
        (
        fvm::ddt(M) + fvm::div(phi,M) -0.5*(fvc::curl(U)^M) 
        - (mu0/(6*rho*nu*fi))*(MxH^M) - (1/tau)*(M0-M)
        );
        
        MEqn.solve();       
}
