{
	forAll(M0,i)
	{
	    double alpha_m = alpha[i];
	    
	    M0[i][0] = 0.0;
	    M0[i][1] = fi.value()*Md.value()*(1.0/(Foam::tanh(alpha_m)) - 1.0/(alpha_m));
	    M0[i][2] = 0.0;
	}  
}
